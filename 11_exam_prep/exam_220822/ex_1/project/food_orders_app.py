from copy import deepcopy

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEALS: set[Meal] = {Starter, MainDish, Dessert}
    
    def __init__(self):
        self.menu: list[Meal] = []
        self.clients_list: list[Client] = []
        self.receipt_id = 1
    
    def increment_receipt_id(self) -> None:
        self.receipt_id += 1
    
    @property
    def receipt_id(self):
        return self.__receipt_id
    
    @receipt_id.setter
    def receipt_id(self, value):
        self.__receipt_id = value
    
    def register_client(self, client_phone_number: str) -> str:
        searched_client = next((client for client in self.clients_list if client.phone_number == client_phone_number),
                               None)
        if searched_client:
            raise Exception("The client has already been registered!")
        
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."
    
    def add_meals_to_menu(self, *meals: Meal) -> None:
        for meal in meals:
            if meal.__class__ in self.VALID_MEALS:
                self.menu.append(meal)
    
    def show_menu(self) -> str:
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = [meal.details() for meal in self.menu]
        return "\n".join(result)
    
    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities) -> str:
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        
        searched_client = next((client for client in self.clients_list if client.phone_number == client_phone_number),
                               None)
        if searched_client is None:
            self.register_client(client_phone_number)
        
        ordered_meals: list[Meal] = []
        for meal_name, quantity in meal_names_and_quantities.items():
            searched_meal = next((meal for meal in self.menu if meal.name == meal_name), None)
            if searched_meal is None:
                ordered_meals.clear()
                raise Exception(f"{meal_name} is not on the menu!")
            
            if searched_meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {searched_meal.__class__.__name__}: {meal_name}!")
            
            searched_meal.quantity -= quantity
            if searched_meal.quantity <= 0:
                self.menu.remove(searched_meal)
            
            new_meal = deepcopy(searched_meal)
            new_meal.quantity = quantity
            ordered_meals.append(new_meal)
        
        sum_meal_prices = sum(meal.price * meal.quantity for meal in ordered_meals)
        searched_client.shopping_cart.extend(ordered_meals)
        searched_client.bill += sum_meal_prices
        
        meal_names = [meal.name for meal in searched_client.shopping_cart]
        return (f"Client {client_phone_number} successfully ordered {', '.join(meal_names)} for "
                f"{searched_client.bill:.2f}lv.")
    
    def cancel_order(self, client_phone_number: str) -> str:
        searched_client = [client for client in self.clients_list if client.phone_number == client_phone_number][0]
        if not searched_client.shopping_cart:
            raise Exception("There are no ordered meals!")
        
        self.menu.extend(deepcopy(searched_client.shopping_cart))
        searched_client.shopping_cart.clear()
        searched_client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."
    
    def finish_order(self, client_phone_number: str) -> str:
        searched_client = [client for client in self.clients_list if client.phone_number == client_phone_number][0]
        if not searched_client.shopping_cart:
            raise Exception("There are no ordered meals!")
        
        paid_money = sum(meal.price * meal.quantity for meal in searched_client.shopping_cart)
        searched_client.shopping_cart.clear()
        searched_client.bill = 0
        self.increment_receipt_id()
        return (f"Receipt #{self.receipt_id - 1} with total amount of {paid_money:.2f} was successfully paid for "
                f"{client_phone_number}.")
    
    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
