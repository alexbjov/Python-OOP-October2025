from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INTEREST = 4.0
    INCREMENT_BY = 2.0
    
    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self.INTEREST)
    
    def increase_clients_interest(self) -> None:
        self.interest += self.INCREMENT_BY
