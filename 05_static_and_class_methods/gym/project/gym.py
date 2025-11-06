from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
	def __init__(self):
		self.customers: list[Customer] = []
		self.trainers: list[Trainer] = []
		self.equipment: list[Equipment] = []
		self.plans: list[ExercisePlan] = []
		self.subscriptions: list[Subscription] = []
	
	def add_customer(self, customer: Customer) -> None:
		if customer not in self.customers:
			self.customers.append(customer)
	
	def add_trainer(self, trainer: Trainer) -> None:
		if trainer not in self.trainers:
			self.trainers.append(trainer)
	
	def add_equipment(self, equipment: Trainer) -> None:
		if equipment not in self.equipment:
			self.equipment.append(equipment)
	
	def add_plan(self, plan: ExercisePlan) -> None:
		if plan not in self.plans:
			self.plans.append(plan)
	
	def add_subscription(self, subscription: Subscription) -> None:
		if subscription not in self.subscriptions:
			self.subscriptions.append(subscription)
	
	def subscription_info(self, subscription_id: int) -> str:
		searched_subscription = next(
			(s for s in self.subscriptions if s.id == subscription_id), None)
		
		searched_customer = next(
			(c for c in self.customers if c.id == searched_subscription.id),
			None)
		
		searched_trainer = next(
			(t for t in self.trainers if t.id == searched_subscription.id),
			None)
		
		searched_plan = next((p for p in self.plans if
							  p.id == searched_subscription.exercise_id), None)
		
		searched_equipment = next(
			(e for e in self.equipment if e.id == searched_plan.equipment_id),
			None)
		
		result = [
			repr(searched_subscription), repr(searched_customer),
			repr(searched_trainer), repr(searched_equipment),
			repr(searched_plan)
		]
		
		return "\n".join(result)
