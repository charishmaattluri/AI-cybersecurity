# risk_engine.py

def analyze_logs(logs):
    score = 0
    reasons = []

    for log in logs:
        if log["event_type"] == "email" and "urgent" in log["details"].lower():
            score += 30
            reasons.append("Suspicious email language detected")

        if log["event_type"] == "login" and log["location"] != "India":
            score += 40
            reasons.append("Login from unusual location")

        if log["event_type"] == "file_access" and "bulk" in log["details"].lower():
            score += 50
            reasons.append("Unusual bulk file access")

    if score >= 70:
        level = "High"
        action = "Lock account and force password reset"
    elif score >= 40:
        level = "Medium"
        action = "Alert administrator"
    else:
        level = "Low"
        action = "Monitor activity"

    explanation = (
        f"This activity is classified as {level} risk because "
        + ", ".join(reasons)
        + "."
    )

    return {
        "risk_score": score,
        "risk_level": level,
        "explanation": explanation,
        "recommended_action": action
    }


# ✅ NEW FUNCTIONS (THIS FIXES YOUR ERROR)

def analyze_phishing():
    logs = [
        {
            "event_type": "email",
            "details": "Urgent password reset required"
        },
        {
            "event_type": "login",
            "location": "Russia",
            "details": "Login attempt"
        }
    ]
    return analyze_logs(logs)


def analyze_insider():
    logs = [
        {
            "event_type": "file_access",
            "details": "Bulk file download detected"
        },
        {
            "event_type": "login",
            "location": "India",
            "details": "Normal login"
        }
    ]
    return analyze_logs(logs)
