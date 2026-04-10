# Anonymization Strategy

> **Document status:** Initial draft
> **Last updated:** 2026-04-10
> **Regulatory references:** GDPR Recital 26, Art. 5(1)(b), 5(1)(e), 25, 89; EDPB WP216
> **Maintained by:** Vitus Püttmann (Data Controller)

---

## 1. Purpose and Scope

This document defines the anonymization strategy for all data processed in this project, in accordance with the data protection by design principle under GDPR Art. 25 and the storage limitation principle under Art. 5(1)(e).

As documented in `docs/compliance/legal_basis.md` and `docs/compliance/processing_activities.md`, the data processed in this project — aggregate weather measurements and bicycle traffic counts retrieved from public APIs — does not constitute personal data within the meaning of GDPR Art. 4(1) and recital 26. Anonymization in the strict legal sense is therefore not required: the data is not personal to begin with, and no legal transformation from regulated to unregulated data is necessary.

---

## 2. Re-identification Risk Assessment

The data processed in this project consists of aggregate meteorological measurements and aggregate bicycle traffic counts at fixed measurement points. Neither dataset contains direct identifiers, quasi-identifiers, or any information relating to identified or identifiable natural persons.

The mosaic effect is assessed as follows: combining fine-grained temporal and spatial traffic counts with other publicly available data — demographic statistics, event calendars, infrastructure maps — could in principle enable inference about the movement patterns of groups. However, since the data relates to counts rather than trajectories or individual records, re-identification of specific natural persons is not a reasonably likely outcome given the means available.

**Conclusion:** No material re-identification risk exists in the current data. This assessment should be revisited if feature engineering introduces derived attributes with greater granularity, or if additional data sources are introduced in a later phase.

---

## 3. Anonymization Techniques Selected

Since the data is not personal, no anonymization techniques are required or applied. The data arrives from public APIs already in aggregate form, and no de-identification step is necessary prior to storage, processing, or use.

**Conclusion:** No anonymization techniques are applied.

---

## 4. Differential Privacy Considerations

Differential privacy guarantees are not required for this project. The training data consists of aggregate, non-personal measurements, and the risks of membership inference and model inversion — which differential privacy is designed to address — presuppose that the training data contains personal or sensitive records that an adversary might seek to recover.

**Conclusion:** Differential privacy is not applied. Reassessment is required if sensitive training data is introduced.

---

## 5. Anonymization Standard Applied

Since no personal data is processed, no anonymization standard needs to be applied to transform regulated data into unregulated data. The data is outside the GDPR's material scope from the point of retrieval.

**Conclusion:** No anonymization standard is applied. The data is outside the GDPR's scope from retrieval.

---

## 6. Verification Approach

Verification of anonymization effectiveness is not required, as no anonymization is applied. No re-identification testing is conducted.

**Conclusion:** No verification is required or conducted.

---

## 7. Transition Point

No anonymization transition point applies, as the data is not personal at any stage of the lifecycle. The data enters the pipeline as aggregate measurements and remains aggregate throughout retrieval, storage, feature engineering, model training, and evaluation.

**Conclusion:** No transition point is defined. This section requires substantive completion if personal data is introduced.

---

## 8. Interaction with Retention Policy

Since the data is not personal, the storage limitation principle does not apply and retention is not constrained by the GDPR. Retention periods will nonetheless be defined in `docs/data_governance/retention_policy.md` as a matter of good data governance practice, independent of legal obligation.

**Conclusion:** No anonymization-driven retention interaction applies. Retention periods are defined independently in `docs/data_governance/retention_policy.md`.

---

## 9. Residual Risk Acknowledgment

Since no anonymization is applied and the data is not personal, there is no residual anonymization risk to acknowledge in the technical sense. The re-identification risk assessed in section 2 — relating to the mosaic effect across aggregate datasets — is accepted as minimal and does not require anonymization as a mitigation measure.

**Conclusion:** No residual anonymization risk is acknowledged beyond what is documented in the DPIA (`docs/compliance/dpia.md`, Risk 1).

---

## 10. Relationship to Other Documents

| Document | Relationship |
|----------|-------------|
| `docs/compliance/legal_basis.md` | Establishes that the data is not personal; provides the basis for the conclusion that anonymization is not required |
| `docs/compliance/dpia.md` | Risk 1 (re-identification) draws on and is informed by the assessment in section 2 of this document |
| `docs/compliance/processing_activities.md` | Retention period entries reference this document for the anonymization-retention interaction |
| `docs/data_governance/retention_policy.md` | Defines retention periods in a manner consistent with section 8 of this document |
