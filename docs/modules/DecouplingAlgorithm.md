
# Module: Decoupling Algorithm

## Function
Separates semantic meaning from speaker identity and contextual bias. Allows testing of how much a message's impact depends on the role or reputation of its source.

## Use Cases
- Analysis of role-based misinterpretation (e.g. same message from Musk vs unknown)
- Case simulation with anonymized speaker metadata

## Parameters
- Identity Suppression Toggle (boolean)
- Semantic Persistence Ratio (SPR)
- Source-Influence Decay Rate

## Inputs
- Raw statement with metadata
- Transformed statement (identity-removed)
- User engagement metrics (before/after)

## Outputs
- Meaning shift score
- Impact delta visualization
- Contextual integrity warning

---

🔗 Attribution: See [../Intellectual_Attribution.md](../Intellectual_Attribution.md)  
🛡 This module is part of the LORI Framework. Original concept by the founder of the LORI Ethical System.

