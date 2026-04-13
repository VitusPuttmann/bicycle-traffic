# Fairness Metrics

> **Document status:** Initial draft — pre-model design (normative framework complete; empirical results pending)
> **Last updated:** 2026-04-10
> **Regulatory references:** EU AI Act Art. 10, 13, 15
> **Maintained by:** Vitus Püttmann (Data Controller and AI System Provider)

---

## 1. Purpose and Scope

This document defines the fairness criteria, proxy groups, evaluation methodology, and acceptance thresholds applied to the project's model, in accordance with EU AI Act Art. 10 (data governance) and Art. 15 (accuracy and robustness).

The document is structured in two stages:

- **Sections 1–5:** Completed before model design — normative framework and evaluation methodology
- **Section 6:** To be completed after training — empirical fairness results

This document is informed by the bias sources analysis (`docs/data_governance/bias_sources.md`) and informs the model card (`docs/model/model_card.md`), the technical documentation (`docs/model/technical_documentation.md`), and the conformity assessment (`docs/compliance/conformity_assessment.md`).

---

## 2. Fairness in the Context of This Project

### 2.1 Nature of the Prediction Task

The project produces aggregate predictions of bicycle traffic volume and, downstream, public transport demand. The model does not make decisions about or produce outputs directly relating to identified individuals. Classical fairness criteria developed for individual classification tasks therefore do not apply directly.

However, aggregate prediction models can be unfair in senses that matter for downstream resource allocation. If the model systematically underperforms for certain sensors, geographic areas, time periods, or infrastructure types, decisions informed by those predictions may disadvantage groups associated with those conditions. Fairness is therefore assessed at the level of **data subgroups** — subsets of the sensor network, time periods, and conditions — rather than at the level of individuals.

### 2.2 Relationship to Bias Sources

The fairness criteria and proxy groups defined in this document are selected on the basis of the bias sources identified in `docs/data_governance/bias_sources.md`. Each a priori bias source identified there generates a corresponding fairness concern addressed here:

| Bias Source | Fairness Concern | Addressed In |
|-------------|-----------------|--------------|
| Sensor coverage bias | Geographic fairness — does model perform equally across areas? | Section 3.1 |
| Temporal coverage bias | Temporal fairness — does model perform equally across periods? | Section 3.2 |
| Weather granularity mismatch | Condition fairness — does model perform equally across weather conditions? | Section 3.3 |
| Seasonal and daylight bias | Temporal fairness — does model perform equally across seasons? | Section 3.2 |
| Infrastructure change bias | Temporal fairness — does model degrade over time? | Section 3.2 |
| Public transport aggregation | Subgroup fairness — does model perform equally across route types? | Section 3.4 |

---

## 3. Proxy Groups

In the absence of individual-level protected attributes, fairness is assessed across the following proxy groups, each of which captures a dimension of potential systematic underperformance identified in the bias sources document.

### 3.1 Geographic Groups

| Group | Definition | Rationale |
|-------|-----------|-----------|
| **Infrastructure level** | Sensors on dedicated cycling infrastructure vs. sensors on shared or informal routes | Sensors on major infrastructure may have higher data quality and more stable relationships between weather and traffic, creating systematic performance differences |
| **Urban area type** | Inner city vs. outer districts | Cycling patterns and weather sensitivity may differ systematically between central and peripheral areas |
| **Sensor density zone** | High-density sensor areas vs. low-density sensor areas | Low-density areas have fewer data points and less cross-validation opportunity, potentially leading to higher prediction error |

### 3.2 Temporal Groups

| Group | Definition | Rationale |
|-------|-----------|-----------|
| **Season** | Spring, Summer, Autumn, Winter | Cycling rates and weather sensitivity differ substantially across seasons; a model trained predominantly on summer data may underperform in winter |
| **Time of day** | Peak hours (07:00–09:00, 16:00–18:00), off-peak, overnight | Cycling patterns and their relationship to weather differ across the day |
| **Day type** | Weekday vs. weekend vs. public holiday | Cycling behavior is structurally different across day types |
| **Daylight condition** | Daylight hours vs. twilight vs. darkness | Cycling rates are sensitive to daylight availability independently of weather |

### 3.3 Weather Condition Groups

| Group | Definition | Rationale |
|-------|-----------|-----------|
| **Precipitation** | Dry conditions vs. light rain vs. heavy rain | Precipitation has a nonlinear effect on cycling rates; model may be less accurate for extreme precipitation events that are underrepresented in training data |
| **Temperature range** | Cold (< 5°C) vs. mild (5–20°C) vs. warm (> 20°C) | Extreme temperatures may be underrepresented in training data relative to their real-world frequency |
| **Wind speed** | Low vs. moderate vs. high wind | High wind events may be rare in training data and disproportionately affect cycling rates |

### 3.4 Route Type Groups (Public Transport Demand)

| Group | Definition | Rationale |
|-------|-----------|-----------|
| **Commuter routes** | Routes connecting residential areas to employment centers | Demand patterns are more weather-sensitive and time-structured than leisure routes |
| **Leisure routes** | Routes connecting parks, waterways, and recreational areas | Demand is more sensitive to weekend and seasonal effects |

> ⚠️ **Note:** Route type classification depends on additional data sources not yet confirmed. This group definition is provisional and subject to revision once those sources are specified.

---

## 4. Fairness Criteria

### 4.1 Primary Criterion: Calibration Across Subgroups

**Definition:** The model's predictions are equally well-calibrated across all proxy groups — a predicted traffic volume of X units is equally accurate regardless of the sensor, time period, or weather condition to which it relates.

**Rationale:** Calibration is the most appropriate primary fairness criterion for a regression model producing aggregate predictions. It directly captures whether the model's outputs can be trusted equally across all conditions, which is the property most relevant to downstream use in resource allocation.

**Measurement:** For each proxy group g, compute the mean prediction error (MPE) and mean absolute error (MAE):

- MPE_g = mean(predicted_g - actual_g)
- MAE_g = mean(|predicted_g - actual_g|)

Calibration fairness is assessed by comparing MPE and MAE across groups. Systematic positive or negative MPE for a specific group indicates directional miscalibration for that group.

### 4.2 Secondary Criterion: Equalized Residuals Across Subgroups

**Definition:** The distribution of prediction errors (residuals) is consistent across proxy groups — no group experiences systematically larger or more variable errors than others.

**Rationale:** Even a well-calibrated model (zero mean error) may have higher variance for some groups, making predictions less reliable for those groups. Equalized residuals captures this second-order fairness concern.

**Measurement:** For each proxy group g, compute the root mean squared error (RMSE) and the standard deviation of residuals (SD_residuals):

- RMSE_g = sqrt(mean((predicted_g - actual_g)²))
- SD_residuals_g = std(predicted_g - actual_g)

Equalized residuals fairness is assessed by comparing RMSE and SD_residuals across groups.

### 4.3 Tertiary Criterion: Performance Across Data Density Levels

**Definition:** The model does not systematically underperform for sensors or time periods with lower data density — areas and periods with fewer historical observations should not be consistently associated with larger prediction errors.

**Rationale:** Low-density areas are structurally disadvantaged in data-driven models. If prediction quality correlates with data density, the model's outputs will be least reliable precisely where the data is most sparse — which, as noted in the bias sources document, may correlate with lower infrastructure investment and lower socioeconomic status.

**Measurement:** Correlate prediction error metrics (MAE, RMSE) with data density (number of observations per sensor per time period) across the test set. A significant positive correlation indicates that error increases with decreasing data density.

---

## 5. Acceptance Thresholds

Acceptance thresholds define the maximum permissible disparity in fairness metrics across proxy groups. These are defined before training to prevent post-hoc threshold selection.

> **Note:** The specific threshold values below are provisional and should be reviewed in light of the empirical distribution of errors observed during training.

| Criterion | Metric | Threshold | Rationale |
|-----------|--------|-----------|-----------|
| Calibration | Max |MPE_g| across groups | ≤ 15% of overall MAE | Directional bias greater than 15% of overall error is considered materially significant |
| Calibration | Max ratio of MAE_g to overall MAE | ≤ 1.5 | No group should have error more than 50% higher than the overall model error |
| Equalized residuals | Max ratio of RMSE_g to overall RMSE | ≤ 1.5 | Consistent with calibration threshold |
| Data density performance | Correlation of MAE with data density | |r| ≤ 0.3 | Weak or negligible correlation between error and data density |

Where a threshold is exceeded, the finding must be documented in the model card and technical documentation, and a mitigation measure must be proposed before the model is considered acceptable for use.

---

## 6. Empirical Fairness Results

> **Status:** 🔜 Pending — to be completed after model training and evaluation.

This section documents the measured fairness metrics for the trained model across all proxy groups defined in section 3. It must be completed before the model card and technical documentation are finalized, and before the model is used for any downstream purpose.

For each proxy group, the following must be reported:

- Sample size (number of observations in the group within the test set)
- MPE, MAE, RMSE, and SD_residuals
- Comparison to overall model metrics
- Assessment against acceptance thresholds in section 5
- Flag if any threshold is exceeded, with proposed mitigation

---

## 7. Fairness-Accuracy Trade-off

Imposing fairness constraints may reduce overall model accuracy. This trade-off should be explicitly assessed and documented during training:

- If a fairness constraint causes overall RMSE to increase by more than 10% relative to an unconstrained model, the trade-off must be documented and justified
- The decision to accept a fairness-accuracy trade-off must be recorded here, with the rationale
- The model card must communicate the trade-off to downstream users

---

## 8. Relationship to Other Documents

| Document | Relationship |
|----------|-------------|
| `docs/data_governance/bias_sources.md` | Bias sources inform the proxy groups and fairness criteria defined in this document |
| `docs/model/performance_thresholds.md` | Overall performance thresholds complement the subgroup fairness thresholds defined here |
| `docs/model/model_card.md` | Empirical fairness results and known limitations are reported in the model card |
| `docs/model/technical_documentation.md` | Fairness evaluation methodology and results are documented in the technical documentation |
| `docs/compliance/conformity_assessment.md` | Art. 10 and Art. 15 compliance assessments reference this document |
