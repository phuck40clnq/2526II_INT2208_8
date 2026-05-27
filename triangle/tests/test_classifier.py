import pytest
from config.loader import load_test
from app.classifier import classify_triangle

_cases = load_test("classifier_cases.yml")


@pytest.mark.parametrize("case", _cases["not_triangle"], ids=[c["id"] for c in _cases["not_triangle"]])
def test_not_triangle(case):
    assert classify_triangle(case["a"], case["b"], case["c"]) == "NOT_TRIANGLE"


@pytest.mark.parametrize("case", _cases["equilateral"], ids=[c["id"] for c in _cases["equilateral"]])
def test_equilateral(case):
    assert classify_triangle(case["a"], case["b"], case["c"]) == "EQUILATERAL"


@pytest.mark.parametrize("case", _cases["isosceles"], ids=[c["id"] for c in _cases["isosceles"]])
def test_isosceles(case):
    assert classify_triangle(case["a"], case["b"], case["c"]) == "ISOSCELES"


@pytest.mark.parametrize("case", _cases["scalene"], ids=[c["id"] for c in _cases["scalene"]])
def test_scalene(case):
    assert classify_triangle(case["a"], case["b"], case["c"]) == "SCALENE"
