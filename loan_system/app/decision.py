def evaluate_decision(
    income: float,
    risk: str,
    employment: str,
) -> str:

    # High risk
    if risk == "HIGH":
        return "REJECT"

    # Income < 15
    if income < 15.0:

        if employment == "F":
            return "REJECT"

        if risk == "MEDIUM":
            return "REJECT"

        return "MANUAL REVIEW"

    # Income >= 15
    if employment == "C":
        return "APPROVE"

    return "MANUAL REVIEW"
