from app.validator import validate_application
from app.risk import classify_risk
from app.decision import evaluate_decision

def process_loan(application):

    validate_application(application)

    risk = classify_risk(application.credit_score)

    return evaluate_decision(
        income=application.income,
        risk=risk,
        employment=application.employment,
    )
