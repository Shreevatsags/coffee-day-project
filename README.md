# ☕ Coffee Day Project

A simple console-based Coffee Machine Simulator built with Python. This project demonstrates Object-Oriented Programming (OOP) concepts by simulating a real coffee vending machine where users can order drinks, make payments, and manage machine resources.

## 🚀 Features

* Order different coffee drinks
* Resource management (water, milk, coffee)
* Coin-based payment system
* Automatic change calculation
* Machine report generation
* Object-Oriented Programming implementation
* Interactive command-line interface

## 📂 Project Structure

```text
coffee-day-project/
│
├── main.py              # Main program execution
├── coffee_maker.py      # Handles coffee preparation and resources
├── menu.py              # Coffee menu and drink definitions
├── money_machine.py     # Handles payment processing
├── README.md            # Project documentation
└── LICENSE              # MIT License
```

## 📋 Available Commands

| Command    | Description                          |
| ---------- | ------------------------------------ |
| espresso   | Order Espresso                       |
| latte      | Order Latte                          |
| cappuccino | Order Cappuccino                     |
| report     | Display current resources and profit |
| off        | Turn off the coffee machine          |

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/coffee-day-project.git
```

### 2. Navigate to the Project Directory

```bash
cd coffee-day-project
```

### 3. Run the Application

```bash
python main.py
```

## ☕ Menu

| Drink      | Ingredients         |
| ---------- | ------------------- |
| Espresso   | Water, Coffee       |
| Latte      | Water, Milk, Coffee |
| Cappuccino | Water, Milk, Coffee |

## 💰 Payment System

The machine accepts:

* Quarters ($0.25)
* Dimes ($0.10)
* Nickels ($0.05)
* Pennies ($0.01)

The system automatically:

* Calculates the total inserted amount
* Verifies sufficient payment
* Returns change when applicable
* Updates profit records

## 🎯 Learning Objectives

This project helps understand:

* Classes and Objects
* Encapsulation
* Modular Programming
* Python File Organization
* User Input Handling
* Resource Management Logic

## 📸 Sample Output

```text
What would you like? (espresso/latte/cappuccino): latte

Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0

Here is $0.50 in change.
Here is your latte ☕. Enjoy!
```


---
## Designed & Developed by
* [Shreevatsa](https://github.com/Shreevatsags)
  
⭐ If you found this project useful, consider giving it a star on GitHub!
