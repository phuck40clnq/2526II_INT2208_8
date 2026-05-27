# triangle

Triangle classification module.

Given three integer side lengths, the system validates them and classifies the triangle into one of four types: `EQUILATERAL`, `ISOSCELES`, `SCALENE`, or `NOT_TRIANGLE`.

---

## Table of Contents

- [Module Overview](#module-overview)
- [Business Rules](#business-rules)
- [File Structure](#file-structure)
- [Key Components](#key-components)
- [Architecture](#architecture)
- [Usage](#usage)
- [Testing](#testing)
- [Design Notes](#design-notes)

---

## Module Overview

This module solves a classic problem in software testing education: classifying a triangle. It is well-suited for practising Equivalence Partitioning and Boundary Value Analysis because the input domain is small but the edge cases are easy to miss — especially the degenerate case where the three sides form a straight line rather than a valid triangle.

---

## Business Rules

### Input validation

| Field | Type | Valid range |
|---|---|---|
| `a` | `int` | 1 – 100 |
| `b` | `int` | 1 – 100 |
| `c` | `int` | 1 – 100 |

`bool` values are rejected even though `bool` is a subclass of `int` in Python. Any violation raises `ValidationError` immediately, naming the offending side.

### Triangle classification

| Condition | Result |
|---|---|
| `a + b ≤ c` or `a + c ≤ b` or `b + c ≤ a` | `NOT_TRIANGLE` |
| `a == b == c` | `EQUILATERAL` |
| Exactly two sides equal | `ISOSCELES` |
| All three sides different | `SCALENE` |

> The inequality is strict (`> c`), so a degenerate case where `a + b == c` (collinear points) is correctly classified as `NOT_TRIANGLE`.

---

## File Structure

```
triangle/
├── app/
│   ├── __init__.py
│   ├── models.py       # TriangleInput dataclass
│   ├── validator.py    # Input validation, raises ValidationError
│   ├── classifier.py   # classify_triangle(a, b, c) → str
│   └── service.py      # process_triangle(inp) → str
├── config/
│   ├── loader.py
│   └── test_cases/
│       ├── validator_cases.yml
│       ├── classifier_cases.yml
│       └── integration_cases.yml
├── tests/
│   ├── conftest.py
│   ├── test_validator.py
│   ├── test_classifier.py
│   └── test_service.py
├── main.py
└── pytest.ini
```

---

## Key Components

**`app/validator.py`** — `validate_triangle(inp)` loops over all three sides and checks type then range for each. Raises `ValidationError` on the first violation with the side name in the message (e.g. `"Side b must be in range [1, 100]"`).

**`app/classifier.py`** — `classify_triangle(a, b, c)` applies the triangle inequality first, then checks for equality between sides. Pure function — no validation inside.

**`app/service.py`** — `process_triangle(inp)` is the single entry point. It calls validate and then classify in order.

---

## How it works

1. `validate_triangle()` — loops over all three sides, checks type then range for each; raises `ValidationError` on the first bad side
2. `classify_triangle()` — applies the triangle inequality, then checks side equality; returns one of the four result strings
3. `process_triangle()` in `service.py` — calls the two steps above in order; the only function callers need

---

## Usage

```python
from app.models import TriangleInput
from app.service import process_triangle
from app.validator import ValidationError

inp = TriangleInput(a=3, b=4, c=5)

try:
    result = process_triangle(inp)   # "SCALENE"
except ValidationError as e:
    print(e)
```

Or run the demo:

```bash
cd triangle && python main.py
```

---

## Testing

```bash
# Full suite + coverage
cd triangle && pytest

# One file
cd triangle && pytest tests/test_classifier.py

# One test
cd triangle && pytest tests/test_classifier.py::test_not_triangle
```

Test data lives in YAML files under `config/test_cases/`. To add a new scenario, add a case to the relevant YAML — do not hard-code values in test functions.

| Test file | What it covers |
|---|---|
| `test_validator.py` | Valid inputs, out-of-range per side, wrong types (float, string, bool) |
| `test_classifier.py` | All four outcomes, all three isosceles orientations, degenerate collinear case |
| `test_service.py` | End-to-end: invalid input + all four classification outcomes |

**Coverage:** 100.00 % (41 tests)

---

## Design Notes

- Validation and classification are in separate files so each can be tested independently.
- The degenerate collinear case (`a + b == c`) is explicitly covered in `classifier_cases.yml` (case `CLS-NT-04`). It is a common boundary mistake — treating `≤` as `<` in the inequality check would pass most tests but fail this case.
- All three orientations of isosceles (`a==b`, `a==c`, `b==c`) are tested separately because a bug that only checks one equality is otherwise easy to miss.
