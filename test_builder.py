import unittest
from patterns.builder import OrderBuilder

class TestBuilder(unittest.TestCase):
    def test_set_address(self):
        builder = OrderBuilder()
        order = builder.reset().set_address("Tehran").set_payment("Online Card").build()
        self.assertEqual(order.address, "Tehran")

    def test_add_item_increases_total(self):
        builder = OrderBuilder()
        order = builder.reset().set_address("Tehran").set_payment("Online Card").add_item("Pizza", 85000).build()
        self.assertEqual(order.total_price, 85000)

    def test_discount_applies_correctly(self):
        builder = OrderBuilder()
        order = builder.reset().set_address("Tehran").set_payment("Online Card").set_discount("FOOD20").add_item("Pizza", 100000).build()
        self.assertEqual(order.get_final_price(), 80000)

    def test_empty_address_raises_error(self):
        builder = OrderBuilder()
        with self.assertRaises(ValueError):
            builder.reset().set_address("").build()

if __name__ == "__main__":
    unittest.main()

