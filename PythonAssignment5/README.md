Here’s a simple and clear README file for your Python OOP project using inheritance and encapsulation:

---

📱 Smart Device OOP Example

This Python project demonstrates Object-Oriented Programming (OOP) concepts including:

- Class creation
- Inheritance
- Encapsulation
- Method overriding

The program simulates a basic model of smart devices — a Smartphone and a Smartwatch — using class-based design.

---

🧱 Project Structure

Classes:

1. Smartphone

   - Attributes: brand, model, screen_size, and private __storage
   - Methods:
     - get_specs() – returns formatted device specs
     - get_storage() – safely accesses encapsulated storage

2. Smartwatch (inherits from Smartphone)
   - Uses default screen size (1.5 inches)
   - Overrides get_specs() to customize smartwatch description

---

✅ Features

- Demonstrates encapsulation using a private attribute (__storage)
- Uses inheritance to extend the Smartphone class
- Illustrates method overriding in Smartwatch
- Emphasizes constructor usage with super()

---

▶ How to Run

Make sure you have Python installed. Then run:

bash
python class_inheritance.py

---

📌 Sample Output

```
*** Smartphone ***
Phone specifications: Samsung Galaxy A03 Core with 6.5 inch screen

Phone Storage: 64 GB

*** Smartwatch ***
Watch specifications: Apple Series 5 Smartwatch with 1.5 inch display
```
