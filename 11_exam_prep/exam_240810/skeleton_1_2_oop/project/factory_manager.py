from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    PRODUCT_TYPES = {'Chair': Chair, 'HobbyHorse': HobbyHorse}
    STORE_TYPES = {'FurnitureStore': FurnitureStore, 'ToyStore': ToyStore}
    
    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []
    
    def produce_item(self, product_type: str, model: str, price: float) -> str:
        if product_type not in self.PRODUCT_TYPES:
            raise Exception('Invalid product type!')
        
        new_product = self.PRODUCT_TYPES[product_type](model, price)
        self.products.append(new_product)
        return f'A product of sub-type {new_product.sub_type} was produced.'
    
    def register_new_store(self, store_type: str, name: str, location: str) -> str:
        if store_type not in self.STORE_TYPES:
            raise Exception(f'{store_type} is an invalid type of store!')
        
        new_store = self.STORE_TYPES[store_type](name, location)
        self.stores.append(new_store)
        return f'A new {store_type} was successfully registered.'
    
    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct) -> str:
        if store.capacity < len(products):
            return f'Store {store.name} has no capacity for this purchase.'
        
        filtered_products = [p for p in products if p.sub_type == str(store)]
        if len(filtered_products) == 0:
            return 'Products do not match in type. Nothing sold.'
        
        for product in filtered_products:
            self.products.remove(product)
            store.products.append(product)
            store.capacity -= 1
            self.income += product.price
        
        return f'Store {store.name} successfully purchased {len(filtered_products)} items.'
    
    def unregister_store(self, store_name: str) -> str:
        searched_store = next((s for s in self.stores if s.name == store_name), None)
        if searched_store is None:
            raise Exception('No such store!')
        
        if searched_store.products:
            return 'The store is still having products in stock! Unregistering is inadvisable.'
        
        self.stores.remove(searched_store)
        return f'Successfully unregistered store {store_name}, location: {searched_store.location}.'
    
    def discount_products(self, product_model: str) -> str:
        discounted_products = [p for p in self.products if p.model == product_model]
        
        for p in discounted_products:
            p.discount()
        
        return f'Discount applied to {len(discounted_products)} products with model: {product_model}'
    
    def request_store_stats(self, store_name: str) -> str:
        searched_store = next((s for s in self.stores if s.name == store_name), None)
        
        if searched_store is None:
            return 'There is no store registered under this name!'
        
        return searched_store.store_stats()
    
    def statistics(self):
        products_dict = {}
        total_price = 0
        for product in self.products:
            if product.model not in products_dict:
                products_dict[product.model] = 0
            products_dict[product.model] += 1
            total_price += product.price
        
        output = [
            f'Factory: {self.name}',
            f'Income: {self.income:.2f}',
            '***Products Statistics***',
            f'Unsold Products: {len(self.products)}. Total net price: {total_price:.2f}'
        ]
        
        for model, num in sorted(products_dict.items(), key=lambda kvp: kvp[0]):
            output.append(f'{model}: {num}')
        
        output.append(f'***Partner Stores: {len(self.stores)}***')
        
        for store in sorted(self.stores, key=lambda s: s.name):
            output.append(store.name)
        
        return '\n'.join(output)
