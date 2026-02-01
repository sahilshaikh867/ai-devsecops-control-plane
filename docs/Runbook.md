

# 🚀 AI DevSecOps Control Plane – Complete Run Guide

This document provides **error-free, step-by-step instructions** to run the AI DevSecOps Control Plane project from scratch, including backend, frontend, and verification steps.

---

## 📁 Step 0: Project Structure Verification

Ensure the project structure is as follows:

```

A01/
│
├── backend/
│   ├── **init**.py
│   ├── main.py
│   ├── models.py
│   ├── risk_engine.py
│   └── audit.py
│
├── frontend/
│   └── index.html
│
├── docs/
│   └── architecture.md
│
├── cicd/
│   └── pipeline.md
│
├── infra/
│   └── infra_plan.md
│
├── README.md
└── .gitignore

````

📸 **Screenshot Placeholder:**  
![Folder-Structure](img/Folder.png)
---

## 🐍 Step 1: Create & Activate Virtual Environment

Open **PowerShell** and navigate to the project root:

```powershell
cd C:\Users\user5\Downloads\A01
python -m venv .venv
````

Activate the virtual environment:

```powershell
& C:\Users\user5\Downloads\A01\.venv\Scripts\Activate.ps1
```

Expected output:

```
(.venv)
```

📸 **Screenshot Placeholder:**

> ![venve](img/venve.png)

---

## 📦 Step 2: Install Dependencies

Install required Python packages:

```powershell
python -m pip install --upgrade pip
python -m pip install fastapi uvicorn
```

Verify installation:

```powershell
python -m uvicorn --version
```

📸 **Screenshot Placeholder:**

> ![Folder-Structure](img/uvicorn.png)

---

## 🚀 Step 3: Start Backend Server

Run the FastAPI backend:

```powershell
python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

Expected output:

```
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
```

📸 **Screenshot Placeholder:**

> ![Folder-Structure](img/server.png)

---

## 🌐 Step 4: Verify Backend Root Endpoint

Open browser and visit:

```
http://127.0.0.1:8000/
```

Expected response:

```json
{
  "status": "AI DevSecOps Control Plane Running"
}
```

📸 **Screenshot Placeholder:**

> *Browser showing root API JSON response*

---

## 📘 Step 5: Open Swagger UI

Open the Swagger documentation:

```
http://127.0.0.1:8000/docs
```

Available endpoints:

* GET `/`
* POST `/deploy`
* POST `/risk-score`
* GET `/audit-logs`

📸 **Screenshot Placeholder:**

> ![Folder-Structure](img/swagger.png)

---

## 🧪 Step 6: Test Deployment API (`/deploy`)

In Swagger UI:

1. Select **POST /deploy**
2. Click **Try it out**
3. Use the payload below:

```json
{
  "service_name": "demo-app",
  "environment": "production",
  "requested_by": "admin"
}
```

4. Click **Execute**

Expected response:

```json
{
  "status": "Pipeline triggered"
}
```

Terminal output:

```
[AUDIT] DEPLOY_REQUESTED: {...}
```

📸 **Screenshot Placeholders:**

> ![Folder-Structure](img/swagger-deploy.png)
> ![Folder-Structure](img/swagger-risk.png)
---

## 🤖 Step 7: Test AI Risk Scoring API (`/risk-score`)

In Swagger UI:

1. Select **POST /risk-score**
2. Click **Try it out**
3. Use the payload below:

```json
{
  "critical": 1,
  "infra_instability": 1,
  "peak_hours": 1,
  "past_failures": 1
}
```

4. Click **Execute**

Expected response:

```json
{
  "risk_score": 75,
  "decision": "BLOCK"
}
```

Terminal output:

```
[AUDIT] RISK_EVALUATED: {...}
```

📸 **Screenshot Placeholders:**

> ![Folder-Structure](img/trigger.png)
> ![Folder-Structure](img/risk.png)

---

## 🖥️ Step 8: Run Frontend Dashboard

Navigate to:

```
frontend/index.html
```

Open the file by **double-clicking** it in a browser.

The UI displays:

* Trigger Deploy button
* Check Risk button
* Response display panel

📸 **Screenshot Placeholder:**

> *Frontend dashboard loaded in browser*

---

## 🖱️ Step 9: Frontend → Backend Interaction

### Trigger Deployment

* Click **Trigger Deploy**
* Response displayed:

```json
{
  "status": "Pipeline triggered"
}
```

### Check Risk

* Click **Check Risk**
* Response displayed:

```json
{
  "risk_score": 75,
  "decision": "BLOCK"
}
```

📸 **Screenshot Placeholders:**

> ![Folder-Structure](img/UI.png)
> *Frontend showing risk decision*

---

## 🏁 Final Result

### ✅ Achievements

* Backend APIs running successfully
* AI-based risk evaluation executed
* Deployment decisions enforced
* Audit logs generated
* Frontend integrated with backend

📸 **Screenshot Placeholder:**

> *Combined view: Swagger + Frontend + Terminal*

---

## 🎓 Conclusion

This project demonstrates a **fully functional AI-driven DevSecOps Control Plane** with:

* Explainable AI risk scoring
* Secure API-based control
* Audit-ready governance
* Web-based user interaction

---

**End of Run Guide** ✅

