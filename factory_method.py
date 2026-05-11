from abc import ABC, abstractmethod
from models.food import Pizza, Burger, Salad

class FoodFactory(ABC):

    @abstractmethod
    def create_food(self):
        pass

class PizzaFactory(FoodFactory):
    def create_food(self) -> Pizza:
        return Pizza()
    
class BurgerFactory(FoodFactory):
    def create_food(self) -> Burger:
        return Burger()
    
class SaladFactory(FoodFactory):
    def create_food(self) -> Salad:
        return Salad()
    
