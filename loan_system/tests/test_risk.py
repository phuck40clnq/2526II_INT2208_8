from app.risk import classify_risk

def test_high_risk():
    assert classify_risk(400) == "HIGH"


def test_medium_risk():
    assert classify_risk(650) == "MEDIUM"


def test_low_risk():
    assert classify_risk(750) == "LOW"
