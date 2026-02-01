from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.models import DeployRequest, RiskRequest
from backend.risk_engine import calculate_risk
from backend.audit import log_event

# ✅ CREATE APP FIRST
app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# ✅ THEN ADD MIDDLEWARE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- ROUTES ----------

@app.get("/")
def root():
    return {"status": "AI DevSecOps Control Plane Running"}

@app.post("/deploy")
def deploy(payload: DeployRequest):
    log_event("DEPLOY_REQUESTED", payload.dict())
    return {"status": "Pipeline triggered"}

@app.post("/risk-score")
def risk_score(data: RiskRequest):
    result = calculate_risk(data.dict())
    log_event("RISK_EVALUATED", result)
    return result

@app.get("/audit-logs")
def audit_logs():
    return {"logs": "Audit logs visible"}
