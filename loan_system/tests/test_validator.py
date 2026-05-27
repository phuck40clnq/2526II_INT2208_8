import pytest
from config.loader import load_test
from app.models import LoanApplication
from app.validator import validate_application, ValidationError

_cases = load_test("validator_cases.yml")


def _make_app(case: dict) -> LoanApplication:
    return LoanApplication(
        age=case["age"],
        income=case["income"],
        credit_score=case["credit_score"],
        employment=case["employment"],
    )


@pytest.mark.parametrize("case", _cases["valid"], ids=[c["id"] for c in _cases["valid"]])
def test_valid_passes_validation(case):
    validate_application(_make_app(case))


@pytest.mark.parametrize("case", _cases["invalid_age"], ids=[c["id"] for c in _cases["invalid_age"]])
def test_invalid_age_raises_validation_error(case):
    with pytest.raises(ValidationError, match=case["error"]):
        validate_application(_make_app(case))


@pytest.mark.parametrize("case", _cases["invalid_income"], ids=[c["id"] for c in _cases["invalid_income"]])
def test_invalid_income_raises_validation_error(case):
    with pytest.raises(ValidationError, match=case["error"]):
        validate_application(_make_app(case))


@pytest.mark.parametrize("case", _cases["invalid_credit_score"], ids=[c["id"] for c in _cases["invalid_credit_score"]])
def test_invalid_credit_score_raises_validation_error(case):
    with pytest.raises(ValidationError, match=case["error"]):
        validate_application(_make_app(case))


@pytest.mark.parametrize("case", _cases["invalid_employment"], ids=[c["id"] for c in _cases["invalid_employment"]])
def test_invalid_employment_raises_validation_error(case):
    with pytest.raises(ValidationError, match=case["error"]):
        validate_application(_make_app(case))


@pytest.mark.parametrize("case", _cases["invalid_type"], ids=[c["id"] for c in _cases["invalid_type"]])
def test_wrong_type_raises_validation_error(case):
    with pytest.raises(ValidationError, match=case["error"]):
        validate_application(_make_app(case))
