# Risk Classification

> **Document status:** Initial draft
> **Last updated:** 2026-04-13
> **Regulatory references:** EU AI Act Art. 3, 5, 6, 50, 51–56; Annex I, Annex III
> **Maintained by:** Vitus Püttmann (AI System Provider)

---

## 1. Purpose and Scope

This document determines and records the risk classification of the AI system developed in this project under the EU AI Act. It is the foundational classification decision from which all other EU AI Act compliance obligations flow, and must be completed before data collection begins.

The classification follows the EU AI Act's four-tier framework:

1. **Prohibited AI practices** (Art. 5) — AI systems whose risks are considered unacceptable and whose development or use is prohibited outright
2. **High-risk AI systems** (Art. 6 + Annex III) — AI systems subject to the full requirements under Chapter III, Section 2 (Art. 9–15), including technical documentation, conformity assessment, registration, and post-market monitoring
3. **AI systems subject to transparency obligations** (Art. 50) — AI systems with limited specific obligations relating to disclosure and labelling
4. **Minimal-risk AI systems** — all other AI systems, for which no specific obligations apply under the Act, though providers remain free to apply voluntary codes of practice

The classification is applied to the system as described in section 2. It must be revisited whenever the system's intended purpose, deployment context, or capabilities change materially — see section 7.

---

## 2. System Description

| Field | Detail |
|-------|--------|
| **System name** | Bicycle Traffic Forecasting and Public Transport Decision-Making |
| **Provider** | Vitus Püttmann, Hamburg, Germany |
| **Intended purpose** | Predicting the daily volume of bicycle traffic in Hamburg from weather data using supervised machine learning; using these predictions together with additional aggregate data to forecast daily demand for public transport |
| **Deployment context** | Educational — local machine only; no real operational deployment; publicly available as open-source code under the MIT License |
| **Affected persons** | No specific natural persons are affected by the system's outputs; outputs are aggregate statistical predictions |
| **Decision type** | Advisory/informational — the system produces predictions, not automated decisions with legal or individually significant effects |
| **Data inputs** | Aggregate weather measurements (public API); aggregate bicycle traffic counts (public API) |
| **Output** | Predicted bicycle traffic volume; derived public transport demand forecast |

---

## 3. Step 1 — Prohibited Practices Assessment (Art. 5)

Art. 5(1) prohibits eight categories of AI practice. Each is assessed below.

### 3.1 Subliminal manipulation (Art. 5(1)(a))

> *AI systems that deploy subliminal techniques beyond a person's consciousness, or purposefully manipulative or deceptive techniques, with the objective or effect of materially distorting behaviour in a way that causes or is reasonably likely to cause significant harm.*

**Assessment:** The system is a statistical forecasting model. It produces predictions about bicycle traffic and public transport demand. It does not interact with natural persons, does not influence behaviour, and deploys no persuasion or deception techniques.

**Conclusion:** Not applicable.

---

### 3.2 Exploitation of vulnerabilities (Art. 5(1)(b))

> *AI systems that exploit any of the vulnerabilities of a natural person or a specific group of persons owing to their age, disability, or social or economic situation, in order to materially distort the behaviour of those persons in a way that causes or is reasonably likely to cause significant harm.*

**Assessment:** The system's outputs are aggregate traffic predictions. The system does not target, identify, or interact with any natural persons, and has no mechanism for exploiting individual vulnerabilities.

**Conclusion:** Not applicable.

---

### 3.3 Social scoring (Art. 5(1)(c))

> *AI systems used by or on behalf of public authorities for the evaluation or classification of natural persons or groups of persons over a period of time based on their social behaviour or known, inferred, or predicted personal or personality characteristics.*

**Assessment:** The system is operated by a private individual for educational purposes. It does not evaluate or classify natural persons. It produces aggregate traffic counts, not scores or rankings of individuals.

**Conclusion:** Not applicable.

---

### 3.4 Criminal offence risk assessment from personal characteristics (Art. 5(1)(d))

> *AI systems used for making risk assessments of natural persons in order to assess or predict the risk of criminal offences, based solely on the profiling of a natural person or on assessing their personality traits and characteristics.*

**Assessment:** The system predicts bicycle traffic volume from weather data. It has no law enforcement application and does not assess any characteristics of natural persons.

**Conclusion:** Not applicable.

---

### 3.5 Untargeted facial recognition database scraping (Art. 5(1)(e))

> *AI systems that create or expand facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage.*

**Assessment:** The system does not process images, facial data, or biometric information of any kind.

**Conclusion:** Not applicable.

---

### 3.6 Emotion inference from biometric data (Art. 5(1)(f))

> *AI systems used to infer the emotions of a natural person in the areas of workplace and education, except where the AI system is intended to be put in place or placed on the market for medical or safety reasons.*

**Assessment:** The system does not process biometric data and has no workplace or educational deployment context.

**Conclusion:** Not applicable.

---

### 3.7 Biometric categorization revealing sensitive characteristics (Art. 5(1)(g))

> *Biometric categorization systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation.*

**Assessment:** The system does not process biometric data and does not categorize individuals.

**Conclusion:** Not applicable.

---

### 3.8 Real-time remote biometric identification in public spaces for law enforcement (Art. 5(1)(h))

> *AI systems used for real-time remote biometric identification of natural persons in publicly accessible spaces for the purpose of law enforcement.*

**Assessment:** The system does not process biometric data, is not a real-time identification system, and has no law enforcement application.

**Conclusion:** Not applicable.

---

### 3.9 Art. 5 Summary

No prohibited AI practice applies to this system. Development and use of the system is not prohibited under Art. 5.

---

## 4. Step 2 — General-Purpose AI Model Assessment (Art. 51–56)

Art. 3(63) defines a general-purpose AI (GPAI) model as an AI model trained on large amounts of data using self-supervision at scale, displaying significant generality, and capable of competently performing a wide range of distinct tasks.

**Assessment:** The system is a supervised machine learning model trained on a narrow, domain-specific dataset (Hamburg weather and bicycle traffic data) for a single, explicitly defined prediction task. It is not capable of a wide range of distinct tasks, is not trained on large-scale diverse data, and does not display the generality characteristic of GPAI models. It is not a GPAI model within the meaning of Art. 3(63).

**Conclusion:** Title VIII (Art. 51–56) does not apply. The system is not a GPAI model.

---

## 5. Step 3 — High-Risk Assessment: Art. 6(1) Safety Component

Art. 6(1) classifies an AI system as high-risk where it is a safety component of a product — or is itself a product — covered by the EU product safety legislation listed in Annex I, and is required to undergo a third-party conformity assessment under that legislation.

Annex I products include, among others: machinery, radio equipment, recreational craft, cableway installations, pressure equipment, personal protective equipment, gas appliances, medical devices, in vitro diagnostic medical devices, lifts, equipment in potentially explosive atmospheres, marine equipment, rail interoperability equipment, aviation equipment, motor vehicles, agricultural vehicles, and high-speed rail equipment.

**Assessment:** The system is a software application for educational use running on a personal computer. It is not embedded in, and does not serve as a safety component of, any product covered by Annex I legislation. The prediction of bicycle traffic volume and public transport demand does not constitute a safety-relevant function within any regulated product category.

**Conclusion:** Art. 6(1) does not apply. The system is not a high-risk AI system on this ground.

---

## 6. Step 4 — High-Risk Assessment: Annex III Standalone Listing

Art. 6(2) classifies an AI system as high-risk where it is listed in Annex III. Annex III identifies eight areas. Each is assessed in turn.

### 6.1 Annex III, Point 1 — Biometric Systems

> *AI systems intended to be used for the biometric identification of natural persons; AI systems intended to be used for biometric categorisation of natural persons to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; AI systems intended to be used for the recognition of emotions of natural persons.*

**Assessment:** The system does not process biometric data and has no biometric identification, categorization, or emotion recognition function.

**Conclusion:** Not applicable.

---

### 6.2 Annex III, Point 2 — Critical Infrastructure

> *AI systems intended to be used as safety components in the management and operation of critical digital infrastructure, road traffic, or the supply of water, gas, heating or electricity.*

**Assessment:** This is the closest category to the system's domain. Public transport is a component of urban mobility infrastructure. However, two conditions must both be met: (i) the system must function as a *safety component*, and (ii) in *management and operation* of critical infrastructure.

The system satisfies neither condition:

- **Safety component:** The system produces advisory demand forecasts, not safety-critical control outputs. It does not monitor physical assets, detect faults, control signals, or trigger protective actions. A demand forecast for public transport is a planning tool, not a safety mechanism. Even if the system's predictions were used by a public transport operator, they would inform scheduling decisions made by humans, not directly control infrastructure.
- **Road traffic:** The system predicts aggregate bicycle traffic volume derived from weather observations. It does not manage or operate road traffic in any sense — it produces a statistical quantity for educational analysis.
- **Electricity/water/gas/heating:** No involvement.

Furthermore, the system is deployed in a local educational context with no operational connection to any infrastructure management system.

**Conclusion:** Not applicable. The system is a forecasting model, not a safety component, and has no operational role in infrastructure management.

> **Note for Phase 2:** If the agentic AI layer planned for Phase 2 were to issue recommendations that feed into real operational decisions by a public transport authority, this classification should be reassessed. The boundary between advisory and safety-component status is context-dependent and fact-sensitive.

---

### 6.3 Annex III, Point 3 — Education and Vocational Training

> *AI systems intended to be used to determine access to or admission to or assignment of natural persons to educational and vocational training institutions; to evaluate the learning outcomes of natural persons; to assess the appropriate level of education for a person or to assess students; to monitor and detect prohibited behaviour of students.*

**Assessment:** The system has no application in education or vocational training. It predicts bicycle traffic volume; it does not assess, admit, or evaluate any individuals.

**Conclusion:** Not applicable.

---

### 6.4 Annex III, Point 4 — Employment and Workers Management

> *AI systems intended to be used for recruitment or selection of natural persons, notably for advertising vacancies, screening or filtering applications, evaluating candidates; to make decisions affecting working conditions, promotion, termination, task allocation, and monitoring and evaluation of performance.*

**Assessment:** The system has no employment or human resources application. It produces aggregate traffic predictions.

**Conclusion:** Not applicable.

---

### 6.5 Annex III, Point 5 — Essential Private and Public Services

> *AI systems intended to be used by public authorities or on behalf of public authorities to evaluate the eligibility of natural persons for essential public services including healthcare, social security and housing; to evaluate creditworthiness of natural persons; to assess risk and pricing in life and health insurance; to evaluate and classify emergency calls including dispatch of emergency services.*

**Assessment:** The system does not determine access to services, creditworthiness, insurance pricing, or emergency dispatch for any natural persons. It produces aggregate statistical predictions with no individual-level output.

**Conclusion:** Not applicable.

---

### 6.6 Annex III, Point 6 — Law Enforcement

> *AI systems intended to be used by or on behalf of competent authorities for risk assessments of natural persons in order to assess the risk of a natural person for offending or reoffending, to carry out polygraph or similar tools, to detect emotional or psychological states, to detect deepfakes, to evaluate the reliability of evidence, to predict the occurrence or recurrence of an actual or potential criminal offence based on profiling, or for profiling of natural persons in the course of detection, investigation or prosecution of criminal offences.*

**Assessment:** The system has no law enforcement application. It predicts bicycle traffic volume from weather data; it has no involvement in crime prediction, investigation, or prosecution of any kind.

**Conclusion:** Not applicable.

---

### 6.7 Annex III, Point 7 — Migration, Asylum, and Border Control

> *AI systems intended to be used by competent public authorities as polygraphs or similar tools, to assess risks including security risks posed by a natural person entering the territory of a Member State, to assist in the examination of applications for asylum, visa, and residence permits and associated complaints, to detect or recognise persons.*

**Assessment:** The system has no migration, asylum, or border control application.

**Conclusion:** Not applicable.

---

### 6.8 Annex III, Point 8 — Administration of Justice and Democratic Processes

> *AI systems intended to be used by judicial authorities or on their behalf to research and interpret facts and the law and to apply the law to a specific set of facts, or to be used in a similar way in alternative dispute resolution; AI systems intended to be used for influencing the outcome of an election or referendum or the voting behaviour of natural persons.*

**Assessment:** The system has no judicial, legal, or electoral application.

**Conclusion:** Not applicable.

---

### 6.9 Annex III Summary

The system does not fall within any of the eight categories listed in Annex III. It is not a high-risk AI system on any Annex III ground.

---

## 7. Step 5 — Transparency Obligations Assessment (Art. 50)

Even where a system is not high-risk, specific transparency obligations apply in certain cases under Art. 50.

### 7.1 Art. 50(1) — AI Systems Interacting with Natural Persons

> *Providers of AI systems intended to interact directly with natural persons must ensure that those persons are informed that they are interacting with an AI system.*

**Assessment:** The system does not interact with natural persons. It is a batch forecasting model that produces outputs read by the developer. No chatbot, conversational, or real-time user-facing interface exists.

**Conclusion:** Not applicable.

---

### 7.2 Art. 50(2) — Emotion Recognition and Biometric Categorization

> *Providers and deployers of AI systems used for emotion recognition or biometric categorisation must inform the natural persons exposed to such systems.*

**Assessment:** The system performs neither emotion recognition nor biometric categorization.

**Conclusion:** Not applicable.

---

### 7.3 Art. 50(3) — Artificially Generated or Manipulated Content

> *Providers of AI systems that generate or manipulate image, audio, or video content constituting a deepfake must ensure the content is labelled in a machine-readable format and is marked as artificially generated or manipulated.*

**Assessment:** The system does not generate or manipulate image, audio, or video content.

**Conclusion:** Not applicable.

---

### 7.4 Art. 50(4) — AI-Generated Text on Matters of Public Interest

> *Providers of AI systems that generate text published for the purpose of informing the public on matters of public interest must ensure the output is labelled as AI-generated in a machine-readable format.*

**Assessment:** The system generates numerical predictions, not public-facing text intended to inform the public on matters of public interest. Model outputs are used internally for educational analysis.

**Conclusion:** Not applicable.

---

### 7.5 Art. 50 Summary

No transparency obligation under Art. 50 applies to this system.

---

## 8. Risk Classification Conclusion

| Classification Question | Answer |
|------------------------|--------|
| Does Art. 5 prohibit the system? | No |
| Is it a GPAI model (Art. 51–56)? | No |
| Is it a safety component of an Annex I product (Art. 6(1))? | No |
| Does it fall within any Annex III category (Art. 6(2))? | No |
| Does Art. 50 impose transparency obligations? | No |
| **Risk classification** | **Minimal risk** |

**The system is a minimal-risk AI system.** No specific obligations under the EU AI Act apply to its development, deployment, or post-market monitoring. The Act imposes no conformity assessment, technical documentation, registration, or transparency requirements on this system.

---

## 9. Voluntary Application of High-Risk Standards

Notwithstanding the minimal-risk classification, this project voluntarily applies the full requirements applicable to high-risk AI systems under Chapter III, Section 2 (Art. 9–15), as documented in `docs/compliance/conformity_assessment.md`.

The voluntary standards applied are:

| Art. | Requirement | Reference |
|------|-------------|-----------|
| Art. 10 | Data and data governance | `docs/data_governance/` |
| Art. 11 | Technical documentation | `docs/model/technical_documentation.md` |
| Art. 12 | Record-keeping and logging | `docs/oversight/logging_auditability.md` |
| Art. 13 | Transparency and explainability | `docs/model/explainability_spec.md` |
| Art. 14 | Human oversight | `docs/oversight/human_in_the_loop.md` |
| Art. 15 | Accuracy, robustness, cybersecurity | `docs/model/performance_thresholds.md` |

Applying voluntary standards does not alter the legal classification. The system remains minimal-risk for purposes of the EU AI Act.

---

## 10. Classification Review Triggers

This classification must be reviewed and, if necessary, updated before proceeding in any of the following circumstances:

| Trigger | Likely Classification Impact | Action |
|---------|---------------------------|--------|
| Phase 2 agentic AI layer | May alter intended purpose; Annex III point 2 should be re-examined if operational transport decisions are informed | Full reclassification before Phase 2 development begins |
| Introduction of personal or sensitive data | Changes Art. 10 compliance posture; Art. 5 re-examination required | Reclassify and update DPIA before new data collection |
| Operational deployment by a public authority | High probability of Annex III (points 2 or 5) or safety-component reclassification | Full reclassification before any deployment negotiations |
| Deployment outside educational context | Changes the weight of the Art. 6(2) assessment | Reclassify before deployment |
| Third-party operational deployment (downstream) | Third party bears provider obligations; disclaimer in `README.md` assigns this responsibility | No action required by this controller; disclaimer must remain prominent |
| Substantial modification of intended purpose | Any change that meaningfully alters the system's function, outputs, or affected population | Reclassify before modification is implemented |

---

## 11. Relationship to Other Documents

| Document | Relationship |
|----------|-------------|
| `docs/compliance/conformity_assessment.md` | Draws its risk classification from this document; documents the voluntary high-risk compliance assessment |
| `docs/compliance/dpia.md` | Informs the Art. 5 and Annex III assessment where data risks intersect with prohibited-practice questions |
| `docs/compliance/legal_basis.md` | Confirms the nature of data processed, relevant to the Art. 5 and Annex III assessments |
| `docs/operations/roles_responsibilities.md` | Identifies the provider and deployer for purposes of Art. 3 and obligation allocation |
| `docs/model/model_card.md` | System description entries in section 2 of this document are drawn from the model card |

---

## 12. Review History

| Date | Version | Trigger | Summary |
|------|---------|---------|---------|
| 2026-04-13 | 0.1 | Initial draft | Pre-data-collection classification; minimal risk on all grounds |
