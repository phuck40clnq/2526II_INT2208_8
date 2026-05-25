import pytest
from config.loader import load_test
from app.models import LoanApplication
from app.service import process_loan
from app.validator import ValidationError

_cases = load_test("integration_cases.yml")


def _make_app(case: dict) -> LoanApplication:
    return LoanApplication(
        age=case["age"],
        income=case["income"],
        credit_score=case["credit_score"],
        employment=case["employment"],
    )


@pytest.mark.parametrize("case", _cases["invalid_input"], ids=[c["id"] for c in _cases["invalid_input"]])
def test_invalid_input_raises_validation_error(case):
    with pytest.raises(ValidationError):
        process_loan(_make_app(case))


@pytest.mark.parametrize("case", _cases["approve_cases"], ids=[c["id"] for c in _cases["approve_cases"]])
def test_eligible_application_approved(case):
    assert process_loan(_make_app(case)) == "APPROVE"


@pytest.mark.parametrize("case", _cases["manual_review_cases"], ids=[c["id"] for c in _cases["manual_review_cases"]])
def test_borderline_application_flagged_for_manual_review(case):
    assert process_loan(_make_app(case)) == "MANUAL REVIEW"


@pytest.mark.parametrize("case", _cases["reject_cases"], ids=[c["id"] for c in _cases["reject_cases"]])
def test_ineligible_application_rejected(case):
    assert process_loan(_make_app(case)) == "REJECT"
