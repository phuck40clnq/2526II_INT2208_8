import pytest
from config.loader import load_test
from app.decision import evaluate_decision

_cases = load_test("decision_cases.yml")


def _evaluate(case: dict) -> str:
    return evaluate_decision(
        income=case["income"],
        risk=case["risk"],
        employment=case["employment"],
    )


@pytest.mark.parametrize("case", _cases["reject_high_risk"], ids=[c["id"] for c in _cases["reject_high_risk"]])
def test_high_risk_always_rejected(case):
    assert _evaluate(case) == "REJECT"


@pytest.mark.parametrize("case", _cases["manual_review_low_income"], ids=[c["id"] for c in _cases["manual_review_low_income"]])
def test_low_income_low_risk_contract_requires_manual_review(case):
    assert _evaluate(case) == "MANUAL REVIEW"


@pytest.mark.parametrize("case", _cases["reject_low_income"], ids=[c["id"] for c in _cases["reject_low_income"]])
def test_low_income_non_qualifying_combination_rejected(case):
    assert _evaluate(case) == "REJECT"


@pytest.mark.parametrize("case", _cases["approve"], ids=[c["id"] for c in _cases["approve"]])
def test_high_income_contract_approved(case):
    assert _evaluate(case) == "APPROVE"


@pytest.mark.parametrize("case", _cases["manual_review_high_income"], ids=[c["id"] for c in _cases["manual_review_high_income"]])
def test_high_income_freelance_requires_manual_review(case):
    assert _evaluate(case) == "MANUAL REVIEW"
