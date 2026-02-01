def calculate_risk(data):
    security = data.get("critical", 0) * 30
    infra = data.get("infra_instability", 0) * 20
    context = data.get("peak_hours", 0) * 15
    history = data.get("past_failures", 0) * 10

    total = security + infra + context + history

    if total > 70:
        decision = "BLOCK"
    elif total > 40:
        decision = "CANARY"
    else:
        decision = "ALLOW"

    return {
        "risk_score": total,
        "decision": decision
    }
