# Chapter 11d: EU AI Act Readiness — What You Need to Verify

## Why This Chapter Exists

The EU AI Act (Regulation 2024/1689) entered into force on 1 August 2024 and applies in phases. Prohibited-practice and AI-literacy provisions have applied since 2 February 2025; governance and general-purpose-model obligations since 2 August 2025; many general provisions and Article 50 transparency duties apply from 2 August 2026. Some high-risk timelines are different and the 2026 simplification package changes parts of the implementation calendar.

**Status checked: 12 July 2026.** Verify the current timeline and your role against the European Commission's [AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) and [official navigation FAQ](https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act), then have qualified counsel classify the actual deployment. This chapter is an operating-readiness guide, not a legal opinion or certification.

This chapter gives operators a practical evidence and governance baseline. The precise legal obligations depend on whether you are a provider or deployer, the intended purpose, the affected people, the risk classification and the specific provision.

## The Risk Classification That Actually Matters

The AI Act uses a risk-based approach. Many internal operational capabilities may sit outside the high-risk categories, but an agent name does not determine classification. Intended purpose and actual use do. The table below is a starting hypothesis for legal review, not an automatic classification.

### How to Classify Your Agents

| Agent Type | Likely Classification | Key Question |
|---|---|---|
| **CS / Customer Service** | Limited risk | Does it interact with customers? → Transparency required |
| **Finance / Reporting** | Minimal risk | Does it make decisions about people's access to financial services? → If no, minimal risk |
| **Marketing / Analytics** | Minimal risk | Does it target vulnerable groups? → If no, minimal risk |
| **Retail / Inventory** | Minimal risk | Decisions about products and logistics, not people |
| **Merchandising** | Minimal risk | Product analysis, not people analysis |
| **Strategy / Coordination** | Minimal risk | Internal coordination, no external-facing decisions |
| **HR / People Ops** | ⚠️ **Depends on use** | Admin (absences, payroll) = limited risk. Recruitment, evaluation, performance monitoring = **high-risk** |

### The HR Agent Is the Critical One

Under Annex III of the AI Act, these employment-related uses are classified as **high-risk**:

- Screening or evaluating job candidates
- Making hiring or firing decisions
- Monitoring employee performance or productivity
- Evaluating employees for promotion or demotion
- Analyzing employee behavior or emotional state
- Deciding employment terms or conditions

If your HR agent does ANY of the above, you need full high-risk compliance: risk management system, data governance, technical documentation, human oversight, accuracy testing, and incident reporting.

**Our recommendation:** keep your HR agent strictly administrative — absences, payroll prep, vacation balances, policy lookups, expense categorization. These are NOT high-risk. The moment you add candidate screening or performance evaluation, you trigger a completely different compliance regime.

Add this explicit guardrail to your HR agent's SOUL.md:

```markdown
## EU AI Act Compliance

### Prohibited Uses (Annex III High-Risk)
This agent NEVER:
- Screens or evaluates job candidates
- Makes hiring, firing, or promotion decisions
- Monitors employee performance or productivity
- Scores or ranks employees

If asked to perform any of the above, respond:
"This is classified as high-risk under the EU AI Act. I cannot perform
employment-related decisions. Please handle this through your HR team."
```

## Practical Baseline For Every Deployment

### 1. Transparency for Customer-Facing Agents (Article 50)

Article 50 includes transparency duties when people interact directly with an AI system and for specified generated or manipulated content. A human using AI to prepare a draft is not automatically the same as a person interacting directly with the system; assess the actual workflow and final guidance. Typical in-scope surfaces can include:

- customer-facing AI chat or messaging interactions
- Chatbots on your website
- AI-generated marketing communications (if personalized)

When disclosure is required, use clear language at the interaction point. A conservative example is:

> *"You are interacting with an AI-assisted service. A team member can review or take over."*

Do not copy that sentence blindly: verify whether the workflow is direct AI interaction, human-reviewed assistance, or generated-content disclosure, and implement the applicable requirement.

### 2. Record-Keeping And Operational Evidence

Article 12 record-keeping duties are tied to high-risk systems and particular regulated roles. Even where the exact statutory duty does not apply, log consequential actions as an operational control:
- Timestamp
- Which agent acted
- What action was taken
- Confidence score
- Data sources used
- Whether a human reviewed it

The playbook's JSONL audit logging format already covers this:

```json
{"timestamp":"2026-04-11T08:15:00Z","agent":"cs-agent","action":"draft_response","confidence":"94%","data":"order_tracking","human_review":false}
```

### 3. Human Oversight (Article 14)

Model confidence is not a compliance mechanism and must not grant authority by itself. Oversight starts with the intended purpose and risk classification of each capability:

| Capability | Default control |
|---|---|
| Read and retrieve | Authenticated identity, scoped source access, citations |
| Analyse and recommend | Logged inputs, validation and a durable receipt |
| Draft external work | Human review until a named capability is separately approved |
| Change operational systems | Explicit grant, limits, rollback and monitoring |
| Money, employment, legal or destructive action | Named human approval; no confidence bypass |

Document who can intervene, what information they receive, how they stop or reverse the action, and how the system behaves when evidence or providers are unavailable. Have qualified counsel validate the final control design for your use case.

### 4. EU Data Residency

Host your infrastructure in the EU. The reference deployment uses Hetzner (Germany). This isn't strictly required by the AI Act, but it simplifies GDPR compliance and avoids cross-border data transfer headaches.

### 5. API Usage, Not Training

Ensure you're using LLM providers via API (not consumer products). API terms explicitly state your data isn't used for model training. This matters for GDPR's "purpose limitation" principle and for the AI Act's data governance requirements.

## Data Protection Impact Assessment (DPIA)

If your agents process personal data at scale — customer emails, employee records, order history — you likely need a DPIA under GDPR Article 35. This is separate from the AI Act but overlaps.

A DPIA template can live in the open-source repo. The key sections:

1. **Description of processing:** what data, what agents, what purpose
2. **Legal basis:** legitimate interest (operational efficiency) or consent
3. **Necessity and proportionality:** why AI agents vs manual processing
4. **Risks to data subjects:** what could go wrong (data leak, incorrect automated response, etc.)
5. **Mitigation measures:** scoped identity, capability authority, human review, audit logging, access controls and rollback
6. **Retention:** how long data is kept, when it's deleted

## What About the LLM Providers?

The AI Act places obligations on both **providers** (Anthropic, OpenAI, Google) and **deployers** (you). The providers handle:

- Model safety testing and evaluation
- Technical documentation of the model
- Compliance with general-purpose AI model requirements (Article 51-55)

You handle:
- Using the system according to the provider's instructions
- Human oversight and monitoring
- Transparency to end users
- Incident reporting if something goes wrong

**You are a deployer, not a provider.** Your obligations are lighter. But they're not zero.

## Readiness Checklist

Before relying on the system after 2 August 2026, and again whenever its intended purpose changes:

- [ ] Classify each agent by risk category (use the table above)
- [ ] Add transparency disclaimers to all customer-facing agent outputs
- [ ] Add explicit "prohibited uses" guardrails to HR agent SOUL.md
- [ ] Verify audit logging is active on all agents (JSONL format)
- [ ] Verify confidence reporting, where used, is never treated as authority
- [ ] Verify human oversight is documented by capability (who reviews what, with which stop and rollback path)
- [ ] Complete a DPIA for personal data processing
- [ ] Document the "intended purpose" of each agent (SOUL.md serves this role)
- [ ] Establish incident reporting procedure (who to notify if an agent causes harm)
- [ ] Quarterly review calendar set: capability authority, closure, corrections, incidents and risk classification

## What This Means for Sales

**Evidence is a selling point; unsupported certification language is a liability.** After the customer has completed and validated the relevant work, describe the evidence precisely:

- "Each deployed capability has a documented intended purpose and reviewed risk hypothesis"
- "Capability-specific authority with documented intervention and rollback paths"
- "Consequential actions produce a durable audit receipt from day one"
- "HR agent has explicit guardrails against high-risk employment uses"
- "EU-hosted infrastructure, API-only LLM usage"

Do not claim "AI Act compliant" from the presence of templates alone. The differentiator is a reviewable evidence package and a control design that qualified advisors can assess.

---

*Next: [Chapter 12 — ROI: The Honest Math →](12-roi.md)*

## Ready-Made Templates (In the Repo)

The repo includes three compliance documents ready to fill in:

### 1. DPIA Template (`knowledge-base/dpia-template.md`)
Complete Data Protection Impact Assessment pre-filled with the multi-agent architecture. 8 sections covering:
- System description with per-agent data access table
- 12 data source mappings
- Legal basis per data category
- 8 risk assessments with likelihood × impact scoring
- Technical, organizational, and contractual mitigations
- Data subject rights procedures
- Signature fields for controller + legal counsel
- Review schedule

**Time to complete:** ~2 hours. Fill in your company name, employee count, specific data types, and retention periods.

### 2. AI System Register Template (`knowledge-base/ai-system-register-template.md`)
Formal register of all 8 AI systems with per-agent documentation:
- System ID, intended purpose, risk classification with justification
- Provider, host location, human oversight assignment
- Autonomy level, data processed, prohibited uses
- Consolidated compliance measures table (10 items)

**Time to complete:** ~1 hour. Fill in your team names, system details, and deployment dates.

### 3. EU AI Act Guardrails Templates (`knowledge-base/eu-ai-act-guardrails.md`)
Copy-paste blocks for agent SOUL.md files:
- HR Agent prohibited uses (Annex III)
- CS Agent transparency obligation (Article 50)
- General compliance block (all agents)
- DPIA summary template

**Time to complete:** ~15 minutes per agent. Copy the relevant block into each SOUL.md.

## Implementation Checklist

Complete these before August 2, 2026:

### Week 1: Foundation
- [ ] Classify each agent by risk category (use the table in this chapter)
- [ ] Add anti-prompt-injection block to ALL agent SOULs
- [ ] Add confidence scoring to ALL agent SOULs
- [ ] Verify audit logging is active on all agents

### Week 2: Transparency + HR
- [ ] Add Article 50 transparency disclaimer to CS agent SOUL
- [ ] Configure CS email template with AI disclosure footer
- [ ] Add Annex III prohibited uses block to HR agent SOUL
- [ ] Verify HR agent cannot perform employment decisions

### Week 3: Documentation
- [ ] Complete DPIA template with your company data
- [ ] Complete AI System Register with all deployed systems
- [ ] Document incident reporting procedure (who to notify, how, timeline)
- [ ] Assign human oversight manager to each agent

### Week 4: Verification
- [ ] Run security-scan.sh on all agents
- [ ] Verify all agents survive a reboot test
- [ ] Review capability authority, closure, correction and confidence calibration
- [ ] Schedule quarterly compliance review (first: 1 month before Aug 2, 2026)

### Ongoing
- [ ] Quarterly review of capability grants, closure, corrections, escalations and calibration
- [ ] Annual DPIA reassessment
- [ ] Update AI System Register when new agents deployed or capabilities change
- [ ] Review incident log (any serious incidents → report to supervisory authority)
