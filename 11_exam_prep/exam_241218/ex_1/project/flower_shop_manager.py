from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    CLIENT_TYPES: dict[str, BaseClient] = {
        "BusinessClient": BusinessClient,
        "RegularClient": RegularClient
    }
    
    PLANT_TYPES: dict[str, BasePlant] = {
        "Flower": Flower,
        "LeafPlant": LeafPlant
    }
    
    def __init__(self):
        self.income: float = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []
    
    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int,
                  plant_extra_data: str) -> str:
        
        if plant_type not in self.PLANT_TYPES:
            raise ValueError("Unknown plant type!")
        
        new_plant = self.PLANT_TYPES[plant_type](plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(new_plant)
        return f"{plant_name} is added to the shop as {plant_type}."
    
    def add_client(self, client_type: str, client_name: str, client_phone_number: str) -> str:
        if client_type not in self.CLIENT_TYPES:
            raise ValueError("Unknown client type!")
        
        searched_client = next((client for client in self.clients if client.phone_number == client_phone_number), None)
        if searched_client:
            raise ValueError("This phone number has been used!")
        
        new_client = self.CLIENT_TYPES[client_type](client_name, client_phone_number)
        self.clients.append(new_client)
        return f"{client_name} is successfully added as a {client_type}."
    
    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int) -> str:
        searched_client = next((client for client in self.clients if client.phone_number == client_phone_number), None)
        if searched_client is None:
            raise ValueError("Client not found!")
        
        searched_plants = [plant for plant in self.plants if plant.name == plant_name]
        if not searched_plants:
            raise ValueError("Plants not found!")
        
        if plant_quantity > len(searched_plants):
            return "Not enough plant quantity."
        
        amount = 0
        for i in range(len(searched_plants)):
            if i >= plant_quantity:
                break
            self.plants.remove(searched_plants[i])
            amount += searched_plants[i].price * (100 - searched_client.discount) / 100
        
        searched_client.update_total_orders()
        searched_client.update_discount()
        self.income += amount
        
        return f"{plant_quantity}pcs. of {plant_name} plant sold for {amount:.2f}"
    
    def remove_plant(self, plant_name: str) -> str:
        searched_plant = next((plant for plant in self.plants if plant.name == plant_name), None)
        if searched_plant is None:
            return "No such plant name."
        
        self.plants.remove(searched_plant)
        return f"Removed {searched_plant.plant_details()}"
    
    def remove_clients(self) -> str:
        counter = 0
        for i in range(len(self.clients) - 1, -1, -1):
            if self.clients[i].total_orders == 0:
                del self.clients[i]
                counter += 1
        
        return f"{counter} client/s removed."
    
    def shop_report(self) -> str:
        unsold_plants = {}
        for plant in self.plants:
            unsold_plants[plant.name] = unsold_plants.get(plant.name, 0) + 1
        
        sorted_unsold_plants = sorted(unsold_plants.items(), key=lambda kvp: (-kvp[1], kvp[0]))
        total_plants = sum(unsold_plants.values())
        
        sorted_clients = sorted(self.clients, key=lambda client: (-client.total_orders, client.phone_number))
        total_orders = sum(client.total_orders for client in sorted_clients)
        
        output: list[str] = [
            "~Flower Shop Report~",
            f"Income: {self.income:.2f}",
            f"Count of orders: {total_orders}",
            f"~~Unsold plants: {total_plants}~~"
        ]
        for plant_name, count in sorted_unsold_plants:
            output.append(f"{plant_name}: {count}")
        
        output.append(f"~~Clients number: {len(sorted_clients)}~~")
        for client in sorted_clients:
            output.append(client.client_details())
        
        return "\n".join(output)
