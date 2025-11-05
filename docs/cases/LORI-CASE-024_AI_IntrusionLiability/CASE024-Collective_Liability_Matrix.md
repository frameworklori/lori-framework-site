# # CASE-024 Collective Liability Matrix

| Actor | Responsibility Type | Liability Weight | Description |
|------|---------------------|-----------------|-------------|
| Human Threat Actor | Intent & Operational Control | **0.45** | Primary origin of harm |
| AI Model Provider | Safeguard Design & Foreseeability | **0.25** | Must anticipate semantic misuse patterns |
| API / Cloud Relay Platform | Access Oversight and Abuse Prevention | **0.15** | Controls infrastructure & throughput policies |
| SOC / Detection Layer | Monitoring Capability | **0.10** | Limited by semantic opacity |
| State / Regulatory Entity | Norm Definition & Enforcement | **0.05** | Defines legal & jurisdictional boundaries |

```mermaid
flowchart TP
A[Human Threat Actor] -->|Intent Injection| B[AI Model]
B -->|Semantic Relay| C[API / Cloud Platform]
C -->|Enterprise Traffic Camouflage| D[SOC / Monitoring]
D -->|Legal & Policy Feedback| E[State Governance]
