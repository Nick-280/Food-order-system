from patterns.singleton import RestaurantManager
from patterns.factory_method import PizzaFactory, BurgerFactory, SaladFactory
from patterns.abstract_factory import EconomyMealFactory, LuxuryMealFactory
from patterns.builder import OrderBuilder

def main():
    print("=" * 50)
    print("Online Food Ordering System")
    print("=" * 50)

    print("\n=== Step 1: Singleton Test ===")
    manager1 = RestaurantManager.get_instance()
    manager2 = RestaurantManager.get_instance()
    print(f"Instance 1 == Instance 2: {manager1 is manager2}")

    print("\n=== Step 2: Factory Method - Create Foods ===")
    pizza_factory = PizzaFactory()
    pizza = pizza_factory.create_food()

    print(f"{pizza.get_name()}: {pizza.get_price():,} IRR")
    print(f"Ingredients: {', '.join(pizza.get_ingredients())}")

    burger_factory = BurgerFactory()
    burger = burger_factory.create_food()

    print(f"{burger.get_name()}: {burger.get_price():,} IRR")
    print(f"Ingredients: {','.join(burger.get_ingredients())}")

    salad_factory = SaladFactory()
    salad = salad_factory.create_food()

    print(f"{salad.get_name()}: {salad.get_price():,} IRR")
    print(f"Ingredients: {','.join(salad.get_ingredients())}")

    print("\n=== Step 3: Abstract Factory - Meal Packages ===")
    economy_factory = EconomyMealFactory()
    economy_package = economy_factory.create_package()
    print("[ECONOMY]")
    print(f"Food: {economy_package.get_food().get_name()} - {economy_package.get_food().get_price():,} IRR")
    print(f"Drink: {economy_package.get_drink().get_name()} - {economy_package.get_drink().get_price():,} IRR")
    print(f"Dessert: {economy_package.get_dessert().get_name()} - {economy_package.get_dessert().get_price():,} IRR")

    total_economy = economy_package.get_food().get_price() + economy_package.get_drink().get_price() + economy_package.get_dessert().get_price()
    print(f"Total: {total_economy:,} IRR")

    luxury_factory = LuxuryMealFactory()
    luxury_package = luxury_factory.create_package()
    print("\n[LUXURY]")
    print(f"Food: {luxury_package.get_food().get_name()} - {luxury_package.get_food().get_price():,} IRR")
    print(f"Drink: {luxury_package.get_drink().get_name()} - {luxury_package.get_drink().get_price():,} IRR")
    print(f"Dessert: {luxury_package.get_dessert().get_name()} - {luxury_package.get_dessert().get_price():,} IRR")

    total_luxury = luxury_package.get_food().get_price() + luxury_package.get_drink().get_price() + luxury_package.get_dessert().get_price()
    print(f"Total: {total_luxury:,} IRR")

    print("\n=== Step 4: Builder - Create Order ===")
    builder = OrderBuilder()
    order = (builder.reset()
    .set_address("Tehran, Azadi St. Apt. 102")
    .set_discount("FOOD20")
    .set_payment("Online Card")
    .set_note("No pickles please, Extra sauce")
    .set_notification("SMS")
    .add_item(pizza.get_name(), pizza.get_price())
    .build())
    print(order)


    print("\n=== Step 5: Submit Order and Notification ===")
    order.order_id = manager1.add_order(order)
    print(f"Order submitted successfully!")
    print(f"Order ID: {order.order_id}")
    print(f"Status: PENDING")
    print(f"SMS sent to customer: +989121234567")
    print(f"Your order has been accepted. Estimated delivery: 30 min")
    print("\n" + "=" * 50)
    print("Program executed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()


