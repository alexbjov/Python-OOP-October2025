from project.products.base_product import BaseProduct


class Chair(BaseProduct):
    DISCOUNT = 0.1
    
    def __init__(self, model: str, price: float):
        super().__init__(model, price, 'Wood', 'Furniture')
    
    def discount(self) -> None:
        self.price *= 1 - self.DISCOUNT
