# Incident Response Plan

> **Document status:** Initial draft
> **Last updated:** 2026-04-10
> **Regulatory references:** GDPR Art. 33, 34, 33(5); EU AI Act Art. 73
> **Maintained by:** Vitus Püttmann (Data Controller)

---

## 1. Purpose and Scope

This document defines the procedures for detecting, classifying, investigating, containing, and reporting incidents arising from the processing activities carried out in this project. It covers four incident categories relevant to the project's specific characteristics: accidental data publication, unauthorized local access, model failure, and credential exposure.

As documented in `docs/compliance/legal_basis.md`, the data processed in this project does not constitute personal data within the meaning of GDPR Art. 4(1). GDPR breach notification obligations under Art. 33 and 34 therefore do not strictly apply.

All incident response responsibilities rest with the data controller: Vitus Püttmann (vitus.puettmann@web.de).

---

## 2. Incident Classification

Incidents are classified on two dimensions prior to response:

**Severity**
- 🔴 **Critical** — data or credentials are publicly exposed or the system is producing harmful outputs; immediate action required
- 🟠 **High** — data or credentials are exposed to an unauthorized party but not publicly; urgent action required within hours
- 🟡 **Medium** — potential exposure identified but not confirmed; investigation required within 24 hours
- 🟢 **Low** — no exposure; operational anomaly requiring investigation but no immediate risk

**Notification obligation (when sensitive data is concerned)**
- **Notifiable** — likely to result in risk to the rights and freedoms of data subjects; supervisory authority notification required within 72 hours under GDPR Art. 33
- **Documented only** — no likely risk to data subjects; internal documentation required under GDPR Art. 33(5) but no notification obligation
- **Not applicable** — data is not personal; no GDPR notification obligation in the current project context

---

## 3. The 72-Hour Clock

When sensitive data is concerned, the GDPR Art. 33 notification window begins running from the moment the controller becomes **aware** of a breach — defined as the point at which the controller has reasonable certainty that a security incident has occurred that has resulted in the accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, personal data.

Awareness does not require complete knowledge of the breach's scope. The 72-hour clock starts when the controller has sufficient information to determine that a breach has likely occurred, not when the investigation is complete. Where full information is not available within 72 hours, an initial notification is submitted with available information, followed by supplementary notifications as the investigation progresses.

For this project, the controller is the sole responsible party. The clock starts when the controller personally becomes aware of the incident.

---

## 4. Incident Response Procedures

### 4.1 Data Breach — Accidental Publication

**Description:** Data files, model outputs, or other content containing personal or sensitive information are accidentally committed to the public GitHub repository and pushed to the remote.

**Severity:** 🔴 Critical — public exposure begins immediately upon push.

**Notification obligation (when sensitive data is concerned):** Notifiable — public exposure constitutes a high-risk breach under GDPR Art. 33 and likely triggers Art. 34 communication to data subjects.

#### Detection
- Pre-commit review identifies a staged data file before push — escalate to containment immediately, push does not occur
- Post-push: accidental inclusion noticed during routine repository review, via a GitHub notification, or reported by a third party

#### Containment
1. **Take the repository private immediately** on GitHub (Settings → Danger Zone → Change repository visibility) to limit further public access
2. Do not delete the commit or attempt remediation before taking the repository private — every second the repository remains public increases exposure
3. Note the exact time at which the push occurred and the time at which the repository was made private — this window defines the exposure period
4. Identify the specific files exposed: their content, the data categories involved, and whether they contain personal data

#### Investigation
5. Determine how the file entered version control — was it absent from `.gitignore`, or was `.gitignore` itself misconfigured?
6. Assess whether the file was indexed by search engines, cached by GitHub, or accessed by any third party during the exposure window — check repository traffic analytics if available
7. Assess whether forks were created during the exposure window

#### Remediation
8. Remove the file from repository history using `git filter-repo`:
   ```bash
   git filter-repo --path <filepath> --invert-paths
   ```
9. Force push the rewritten history:
   ```bash
   git push origin --force --all
   git push origin --force --tags
   ```
10. Contact GitHub Support to request server-side cache purge
11. Add the file pattern to `.gitignore` if not already present
12. Restore the repository to public once history has been cleaned and cache purge confirmed — or leave private if the exposure risk justifies it
13. When sensitive data is concerned: rotate any exposed credentials; notify affected data subjects if required under Art. 34; notify HmbBfDI within 72 hours of becoming aware

#### Post-Incident
14. Update the incident log in section 6
15. Review and strengthen pre-commit review practices
16. Assess whether a `.gitignore` linting tool or pre-commit hook should be introduced to prevent recurrence

---

### 4.2 Data Breach — Unauthorized Local Access

**Description:** An unauthorized party gains access to the controller's local machine — through physical theft, malware, remote exploitation, or unauthorized physical access — and may have accessed locally stored data files.

**Severity:** 🔴 Critical if confirmed access to data files; 🟠 High if device is compromised but data access is unconfirmed.

**Notification obligation (when sensitive data is concerned):** Notifiable if access to personal data is confirmed or cannot be ruled out.

#### Detection
- Device reported stolen or physically missing
- Antivirus or endpoint security tool reports malware or unauthorized remote access
- Unusual file access patterns or login events identified in system logs
- Unexpected network traffic suggesting data exfiltration

#### Containment
1. **Isolate the device** from all networks immediately — disable Wi-Fi, disconnect Ethernet, disable Bluetooth
2. Do not power off the device if forensic investigation is anticipated — powering off may destroy volatile evidence; consult a professional if in doubt
3. Change passwords for all accounts accessible from the device, particularly GitHub, email, and any API accounts, from a separate, uncompromised device
4. Revoke and rotate any API keys or tokens that were stored on the compromised device
5. Suspend OneDrive sync from a separate device if the compromised machine had access

#### Investigation
6. Determine the nature and timeline of the compromise — when did unauthorized access begin, what was accessible, and what evidence of data access or exfiltration exists
7. Identify which data files were stored on the device at the time of the incident and assess whether they were accessed or copied
8. Review system access logs, file access timestamps, and network logs for evidence of data exfiltration
9. When sensitive data is concerned: determine whether the accessed data constitutes personal data and whether the breach meets the Art. 33 notification threshold

#### Remediation
10. Restore the device from a clean backup or perform a full reinstall before returning it to use
11. Re-enable full-disk encryption and verify all security measures are in place before restoring data
12. When sensitive data is concerned: notify HmbBfDI within 72 hours if personal data access is confirmed or cannot be ruled out; notify affected data subjects if high risk is established under Art. 34
13. File a police report if the device was stolen — this creates an official record relevant to any regulatory inquiry

#### Post-Incident
14. Update the incident log in section 6
15. Review and strengthen local security measures — encryption, access controls, screen lock timeout
16. Assess whether sensitive data should be stored in an encrypted container rather than directly on the filesystem

---

### 4.3 Model Failure

**Description:** The model produces systematically incorrect, biased, or otherwise unreliable predictions due to data quality issues, distribution shift, implementation errors, or other causes.

**Severity:** 🟡 Medium in training context; 🔴 Critical in a deployment context where predictions inform decisions.

**Notification obligation:** Not a GDPR breach. In a real high-risk AI deployment, systematic model failure may trigger EU AI Act Art. 73 serious incident reporting if it causes or contributes to harm.

#### Detection
- Evaluation metrics during routine model assessment fall below defined performance thresholds
- Distribution shift detected in incoming data relative to training data distribution
- Unexpected model behavior identified during manual review of predictions
- Anomalous outputs flagged by monitoring infrastructure

#### Containment
1. **Suspend use of model outputs** for any downstream purpose until the failure is understood and resolved — in an operational context this means ceasing automated use immediately
2. Document the point in time at which the failure was first detected and the point at which it is believed to have begun — these may differ if the failure developed gradually
3. Preserve the failing model artifact and the data on which the failure was observed — do not overwrite until investigation is complete

#### Investigation
4. Determine the root cause from the following categories:
   - **Data quality failure** — errors, gaps, or anomalies in the input data
   - **Distribution shift** — the statistical properties of incoming data have diverged from the training data distribution
   - **Implementation error** — a bug in the preprocessing, feature engineering, or inference pipeline
   - **Model degradation** — the model's parameters are no longer appropriate for the current data distribution
5. Quantify the scope of the failure — which predictions were affected, over what time period, and to what degree
6. In a real operational context: assess whether any decisions informed by the failing model caused harm to individuals or organizations

#### Remediation
7. Address the root cause:
   - Data quality failure → clean or re-source the affected data; review data validation pipeline
   - Distribution shift → retrain the model on more recent data; implement drift detection in monitoring
   - Implementation error → fix the bug; add a regression test to prevent recurrence; review related code paths
   - Model degradation → retrain or fine-tune; review retraining schedule
8. Validate the remediated model against performance thresholds before restoring use
9. In a real operational context: assess whether affected decisions need to be reviewed or reversed; notify affected parties if required

#### Post-Incident
10. Update the incident log in section 6
11. Review and strengthen monitoring and drift detection infrastructure

---

### 4.4 Credential Exposure

**Description:** API keys, access tokens, passwords, or other credentials are accidentally committed to the public GitHub repository, included in published documentation, or otherwise disclosed to unauthorized parties.

**Severity:** 🔴 Critical — credential exposure creates the immediate conditions for unauthorized data access and must be treated with equivalent urgency to a confirmed breach.

**Notification obligation:** Documented only in isolation — credential exposure is not itself a data breach. However, if the exposed credentials are used to access personal data before they are rotated, the resulting unauthorized access constitutes a notifiable breach under Art. 33.

#### Detection
- Pre-commit review identifies a staged credential before push
- Post-push: credential identified in repository during routine review or reported by a third party
- GitHub's secret scanning feature generates an alert — GitHub automatically scans public repositories for known credential patterns and notifies repository owners
- An API provider notifies the controller of suspicious usage patterns consistent with credential theft

#### Containment
1. **Revoke and rotate the exposed credential immediately** — this is the single most important action and takes priority over all others. Do not delay rotation to investigate first; the credential is compromised from the moment of exposure
2. Contact the relevant API provider to confirm revocation and check access logs for unauthorized use during the exposure window
3. If the credential was committed to the repository: take the repository private immediately, following the procedure in section 4.1 steps 1–3

#### Investigation
4. Determine the exposure window — from the time of the commit or publication to the time of revocation
5. Review API provider access logs for the exposure window to determine whether the credential was used by an unauthorized party
6. Identify how the credential entered version control or documentation — was it hardcoded in a script, included in a configuration file, or embedded in a notebook output?
7. If unauthorized use is confirmed: assess what data or systems were accessed and whether a personal data breach has occurred

#### Remediation
8. Remove the credential from repository history using `git filter-repo`, following the procedure in section 4.1 steps 8–12
9. Add the credential pattern to `.gitignore` and, where appropriate, to a `.env` file excluded from version control
10. Implement environment variable management for all credentials — no credential should ever appear in source code or documentation
11. If unauthorized access to personal data is confirmed: escalate to the data breach procedure in section 4.2 and assess Art. 33 notification obligation

#### Post-Incident
12. Update the incident log in section 6
13. Review all other credentials in use — if one credential was exposed through careless handling, others may be at similar risk
14. Assess whether a secrets scanning pre-commit hook should be introduced to prevent recurrence

---

## 5. Supervisory Authority Contact

When sensitive data is concerned, Art. 33 notifications are submitted to:

| Field | Detail |
|-------|--------|
| **Authority** | Hamburgische Beauftragte für Datenschutz und Informationsfreiheit (HmbBfDI) |
| **Website** | [datenschutz.hamburg.de](https://datenschutz.hamburg.de) |
| **Online notification** | Available via the HmbBfDI website |

---

## 6. Incident Log

All incidents — regardless of severity and regardless of whether they trigger a notification obligation — are recorded below in accordance with GDPR Art. 33(5).

| ID | Date Detected | Category | Severity | Description | Actions Taken | Notified | Closed |
|----|--------------|----------|----------|-------------|---------------|---------|--------|
| — | — | — | — | — | — | — | — |

---

## 9. Relationship to Other Documents

| Document | Relationship |
|----------|-------------|
| `docs/compliance/processing_activities.md` | Identifies data categories and processors relevant to scoping a breach |
| `docs/operations/roles_responsibilities.md` | Supplies supervisory authority contact details for Art. 33 notification |
| `docs/compliance/dpia.md` | Risk assessments inform the severity classification of incidents |
| `docs/data_governance/retention_policy.md` | Deletion procedures are relevant to containment and remediation |
| `docs/data_governance/anonymization_strategy.md` | Informs assessment of whether exposed data constitutes personal data |
