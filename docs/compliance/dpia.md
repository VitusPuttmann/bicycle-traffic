# Data Protection Impact Assessment (DPIA)

> **Document status:** Initial draft
> **Last updated:** 2026-04-10
> **Regulatory reference:** GDPR Art. 35, 36; EDPB Guidelines WP248
> **Maintained by:** Vitus Püttmann (Data Controller)

---

## 1. Purpose and Scope

This DPIA assesses the risks to the rights and freedoms of natural persons arising from the processing activities carried out in this project, in accordance with Art. 35 GDPR and the EDPB Guidelines on Data Protection Impact Assessment (WP248).

As documented in `docs/compliance/legal_basis.md` and `docs/compliance/processing_activities.md`, the data processed in this project — aggregate weather measurements and bicycle traffic counts — do not constitute personal data within the meaning of Art. 4(1) GDPR. A DPIA is therefore not strictly required under Art. 35(1).

---

## 2. Description of Processing

The following processing activities are assessed in this DPIA. Full descriptions are provided in the Processing Activities Register (`docs/compliance/processing_activities.md`).

| Activity ID | Activity | Data Involved |
|-------------|----------|---------------|
| PA-01 | Retrieval of weather data from public API | Aggregate meteorological measurements |
| PA-02 | Retrieval of bicycle traffic data from public API | Aggregate bicycle traffic counts |
| PA-03 | Local storage and processing of retrieved data | PA-01 and PA-02 data, including derived features |
| PA-04 | Publication of code and documentation via GitHub | Source code and compliance documentation; no raw data |

### 2.1 Purposes of Processing

The processing activities are carried out exclusively for the following purposes:

- Training and evaluating a supervised machine learning model predicting bicycle traffic volume in Hamburg based on weather data
- Using model predictions, together with additional data, to forecast daily demand for public transport

### 2.2 Controller and Processors

| Role | Party | Reference |
|------|-------|-----------|
| Data Controller | Vitus Püttmann | `docs/operations/roles_responsibilities.md` |
| Data Processor | Microsoft (GitHub & OneDrive) | `docs/operations/roles_responsibilities.md` |
| Data Processor — Weather API | To be specified | `docs/operations/roles_responsibilities.md` |
| Data Processor — Traffic API | To be specified | `docs/operations/roles_responsibilities.md` |

---

## 3. Assessment of Necessity and Proportionality

### 3.1 Legal Basis

All processing activities rely on Art. 6(1)(f) GDPR — legitimate interests — as documented in `docs/compliance/legal_basis.md`. The legitimate interest pursued is the acquisition of practical knowledge in compliant machine learning system design. The three-step Legitimate Interests Assessment concludes that processing is necessary and that the controller's interests are not overridden by data subjects' interests, given the aggregate and non-personal nature of the data.

### 3.2 Data Minimization

| Principle | Assessment |
|-----------|------------|
| **Minimization** | Only weather and traffic data strictly necessary for the prediction task are retrieved. No individual-level data is sought or stored. |
| **Purpose limitation** | Data is used exclusively for model training, evaluation, and documentation. No secondary use is intended or permitted without a fresh legal basis assessment. |
| **Storage limitation** | Retention periods are to be defined in `docs/data_governance/retention_policy.md`. Raw data will be deleted or anonymized once no longer necessary for the documented purposes. |
| **Accuracy** | Data is retrieved directly from authoritative public APIs. No manual transformation is applied prior to storage. |

### 3.3 Data Subject Rights

As documented in `docs/compliance/legal_basis.md`, section 4, the reliance on Art. 6(1)(f) gives data subjects the right to object under Art. 21. All other applicable rights are of limited relevance given the non-personal, aggregate nature of the data. No automated decision-making with legal or similarly significant effects on individuals takes place, and Art. 22 therefore does not apply.

### 3.4 Proportionality Assessment

The processing is proportionate to its purpose: the data used is the minimum necessary, is publicly available, relates to no identified or identifiable individuals in its raw form, is stored exclusively on the controller's local machine, and is used for an educational objective with no commercial dimension. The privacy intrusion is minimal relative to the benefit of the compliance learning exercise.

---

## 4. Risk Assessment

Each risk is assessed on two dimensions prior to mitigation:

- **Likelihood:** Low / Medium / High
- **Severity:** Low / Medium / High

Residual risk is assessed after mitigation measures are applied.

---

### Risk 1 — Re-identification Through Dataset Combination

| Field | Detail |
|-------|--------|
| **Description** | Although weather and traffic data are aggregate and non-personal in isolation, combining them with other publicly available datasets — demographic data, infrastructure maps, event calendars — could in principle enable indirect identification of individual movement patterns or routines |
| **Likelihood (pre-mitigation)** | Low — the data consists of counts at fixed measurement points, not trajectories or individual records |
| **Severity (pre-mitigation)** | Medium — if re-identification were achieved, it could reveal information about individuals' routines and mobility |
| **Mitigation measures** | No individual-level data is retrieved or stored; data is used at aggregate level throughout; no dataset combination with individual-level data is planned; purpose limitation documented in `docs/compliance/legal_basis.md` |
| **Residual likelihood** | Very low |
| **Residual severity** | Low |
| **Residual risk** | Acceptable |

---

### Risk 2 — Unauthorized Access to Locally Stored Data

| Field | Detail |
|-------|--------|
| **Description** | Data stored on the controller's local machine is subject to risks of unauthorized physical or remote access, including device theft, malware, or unauthorized access by third parties |
| **Likelihood (pre-mitigation)** | Low — the controller's machine is a personal device with standard security measures |
| **Severity (pre-mitigation)** | Low — Unauthorized access would not immediately expose personal information |
| **Mitigation measures** | OS-level access controls; antivirus and firewall in place; raw data excluded from cloud sync and version control; no remote access to the machine enabled for this project |
| **Residual likelihood** | Very low |
| **Residual severity** | Very low |
| **Residual risk** | Acceptable |

---

### Risk 3 — Inadvertent Data Exposure via Version Control

| Field | Detail |
|-------|--------|
| **Description** | Raw or processed data files, API credentials, or sensitive configuration could be accidentally committed to the public GitHub repository |
| **Likelihood (pre-mitigation)** | Medium — accidental commits of sensitive files are a common occurrence in software projects |
| **Severity (pre-mitigation)** | High — once committed to a public repository, data is immediately publicly accessible and may be indexed or cached before removal |
| **Mitigation measures** | `.gitignore` configured to exclude all data directories, credentials, and environment files from version control; data directory structure reviewed before each commit; no API keys or credentials stored in code files |
| **Residual likelihood** | Low |
| **Residual severity** | Medium — removal from Git history is possible but complex; cached copies may persist |
| **Residual risk** | Acceptable — with note that this risk requires ongoing vigilance |

---

### Risk 4 — Data Exposure via Cloud Sync (OneDrive)

| Field | Detail |
|-------|--------|
| **Description** | If data files are placed in an OneDrive-synced directory, they would be transmitted to Microsoft's cloud servers, potentially outside the EEA, and processed under Microsoft's DPA |
| **Likelihood (pre-mitigation)** | Medium — the project directory may overlap with OneDrive-synced folders if not explicitly configured otherwise |
| **Severity (pre-mitigation)** | Low — unintended cloud transmission would not immediately expose personal information |
| **Mitigation measures** | Data directory explicitly excluded from OneDrive sync; project folder structure reviewed to confirm no data files reside in synced directories; OneDrive sync settings verified |
| **Residual likelihood** | Very low |
| **Residual severity** | Low |
| **Residual risk** | Acceptable |

---

### Risk 5 — Model Outputs as Proxy for Sensitive Information

| Field | Detail |
|-------|--------|
| **Description** | Model predictions — even if derived from non-personal inputs — could in combination with other data be used to infer information about individuals' routines, health status, socioeconomic circumstances, or other sensitive attributes |
| **Likelihood (pre-mitigation)** | Low — predictions are aggregate traffic volume figures, not individual-level outputs |
| **Severity (pre-mitigation)** | Medium — inferential risks from aggregate ML outputs are an active area of regulatory concern |
| **Mitigation measures** | Model outputs are aggregate predictions, not individual records; no deployment in a real operational context is planned; README disclaimer explicitly limits intended use to educational purposes; downstream use risk addressed separately in Risk 6 |
| **Residual likelihood** | Very low |
| **Residual severity** | Low |
| **Residual risk** | Acceptable |

---

### Risk 6 — Downstream Deployment by Third Parties

| Field | Detail |
|-------|--------|
| **Description** | Since the code is publicly available under an open-source license, third parties may deploy the system in operational contexts with materially different risk profiles — including contexts involving personal data, automated decisions with significant effects, or vulnerable data subjects |
| **Likelihood (pre-mitigation)** | Low to medium — the repository is public and the code is reusable |
| **Severity (pre-mitigation)** | High — a downstream deployment in a high-risk context without appropriate compliance measures could cause significant harm to data subjects |
| **Mitigation measures** | README includes an explicit disclaimer stating that the code is for educational use only and that anyone deploying it operationally assumes provider and/or deployer obligations under the EU AI Act; MIT License warranty disclaimer limits the controller's liability; technical documentation and model card will describe the system's limitations and intended use boundaries |
| **Residual likelihood** | Low — the disclaimer is prominent and the legal responsibility is clearly assigned to downstream users |
| **Residual severity** | High — the controller cannot prevent misuse by third parties once the code is published |
| **Residual risk** | Acceptable for the controller — with acknowledgment that residual severity remains high if the disclaimer is disregarded by downstream users |

---

### Risk 7 — Publication of Controller's Personal Data

| Field | Detail |
|-------|--------|
| **Description** | The controller's name and email address appear in compliance documents published to the public GitHub repository, exposing them to the public internet |
| **Likelihood (pre-mitigation)** | Certain — this is an intentional disclosure |
| **Severity (pre-mitigation)** | Low — the information is voluntarily disclosed by the controller in their capacity as project author |
| **Mitigation measures** | Disclosure is voluntary and intentional per GDPR recital 18; the controller accepts the associated risks knowingly; use of a project-specific or professional email address is recommended over a primary personal address |
| **Residual likelihood** | Certain |
| **Residual severity** | Low |
| **Residual risk** | Accepted by the controller |

---

## 5. Summary of Risk Assessment

| Risk | Pre-Mitigation Likelihood | Pre-Mitigation Severity | Residual Risk |
|------|--------------------------|------------------------|---------------|
| R1 — Re-identification | Low | Medium | Acceptable |
| R2 — Unauthorized local access | Low | Medium | Acceptable |
| R3 — Inadvertent version control exposure | Medium | High | Acceptable — ongoing vigilance required |
| R4 — Cloud sync exposure | Medium | Medium | Acceptable |
| R5 — Model output inference | Low | Medium | Acceptable |
| R6 — Downstream deployment | Low–Medium | High | Acceptable for controller |
| R7 — Controller personal data | Certain | Low | Accepted by controller |

No risk presents a high residual risk requiring prior consultation with the HmbBfDI under Art. 36 GDPR.

---

## 6. Prior Consultation

Art. 36 GDPR requires the controller to consult the competent supervisory authority prior to processing where a DPIA indicates that processing would result in a high residual risk in the absence of measures taken by the controller to mitigate it.

**Prior consultation is not required.** No processing activity assessed in this DPIA presents a high residual risk after mitigation measures are applied. This assessment should be revisited if the scope of the project changes materially — in particular if real personal or sensitive data is introduced, if the model is deployed in an operational context, or if automated decisions with significant effects on individuals are implemented.

---

## 7. DPO Consultation

As documented in `docs/operations/roles_responsibilities.md`, no DPO has been designated for this project. DPO consultation under Art. 35(2) is therefore not applicable.

---

## 8. Relationship to Other Documents

| Document | Relationship |
|----------|-------------|
| `docs/compliance/processing_activities.md` | Source of processing activity descriptions assessed in this DPIA |
| `docs/compliance/legal_basis.md` | Informs the necessity and proportionality assessment in section 3 |
| `docs/compliance/conformity_assessment.md` | This DPIA feeds into the broader EU AI Act conformity assessment |
| `docs/operations/roles_responsibilities.md` | Identifies controller, processors, and supervisory authority |
| `docs/data_governance/retention_policy.md` | Informs the data minimization and proportionality assessment |
| `docs/data_governance/anonymization_strategy.md` | Informs risk mitigation measures for R1 and R3 |

---
