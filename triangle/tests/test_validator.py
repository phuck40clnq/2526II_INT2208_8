import pytest
from config.loader import load_test
from app.models import TriangleInput
from app.validator import validate_triangle, ValidationError

_cases = load_test("validator_cases.yml")


@pytest.mark.parametrize("case", _cases["valid"], ids=[c["id"] for c in _cases["valid"]])
def test_valid_sides_pass_validation(case):
    inp = TriangleInput(a=case["a"], b=case["b"], c=case["c"])
    validate_triangle(inp)


@pytest.mark.parametrize("case", _cases["invalid"], ids=[c["id"] for c in _cases["invalid"]])
def test_out_of_range_sides_raise_validation_error(case):
    inp = TriangleInput(a=case["a"], b=case["b"], c=case["c"])
    with pytest.raises(ValidationError):
        validate_triangle(inp)
