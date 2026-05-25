import pytest
from config.loader import load_test
from app.models import TriangleInput
from app.service import process_triangle
from app.validator import ValidationError

_cases = load_test("integration_cases.yml")

_invalid_cases = _cases["invalid"]
_valid_cases = _cases["valid"]


@pytest.mark.parametrize("case", _invalid_cases, ids=[c["id"] for c in _invalid_cases])
def test_out_of_range_input_raises_validation_error(case):
    inp = TriangleInput(a=case["a"], b=case["b"], c=case["c"])
    with pytest.raises(ValidationError):
        process_triangle(inp)


@pytest.mark.parametrize("case", _valid_cases, ids=[c["id"] for c in _valid_cases])
def test_valid_input_returns_correct_classification(case):
    inp = TriangleInput(a=case["a"], b=case["b"], c=case["c"])
    assert process_triangle(inp) == case["expected"]
