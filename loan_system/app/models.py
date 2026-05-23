from dataclasses import dataclass

@dataclass
class LoanApplication:
    age: int
    income: float
    credit_score: int
    employment: str
