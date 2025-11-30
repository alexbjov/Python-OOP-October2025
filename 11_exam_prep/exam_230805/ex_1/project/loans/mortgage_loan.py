from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INTEREST_RATE: float = 3.5
    AMOUNT: float = 50_000.0
    INCREASE_RATE_BY: float = 0.5
    
    def __init__(self):
        super().__init__(self.INTEREST_RATE, self.AMOUNT)
    
    def increase_interest_rate(self) -> None:
        self.interest_rate += self.INCREASE_RATE_BY
