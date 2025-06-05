# LORI Jury System v2.0 Upgrade Plan

_Last updated: 2025-06-05_

---

## Overview

This v2.0 Upgrade Plan introduces essential flexibility layers into the LORI Jury System, addressing key structural gaps identified during framework reviews.

Key objectives:

- Add formal **Appeal & Rehearing Mechanism**
- Integrate **Feedback Loop** into Jury decisions
- Enable **External Stakeholder Participation**
- Prevent rigidity / "single-verdict finality" risk
- Increase community trust and long-term governance adaptability

---

## Upgraded Structure Diagram

![LORI-JurySystem_v2.0_Structure](LORI-JurySystem_v2.0_Structure.png)

---

## Core Enhancements

### 1️⃣ Appeal & Rehearing Layer

- 30-day appeal window after public verdict release.
- Appeals can be triggered by:
- Human Judges (main or independent)
- External monitors / stakeholders
- AI Agent internal confidence divergence
- Rehearing Jury:
- Expanded jury composition (more AI agents + human judges), or
- Human-majority ethical panel for complex cases.

---

### 2️⃣ Feedback Loop Integration

- Open Feedback window (e.g. 60 days).
- Weighted feedback system:
- High-weight: Human Judges, independent experts
- Medium-weight: Civic organizations, academic feedback
- Low-weight: General community
- When feedback threshold exceeded:
- Trigger **automatic review** or **module update workflow**.

---

### 3️⃣ Stakeholder Review Layer

- External Expert Feedback Portal.
- Inputs from:
- Academia
- Civic groups
- Legal & governance experts
- International observers
- High-impact feedback triggers **mandatory Governance Committee review**.

---

### 4️⃣ Case Versioning & Transparency

- Cases will support versioning:
- CASE v1.0 → v1.1 → v2.0
- Each version includes:
- Initial verdict
- Appeal outcome (if any)
- Summary of accepted feedback
- External review notes

---

## Example Index Fields to Add

```markdown
## Appeal Status
- Appeal Window: OPEN / CLOSED
- Rehearing Jury Triggered: YES / NO
- Rehearing Verdict Summary: (if applicable)

## Feedback Integration
- Feedback Window: OPEN / CLOSED
- High-weight Feedback Count: N
- Triggered Module Update: YES / NO
- Summary of Accepted Feedback:

## Stakeholder Review
- External Feedback Received: YES / NO
- Governance Committee Review Triggered: YES / NO
- Summary of Stakeholder Inputs:

