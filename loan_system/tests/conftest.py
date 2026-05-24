import pytest

from config.loader import load_test


@pytest.fixture
def validator_cases():
    return load_test("validator_cases.yml")


@pytest.fixture
def risk_cases():
    return load_test("risk_cases.yml")


@pytest.fixture
def decision_cases():
    return load_test("decision_cases.yml")


@pytest.fixture
def integration_cases():
    return load_test("integration_cases.yml")
