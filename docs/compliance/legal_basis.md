# Legal Basis

> **Document status:** Initial draft
> **Last updated:** 2026-04-07
> **Regulatory references:** GDPR Art. 5(1)(a), 6(1), 7, 9, 13, 14, 21, 30

---

## 1. Overview

This document identifies and justifies the lawful grounds for each processing activity carried out in this project, in accordance with the GDPR principle of lawfulness under Art. 5(1)(a). The legal basis for each activity is determined before processing begins and is recorded here as the authoritative internal reference for the Processing Activities Register (`docs/compliance/processing_activities.md`), the Data Protection Impact Assessment (`docs/compliance/dpia.md`), and any transparency notices directed at data subjects.

The legal basis cannot be changed retroactively once processing has commenced.

---

## 2. Processing Activities and Legal Bases

### 2.1 Retrieval of Weather Data from Public API

| Field | Detail |
|-------|--------|
| **Processing activity** | Retrieving weather measurements from a public open-access API for use as model input features |
| **Data involved** | Meteorological measurements (e.g. temperature, precipitation, wind speed, humidity) — not personal data in their raw form |
| **Legal basis** | Art. 6(1)(f) — Legitimate interests |
| **Data subject rights affected** | Right to object (Art. 21); no consent-based rights apply |

#### Legitimate Interests Assessment

**Step 1 — Legitimate interest pursued**
The controller pursues the legitimate interest of acquiring practical, hands-on knowledge in the compliant design of machine learning systems, with particular reference to the EU AI Act and GDPR. This is a genuine, lawful objective with broader educational value.

**Step 2 — Necessity of processing**
Retrieval of weather data is strictly necessary to achieve this objective. The machine learning model cannot be developed, trained, or evaluated without input data. No less privacy-intrusive means of achieving the same objective is reasonably available.

**Step 3 — Balancing test**
The weather data retrieved consists of aggregate meteorological measurements tied to geographic locations and time periods. It does not relate to identified or identifiable individuals. The impact on the interests, rights, and freedoms of data subjects is therefore minimal. The controller's legitimate interest is not overridden.

**Conclusion:** Art. 6(1)(f) applies. Processing is lawful.

---

### 2.2 Retrieval of Bicycle Traffic Data from Public API

| Field | Detail |
|-------|--------|
| **Processing activity** | Retrieving bicycle traffic counts from a public open-access API for use as the model target variable |
| **Data involved** | Aggregate bicycle traffic volume counts — not personal data in their raw form |
| **Legal basis** | Art. 6(1)(f) — Legitimate interests |
| **Data subject rights affected** | Right to object (Art. 21); no consent-based rights apply |

#### Legitimate Interests Assessment

**Step 1 — Legitimate interest pursued**
As per section 2.1: the acquisition of practical knowledge in compliant machine learning system design.

**Step 2 — Necessity of processing**
Retrieval of bicycle traffic data is strictly necessary to train and evaluate a supervised machine learning model predicting traffic volume. The prediction task cannot be defined or evaluated without target variable data.

**Step 3 — Balancing test**
The traffic data consists of aggregate counts of bicycle movements at fixed measurement points. It does not identify or single out individual cyclists. The data is publicly available and has already been disclosed by the originating authority. The impact on data subjects' interests is minimal. The controller's legitimate interest is not overridden.

**Conclusion:** Art. 6(1)(f) applies. Processing is lawful.

---

### 2.3 Local Storage and Processing of Retrieved Data

| Field | Detail |
|-------|--------|
| **Processing activity** | Storing retrieved data on the controller's local machine and processing it for feature engineering, model training, and evaluation |
| **Data involved** | Weather measurements and bicycle traffic counts as described in 2.1 and 2.2 |
| **Legal basis** | Art. 6(1)(f) — Legitimate interests — continuous with the retrieval activities above |
| **Data subject rights affected** | Right to object (Art. 21); no consent-based rights apply |

#### Legitimate Interests Assessment

Local storage and processing is the direct continuation of the retrieval activities documented in 2.1 and 2.2 and is necessary to achieve the same legitimate interest. No additional balancing test is required beyond what is documented above, as the purpose, data, and impact on data subjects are identical. Processing is confined to the controller's local machine and is not shared with third parties beyond what is documented in `docs/operations/roles_responsibilities.md`.

**Conclusion:** Art. 6(1)(f) applies. Processing is lawful.

---

### 2.4 Publication of Code and Documentation via GitHub

| Field | Detail |
|-------|--------|
| **Processing activity** | Publishing source code, model documentation, and compliance documents to a public GitHub repository |
| **Data involved** | No personal data or raw data is committed to the repository; only source code and documentation are published |
| **Legal basis** | Not applicable — no personal data is processed in this activity |
| **Data subject rights affected** | None |

The controller's name and email address appear in compliance documentation published to the repository. This constitutes processing of the controller's own personal data, which the controller discloses voluntarily in their capacity as author and maintainer of a public educational project. No legal basis under Art. 6 is required for a natural person processing their own data for personal or household purposes per GDPR recital 18. The controller accepts this disclosure knowingly and intentionally.

---

## 3. Art. 9 Assessment

Art. 9(1) prohibits the processing of special categories of personal data unless one of the conditions in Art. 9(2) applies. Special categories include data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data, health data, and data concerning sex life or sexual orientation.

None of the data processed in this project falls within the special categories enumerated in Art. 9(1). The weather and bicycle traffic data retrieved from public APIs are aggregate measurements with no connection to the health, beliefs, identity, or biometric characteristics of identifiable individuals.

**Art. 9 does not apply to this project.** No additional condition under Art. 9(2) is required.

---

## 4. Consequences for Data Subject Rights

The reliance on Art. 6(1)(f) as the exclusive legal basis across all processing activities has the following implications for data subject rights:

| Right | Applicability | Notes |
|-------|--------------|-------|
| Right of access (Art. 15) | Limited | Data is aggregate and not linked to identifiable individuals; no individual access requests are anticipated |
| Right to rectification (Art. 16) | Limited | As above |
| Right to erasure (Art. 17) | Limited | Applies where processing is no longer necessary or where the data subject objects and no overriding legitimate grounds exist |
| Right to restriction (Art. 18) | Applicable | Controller must restrict processing upon valid request while the legitimacy of processing is assessed |
| Right to data portability (Art. 20) | Not applicable | Portability applies only to processing based on consent (Art. 6(1)(a)) or contract (Art. 6(1)(b)) |
| Right to object (Art. 21) | Applicable | Data subjects may object to processing based on Art. 6(1)(f); the controller must cease processing unless compelling legitimate grounds are demonstrated |
| Rights related to automated decision-making (Art. 22) | Not applicable | The system does not make decisions producing legal or similarly significant effects on individuals |

---

## 5. Purpose Limitation

In accordance with Art. 5(1)(b), data collected for the purposes documented above will not be processed for any purpose incompatible with those stated. Specifically:

- Weather and traffic data will be used exclusively for training, evaluating, and documenting the machine learning model described in this project
- Data will not be used for profiling, commercial purposes, or any purpose beyond the educational objectives of the project
- Any further processing for a new purpose will require a fresh legal basis assessment before it commences

---

## 6. Relationship to Other Documents

| Document | Relationship |
|----------|-------------|
| `docs/compliance/processing_activities.md` | Draws legal basis entries directly from this document |
| `docs/compliance/dpia.md` | Uses this document as the starting point for the lawfulness assessment |
| `docs/operations/roles_responsibilities.md` | Identifies the controller responsible for maintaining this document |
| `docs/data_governance/retention_policy.md` | Retention periods must be consistent with the purposes documented here |

---
