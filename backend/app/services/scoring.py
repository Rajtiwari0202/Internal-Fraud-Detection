def calculate_risk_score(row):
    score = 0

    # ML anomaly
    if row["anomaly"] == -1:
        score += 40

    # High amount
    if row.get("is_high_amount", 0) == 1:
        score += 30

    # Off-hour activity
    if row.get("is_off_hour", 0) == 1:
        score += 20

    # High activity count
    if row.get("action_count", 0) > 50:
        score += 10

    return score


def assign_risk_level(score):
    if score >= 70:
        return "HIGH"
    elif score >= 40:
        return "MEDIUM"
    else:
        return "LOW"