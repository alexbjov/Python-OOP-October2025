from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    INTEREST_RATE: float = 1.5
    AMOUNT: float = 2_000.0
    INCREASE_RATE_BY: float = 0.2
    
    def __init__(self):
        super().__init__(self.INTEREST_RATE, self.AMOUNT)
    
    def increase_interest_rate(self) -> None:
        self.interest_rate += self.INCREASE_RATE_BY
