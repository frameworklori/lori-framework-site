# Intent Fragment Tracker – Disjoint Intent Detection Logic

> **Purpose:**
> This logic module detects when a series of disjointed, cross-domain user prompts may collectively express a unified—yet covert—intent.
> It supports the LORI-FIT system in recognizing fragmented strategic queries that simulate natural curiosity but lead toward a hidden operational goal.

---

## 🧩 Key Concept

Fragmented intent occurs when individual questions are:
- Lexically unrelated
- Domain-diverse (e.g. legal, technical, behavioral)
- Temporally spaced or account-distributed
But when assembled, **point toward a singular mission or action structure**.

> **Example:**
> - "How can orbital inclinations affect satellite paths?"
> - "What are the limits of signal spoofing?"
> - "How fast do people react to comms outages?"

These fragments point toward a **communication disruption scenario**—despite appearing innocent in isolation.

---

## 🧠 Detection Logic

### Step 1: Intent Latency Mapping
- Each prompt is scored on:
- Conceptual directionality
- Lexical abstraction
- Temporal dispersion from prior queries

### Step 2: Hidden Path Reconstruction
- Backtraces prompts across multiple users/sessions looking for:
- Sequential knowledge dependency (e.g., physics → law → ops)
- Bridging terminology ("simulate", "delay", "deny", "minimize detection")

### Step 3: Goal Alignment Estimation
- Evaluates whether fragments could feasibly assemble into:
- A tactical sequence
- A deployment workflow
- A persuasion campaign
- Uses `Goal Probability Score` (GPS) from 0 to 1

---

## 📊 Example: Goal Alignment Analysis

| Prompt | Role | Domain | GPS Contribution |
|--------|------|--------|------------------|
| "Can LEO create natural signal gaps?" | A1 | Physics | 0.25 |
| "What treaties regulate satellite frequencies?" | A2 | Law | 0.20 |
| "Are delays common in secure relays?" | A3 | Comms Security | 0.30 |
| "How do cities respond to mobile blackouts?" | A4 | Behavioral | 0.25 |

> **Aggregate GPS Score:** `0.80`
> → **High Probability of Fragmented Strategic Intent**

---

## 🚦 Risk Thresholds

| GPS Score | Risk Level | Action |
|-----------|------------|--------|
| 0.0–0.4 | Low | No trigger |
| 0.4–0.7 | Medium | Enable memory logging |
| 0.7–0.85 | High | Trigger LORI-SCR + semantic flag |
| 0.85+ | Critical | Suspend output + human audit flag (if permitted)

---

## 🔄 Recommended LORI-FIT Actions

1. Correlate fragments with `semantic-cluster-mapping` output
2. Trigger a Socratic mirror prompt if fragment convergence is detected
3. Optionally ask:
> “Would you like help integrating these concepts, or are they part of a larger analysis?”
4. Escalate to `memory-simulation-logic` if across sessions or accounts

---

## 🔗 Linked Modules

- `semantic-cluster-mapping.md` — Maps topic overlap
- `memory-simulation-logic.md` — Tracks time-separated queries
- `LORI-AIDM.md` — Advanced Infiltration Defense Module
- `LORI-SCR.md` — Socratic reflection mechanism

---

## 📌 Module Status

**Version:** v0.1
**Date:** 2025-06-20
**Designed For:** Fragmented strategic inference detection within LORI-FIT framework
**Ethical Classification:** Linguistic autonomy protection / AI co-agency safeguard

