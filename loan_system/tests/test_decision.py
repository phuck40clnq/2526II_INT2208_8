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


@pytest.mark.parametrize("case", _cases["reject"], ids=[c["id"] for c in _cases["reject"]])
def test_reject(case):
    assert _evaluate(case) == "REJECT"


@pytest.mark.parametrize("case", _cases["manual_review"], ids=[c["id"] for c in _cases["manual_review"]])
def test_manual_review(case):
    assert _evaluate(case) == "MANUAL REVIEW"


@pytest.mark.parametrize("case", _cases["approve"], ids=[c["id"] for c in _cases["approve"]])
def test_approve(case):
    assert _evaluate(case) == "APPROVE"
