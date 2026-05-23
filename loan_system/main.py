from app.models import LoanApplication
from app.service import process_loan
from app.validator import ValidationError


def main():

    application = LoanApplication(
        age=30,
        income=20.0,
        credit_score=750,
        employment="C",
    )

    try:
        result = process_loan(application)

        print("=== Loan Evaluation Result ===")
        print(f"Application: {application}")
        print(f"Decision: {result}")

    except ValidationError as error:
        print("=== Validation Error ===")
        print(error)


if __name__ == "__main__":
    main()
