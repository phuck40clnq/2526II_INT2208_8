# Triangle Classifier — Test Documentation

## Requirement Summary

Given three integer sides `a`, `b`, `c`, each constrained to `[1, 100]`, classify the triangle.

| Return Value | Condition |
|---|---|
| `INVALID` | Any side is outside `[1, 100]` |
| `NOT_TRIANGLE` | Triangle inequality violated: `a+b ≤ c` (or any permutation) |
| `EQUILATERAL` | `a == b == c` |
| `ISOSCELES` | Exactly two sides are equal |
| `SCALENE` | All three sides are different |

---

## Equivalence Partitioning

| Class | Condition | Result |
|---|---|---|
| EC1 | Any side `< 1` | INVALID |
| EC2 | Any side `> 100` | INVALID |
| EC3 | All sides in `[1, 100]`, triangle inequality **violated** | NOT_TRIANGLE |
| EC4 | All sides valid, `a == b == c` | EQUILATERAL |
| EC5 | All sides valid, exactly 2 sides equal | ISOSCELES |
| EC6 | All sides valid, all sides different, inequality holds | SCALENE |

---

## Boundary Value Analysis

| Variable | BV− (invalid) | BV min (valid) | BV max (valid) | BV+ (invalid) |
|---|---|---|---|---|
| a | 0 | 1 | 100 | 101 |
| b | 0 | 1 | 100 | 101 |
| c | 0 | 1 | 100 | 101 |

**Triangle inequality boundary:**

| Case | Values | Result |
|---|---|---|
| Degenerate (a+b = c) | 1, 1, 2 | NOT_TRIANGLE |
| Just-valid isosceles | 2, 2, 3 | ISOSCELES |
| Near-equilateral | 99, 99, 100 | ISOSCELES |
| Max boundary scalene | 98, 99, 100 | SCALENE |

---

## Decision Table

| Rule | Valid range? | Triangle inequality? | a==b==c? | 2 sides equal? | Result |
|---|---|---|---|---|---|
| R1 | No | — | — | — | INVALID |
| R2 | Yes | No | — | — | NOT_TRIANGLE |
| R3 | Yes | Yes | Yes | — | EQUILATERAL |
| R4 | Yes | Yes | No | Yes | ISOSCELES |
| R5 | Yes | Yes | No | No | SCALENE |

The table is already minimal — 5 rules, no further reduction possible as each produces a distinct output.

---

## Test Strategy

Tests are organized in three layers, each in a separate file:

| File | Scope | Method |
|---|---|---|
| `test_validator.py` | Input range validation | BVA per side (0, 1, 100, 101 for each of a, b, c) |
| `test_classifier.py` | Business classification logic | One parametrized group per output class |
| `test_service.py` | End-to-end integration | INVALID → ValidationError; valid → expected output |

All test data lives in `config/test_cases/*.yml`. Tests use `@pytest.mark.parametrize` with YAML-sourced cases.

---

## How to Run

```bash
cd triangle
pytest                              # all tests with coverage report
pytest tests/test_classifier.py    # single layer
pytest -k "equilateral"            # filter by keyword
pytest --cov=app --cov-report=term-missing  # coverage in terminal
```

Coverage threshold: **90%** (enforced in `pytest.ini`). HTML report written to `htmlcov/`.
