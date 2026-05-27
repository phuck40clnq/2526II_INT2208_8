from app.models import LoanApplication

class ValidationError(Exception):
    pass

def validate_application(app: LoanApplication) -> None:

    # Age
    if isinstance(app.age, bool) or not isinstance(app.age, int):
        raise ValidationError("Age must be integer")

    if not (18 <= app.age <= 65):
        raise ValidationError("Invalid age")

    # Income
    if isinstance(app.income, bool) or not isinstance(app.income, (int, float)):
        raise ValidationError("Income must be a number")

    if not (5.0 <= app.income <= 500.0):
        raise ValidationError("Invalid income")

    # Credit score
    if isinstance(app.credit_score, bool) or not isinstance(app.credit_score, int):
        raise ValidationError("Credit score must be integer")

    if not (300 <= app.credit_score <= 850):
        raise ValidationError("Invalid credit score")

    # Employment
    if app.employment not in ["C", "F"]:
        raise ValidationError("Invalid employment")
