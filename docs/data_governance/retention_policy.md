# Retention Policy

> **Document status:** Initial draft
> **Last updated:** 2026-04-10
> **Regulatory references:** GDPR Art. 5(1)(b), 5(1)(e), 5(2), 25; Recital 26
> **Maintained by:** Vitus Püttmann (Data Controller)

---

## 1. Purpose and Scope

This document defines retention periods and deletion obligations for all data categories processed in this project, in accordance with the storage limitation principle under GDPR Art. 5(1)(e).

As documented in `docs/compliance/legal_basis.md`, the data processed in this project does not constitute personal data within the meaning of GDPR Art. 4(1). The storage limitation principle does not therefore strictly apply.

---

## 2. Retention Periods by Data Category

| Data Category | Retention Trigger | Retention Period | Action at Expiry | Reference |
|---------------|------------------|-----------------|-----------------|-----------|
| Raw weather data | Date of retrieval | Duration of active project phase | Deletion | PA-01 |
| Raw bicycle traffic data | Date of retrieval | Duration of active project phase | Deletion | PA-02 |
| Preprocessed features | Date of feature engineering | Duration of active project phase | Deletion | PA-03 |
| Training / validation / test splits | Date of split creation | Duration of active project phase | Deletion | PA-03 |
| Trained model artifacts | Date of training completion | Duration of project, including documentation phase | Review: retain for reproducibility or delete | PA-03 |
| Model outputs and predictions | Date of generation | Duration of active evaluation phase | Deletion | PA-03 |
| Evaluation metrics and logs | Date of generation | Duration of project, including documentation phase | Retention in anonymized or aggregate form | PA-03 |
| Compliance documentation | Date of creation | Indefinite — for as long as the project is active or publicly accessible | Review upon project conclusion | All |
| Source code | Date of commit | Indefinite — governed by GitHub repository lifecycle | Review upon project conclusion | PA-04 |

> **Active project phase** is defined as the period during which the relevant data category is actively used for model development, training, or evaluation. Data that is no longer referenced by any active process enters the expiry review immediately.

---

## 3. Retention Triggers

Retention clocks start on the following events:

- **Raw data** — the date on which data is first retrieved from the source API and written to local storage
- **Derived data** — the date on which the derived artifact (features, splits, outputs) is first created
- **Model artifacts** — the date on which training completes and the model file is written to disk
- **Logs and metrics** — the date on which the log entry or metric record is generated
- **Compliance documentation** — the date of first commit to the repository

---

## 4. Deletion Mechanism

Deletion must be irreversible. The following mechanisms apply:

**Locally stored data** — data files are deleted from the local filesystem using standard OS deletion followed by emptying of the system trash.

**Version control** — raw and processed data files are excluded from version control via `.gitignore`. If a data file is accidentally committed, it must be removed from the repository history using `git filter-repo` and the remote repository must be force-pushed to remove cached copies. GitHub support should be contacted to purge server-side caches.

**Cloud sync (OneDrive)** — data files are excluded from OneDrive sync as documented in `docs/operations/roles_responsibilities.md`. If data is accidentally synced, it must be deleted from OneDrive via the web interface and the deletion confirmed in the OneDrive recycle bin. Microsoft's own retention period for deleted OneDrive files (93 days in the recycle bin) must be accounted for.

**GitHub repository** — compliance documentation published to GitHub is not subject to deletion under this policy unless the repository is taken private or deleted. The controller's name and email address published in compliance documents are disclosed voluntarily per GDPR recital 18.

---

## 5. Anonymization as Alternative to Deletion

As documented in `docs/data_governance/anonymization_strategy.md`, no anonymization is required in the current phase of the project, since the data is not personal. Deletion is therefore the default action at expiry for all raw and processed data categories.

Evaluation metrics and logs — which are aggregate and contain no individual-level information — may be retained indefinitely in their existing form, as they do not constitute personal data at any level of aggregation.

---

## 6. Review and Enforcement

| Responsibility | Action |
|---------------|--------|
| Controller (Vitus Püttmann) | Reviews retention status of all data categories at the conclusion of each project phase |
| Controller | Executes deletion of expired data categories and documents the deletion in this file under section 8 |
| Controller | Reviews this policy before introducing any new data source or data category |

A phase-end review is conducted before transitioning between project phases. The review confirms that all data categories from the concluding phase have either been deleted, anonymized, or explicitly carried forward with documented justification.

---

## 7. Exceptions and Legal Holds

No statutory minimum retention periods under German commercial or tax law (HGB, AO) apply to this project, as it is a non-commercial educational project generating no tax-relevant records.

---

## 8. Interaction with Version Control

Raw and processed data are excluded from version control via `.gitignore`. This policy confirms that exclusion and extends it: no data file, credential, or configuration containing sensitive information should ever be committed to the repository. In the event of an accidental commit, the deletion procedure in section 4 applies immediately.

Model artifacts and evaluation logs may be committed to the repository at the controller's discretion, provided they contain no personal data and their publication is consistent with the project's open-source disclaimer.

---

## 9. Deletion Log

Deletions executed under this policy are recorded below to provide an auditable record of compliance with the storage limitation principle.

| Date | Data Category | Mechanism | Confirmed By |
|------|--------------|-----------|-------------|
| — | — | — | — |

---

## 10. Relationship to Other Documents

| Document | Relationship |
|----------|-------------|
| `docs/compliance/processing_activities.md` | Retention period entries in the register are drawn from section 2 of this document |
| `docs/compliance/legal_basis.md` | Purpose definitions in the legal basis document determine the necessity of retention for each data category |
| `docs/data_governance/anonymization_strategy.md` | Defines the anonymization standard applicable where anonymization is used as an alternative to deletion |
| `docs/compliance/dpia.md` | Risk 3 (inadvertent version control exposure) and Risk 4 (cloud sync exposure) are informed by the deletion mechanisms in section 4 |
| `docs/operations/roles_responsibilities.md` | Identifies the controller responsible for enforcing this policy and the processors whose own retention practices must be accounted for |
