import pytest
from config.loader import load_test
from app.models import TriangleInput
from app.validator import validate_triangle, ValidationError

_cases = load_test("validator_cases.yml")


def _make_inp(case: dict) -> TriangleInput:
    return TriangleInput(
        a=case["a"],
        b=case["b"],
        c=case["c"],
    )


@pytest.mark.parametrize("case", _cases["valid"], ids=[c["id"] for c in _cases["valid"]])
def test_valid_passes_validation(case):
    validate_triangle(_make_inp(case))


@pytest.mark.parametrize("case", _cases["invalid_a"], ids=[c["id"] for c in _cases["invalid_a"]])
def test_invalid_a_raises_validation_error(case):
    with pytest.raises(ValidationError, match=case["error"]):
        validate_triangle(_make_inp(case))


@pytest.mark.parametrize("case", _cases["invalid_b"], ids=[c["id"] for c in _cases["invalid_b"]])
def test_invalid_b_raises_validation_error(case):
    with pytest.raises(ValidationError, match=case["error"]):
        validate_triangle(_make_inp(case))


@pytest.mark.parametrize("case", _cases["invalid_c"], ids=[c["id"] for c in _cases["invalid_c"]])
def test_invalid_c_raises_validation_error(case):
    with pytest.raises(ValidationError, match=case["error"]):
        validate_triangle(_make_inp(case))


@pytest.mark.parametrize("case", _cases["invalid_type"], ids=[c["id"] for c in _cases["invalid_type"]])
def test_wrong_type_raises_validation_error(case):
    with pytest.raises(ValidationError, match=case["error"]):
        validate_triangle(_make_inp(case))
