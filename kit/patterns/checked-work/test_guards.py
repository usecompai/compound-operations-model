import unittest
from dataclasses import replace
from datetime import datetime, timedelta, timezone
from guards import Source, source_fingerprint, draft_state, next_attempt, onboarding_state


class CheckedWorkTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 1, 1, tzinfo=timezone.utc)
        self.sources = [Source("example-order", "v1", "fixture-digest", True, True)]

    def draft(self, current=None, **kwargs):
        return draft_state(self.sources, self.sources if current is None else current,
                           now=self.now, expires_at=self.now + timedelta(minutes=5), **kwargs)

    def test_valid_is_still_only_private_draft(self):
        self.assertEqual(self.draft(), "private_draft_for_review")

    def test_changed_content_invalidates(self):
        self.assertEqual(self.draft([replace(self.sources[0], digest="changed")]), "stale_source")

    def test_changed_revision_invalidates(self):
        self.assertEqual(self.draft([replace(self.sources[0], revision="v2")]), "stale_source")

    def test_missing_source_invalidates(self):
        with self.assertRaises(ValueError): self.draft([])

    def test_incomplete_source_is_not_an_empty_success(self):
        self.assertEqual(self.draft([replace(self.sources[0], complete=False)]), "incomplete_source")

    def test_access_revoked_also_blocks_human_edit(self):
        self.assertEqual(self.draft([replace(self.sources[0], permitted=False)], human_edited=True), "access_blocked")

    def test_human_text_is_not_overwritten(self):
        self.assertEqual(self.draft([replace(self.sources[0], revision="v2")], human_edited=True), "preserve_human_edit_recheck_sources")

    def test_expiry_boundary(self):
        self.assertEqual(draft_state(self.sources, self.sources, now=self.now, expires_at=self.now), "expired")

    def test_naive_clock_rejected(self):
        with self.assertRaises(ValueError):
            draft_state(self.sources, self.sources, now=self.now.replace(tzinfo=None), expires_at=self.now)

    def test_duplicate_and_empty_identities_rejected(self):
        for sources in [[], self.sources * 2]:
            with self.subTest(sources=sources), self.assertRaises(ValueError): source_fingerprint(sources)
        for field, value in [("key", ""), ("revision", " "), ("digest", 1),
                             ("complete", "true"), ("permitted", 1)]:
            with self.subTest(field=field), self.assertRaises(ValueError):
                replace(self.sources[0], **{field: value})
        with self.assertRaises(ValueError): self.draft(human_edited="false")

    def test_source_order_does_not_change_identity(self):
        sources=self.sources + [replace(self.sources[0], key="example-policy")]
        self.assertEqual(source_fingerprint(sources), source_fingerprint(list(reversed(sources))))

    def test_unknown_outcome_is_not_retryable(self):
        self.assertEqual(next_attempt("uncertain", used=0, limit=2), "reconcile_destination")

    def test_verified_is_not_reexecuted(self):
        self.assertEqual(next_attempt("verified", used=2, limit=2), "done")

    def test_budget_and_invalid_states(self):
        self.assertEqual(next_attempt("new", used=2, limit=2), "stop_budget_exhausted")
        self.assertEqual(next_attempt("not_started", used=1, limit=2), "eligible_for_dispatch")
        for state, used, limit in [("invented",0,2),("new",-1,2),("new",0,0),("new",True,2)]:
            with self.subTest(state=state), self.assertRaises(ValueError): next_attempt(state,used=used,limit=limit)

    def test_onboarding_gates(self):
        names=["signed_offer_checked","employment_documents_checked","activation_approved","tasks_done","first_access_checked"]
        expected=["await_offer_review","await_document_review","await_person_approval","onboarding_incomplete","onboarding_incomplete"]
        for name, state in zip(names,expected):
            facts=dict.fromkeys(names, True); facts[name]=False
            self.assertEqual(onboarding_state(**facts),state)
        self.assertEqual(onboarding_state(**dict.fromkeys(names,True)),"completion_evidence_present")

    def test_text_is_not_evidence(self):
        with self.assertRaises(ValueError):
            onboarding_state(signed_offer_checked="yes",employment_documents_checked=True,
                             activation_approved=True,tasks_done=True,first_access_checked=True)


if __name__ == "__main__": unittest.main()
