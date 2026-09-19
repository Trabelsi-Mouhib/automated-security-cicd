# 🛡️ Automated DevSecOps CI/CD Pipeline

![Build Status](https://img.shields.io/github/actions/workflow/status/Trabelsi-Mouhib/automated-security-cicd/security-pipeline.yml?branch=main&label=DevSecOps%20Pipeline)
![Docker Image](https://img.shields.io/badge/GHCR-devsecops--app-blue?logo=docker)
![Security Stack](https://img.shields.io/badge/Security-TruffleHog%20%7C%20Semgrep%20%7C%20Snyk%20%7C%20Trivy%20%7C%20ZAP-red)

This project implements an enterprise-grade **DevSecOps** software factory based on a containerized Python (Flask) application. It features end-to-end security test automation integrated into GitHub Actions—combining **SAST**, **SCA**, **Secret Scanning**, **Container Scanning**, and **DAST**—paired with Continuous Delivery (**CD**) to **GitHub Container Registry (GHCR)**.

---

## 📐 Pipeline Architecture

The pipeline follows the **"Shift Left"** security principle: every code change is scanned early in the development lifecycle. If any security check fails, branch protection rules physically block merging into the `main` branch.

```mermaid
graph TD
    A[Push / PR to GitHub] --> B(1. TruffleHog: Secret Scanning)
    A --> C(2. Semgrep: SAST)
    A --> D(3. Snyk: SCA)
    A --> E(4. Trivy: Container Scan)
    
    C --> F(5. OWASP ZAP: DAST)
    D --> F
    E --> F
    
    F --> G{Security Quality Gates Passed?}
    G -- Yes (main branch) --> H[CD: Publish Docker Image to GHCR]
    G -- No (Vulnerable PR) --> I[Automatic Merge Blocked]
```

---

## 🛠️ Tech & Security Stack

| Category | Tool | Pipeline Role |
| :--- | :--- | :--- |
| **Application** | Python / Flask | Containerized REST API |
| **CI/CD & Registry** | GitHub Actions / GHCR | Workflow orchestration and production Docker image hosting |
| **Secret Scanning** | **TruffleHog** | Automated detection of hardcoded API keys, tokens, and credentials |
| **SAST** | **Semgrep** | Static source code analysis (command injection, OWASP Top 10) |
| **SCA** | **Snyk** | Dependency vulnerability scanning (`requirements.txt`) and CVE tracking |
| **Container Scan** | **Trivy** | OS package and base Docker image vulnerability scanning |
| **DAST** | **OWASP ZAP** | Dynamic application security testing on a running container |

---

## 🔒 Security Quality Gates Demonstration

This repository demonstrates automated security enforcement across two dedicated branches:

### 1. `main` Branch (Production Ready)
* Contains secure code and patched dependencies (`werkzeug>=3.0.6`).
* All security checks pass successfully.
* **Result:** The Docker image is built and automatically published to **GHCR**.

![Pipeline Success](docs/images/pipeline-success.png)

### 2. `vulnerable-demo` Branch (Blocking Simulation)
* Contains intentionally injected vulnerabilities:
  * **SAST:** Command injection via `os.system()` in `app.py`.
  * **SCA:** Outdated Python dependencies with known CVEs in `requirements.txt`.
  * **Secrets:** Hardcoded credentials/tokens.
* **Result:** GitHub Actions flags all issues, posts inline security comments directly on the code diff, and **blocks pull request merging**.

![PR Blocked](docs/images/pr-blocked.png)

![Security Findings](docs/images/security-findings.png)

---

## 🚀 Getting Started & Deployment

### Pull Production Image from GHCR
To download and run the verified production image directly from GitHub Container Registry:

```bash
docker pull ghcr.io/trabelsi-mouhib/automated-security-cicd:latest
docker run -d -p 5000:5000 ghcr.io/trabelsi-mouhib/automated-security-cicd:latest
```

### Local Setup
```bash
# Clone the repository
git clone [https://github.com/Trabelsi-Mouhib/automated-security-cicd.git](https://github.com/Trabelsi-Mouhib/automated-security-cicd.git)
cd automated-security-cicd

# Build and run locally with Docker
docker build -t app:local .
docker run -p 5000:5000 app:local
```

---

## 📂 Repository Structure

```text
.
├── .github/
│   └── workflows/
│       └── security-pipeline.yml   # DevSecOps GitHub Actions workflow
├── app.py                          # Flask API application
├── Dockerfile                      # Container build instructions
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## 👤 Author

* **Mouhib Trabelsi** - [GitHub Profile](https://github.com/Trabelsi-Mouhib)