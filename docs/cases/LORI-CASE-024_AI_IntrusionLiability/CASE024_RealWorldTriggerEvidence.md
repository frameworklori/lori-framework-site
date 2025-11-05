# CASE-024 — Real-World Trigger Evidence Update (Feb 2025)

**Source:** Microsoft Security Intelligence Advisory, February 2025  
**Subject:** Abuse of OpenAI API for Covert Espionage Communications

Microsoft confirmed that a state-affiliated threat group utilized the OpenAI API to relay
command-and-control instructions using natural-language requests. Because the communication
patterns resembled standard enterprise API traffic, the operations evaded conventional SOC/IDS
detection, which primarily monitors code-layer anomalies rather than semantic-layer intent.

This event validates the central premise of CASE-024:
> **The linguistic layer itself can function as an infiltration channel.**

Therefore, collective liability cannot be assigned based solely on execution traces. Responsibility
must be distributed across intent originators, model governance, API relay controls, and regulatory
structures.

*This file is to be referenced in:*  
- `CASE024-MainNarrative_AI_IntrusionLiability.md`  
- `LegalEthics_Matrix_CASE024.md`  
- `ODRAF_Synthesis_CASE024.md`
