# Roles & Responsibilities

> **Document status:** Initial draft  
> **Last updated:** 2026-04-07  
> **Regulatory references:** GDPR Art. 4, 26, 28, 37–39; EU AI Act Art. 3

---

## 1. GDPR Roles

### 1.1 Data Controller

| Field | Detail |
|-------|--------|
| **Name** | Vitus Püttmann |
| **Email** | vitus.puettmann@web.de |
| **Role** | Data Controller per GDPR Art. 4(7) |
| **Basis** | Determines the purposes and means of processing as the sole individual responsible for this project |

The data controller is the natural person who decides why and how personal data is processed. In this project, all such decisions rest exclusively with Vitus Püttmann.

### 1.2 Data Processors

A data processor is any natural or legal person that processes data on behalf of the controller (GDPR Art. 4(8)), and must be bound by a Data Processing Agreement (DPA) per Art. 28.

| Processor | Service | Data Involved | DPA Required | Notes |
|-----------|---------|---------------|--------------|-------|
| **Microsoft** | Version control and public code repository (GitHub); cloud storage and sync (OneDrive) | Source code, documentation, and any data derivatives explicitly committed to GitHub; any project files located in OneDrive-synced directories | Yes — covered by Microsoft's Data Protection Agreement, applicable to both GitHub and OneDrive | Raw data and personal data are not uploaded to GitHub and are explicitly excluded from OneDrive sync. Microsoft's DPA is accepted upon account creation for both services. Data residency is within the EEA; to be verified and documented in the Processing Activities Register. |
| **API Provider (weather data)** | Public open-access weather data API | API requests originating from the controller's machine | No personal data transmitted per current knowledge — to be reassessed if API key or account registration becomes required | Provider to be specified once data source is confirmed |
| **API Provider (bicycle traffic data)** | Public open-access bicycle traffic data API | API requests originating from the controller's machine | No personal data transmitted per current knowledge — to be reassessed if API key or account registration becomes required | Provider to be specified once data source is confirmed |

> ⚠️ **Note:** All data processing takes place exclusively on the controller's local machine. No data is transferred to cloud services, remote storage, or third-party platforms beyond what is explicitly described above. This significantly limits the processor surface.

### 1.3 Joint Controllers

Joint controllership under GDPR Art. 26 applies where two or more parties jointly determine the purposes and means of processing. **This does not apply** to this project: all processing decisions are made solely by Vitus Püttmann. No institutional, academic, or commercial collaboration is involved.

### 1.4 Data Protection Officer (DPO)

Under GDPR Art. 37, designation of a DPO is mandatory for public authorities, organizations carrying out large-scale systematic monitoring, or organizations processing special categories of data at large scale. **No DPO is required** for this project on the following grounds:

- The controller is a private individual
- Processing is carried out for purely educational purposes
- No large-scale processing takes place
- No special categories of data (Art. 9) are actually processed; sensitive data handling is simulated as a compliance learning exercise

This assessment should be revisited if the scope of the project changes materially.

### 1.5 EU Representative

An EU representative under GDPR Art. 27 is required only where a controller or processor is not established in the EU. **This does not apply:** the controller is an individual established and resident in the EU.

### 1.6 Competent Supervisory Authority

The supervisory authority with territorial jurisdiction for this project is:

| Field | Detail |
|-------|--------|
| **Authority** | Hamburgische Beauftragte für Datenschutz und Informationsfreiheit (HmbBfDI) |
| **Website** | [datenschutz.hamburg.de](https://datenschutz.hamburg.de) |
| **Jurisdiction** | Hamburg, Germany — place of residence and processing of the controller |

---

## 2. EU AI Act Roles

### 2.1 Provider

| Field | Detail |
|-------|--------|
| **Name** | Vitus Püttmann |
| **Email** | vitus.puettmann@web.de |
| **Role** | Provider per EU AI Act Art. 3(3) |
| **Basis** | Develops the AI system and makes it publicly available via GitHub under their own name |

The provider is responsible for technical documentation, conformity assessment, and post-market monitoring obligations under the EU AI Act. In this project, all provider obligations rest with Vitus Püttmann.

### 2.2 Deployer

| Field | Detail |
|-------|--------|
| **Name** | Vitus Püttmann |
| **Email** | vitus.puettmann@web.de |
| **Role** | Deployer per EU AI Act Art. 3(4) |
| **Basis** | Operates the AI system under their own authority for educational purposes |

The deployer is responsible for human oversight and appropriate use obligations under the EU AI Act. **In this project, provider and deployer are the same individual.** This concentration of roles is explicitly acknowledged: all obligations assigned separately to providers and deployers by the EU AI Act are borne by a single person.

### 2.3 Authorised Representative

An authorised representative under EU AI Act Art. 22 is required only where a provider is not established in the EU. **This does not apply:** the provider is an individual established in the EU.

---

## 3. Summary Table

| Role | Regulatory Reference | Assigned To |
|------|----------------------|-------------|
| Data Controller | GDPR Art. 4(7) | Vitus Püttmann |
| Data Processor — Microsoft (GitHub & OneDrive) | GDPR Art. 4(8), Art. 28 | Microsoft |
| Data Processor — Weather API | GDPR Art. 4(8) | To be specified |
| Data Processor — Traffic API | GDPR Art. 4(8) | To be specified |
| Joint Controller | GDPR Art. 26 | Not applicable |
| Data Protection Officer | GDPR Art. 37 | Not required |
| EU Representative (GDPR) | GDPR Art. 27 | Not applicable |
| Supervisory Authority | GDPR Art. 4(21) | HmbBfDI, Hamburg |
| AI System Provider | EU AI Act Art. 3(3) | Vitus Püttmann |
| AI System Deployer | EU AI Act Art. 3(4) | Vitus Püttmann |
| Authorised Representative (AI Act) | EU AI Act Art. 22 | Not applicable |

---
