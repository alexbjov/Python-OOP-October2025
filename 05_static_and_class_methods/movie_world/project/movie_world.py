from project.customer import Customer

from project.dvd import DVD


class MovieWorld:
	def __init__(self, name: str):
		self.name = name
		self.customers: list[Customer] = []
		self.dvds: list[DVD] = []
	
	@staticmethod
	def dvd_capacity():
		return 15
	
	@staticmethod
	def customer_capacity():
		return 10
	
	def add_customer(self, customer: Customer) -> None:
		if len(self.customers) < self.customer_capacity():
			self.customers.append(customer)
	
	def add_dvd(self, dvd: DVD) -> None:
		if len(self.dvds) < self.dvd_capacity():
			dvd.is_rented = False
			self.dvds.append(dvd)
	
	def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
		customer = next((c for c in self.customers if c.id == customer_id),
			None)
		dvd = next((d for d in self.dvds if d.id == dvd_id), None)
		
		if dvd:
			if dvd in customer.rented_dvds:
				return f"{customer.name} has already rented {dvd.name}"
			
			if customer.age < dvd.age_restriction:
				return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
			
			if not dvd.is_rented:
				dvd.is_rented = True
				customer.rented_dvds.append(dvd)
				return f"{customer.name} has successfully rented {dvd.name}"
		
		return f"DVD is already rented"
	
	def return_dvd(self, customer_id: int, dvd_id: int) -> str:
		customer = next((c for c in self.customers if c.id == customer_id),
			None)
		dvd = next((d for d in customer.rented_dvds if d.id == dvd_id), None)
		
		if dvd:
			customer.rented_dvds.remove(dvd)
			dvd.is_rented = False
			return f"{customer.name} has successfully returned {dvd.name}"
		
		return f"{customer.name} does not have that DVD"
	
	def __repr__(self):
		result = []
		for customer in self.customers:
			result.append(repr(customer))
		
		for dvd in self.dvds:
			result.append(repr(dvd))
		
		return "\n".join(result)
