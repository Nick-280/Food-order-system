import unittest
from patterns.singleton import RestaurantManager


class TestSingleton(unittest.TestCase):
    def test_two_instances_are_same(self):
        m1 = RestaurantManager.get_instance()
        m2 = RestaurantManager.get_instance()
        self.assertIs(m1, m2)

    def test_add_order_returns_id(self):
        manager = RestaurantManager.get_instance()
        
        class SampleOrder:
            def __init__(self):
                self.order_id = None
                
        order = SampleOrder()
        order_id = manager.add_order(order)
        self.assertEqual(order_id, 1001)


if __name__ == "__main__":
    unittest.main()

