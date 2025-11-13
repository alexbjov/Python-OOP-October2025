from abc import ABC, abstractmethod


class Order:
	def __init__(self, items: list[tuple[str, int, float]]):
		self.items = items
	
	def calculate_total(self) -> float:
		return sum(quantity * price for _, quantity, price in self.items)


class PaymentMethod(ABC):
	@abstractmethod
	def pay(self, amount) -> None:
		pass


class CreditCardPayment(PaymentMethod):
	def pay(self, amount) -> None:
		print(f'Processing credit card payment for ${amount}')


class PayPalPayment(PaymentMethod):
	def pay(self, amount) -> None:
		print(f'Processing PayPal payment for ${amount}')


class PaymentProcessor:
	def __init__(self, payment_method: PaymentMethod):
		self.payment_method = payment_method
	
	def process_payment(self, order: Order):
		total_amount = order.calculate_total()
		self.payment_method.pay(total_amount)


order_obj = Order([
	('Apple', 2, 1.0), ('Banana', 5, 0.5)
])

credit_card_payment = CreditCardPayment()
payment_processor = PaymentProcessor(credit_card_payment)
payment_processor.process_payment(order_obj)
