import unittest
from patterns.abstract_factory import EconomyMealFactory, LuxuryMealFactory

class TestAbstractFactory(unittest.TestCase):
    def test_economy_package(self):
        factory = EconomyMealFactory()
        package = factory.create_package()
        self.assertIsNotNone(package.get_food())
        self.assertIsNotNone(package.get_drink())
        self.assertIsNotNone(package.get_dessert())

    def test_luxury_package(self):
        factory = LuxuryMealFactory()
        package = factory.create_package()
        self.assertIsNotNone(package.get_food())
        self.assertIsNotNone(package.get_drink())
        self.assertIsNotNone(package.get_dessert())

if __name__ == "__main__":
    unittest.main()
    