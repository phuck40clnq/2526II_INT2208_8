# INT2208 — Software Testing Practicum

Course practicum for **INT2208 (Software Testing)**, group `2526II_INT2208_8`, academic year 2025–2026.

This repo contains two independent Python modules. Each one solves a different problem and comes with a complete test suite built using Equivalence Partitioning, Boundary Value Analysis, and Decision Tables — the core testing techniques covered in the course.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Business / Domain Context](#business--domain-context)
- [Project Structure](#project-structure)
- [Directory Responsibilities](#directory-responsibilities)
- [Architecture Overview](#architecture-overview)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Coverage & Tooling](#coverage--tooling)
- [Educational Goals](#educational-goals)

---

## Project Overview

The repo is a monorepo with two self-contained modules:

| Module | What it does |
|---|---|
| [`loan_system/`](loan_system/) | Validates a loan application and outputs `APPROVE`, `MANUAL REVIEW`, or `REJECT` |
| [`triangle/`](triangle/) | Validates three side lengths and classifies the triangle as `EQUILATERAL`, `ISOSCELES`, `SCALENE`, or `NOT_TRIANGLE` |

Each module is independent — it has its own `pytest.ini` and must be run from within its own directory.

---

## Features

- Input validation with clear error messages for every bad input type
- Pure business logic — no side effects, no I/O inside the core functions
- YAML-driven parametrised tests — all test data lives in `config/test_cases/`, not in test functions
- 90 %+ line coverage enforced on every run
- HTML coverage report generated automatically

---

## Business / Domain Context

**`loan_system/`** — Based on a fictional bank (CS2045) that needs to automate personal loan decisions. Given a customer's age, income, credit score, and employment type, the system first validates the input, then classifies the credit risk, and finally produces a lending decision.

**`triangle/`** — A classic geometry problem used in software testing education. Given three integer side lengths, the system validates them and classifies the resulting triangle. It is a well-known example because the equivalence classes and boundary values are easy to reason about but subtle to get right.

---

## Project Structure

```
se/
├── loan_system/
│   ├── app/
│   ├── config/
│   │   └── test_cases/
│   ├── tests/
│   ├── main.py
│   └── pytest.ini
│
├── triangle/
│   ├── app/
│   ├── config/
│   │   └── test_cases/
│   ├── tests/
│   ├── main.py
│   └── pytest.ini
│
├── requirements.txt
└── README.md
```

---

## Directory Responsibilities

Both modules share the same internal layout:

| Directory / File | Responsibility |
|---|---|
| `app/models.py` | Input dataclass (no logic) |
| `app/validator.py` | Checks types and value ranges, raises `ValidationError` |
| `app/risk.py` or `app/classifier.py` | Classification logic (pure function) |
| `app/decision.py` | Decision logic (pure function, `loan_system` only) |
| `app/service.py` | Orchestrates validate → classify → decide |
| `config/loader.py` | Loads YAML files from `config/test_cases/` |
| `config/test_cases/` | All test input/output data in YAML |
| `tests/conftest.py` | Shared pytest fixtures |
| `tests/test_*.py` | One test file per `app/` layer |
| `main.py` | Demo runner — not part of the test suite |

---

## Architecture Overview

Both modules use the same three-step pipeline:

1. `validate()` — checks every input field; raises `ValidationError` immediately on the first violation
2. `classify()` / `evaluate()` — pure business logic; takes validated data and returns a result string
3. `process()` in `service.py` — the single public entry point that wires steps 1 and 2 together

Validation is always a separate step from the decision logic — the two are never merged.

---

## Installation

```bash
# From the repository root
python -m venv se_venv
source se_venv/bin/activate
pip install -r requirements.txt
```

**Dependencies:** `pytest`, `pytest-cov`, `pyyaml`

---

## Running the Application

Each module must be run from inside its own directory:

```bash
cd loan_system && python main.py
cd triangle    && python main.py
```

---

## Running Tests

```bash
# Full test run with coverage
cd loan_system && pytest
cd triangle    && pytest

# Single test file
cd loan_system && pytest tests/test_validator.py

# Single test by name
cd loan_system && pytest tests/test_risk.py::test_high_risk
```

---

## Coverage & Tooling

| Tool | Role |
|---|---|
| `pytest` | Test runner |
| `pytest-cov` | Coverage measurement |
| `pyyaml` | Loads parametrised test data from YAML |

Coverage is measured over the `app/` package only. Both modules require **≥ 90 % line coverage** — the run fails if the threshold is not met. HTML reports are written to `htmlcov/` after each run.

| Module | Test count | Coverage |
|---|---|---|
| `loan_system/` | 61 | 100.00 % |
| `triangle/` | 41 | 100.00 % |

---

## Educational Goals

This practicum covers four tasks per module:

1. **Equivalence Partitioning & Boundary Value Analysis** — identify valid/invalid input classes and list boundary values for each input variable
2. **Decision Table** — model the business rules as a table, then reduce it to the minimum number of test scenarios
3. **Test case list** — combine boundary values and decision-table rules into a complete, numbered catalogue
4. **Implementation** — write the code and prove every test case passes
