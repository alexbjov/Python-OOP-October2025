from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    def update_discount(self) -> None:
        if self.total_orders >= 1:
            self.discount = 5.0
        else:
            self.discount = 0.0
