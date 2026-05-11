import unittest
from patterns.factory_method import PizzaFactory, BurgerFactory, SaladFactory

class TestFactory(unittest.TestCase):
    def test_pizza_creation(self):
        factory = PizzaFactory()
        pizza = factory.create_food()
        self.assertEqual(pizza.get_name(), "Pizza Margherita")
        self.assertEqual(pizza.get_price(), 85000)

    def test_burger_creation(self):
        factory = BurgerFactory()
        burger = factory.create_food()
        self.assertEqual(burger.get_name(), "Burger Classic")
        self.assertEqual(burger.get_price(), 65000)

    def test_salad_creation(self):
        factory = SaladFactory()
        salad = factory.create_food()
        self.assertEqual(salad.get_name(), "Salad Caesar")
        self.assertEqual(salad.get_price(), 45000)

if __name__ == "__main__":
    unittest.main()
    