# Juror Feedback Schema (v1.0)

This schema defines the standard structure for juror feedback entries within the LORI Jury-Based Judgment System. It is designed for integration with STL (Systemic Trust Layer) and automated parsing during ethical co-governance deliberations.

## 🧩 Schema Fields

| Field | Type | Description |
|-------|------|-------------|
| `juror_id` | `string` | An anonymized or hashed identifier for the juror. |
| `feedback_category` | `enum (string)` | One of: `ethical clarity`, `emotional impact`, `policy realism`, `cultural context`, or `resilience trade-off`. |
| `comment` | `string` | The free-form written feedback from the juror. |
| `ethical_weighting` | `number (0.0–1.0)` | Optional score representing ethical relevance of this feedback. |
| `timestamp` | `ISO 8601 string` | The exact submission time of the feedback. |

## 🌐 Compliance

- Follows [JSON Schema Draft 2020-12](https://json-schema.org/)
- Designed to be parsed in real-time for ethical traceability and trust signal calibration.

## 📎 Example Entry

```json
{
"juror_id": "JX-104",
"feedback_category": "cultural context",
"comment": "This case made me think about indigenous stewardship models, not just Western water law.",
"ethical_weighting": 0.85,
"timestamp": "2025-07-13T12:30:00+09:00"
}

