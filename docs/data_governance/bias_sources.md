# Bias Sources

> **Document status:** Initial draft — pre-data collection (a priori section complete; empirical section pending)
> **Last updated:** 2026-04-10
> **Regulatory references:** EU AI Act Art. 10; GDPR Art. 5(1)(d)
> **Maintained by:** Vitus Püttmann (Data Controller)

---

## 1. Purpose and Scope

This document identifies and documents potential sources of bias in the data used to train, validate, and test the project's main model, in accordance with EU AI Act Art. 10. It covers both biases identifiable before data retrieval on the basis of knowledge about the data collection mechanism and sources (a priori), and biases discovered empirically during data retrieval and exploratory analysis (to be completed before training).

The document is structured in two stages reflecting the project's development phases:

- **Sections 1–4:** Completed before data collection — a priori bias identification
- **Section 5:** To be completed during exploratory data analysis, before training

This document informs the fairness metrics specification (`docs/model/fairness_metrics.md`), the model card (`docs/model/model_card.md`), the technical documentation (`docs/model/technical_documentation.md`), and the DPIA (`docs/compliance/dpia.md`).

---

## 2. Bias Taxonomy

Bias sources are classified using the taxonomy of Suresh and Guttag (2021), which identifies seven bias types arising at distinct stages of the ML pipeline:

| Bias Type | Pipeline Stage | Description |
|-----------|---------------|-------------|
| **Historical bias** | Data | Reflects real-world inequities or structural conditions embedded in the data, regardless of collection quality |
| **Representation bias** | Data | Systematic underrepresentation of certain conditions, groups, or contexts in the dataset |
| **Measurement bias** | Data | Errors or inconsistencies introduced by the measurement instrument or collection process |
| **Aggregation bias** | Data / Features | Inappropriate grouping of heterogeneous subpopulations whose behavior differs meaningfully |
| **Learning bias** | Training | Bias introduced by the model architecture, objective function, or optimization process |
| **Evaluation bias** | Evaluation | Use of benchmarks or metrics that do not reflect the diversity of real-world conditions |
| **Deployment bias** | Deployment | Mismatch between the conditions under which the model was developed and those in which it is deployed |

---

## 3. A Priori Bias Sources

### 3.1 Sensor Coverage Bias

| Field | Detail |
|-------|--------|
| **Bias type** | Representation bias |
| **Pipeline stage** | Data |
| **Description** | Bicycle traffic counting sensors are not uniformly distributed across Hamburg. Sensors are more likely to be installed on major cycling infrastructure — dedicated cycle lanes, cycling bridges, routes connecting major destinations — than on residential streets, informal routes, or areas with lower existing cycling rates. The dataset therefore represents high-infrastructure, high-traffic routes more thoroughly than low-infrastructure routes. |
| **Consequence for model** | The model may learn to predict traffic volumes accurately for well-instrumented routes while performing poorly for routes and conditions not captured by the sensor network. Predictions for underserved areas may be systematically biased. |
| **Mitigation** | Document the geographic coverage of the sensor network; assess whether predictions are intended to generalize beyond instrumented routes; if so, flag generalization limitations explicitly in the model card |
| **Status** | Identified a priori — sensor locations to be confirmed during data retrieval |

---

### 3.2 Temporal Coverage Bias

| Field | Detail |
|-------|--------|
| **Bias type** | Representation bias |
| **Pipeline stage** | Data |
| **Description** | The available traffic count data may not cover all time periods equally. Gaps may exist due to sensor maintenance, data transmission failures, seasonal data collection practices, or deliberate exclusion of anomalous periods. Public holidays, special events, school holidays, and extreme weather events may be underrepresented or absent. |
| **Consequence for model** | A model trained on data with temporal gaps may perform poorly precisely in the atypical conditions — holidays, extreme weather, events — where accurate prediction is most operationally valuable. The model may also be biased toward predicting traffic levels typical of the periods for which data is abundant. |
| **Mitigation** | Examine the temporal distribution of retrieved data during exploratory analysis; identify and document gaps; assess whether missing periods can be imputed or whether the model's scope should be explicitly limited to exclude them |
| **Status** | Identifiable a priori — specific gaps to be confirmed empirically |

---

### 3.3 Weather Data Granularity Mismatch

| Field | Detail |
|-------|--------|
| **Bias type** | Measurement bias |
| **Pipeline stage** | Data / Features |
| **Description** | Weather measurements are typically recorded at specific meteorological stations, which may not correspond geographically to the locations of bicycle traffic sensors. The weather conditions at a measurement station may differ meaningfully from conditions at the point where cycling behavior is observed — particularly for precipitation, wind, and temperature in a coastal city like Hamburg where microclimatic variation is significant. |
| **Consequence for model** | The relationship between the measured weather variable and actual cycling conditions at the traffic sensor location may be imprecise, introducing noise into the feature-target relationship and potentially biasing predictions for sensors geographically distant from weather stations. |
| **Mitigation** | Document the geographic relationship between weather stations and traffic sensors; assess whether interpolation between stations is appropriate; consider distance to nearest weather station as a data quality indicator |
| **Status** | Identifiable a priori — specific station-sensor distances to be quantified during data retrieval |

---

### 3.4 Seasonal and Daylight Bias

| Field | Detail |
|-------|--------|
| **Bias type** | Representation bias / Historical bias |
| **Pipeline stage** | Data |
| **Description** | Bicycle traffic in Hamburg follows strong seasonal patterns driven by daylight hours, temperature, and weather. If the training dataset covers a limited time window — for example, predominantly summer months — the model will be trained on a non-representative sample of annual cycling conditions and will likely underperform during winter months, early mornings, and late evenings when cycling rates are structurally lower. |
| **Consequence for model** | Systematic overestimation of traffic during low-cycling periods if the model is trained predominantly on high-cycling seasons; poor calibration for dawn and dusk periods if daylight hours are not explicitly represented as a feature. |
| **Mitigation** | Assess the seasonal and diurnal distribution of training data during exploratory analysis; ensure training data spans at least one full calendar year where possible; include daylight hours or sunrise/sunset times as explicit features |
| **Status** | Identifiable a priori — specific temporal distribution to be confirmed empirically |

---

### 3.5 Infrastructure Change Bias

| Field | Detail |
|-------|--------|
| **Bias type** | Historical bias / Deployment bias |
| **Pipeline stage** | Data / Deployment |
| **Description** | Hamburg's cycling infrastructure changes over time — new cycle lanes are added, road layouts are modified, and sensor locations may change. Historical traffic data reflects the infrastructure conditions at the time of collection. If the infrastructure has changed materially between the training data period and the deployment period, the model's learned relationships may no longer be valid. |
| **Consequence for model** | Distribution shift between training and deployment conditions; predictions may be systematically incorrect for routes where infrastructure has changed since the training data was collected. |
| **Mitigation** | Document the time period covered by training data; identify any known infrastructure changes during or since that period; include infrastructure change monitoring in the post-deployment monitoring plan |
| **Status** | Identifiable a priori — specific infrastructure changes to be assessed during data retrieval |

---

### 3.6 Public Transport Demand as Downstream Target

| Field | Detail |
|-------|--------|
| **Bias type** | Aggregation bias |
| **Pipeline stage** | Features / Deployment |
| **Description** | The project's second objective — forecasting public transport demand — uses bicycle traffic predictions as an input alongside additional data. Public transport demand aggregates across diverse user groups with heterogeneous relationships to weather and cycling behavior: commuters, leisure users, tourists, and mobility-impaired individuals respond differently to weather conditions and cycling availability. Treating public transport demand as a single aggregate target may obscure meaningful subgroup variation. |
| **Consequence for model** | A model optimized for aggregate demand prediction may systematically underperform for subgroups whose behavior diverges from the aggregate pattern — for example, predicting well for commuter-heavy routes while performing poorly for leisure-dominated routes. |
| **Mitigation** | Assess whether public transport demand data can be disaggregated by route type or user category; document the aggregation level at which predictions are made; flag subgroup performance as a known limitation in the model card |
| **Status** | Identifiable a priori — to be reassessed once the additional data sources for Phase 1 are confirmed |

---

### 3.7 API Data Provenance Bias

| Field | Detail |
|-------|--------|
| **Bias type** | Measurement bias |
| **Pipeline stage** | Data |
| **Description** | The provenance and collection methodology of the data provided by the public APIs is not fully transparent. The algorithms used to process raw sensor readings into published counts — including how sensor failures are handled, how anomalous readings are filtered, and how data gaps are imputed — may introduce systematic biases that are not visible in the published dataset. |
| **Consequence for model** | The model learns from processed data whose properties reflect not only real-world cycling behavior but also the assumptions embedded in the API provider's data processing pipeline. These assumptions are opaque and cannot be fully assessed without access to the raw sensor data. |
| **Mitigation** | Review available API documentation for information on data processing methodology; document known and unknown processing steps; acknowledge opaque provenance as a limitation in the model card |
| **Status** | Partially assessable a priori — to be supplemented with API documentation review during data retrieval |

---

## 4. A Priori Bias Summary

| Bias Source | Type | Stage | Severity | Mitigation Status |
|-------------|------|-------|----------|------------------|
| Sensor coverage | Representation | Data | Medium | Documented — to be quantified |
| Temporal coverage | Representation | Data | High | Documented — to be quantified |
| Weather granularity mismatch | Measurement | Data/Features | Medium | Documented — to be quantified |
| Seasonal and daylight | Representation/Historical | Data | High | Documented — mitigation planned |
| Infrastructure change | Historical/Deployment | Data/Deployment | Medium | Documented — monitoring planned |
| Public transport aggregation | Aggregation | Features/Deployment | Medium | Documented — scope dependent |
| API provenance opacity | Measurement | Data | Medium | Documented — partially mitigable |

**Severity scale:** High — likely to materially affect model performance or fairness; Medium — may affect performance in specific conditions; Low — minor or unlikely to affect outputs meaningfully.

---

## 5. Empirical Bias Sources

> **Status:** 🔜 Pending — to be completed during exploratory data analysis, before training commences.

This section documents biases identified empirically after data retrieval and initial exploratory analysis. It should be completed before training and must be reviewed before the model card and technical documentation are finalized.

The following questions should be addressed during exploratory analysis and documented here:

- What is the geographic distribution of traffic sensors, and which areas of Hamburg are underrepresented?
- What is the temporal distribution of data, and where are the gaps?
- Are there systematic differences in data quality or completeness across sensors, time periods, or weather conditions?
- Are the distributions of weather features and traffic counts consistent with domain knowledge about Hamburg's cycling patterns?
- Are there outliers or anomalies that suggest measurement errors or data processing artifacts?
- Are traffic counts at different sensor locations correlated in ways that suggest shared infrastructure dependencies?
- Does the relationship between weather features and traffic volume appear consistent across seasons, locations, and time of day?

---

## 6. Bias Mitigation Plan

The following mitigation measures are planned across the project pipeline. Specific implementation details will be documented in `docs/model/technical_documentation.md` and `docs/model/fairness_metrics.md`.

| Bias Source | Mitigation Measure | Phase |
|-------------|-------------------|-------|
| Sensor coverage | Document coverage gaps; limit generalization claims in model card | Before training |
| Temporal coverage | Assess and document gaps; consider imputation or exclusion | Before training |
| Weather granularity | Quantify station-sensor distances; consider spatial interpolation | Before training |
| Seasonal and daylight | Ensure full-year coverage; add daylight features | Before training |
| Infrastructure change | Document data period; include in monitoring plan | Before deployment |
| Public transport aggregation | Assess disaggregation options; document aggregation level | Before training |
| API provenance | Review API documentation; document processing methodology | Before training |
| Empirical biases (TBD) | To be defined after exploratory analysis | Before training |

---

## 7. Relationship to Other Documents

| Document | Relationship |
|----------|-------------|
| `docs/model/fairness_metrics.md` | Fairness metrics are selected on the basis of the bias sources identified here |
| `docs/model/model_card.md` | Known limitations section draws directly on this document |
| `docs/model/technical_documentation.md` | Data quality and representativeness assessment references this document |
| `docs/compliance/dpia.md` | Risk 1 (re-identification) and the proportionality assessment reference this document |
| `docs/data_governance/anonymization_strategy.md` | Shares the assessment of dataset characteristics |
| `docs/operations/monitoring_plan.md` | Infrastructure change bias informs the distribution shift monitoring plan |
| `docs/compliance/conformity_assessment.md` | Art. 10 compliance assessment references this document |
