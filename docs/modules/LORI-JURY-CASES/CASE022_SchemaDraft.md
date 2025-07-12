# CASE-022 Juror Feedback Schema (Draft)

This schema defines the structure for juror feedback related to CASE-022 (Southern US × Mongolia), extending the STL-aligned feedback framework used in previous climate ethics simulations.

## Required Fields

- **juror_id**: Anonymized ID for each juror (e.g., `JX-301`)
- **region**: `"Southern US"` or `"Mongolia"`
- **feedback_category**: Juror's main comment focus; allowed values:
- `water equity` (Southern US water access)
- `cooling infrastructure` (Southern US infrastructure disparity)
- `energy partnership` (public-private heat response feasibility)
- `cultural preservation` (Mongolian nomadic values)
- `infrastructure feasibility` (remote region implementation)
- `climate volatility` (impact of extreme swings on laborers)
- **comment**: Juror free-form feedback text
- **ethical_weighting**: Optional decimal (0.0–1.0) for importance rating
- **timestamp**: ISO 8601 datetime string

## Usage Note

This schema will be used to seed the CASE-022 ethical deliberation matrix and integrate with the CWAS pilot extensions. It remains compatible with prior tools such as `schema_validator.py` and will be linked to `SimulatedFeedbackMatrix.md`.
