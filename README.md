```markdown
# Online Food Ordering System

## Description
This project is for my Design Patterns course.  
An online food ordering system built with 4 design patterns.

## Design Patterns Used
- Singleton (RestaurantManager)
- Factory Method (Food creation)
- Abstract Factory (Meal packages)
- Builder (Order creation)

## Project Structure
OnlineFoodOrderingSystem/
│
├── main.py
├── README.md
├── requirements.txt
│
├── models/
│   ├── __init__.py
│   ├── food.py
│   ├── order.py
│   ├── payment.py
│   └── notification.py
│
├── patterns/
│   ├── __init__.py
│   ├── singleton.py
│   ├── factory_method.py
│   ├── abstract_factory.py
│   └── builder.py
│
└── tests/
    ├── __init__.py
    ├── test_singleton.py
    ├── test_factory.py
    ├── test_abstract.py
    └── test_builder.py

## How to Run
Open terminal in project folder and run:

```bash
python main.py

## How to Run tests
python -m unittest discover tests

## Sample 
==================================================
Online Food Ordering System
==================================================

=== Step 1: Singleton Test ===
Instance 1 == Instance 2: True

=== Step 2: Factory Method - Create Foods ===
Pizza Margherita: 85,000 IRR
Ingredients: dough, tomato sauce, mozzarella, basil
Burger Classic: 65,000 IRR
Salad Caesar: 45,000 IRR

=== Step 3: Abstract Factory - Meal Packages ===
[ECONOMY]
Food: Pizza Margherita - 85,000 IRR
Drink: Water - 5,000 IRR
Dessert: Jello - 10,000 IRR
Total: 100,000 IRR

[LUXURY]
Food: Burger Classic - 65,000 IRR
Drink: Wine - 80,000 IRR
Dessert: Tiramisu - 30,000 IRR
Total: 175,000 IRR

=== Step 4: Builder - Create Order ===
Order ID #1001:
Address: Tehran, Azadi St. Apt. 102
Discount Code: FOOD20
Payment Method: Online Card
Special Note: No pickles please, Extra sauce
Notification: SMS
Total Price: 80,000 IRR

=== Step 5: Submit Order and Notification ===
Order submitted successfully!
Order ID: 1001
Status: PENDING
SMS sent to customer: +989121234567
Your order has been accepted. Estimated delivery: 30 min

==================================================
Program executed successfully!
==================================================
```

## Author
AtrinYassari


