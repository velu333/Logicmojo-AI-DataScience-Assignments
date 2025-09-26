# Assignment-04 (Python OOP )

This folder contains solutions to **five problems** based on Object-Oriented Programming (OOP) concepts in Python, as well as the use of the **`pint`** library for unit handling.

---

## 📌 Problem 1: Library System
- **Classes:**
  - `Book`: Represents a book with attributes such as title, author, and ISBN.
  - `Patron`: Represents a library member with attributes like name and borrowed books.
  - `Library`: Represents the collection of books and manages patrons.
- **Features:**
  - Add books, register patrons, and handle borrowing/returning of books.

---

## 📌 Problem 2: Shape Hierarchy
- **Base Class:**
  - `Shape`: Contains abstract methods `area()` and `perimeter()`. The `perimeter()` raises `NotImplementedError`.
- **Derived Classes:**
  - `Rectangle`: Implements both `area()` and `perimeter()`.
  - `Circle`: Implements both `area()` and `perimeter()`.
- **Demonstration:**
  - Create instances of `Rectangle` and `Circle`, and compute their areas and perimeters.

---

## 📌 Problem 3: Employee System
- **Base Class:**
  - `Employee`: Attributes → `name`, `employee_id`.
- **Subclasses:**
  - `SalariedEmployee`: Attribute → `monthly_salary`.  
    Method → `calculate_paycheck()` returns the monthly salary.
  - `HourlyEmployee`: Attributes → `hourly_rate`, `hours_worked`.  
    Method → `calculate_paycheck()` returns total weekly pay.
- **Demonstration:**
  - Instances of both employee types are created and their paycheck calculations shown.

---

## 📌 Problem 4: Polynomial Class
- **Class: `Polynomial`**
  - Attributes:
    - `degree` (positive integer, except for constant case).
    - `coefficients` (list of floats, length = degree + 1).
  - **Methods:**
    - `evaluate(x)`: Evaluates the polynomial at a given `x`.
    - `plot([x1, x2])`: Plots the polynomial in the given range.
    - `derivative(x)`: Evaluates the derivative at a given `x`.
    - `plot_derivative([x1, x2])`: Plots the derivative in the given range.
  - **Validation:**
    - Checks that the degree matches the number of coefficients.
- **Examples:**
  - `3x^4 + 5x^3 + x^2 + 9x + 10 → [3, 5, 1, 9, 10]`
  - `0.7x^3 + 2.5x → [0.7, 0, 2.5, 0]`

---

## 📌 Problem 5: Online Shopping Cart
- **Classes:**
  - `Product`: Attributes → `name`, `price`.
  - `ShoppingCart`: Maintains a list of products.
- **Methods:**
  - `add_item(product)`: Add a product to the cart.
  - `remove_item(product_name)`: Remove a product by name.
  - `calculate_total()`: Compute total cost of items in the cart.

---

## 📦 Requirements
This project uses the [`pint`](https://pint.readthedocs.io/) library for unit handling in Python.  

### requirements.txt
```
pint
```

---

## ▶️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/velu333/Logicmojo-AI-DataScience-Assignments.git
   cd Logicmojo-AI-DataScience-Assignments/Assignment-4
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Open the notebook:
   ```bash
   jupyter notebook assignment_04_velayutham_augustheesan_python_oop.ipynb
   ```

4. Run the cells to see implementations and test outputs.

---

## 📖 Notes
- The **`pint`** library is included in `requirements.txt` for easy installation.  
  Example usage:
  ```python
  from pint import UnitRegistry
  ureg = UnitRegistry()
  length = 5 * ureg.meter
  print(length.to("centimeter"))  # 500 centimeter
  ```
- The notebook demonstrates problem solutions step by step.
- Example plots for the polynomial and its derivative are included.

---
