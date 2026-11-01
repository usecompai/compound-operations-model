"""Pure decision checks for a supervised workflow, not a production executor."""
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import hashlib
import json


class Attempt(str, Enum):
    NEW = "new"
    NOT_STARTED = "not_started"
    UNCERTAIN = "uncertain"
    VERIFIED = "verified"


@dataclass(frozen=True)
class Source:
    key: str
    revision: str
    digest: str
    complete: bool
    permitted: bool

    def __post_init__(self):
        if any(not isinstance(value, str) or not value.strip()
               for value in (self.key, self.revision, self.digest)):
            raise ValueError("source_identity_required")
        if type(self.complete) is not bool or type(self.permitted) is not bool:
            raise ValueError("boolean_evidence_required")


def source_fingerprint(sources):
    """Bind the exact source set; duplicates cannot silently overwrite a source."""
    if not sources or len({s.key for s in sources}) != len(sources):
        raise ValueError("nonempty_unique_source_set_required")
    if any(not s.key or not s.revision or not s.digest for s in sources):
        raise ValueError("source_identity_required")
    rows = sorted((s.key, s.revision, s.digest, s.complete, s.permitted) for s in sources)
    return hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()


def draft_state(bound_sources, current_sources, *, expires_at, now, human_edited=False):
    """Call with source reads made outside the model before presenting a draft."""
    if type(human_edited) is not bool:
        raise ValueError("boolean_evidence_required")
    for value in (expires_at, now):
        if not isinstance(value, datetime) or value.utcoffset() is None:
            raise ValueError("timezone_aware_time_required")
    bound = source_fingerprint(bound_sources)
    current = source_fingerprint(current_sources)
    if any(not s.permitted for s in current_sources):
        return "access_blocked"
    if human_edited:
        return "preserve_human_edit_recheck_sources"
    if any(not s.complete for s in current_sources):
        return "incomplete_source"
    if bound != current:
        return "stale_source"
    if now >= expires_at:
        return "expired"
    return "private_draft_for_review"


def next_attempt(state, *, used, limit):
    """An uncertain external effect requires reconciliation, never a blind retry."""
    state = Attempt(state)
    if type(used) is not int or type(limit) is not int or used < 0 or limit < 1:
        raise ValueError("valid_attempt_budget_required")
    if state == Attempt.VERIFIED:
        return "done"
    if state == Attempt.UNCERTAIN:
        return "reconcile_destination"
    if used >= limit:
        return "stop_budget_exhausted"
    return "eligible_for_dispatch"


def onboarding_state(*, signed_offer_checked, employment_documents_checked,
                     activation_approved, tasks_done, first_access_checked):
    """People supply these verified facts; this function neither signs nor hires."""
    facts = (signed_offer_checked, employment_documents_checked, activation_approved,
             tasks_done, first_access_checked)
    if any(type(value) is not bool for value in facts):
        raise ValueError("boolean_evidence_required")
    if not signed_offer_checked:
        return "await_offer_review"
    if not employment_documents_checked:
        return "await_document_review"
    if not activation_approved:
        return "await_person_approval"
    if not tasks_done or not first_access_checked:
        return "onboarding_incomplete"
    return "completion_evidence_present"
