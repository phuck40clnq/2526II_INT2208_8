import pytest
from config.loader import load_test
from app.models import TriangleInput
from app.service import process_triangle
from app.validator import ValidationError

_cases = load_test("integration_cases.yml")


def _make_inp(case: dict) -> TriangleInput:
    return TriangleInput(
        a=case["a"],
        b=case["b"],
        c=case["c"],
    )


@pytest.mark.parametrize("case", _cases["invalid_input"], ids=[c["id"] for c in _cases["invalid_input"]])
def test_invalid_input_raises_validation_error(case):
    with pytest.raises(ValidationError, match=case["error"]):
        process_triangle(_make_inp(case))


@pytest.mark.parametrize("case", _cases["not_triangle"], ids=[c["id"] for c in _cases["not_triangle"]])
def test_not_triangle(case):
    assert process_triangle(_make_inp(case)) == "NOT_TRIANGLE"


@pytest.mark.parametrize("case", _cases["equilateral"], ids=[c["id"] for c in _cases["equilateral"]])
def test_equilateral(case):
    assert process_triangle(_make_inp(case)) == "EQUILATERAL"


@pytest.mark.parametrize("case", _cases["isosceles"], ids=[c["id"] for c in _cases["isosceles"]])
def test_isosceles(case):
    assert process_triangle(_make_inp(case)) == "ISOSCELES"


@pytest.mark.parametrize("case", _cases["scalene"], ids=[c["id"] for c in _cases["scalene"]])
def test_scalene(case):
    assert process_triangle(_make_inp(case)) == "SCALENE"
