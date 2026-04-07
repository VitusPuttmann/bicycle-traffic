# Processing Activities Register

> **Document status:** Initial draft
> **Last updated:** 2026-04-07
> **Regulatory reference:** GDPR Art. 30
> **Maintained by:** Vitus Püttmann (Data Controller)

---

## 1. Purpose and Scope

This register documents all processing activities carried out in the context of this project, in accordance with Art. 30(1) GDPR. It is an internal accountability document and must be made available to the competent supervisory authority — the Hamburgische Beauftragte für Datenschutz und Informationsfreiheit (HmbBfDI) — upon request.

As documented in `docs/compliance/legal_basis.md`, the data processed in this project — aggregate weather measurements and bicycle traffic counts — does not constitute personal data within the meaning of Art. 4(1) GDPR. The GDPR's material scope under Art. 2(1) therefore does not strictly apply, but this register is maintained as part of the project's compliance framework.

This register must be reviewed and updated whenever the nature, purpose, scope, or technical means of processing change.

---

## 2. Controller Details

| Field | Detail |
|-------|--------|
| **Name** | Vitus Püttmann |
| **Email** | vitus.puettmann@web.de |
| **Role** | Data Controller per GDPR Art. 4(7) |
| **Establishment** | Hamburg, Germany |
| **DPO** | Not designated — see `docs/operations/roles_responsibilities.md` for justification |

---

## 3. Processing Activities

### 3.1 Retrieval of Weather Data

| Field | Detail |
|-------|--------|
| **Activity ID** | PA-01 |
| **Activity name** | Retrieval of weather data from public API |
| **Purpose** | Obtaining input features for a supervised machine learning model predicting bicycle traffic volume |
| **Legal basis** | Art. 6(1)(f) — Legitimate interests (documented in `docs/compliance/legal_basis.md`, section 2.1) |
| **Categories of data subjects** | None — data is not personal |
| **Categories of data** | Aggregate meteorological measurements (e.g. temperature, precipitation, wind speed, humidity) |
| **Source of data** | Public open-access weather API — provider to be specified |
| **Recipients** | None — data is processed locally and not shared with third parties |
| **Third country transfers** | None — all processing takes place on the controller's local machine in Hamburg, Germany |
| **Retention period** | To be defined in `docs/data_governance/retention_policy.md` |
| **Technical and organizational measures** | Local storage only; data directory excluded from version control via `.gitignore`; no cloud sync of raw data files |
| **Processor** | None engaged for this activity |

---

### 3.2 Retrieval of Bicycle Traffic Data

| Field | Detail |
|-------|--------|
| **Activity ID** | PA-02 |
| **Activity name** | Retrieval of bicycle traffic data from public API |
| **Purpose** | Obtaining the target variable for a supervised machine learning model predicting bicycle traffic volume |
| **Legal basis** | Art. 6(1)(f) — Legitimate interests (documented in `docs/compliance/legal_basis.md`, section 2.2) |
| **Categories of data subjects** | None — data is not personal |
| **Categories of data** | Aggregate bicycle traffic counts at fixed measurement points in Hamburg |
| **Source of data** | Public open-access bicycle traffic API — provider to be specified |
| **Recipients** | None — data is processed locally and not shared with third parties |
| **Third country transfers** | None — all processing takes place on the controller's local machine in Hamburg, Germany |
| **Retention period** | To be defined in `docs/data_governance/retention_policy.md` |
| **Technical and organizational measures** | Local storage only; data directory excluded from version control via `.gitignore`; no cloud sync of raw data files |
| **Processor** | None engaged for this activity |

---

### 3.3 Local Storage and Processing of Retrieved Data

| Field | Detail |
|-------|--------|
| **Activity ID** | PA-03 |
| **Activity name** | Local storage and processing of weather and traffic data |
| **Purpose** | Feature engineering, model training, model evaluation, and documentation of a supervised machine learning model |
| **Legal basis** | Art. 6(1)(f) — Legitimate interests — continuous with PA-01 and PA-02 (documented in `docs/compliance/legal_basis.md`, section 2.3) |
| **Categories of data subjects** | None — data is not personal |
| **Categories of data** | Weather measurements (PA-01) and bicycle traffic counts (PA-02), including derived features produced during preprocessing |
| **Source of data** | PA-01 and PA-02 |
| **Recipients** | None — data is not shared with third parties |
| **Third country transfers** | None |
| **Retention period** | To be defined in `docs/data_governance/retention_policy.md` |
| **Technical and organizational measures** | Processing confined to local machine; raw and processed data directories excluded from version control and cloud sync; access limited to the controller |
| **Processor** | None engaged for this activity |

---

### 3.4 Publication of Code and Documentation via GitHub

| Field | Detail |
|-------|--------|
| **Activity ID** | PA-04 |
| **Activity name** | Publication of source code and compliance documentation to a public GitHub repository |
| **Purpose** | Sharing the project publicly for educational purposes under an open-source license |
| **Legal basis** | Not applicable — no personal data is published; the controller's own name and email address in documentation are disclosed voluntarily per GDPR recital 18 |
| **Categories of data subjects** | The controller (Vitus Püttmann) — name and email address appear in compliance documents |
| **Categories of data** | Source code; compliance and governance documentation; no raw or processed data |
| **Source of data** | Produced by the controller |
| **Recipients** | The public — the repository is publicly accessible on GitHub |
| **Third country transfers** | GitHub (Microsoft) servers may be located outside the EEA; addressed under Microsoft's Data Protection Agreement incorporating EU Standard Contractual Clauses — see `docs/operations/roles_responsibilities.md` |
| **Retention period** | Indefinite — for as long as the repository remains public; deletion requires manual removal from GitHub |
| **Technical and organizational measures** | Raw and processed data excluded from version control via `.gitignore`; sensitive information (e.g. API keys) excluded via `.gitignore`; repository access managed via GitHub account credentials |
| **Processor** | Microsoft (GitHub & OneDrive) — DPA accepted upon account creation; see `docs/operations/roles_responsibilities.md` |

---

## 5. Relationship to Other Documents

| Document | Relationship |
|----------|-------------|
| `docs/compliance/legal_basis.md` | Provides the legal basis justification referenced in each activity entry |
| `docs/compliance/dpia.md` | Draws on this register to identify processing activities requiring impact assessment |
| `docs/operations/roles_responsibilities.md` | Supplies controller, processor, and supervisory authority details |
| `docs/data_governance/retention_policy.md` | Defines the retention periods referenced in each activity entry |
| `docs/data_governance/anonymization_strategy.md` | Informs retention period entries where anonymization is applied prior to deletion |

---
