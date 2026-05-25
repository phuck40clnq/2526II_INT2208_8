# Loan Approval System — Test Documentation

## Requirement Summary

An automated loan decision module for bank CS2045 processing 4 inputs and returning one of three outcomes, or raising `ValidationError` on invalid input.

| Field | Type | Valid Range |
|---|---|---|
| `age` | `int` | `[18, 65]` |
| `income` | `float` | `[5.0, 500.0]` million VND |
| `credit_score` | `int` | `[300, 850]` |
| `employment` | `str` | `"C"` (Contract) or `"F"` (Freelance) |

**Outcomes:** `APPROVE` · `MANUAL REVIEW` · `REJECT` · `ValidationError` (invalid input)

---

## Equivalence Partitioning

### Input Validation

| Variable | Class | Range | Validity |
|---|---|---|---|
| age | EC1 | `< 18` | Invalid |
| age | EC2 | `18–65` | Valid |
| age | EC3 | `> 65` | Invalid |
| income | EC4 | `< 5.0` | Invalid |
| income | EC5 | `5.0–500.0` | Valid |
| income | EC6 | `> 500.0` | Invalid |
| credit_score | EC7 | `< 300` | Invalid |
| credit_score | EC8 | `300–850` | Valid |
| credit_score | EC9 | `> 850` | Invalid |
| employment | EC10 | not in `{C, F}` | Invalid |
| employment | EC11 | `C` or `F` | Valid |

### Business Logic

| Class | Condition | Decision |
|---|---|---|
| EC12 | HIGH risk (any income, any employment) | REJECT |
| EC13 | income `< 15`, LOW risk, Contract | MANUAL REVIEW |
| EC14 | income `< 15`, MEDIUM risk OR Freelance | REJECT |
| EC15 | income `≥ 15`, Contract | APPROVE |
| EC16 | income `≥ 15`, Freelance | MANUAL REVIEW |

---

## Boundary Value Analysis

| Variable | BV− (invalid) | BV min | BV max | BV+ (invalid) |
|---|---|---|---|---|
| age | 17 | 18 | 65 | 66 |
| income | 4.9 | 5.0 | 500.0 | 500.1 |
| credit_score | 299 | 300 | 850 | 851 |

**Internal split boundaries:**

| Boundary | BV− | BV |
|---|---|---|
| income split | 14.9 | 15.0 |
| HIGH → MEDIUM | 500 | 501 |
| MEDIUM → LOW | 700 | 701 |

---

## Decision Table

Full table (9 distinct rules after collapsing HIGH-risk variants):

| Rule | Risk | Income | Employment | Decision |
|---|---|---|---|---|
| 1a | HIGH | `< 15` | C | REJECT |
| 1b | HIGH | `< 15` | F | REJECT |
| 1c | HIGH | `≥ 15` | C | REJECT |
| 1d | HIGH | `≥ 15` | F | REJECT |
| 2 | LOW | `< 15` | C | MANUAL REVIEW |
| 3 | MEDIUM | `< 15` | C | REJECT |
| 4 | LOW/MEDIUM | `< 15` | F | REJECT |
| 5 | LOW | `≥ 15` | C | APPROVE |
| 6 | MEDIUM | `≥ 15` | C | APPROVE |
| 7 | LOW | `≥ 15` | F | MANUAL REVIEW |
| 8 | MEDIUM | `≥ 15` | F | MANUAL REVIEW |

### Reduced Decision Table — 5 rules

Rules 1a–1d collapse (all HIGH → REJECT). Rules 5+6 collapse (LOW/MEDIUM + income≥15 + C → APPROVE). Rules 7+8 collapse (LOW/MEDIUM + income≥15 + F → MANUAL REVIEW).

| Rule | Risk | Income | Employment | Decision |
|---|---|---|---|---|
| **R1** | HIGH | — | — | REJECT |
| **R2** | LOW | `< 15` | C | MANUAL REVIEW |
| **R3** | LOW/MEDIUM | `< 15` | not (LOW+C) | REJECT |
| **R4** | LOW/MEDIUM | `≥ 15` | C | APPROVE |
| **R5** | LOW/MEDIUM | `≥ 15` | F | MANUAL REVIEW |

---

## Test Strategy

| File | Layer | Coverage focus |
|---|---|---|
| `test_validator.py` | Unit | BVA per field; EP valid/invalid classes |
| `test_risk.py` | Unit | All 6 credit_score boundaries (300, 500, 501, 700, 701, 850) |
| `test_decision.py` | Unit | Each of the 5 reduced rules with representative values |
| `test_service.py` | Integration | End-to-end: invalid input → `ValidationError`; valid → correct decision |

All test data is stored in `config/test_cases/*.yml` and loaded parametrically via `config/loader.py`. This keeps test logic and test data decoupled.

---

## How to Run

```bash
cd loan_system
pytest                                       # all tests with coverage
pytest tests/test_validator.py              # single layer
pytest tests/test_decision.py -k "approve"  # filter by keyword
pytest --cov=app --cov-report=term-missing  # coverage in terminal
```

Coverage threshold: **90%** (enforced in `pytest.ini`). HTML report written to `htmlcov/`.
