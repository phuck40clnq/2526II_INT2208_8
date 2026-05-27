def classify_risk(credit_score: int) -> str:

    if not 300 <= credit_score <= 850:
        raise ValueError(f"credit_score {credit_score} is outside the valid range 300–850")

    if credit_score <= 500:
        return "HIGH"

    if credit_score <= 700:
        return "MEDIUM"

    return "LOW"
