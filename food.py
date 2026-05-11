from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> int:
        pass

    @abstractmethod
    def get_ingredients(self) -> list:
        pass

class Pizza(Food):
    def get_name(self) -> str:
        return "Pizza Margherita"
    
    def get_price(self) -> int:
        return 85000
    
    def get_ingredients(self) -> list:
        return ["dough", "tomato sauce", "mozzarella", "basil"]
    
class Burger(Food):
    def get_name(self) -> str:
        return "Burger Classic"
    
    def get_price(self) -> int:
        return 65000
    
    def get_ingredients(self) -> list:
        return ["bun", "beef patty", "lettuce", "tomato"]
    
class Salad(Food):
    def get_name(self) -> str:
        return "Salad Caesar"
    
    def get_price(self) -> int:
        return 45000
    
    def get_ingredients(self) -> list:
        return ["romaine", "croutons", "parmesan", "dressing"]
    

