# loan_system

Automated personal loan approval module for bank **CS2045**.

Given a customer's application, the system validates the inputs, assesses credit risk, and produces one of three lending decisions: `APPROVE`, `MANUAL REVIEW`, or `REJECT`.

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

This module implements the core decision engine for a personal loan product. It takes four inputs from a loan application, validates them, classifies the applicant's credit risk, and applies a set of lending rules to produce a final decision.

The module is entirely pure Python — no database, no HTTP, no side effects. All business logic is in `app/` and all test data is in `config/test_cases/`.

---

## Business Rules

### Input validation

| Field | Type | Valid range |
|---|---|---|
| `age` | `int` | 18 – 65 |
| `income` | `float` | 5.0 – 500.0 (million VND) |
| `credit_score` | `int` | 300 – 850 |
| `employment` | `str` | `"C"` (Contract) or `"F"` (Freelance) |

Any field outside its valid range raises a `ValidationError` immediately. `bool` values are rejected even for integer fields.

### Risk classification

| Credit score | Risk level |
|---|---|
| 300 – 500 | `HIGH` |
| 501 – 700 | `MEDIUM` |
| 701 – 850 | `LOW` |

### Decision rules (reduced decision table)

| income | risk | employment | decision |
|---|---|---|---|
| any | `HIGH` | any | `REJECT` |
| < 15 | any | `F` | `REJECT` |
| < 15 | `MEDIUM` | `C` | `REJECT` |
| < 15 | `LOW` | `C` | `MANUAL REVIEW` |
| ≥ 15 | `LOW` or `MEDIUM` | `C` | `APPROVE` |
| ≥ 15 | `LOW` or `MEDIUM` | `F` | `MANUAL REVIEW` |

---

## File Structure

```
loan_system/
├── app/
│   ├── __init__.py
│   ├── models.py       # LoanApplication dataclass
│   ├── validator.py    # Input validation, raises ValidationError
│   ├── risk.py         # classify_risk(credit_score) → str
│   ├── decision.py     # evaluate_decision(income, risk, employment) → str
│   └── service.py      # process_loan(application) → str
├── config/
│   ├── loader.py
│   └── test_cases/
│       ├── validator_cases.yml
│       ├── risk_cases.yml
│       ├── decision_cases.yml
│       └── integration_cases.yml
├── tests/
│   ├── conftest.py
│   ├── test_validator.py
│   ├── test_risk.py
│   ├── test_decision.py
│   └── test_service.py
├── main.py
└── pytest.ini
```

---

## Key Components

**`app/validator.py`** — `validate_application(app)` checks every field and raises `ValidationError` with a descriptive message on the first violation found. It checks types before ranges.

**`app/risk.py`** — `classify_risk(credit_score)` maps a score to `"HIGH"`, `"MEDIUM"`, or `"LOW"`. Raises `ValueError` if the score is outside 300–850.

**`app/decision.py`** — `evaluate_decision(income, risk, employment)` applies the lending rules and returns the decision string. Pure function — no I/O.

**`app/service.py`** — `process_loan(application)` is the single public entry point. It calls validate → classify → decide in order and returns the final decision string.

---

## How it works

1. `validate_application()` — checks all four fields; raises `ValidationError` on the first violation
2. `classify_risk()` — maps credit score to `HIGH` / `MEDIUM` / `LOW`
3. `evaluate_decision()` — applies the lending rules and returns `APPROVE` / `MANUAL REVIEW` / `REJECT`
4. `process_loan()` in `service.py` — calls the three steps above in order; the only function callers need to know about

---

## Usage

```python
from app.models import LoanApplication
from app.service import process_loan
from app.validator import ValidationError

app = LoanApplication(age=30, income=20.0, credit_score=750, employment="C")

try:
    result = process_loan(app)   # "APPROVE"
except ValidationError as e:
    print(e)
```

Or run the demo:

```bash
cd loan_system && python main.py
```

---

## Testing

```bash
# Full suite + coverage
cd loan_system && pytest

# One file
cd loan_system && pytest tests/test_decision.py

# One test
cd loan_system && pytest tests/test_risk.py::test_high_risk
```

Test data is in YAML files under `config/test_cases/`. Each file groups cases by category (e.g. `reject`, `approve`, `invalid_age`). Tests load these files at module level and use `@pytest.mark.parametrize` with the case list.

| Test file | What it covers |
|---|---|
| `test_validator.py` | Valid inputs, out-of-range values, wrong types |
| `test_risk.py` | All three risk bands and their boundaries |
| `test_decision.py` | All six rows of the decision table |
| `test_service.py` | End-to-end: invalid input, all three decision outcomes |

**Coverage:** 97.83 % (59 tests)

---

## Design Notes

- Validation and decision logic are intentionally kept in separate files. Merging them would make the code harder to test and modify independently.
- `risk.py` does not re-validate its input. It assumes `validate_application` ran first. Calling it directly with a score outside 300–850 raises `ValueError` as a defensive measure.
- All test values come from YAML — no magic numbers in test functions. To add a new scenario, add a case to the relevant YAML file.
