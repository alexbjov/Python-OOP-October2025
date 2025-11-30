from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    ALLOWED_SERVICES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }
    
    ALLOWED_ROBOTS = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }
    
    def __init__(self):
        self.robots: list[BaseRobot] = []
        self.services: list[BaseService] = []
    
    def add_service(self, service_type: str, name: str) -> str:
        if service_type not in self.ALLOWED_SERVICES:
            raise Exception("Invalid service type!")
        
        new_service = self.ALLOWED_SERVICES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."
    
    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        if robot_type not in self.ALLOWED_ROBOTS:
            raise Exception("Invalid robot type!")
        
        new_robot = self.ALLOWED_ROBOTS[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."
    
    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        searched_robot = [robot for robot in self.robots if robot.name == robot_name][0]
        searched_service = [service for service in self.services if service.name == service_name][0]
        
        if searched_robot.POSSIBLE_SERVICE != searched_service.__class__.__name__:
            return "Unsuitable service."
        
        if len(searched_service.robots) >= searched_service.capacity:
            raise Exception("Not enough capacity for this robot!")
        
        self.robots.remove(searched_robot)
        searched_service.robots.append(searched_robot)
        return f"Successfully added {robot_name} to {service_name}."
    
    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        searched_service = [service for service in self.services if service.name == service_name][0]
        searched_robot = next((robot for robot in searched_service.robots if robot.name == robot_name), None)
        if searched_robot is None:
            raise Exception("No such robot in this service!")
        
        searched_service.robots.remove(searched_robot)
        self.robots.append(searched_robot)
        return f"Successfully removed {robot_name} from {service_name}."
    
    def feed_all_robots_from_service(self, service_name: str) -> str:
        searched_service = [service for service in self.services if service.name == service_name][0]
        
        if searched_service.robots:
            for robot in searched_service.robots:
                robot.eating()
        
        return f"Robots fed: {len(searched_service.robots)}."
    
    def service_price(self, service_name: str) -> str:
        searched_service = [service for service in self.services if service.name == service_name][0]
        sum_robots_price = 0
        if searched_service.robots:
            robots_prices = [robot.price for robot in searched_service.robots]
            sum_robots_price = sum(robots_prices)
        
        return f"The value of service {service_name} is {sum_robots_price:.2f}."
    
    def __str__(self):
        result: list[str] = []
        for service in self.services:
            result.append(service.details())
        
        return "\n".join(result)
