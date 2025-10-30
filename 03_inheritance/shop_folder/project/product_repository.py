from project.product import Product


class ProductRepository:
	def __init__(self):
		self.products: list[Product] = []
	
	def add(self, product: Product) -> None:
		self.products.append(product)
	
	def find(self, product_name: str) -> Product | None:
		searched_product = next(
			(p for p in self.products if p.name == product_name), None)
		
		return searched_product
	
	def remove(self, product_name: str) -> None:
		searched_product = self.find(product_name)
		
		if searched_product:
			self.products.remove(searched_product)
	
	def __repr__(self) -> str:
		output = []
		for product in self.products:
			output.append(f"{product.name}: {product.quantity}")
		
		return "\n".join(output)
