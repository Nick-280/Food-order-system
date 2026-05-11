from abc import ABC, abstractmethod
from models.food import Pizza, Burger, Salad

class Drink(ABC):
    def get_name(self):
        pass

    def get_price(self):
        pass

class Water(Drink):
    def get_name(self):
        return "Water"
    
    def get_price(self):
        return 5000
    
class Wine(Drink):
    def get_name(self):
        return "Wine"
    
    def get_price(self):
        return 80000
    
class Dessert(ABC):
    def get_name(self):
        pass

    def get_price(self):
        pass

class Jello(Dessert):
    def get_name(self):
        return "Jello"
    
    def get_price(self):
        return 10000
    
class Tiramisu(Dessert):
    def get_name(self):
        return "Tiramisu"
    
    def get_price(self):
        return 30000
    

class MealPackage(ABC):
    def get_food(self):
        pass

    def get_drink(self):
        pass

    def get_dessert(self):
        pass
    

class EconomyPackage(MealPackage):
    def get_food(self):
        return Pizza()
    
    def get_drink(self):
        return Water()
    
    def get_dessert(self):
        return Jello()

class StandardPackage(MealPackage):
    def get_food(self):
        return Salad()
    
    def get_drink(self):
        return Water()
    
    def get_dessert(self):
        return Tiramisu()


class LuxuryPackage(MealPackage):
    def get_food(self):
        return Burger()
    
    def get_drink(self):
        return Wine()
    
    def get_dessert(self):
        return Tiramisu()



class MealPackageFactory(ABC):
    @abstractmethod
    def create_package(self):
        pass


class EconomyMealFactory(MealPackageFactory): 
    def create_package(self):
        return EconomyPackage()
    
    
class StandardMealFactory(MealPackageFactory):
    def create_package(self):
        return StandardPackage()
    
    
class LuxuryMealFactory(MealPackageFactory):
    def create_package(self):
        return LuxuryPackage()

    
