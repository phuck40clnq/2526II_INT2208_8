def classify_risk(credit_score: int) -> str:

    if 300 <= credit_score <= 500:
        return "HIGH"

    if 501 <= credit_score <= 700:
        return "MEDIUM"

    return "LOW"
