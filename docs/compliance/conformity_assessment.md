# Conformity Assessment

> **Document status:** Initial draft — pre-training
> **Last updated:** 2026-04-10
> **Regulatory references:** EU AI Act Art. 6, 10–15, 28, 43, 47, 71; Annex III, Annex IV
> **Maintained by:** Vitus Püttmann (AI System Provider)

---

## 1. Purpose and Scope

This document records the conformity assessment for the AI system developed in this project, in accordance with EU AI Act Art. 43. It synthesizes the compliance framework established across all preceding documentation and evaluates the system's compliance with the requirements applicable to high-risk AI systems under Chapter III, Section 2 (Art. 10–15).

As established in `docs/compliance/risk_classification.md` (to be completed), the system's real-world risk classification is **minimal risk** — it does not fall within any Annex III category and is not a safety component of an Annex I product. A conformity assessment is therefore not strictly required under the EU AI Act. 

This document is a living record. It must be reviewed and updated at the conclusion of each project phase, upon any substantial modification to the system under Art. 28, and before any deployment beyond the controller's local machine.

---

## 2. System Description

| Field | Detail |
|-------|--------|
| **System name** | Bicycle Traffic Forecasting and Public Transport Decision-Making |
| **Version** | Phase 1 — initial ML model |
| **Provider** | Vitus Püttmann |
| **Deployer** | Vitus Püttmann (provider and deployer are the same individual — see `docs/operations/roles_responsibilities.md`) |
| **Intended purpose** | Predicting the volume of bicycle traffic in Hamburg based on weather data using supervised machine learning; using these predictions, together with additional data, to forecast the daily demand for public transport |
| **Deployment context** | Educational — local machine only; no operational deployment |
| **Input data** | Weather measurements retrieved from a public API |
| **Output** | Predicted bicycle traffic volume; derived public transport demand forecast |
| **Model type** | To be determined — see `docs/model/technical_documentation.md` |
| **License** | MIT |

---

## 3. Risk Classification

### 3.1 Annex III Assessment

Annex III lists eight areas in which AI systems are presumed high-risk. Each is assessed below.

| Annex III Category | Applicable | Reasoning |
|--------------------|-----------|-----------|
| 1. Biometric identification and categorisation | No | The system does not process biometric data or identify natural persons |
| 2. Critical infrastructure | No | Bicycle traffic prediction does not directly manage or control critical infrastructure; public transport demand forecasting is advisory only |
| 3. Education and vocational training | No | The system does not determine access to education or assess individuals |
| 4. Employment and workers management | No | The system does not make or inform employment decisions |
| 5. Access to essential private services and public services | No | The system does not determine access to services or benefits for individuals |
| 6. Law enforcement | No | The system has no law enforcement application |
| 7. Migration, asylum and border control | No | The system has no migration or border control application |
| 8. Administration of justice and democratic processes | No | The system has no justice or democratic process application |

### 3.2 Art. 6(1) Safety Component Assessment

The system is not embedded in any product covered by EU product safety legislation listed in Annex I and does not function as a safety component of any such product.

### 3.3 Risk Classification Conclusion

| Field | Detail |
|-------|--------|
| **Classification** | Minimal risk |
| **Conformity assessment legally required** | No |
| **Conformity assessment conducted** | Yes |
| **Assessment route** | Self-assessment per Art. 43(2) |

---

## 4. Requirements Assessment

Each requirement under EU AI Act Chapter III, Section 2 is assessed below. Compliance status is indicated as follows:

- ✅ **Compliant** — requirement is fully met and documented
- 🔄 **In progress** — requirement is partially met; open items identified
- 🔜 **Pending** — requirement has not yet been addressed; due before the indicated milestone
- ➖ **Not applicable** — requirement does not apply to this system in its current form

---

### 4.1 Art. 10 — Data and Data Governance

*Training, validation, and testing data must be subject to appropriate data governance practices, examined for possible biases, and verified as relevant, sufficiently representative, and free of errors.*

| Sub-requirement | Status | Reference | Notes |
|----------------|--------|-----------|-------|
| Data governance practices documented | ✅ | `docs/data_governance/` | Covers anonymization, retention, and bias sources |
| Legal basis for data processing documented | ✅ | `docs/compliance/legal_basis.md` | Art. 6(1)(f) — legitimate interests |
| Data categories documented | ✅ | `docs/compliance/processing_activities.md` | PA-01, PA-02 |
| Bias sources identified and documented | 🔜 | `docs/data_governance/bias_sources.md` | To be completed before training |
| Training data examined for representativeness | 🔜 | `docs/data_governance/bias_sources.md` | To be completed before training |
| Training / validation / test split documented | 🔜 | `docs/model/technical_documentation.md` | To be completed before training |
| Data quality assessment conducted | 🔜 | `docs/model/technical_documentation.md` | To be completed before training |

---

### 4.2 Art. 11 — Technical Documentation

*Technical documentation must be prepared before the system is placed on the market and kept up to date. It must contain the information specified in Annex IV.*

| Sub-requirement | Status | Reference | Notes |
|----------------|--------|-----------|-------|
| System description and intended purpose | 🔄 | `docs/model/model_card.md` | Model card initiated; to be completed after training |
| Design choices and assumptions documented | 🔜 | `docs/model/technical_documentation.md` | To be completed during model design |
| Model architecture documented | 🔜 | `docs/model/technical_documentation.md` | To be completed after model selection |
| Training methodology documented | 🔜 | `docs/model/technical_documentation.md` | To be completed after training |
| Performance metrics documented | 🔜 | `docs/model/technical_documentation.md` | To be completed after evaluation |
| Known limitations documented | 🔜 | `docs/model/model_card.md` | To be completed after evaluation |
| Instructions for use prepared | 🔜 | `docs/model/model_card.md` | To be completed before deployment |

---

### 4.3 Art. 12 — Record-Keeping

*High-risk AI systems must automatically log events relevant to identifying risks and facilitating post-market monitoring, to the extent technically feasible.*

| Sub-requirement | Status | Reference | Notes |
|----------------|--------|-----------|-------|
| Logging requirements specified | 🔜 | `docs/oversight/logging_auditability.md` | To be completed before deployment |
| Logging mechanism implemented | 🔜 | `src/` | To be implemented during development |
| Log retention defined | 🔜 | `docs/data_governance/retention_policy.md` | Evaluation metrics and logs retention defined; inference logging to be added |
| Log review process defined | 🔜 | `docs/operations/monitoring_plan.md` | To be completed before deployment |

---

### 4.4 Art. 13 — Transparency and Provision of Information

*High-risk AI systems must be sufficiently transparent that deployers can interpret outputs and use the system appropriately. Instructions for use must be provided.*

| Sub-requirement | Status | Reference | Notes |
|----------------|--------|-----------|-------|
| Explainability requirements specified | 🔄 | `docs/model/explainability_spec.md` | To be completed during model design |
| Global explainability method selected | 🔜 | `docs/model/explainability_spec.md` | Depends on model selection |
| Local explainability method selected | 🔜 | `docs/model/explainability_spec.md` | Depends on model selection |
| Audience-appropriate explanations defined | 🔜 | `docs/model/explainability_spec.md` | To be completed before deployment |
| System capabilities and limitations communicated | 🔜 | `docs/model/model_card.md` | To be completed after evaluation |
| Open-source disclaimer published | ✅ | `README.md` | Addresses downstream deployer transparency obligations |

---

### 4.5 Art. 14 — Human Oversight

*High-risk AI systems must be designed to allow effective human oversight. Deployers must be provided with appropriate tools and information to exercise oversight.*

| Sub-requirement | Status | Reference | Notes |
|----------------|--------|-----------|-------|
| Human oversight requirements specified | 🔜 | `docs/oversight/human_in_the_loop.md` | To be completed during model design |
| Automated vs. human-reviewed decisions documented | 🔜 | `docs/oversight/human_in_the_loop.md` | To be completed during model design |
| Override mechanisms defined | 🔜 | `docs/oversight/human_in_the_loop.md` | To be completed during model design |
| Deployer instructions for oversight prepared | 🔜 | `docs/model/model_card.md` | To be completed before deployment |

---

### 4.6 Art. 15 — Accuracy, Robustness, and Cybersecurity

*High-risk AI systems must achieve appropriate levels of accuracy and must be resilient to errors, faults, and adversarial attacks throughout their lifecycle.*

| Sub-requirement | Status | Reference | Notes |
|----------------|--------|-----------|-------|
| Accuracy metrics defined | 🔜 | `docs/model/performance_thresholds.md` | To be completed before training |
| Performance thresholds defined | 🔜 | `docs/model/performance_thresholds.md` | To be completed before training |
| Robustness assessment planned | 🔜 | `docs/model/technical_documentation.md` | To be completed after training |
| Adversarial robustness assessed | 🔜 | `docs/compliance/dpia.md` | Threat model to be completed; see DPIA open items |
| Cybersecurity measures documented | 🔄 | `docs/compliance/dpia.md` | Local security measures addressed in DPIA Risk 2; to be extended |
| Distribution shift monitoring defined | 🔜 | `docs/operations/monitoring_plan.md` | To be completed before deployment |

---

## 5. Compliance Summary

| Requirement | Compliant | In Progress | Pending | Not Applicable |
|-------------|-----------|-------------|---------|----------------|
| Art. 10 — Data governance | 3 | 0 | 4 | 0 |
| Art. 11 — Technical documentation | 0 | 1 | 6 | 0 |
| Art. 12 — Record-keeping | 0 | 0 | 4 | 0 |
| Art. 13 — Transparency | 1 | 1 | 4 | 0 |
| Art. 14 — Human oversight | 0 | 0 | 4 | 0 |
| Art. 15 — Accuracy and robustness | 0 | 1 | 5 | 0 |
| **Total** | **4** | **3** | **27** | **0** |

The high number of pending items reflects that this assessment is prepared at the pre-training stage of Phase 1. The pending items are expected and appropriate at this stage — they define the compliance roadmap for the remainder of Phase 1 and provide the basis for Phase 2 planning.

---

## 6. Substantial Modification Assessment

Art. 28 requires a new conformity assessment where a high-risk AI system undergoes a substantial modification — defined as any change affecting the system's compliance with the Act's requirements or altering its intended purpose.

The following events are pre-identified as likely triggers for a substantial modification assessment in this project:

| Event | Likely Substantial Modification | Action Required |
|-------|--------------------------------|----------------|
| Implementation of agentic AI layer | Yes — new intended purpose and capabilities | Full conformity assessment review before Phase 2 deployment |
| Introduction of personal or sensitive data | Yes — materially changes Art. 10 and Art. 15 compliance | Data governance and robustness sections must be reassessed |
| Deployment outside local machine | Yes — changes deployment context and risk profile | Full conformity assessment review before deployment |
| Change of model architecture | Depends on scope — reassess Art. 11 and Art. 15 | Technical documentation and performance assessment must be updated |
| Introduction of automated decision-making | Yes — triggers Art. 14 and potentially Art. 22 GDPR | Human oversight and transparency sections must be reassessed |

---

## 7. EU Declaration of Conformity (Draft)

**EU DECLARATION OF CONFORMITY**

**Provider:** Vitus Püttmann, Hamburg, Germany (vitus.puettmann@web.de)

**AI System:** Bicycle Traffic and Public Transport Demand Forecasting System

**This declaration of conformity is issued under the sole responsibility of the provider.**

The AI system described above is in conformity with Regulation (EU) [EU AI Act], in particular with the requirements set out in Chapter III, Section 2 (Articles 10–15), on the basis of the self-assessment conducted in accordance with Article 43(2).

**Harmonized standards and common specifications applied:** None designated at time of drafting — to be updated as harmonized standards are adopted under the EU AI Act.

**Notified body:** Not applicable — self-assessment route.

**Place and date:** Hamburg, [date of completion]

**Signatory:** Vitus Püttmann

**Function:** AI System Provider and Data Controller

---

## 8. EU Database Registration

Under Art. 71, providers of high-risk AI systems must register their systems in the EU database before placing them on the market. As the system is classified as minimal risk, registration is not required. This section documents what the registration should contain, when the project shifts to a high-risk deployment context.

| Registration Field | Content |
|-------------------|---------|
| Provider name and contact | Vitus Püttmann, vitus.puettmann@web.de |
| System name and version | Bicycle Traffic Forecasting and Public Transport Decision-Making, Phase 1 |
| Intended purpose | Bicycle traffic volume prediction; public transport demand forecasting |
| Risk category | Minimal risk (educational context) |
| Conformity assessment route | Self-assessment per Art. 43(2) |
| Member state of deployment | Germany |

---

## 9. Review History

| Date | Version | Trigger | Summary of Changes |
|------|---------|---------|-------------------|
| 2026-04-10 | 0.1 | Initial draft | Pre-training assessment; 27 pending items identified |

---

## 10. Relationship to Other Documents

| Document | Relationship |
|----------|-------------|
| `docs/compliance/risk_classification.md` | Provides the risk classification that determines the conformity assessment route |
| `docs/compliance/dpia.md` | Risk assessments inform the Art. 15 cybersecurity and robustness assessment |
| `docs/compliance/legal_basis.md` | Informs the Art. 10 data governance assessment |
| `docs/compliance/processing_activities.md` | Informs the Art. 10 and Art. 11 assessments |
| `docs/model/model_card.md` | Primary reference for Art. 11, 13, and 14 assessments |
| `docs/model/technical_documentation.md` | Primary reference for Art. 11 and Art. 15 assessments |
| `docs/model/explainability_spec.md` | Primary reference for Art. 13 assessment |
| `docs/model/performance_thresholds.md` | Primary reference for Art. 15 assessment |
| `docs/oversight/human_in_the_loop.md` | Primary reference for Art. 14 assessment |
| `docs/operations/roles_responsibilities.md` | Supplies provider and deployer details for the declaration of conformity |
