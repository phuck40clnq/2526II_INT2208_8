import pytest
from config.loader import load_test
from app.risk import classify_risk

_cases = load_test("risk_cases.yml")


@pytest.mark.parametrize("case", _cases["high_risk"], ids=[c["id"] for c in _cases["high_risk"]])
def test_high_risk_classification(case):
    assert classify_risk(case["credit_score"]) == "HIGH"


@pytest.mark.parametrize("case", _cases["medium_risk"], ids=[c["id"] for c in _cases["medium_risk"]])
def test_medium_risk_classification(case):
    assert classify_risk(case["credit_score"]) == "MEDIUM"


@pytest.mark.parametrize("case", _cases["low_risk"], ids=[c["id"] for c in _cases["low_risk"]])
def test_low_risk_classification(case):
    assert classify_risk(case["credit_score"]) == "LOW"
