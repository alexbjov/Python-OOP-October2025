class Shop:
	def __init__(self, name: str, shop_type: str, capacity: int):
		self.name = name
		self.type = shop_type
		self.capacity = capacity
		self.items: dict[str, int] = {}
	
	@classmethod
	def small_shop(cls, name: str, shop_type: str):
		return cls(name, shop_type, 10)
	
	def add_item(self, item_name: str) -> str:
		if sum(self.items.values()) >= self.capacity:
			return "Not enough capacity in the shop"
		
		self.items[item_name] = self.items.get(item_name, 0) + 1
		return f"{item_name} added to the shop"
	
	def remove_item(self, item_name: str, amount: int) -> str:
		if item_name not in self.items:
			return f"Cannot remove {amount} {item_name}"
		
		if self.items[item_name] < amount:
			return f"Cannot remove {amount} {item_name}"
		
		self.items[item_name] -= amount
		if self.items[item_name] == 0:
			del self.items[item_name]
		
		return f"{amount} {item_name} removed from the shop"
	
	def __repr__(self) -> str:
		return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)

ex = {"a": 2, "b": 5, "c": 6}
print(sum(ex.values()))
