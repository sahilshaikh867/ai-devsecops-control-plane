from pydantic import BaseModel

class DeployRequest(BaseModel):
    service_name: str
    environment: str
    requested_by: str

class RiskRequest(BaseModel):
    critical: int
    infra_instability: int
    peak_hours: int
    past_failures: int
