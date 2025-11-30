from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
	def __init__(self, name: str, location: str):
		super().__init__(name, location, 50)
	
	@property
	def store_type(self):
		return 'FurnitureStore'
	
	def __str__(self):
		return 'Furniture'
