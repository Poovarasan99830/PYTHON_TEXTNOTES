<!-- Perfect 👌 Let’s build the **E-Commerce Order Management System** step by step using **OOP concepts**.

I’ll break it into clear **tasks with code examples** so you can implement gradually.

---

## 🔹 Step 1: Product Class (Encapsulation + Inheritance)

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.__stock = stock   # private attribute for encapsulation

    def get_stock(self):
        return self.__stock

    def reduce_stock(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
        else:
            raise ValueError(f"Not enough stock for {self.name}")

    def increase_stock(self, quantity):
        self.__stock += quantity


# Inheritance
class PhysicalProduct(Product):
    def __init__(self, name, price, stock, weight):
        super().__init__(name, price, stock)
        self.weight = weight


class DigitalProduct(Product):
    def __init__(self, name, price, stock, file_size):
        super().__init__(name, price, stock)
        self.file_size = file_size
```

---

## 🔹 Step 2: Customer Class

```python
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.order_history = []

    def add_order(self, order):
        self.order_history.append(order)

    def view_orders(self):
        for order in self.order_history:
            print(order)
```

---

## 🔹 Step 3: Cart Class

```python
class Cart:
    def __init__(self):
        self.items = {}   # {product: quantity}

    def add_product(self, product, quantity=1):
        if product.get_stock() >= quantity:
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
        else:
            print(f"Not enough stock for {product.name}")

    def remove_product(self, product, quantity=1):
        if product in self.items:
            self.items[product] -= quantity
            if self.items[product] <= 0:
                del self.items[product]

    def calculate_total(self):
        return sum(product.price * qty for product, qty in self.items.items())

    def show_cart(self):
        for product, qty in self.items.items():
            print(f"{product.name} x {qty} = {product.price * qty}")
        print("Total:", self.calculate_total())
```

---

## 🔹 Step 4: Order Class

```python
import uuid

class Order:
    def __init__(self, customer, items):
        self.order_id = str(uuid.uuid4())[:8]   # random short order id
        self.customer = customer
        self.items = items
        self.total = sum(product.price * qty for product, qty in items.items())

        # update stock when order is created
        for product, qty in items.items():
            product.reduce_stock(qty)

    def __str__(self):
        return f"OrderID: {self.order_id}, Customer: {self.customer.name}, Total: {self.total}"
```

---

## 🔹 Step 5: Integration Example

```python
# Create Products
laptop = PhysicalProduct("Laptop", 50000, 5, 2.5)
ebook = DigitalProduct("Python Ebook", 500, 100, "5MB")

# Customer
cust1 = Customer("Alice", "alice@example.com")

# Cart
cart = Cart()
cart.add_product(laptop, 1)
cart.add_product(ebook, 2)
cart.show_cart()

# Checkout -> Create Order
order1 = Order(cust1, cart.items)
cust1.add_order(order1)

print("\nAfter Checkout:")
print("Laptop Stock:", laptop.get_stock())
print("Ebook Stock:", ebook.get_stock())

cust1.view_orders()
```

---

✅ **Concepts Covered**:

* **Encapsulation** → stock is private and only updated via methods.
* **Inheritance** → `PhysicalProduct` and `DigitalProduct`.
* **Polymorphism (indirect)** → product subclasses behave differently (weight vs file\_size).
* **Association** → Customer ↔ Order ↔ Product.

---

👉 Do you want me to make this into a **menu-driven CLI app** (like a small e-commerce console where user can choose to add to cart, checkout, view orders, etc.) so it feels like a **real project demo**? -->
from abc import ABC, abstractmethod

# ---------------- 1. Encapsulation ----------------
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance


# ---------------- 2. Inheritance ----------------
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"{self.brand} is moving at {self.speed} km/h")


class Car(Vehicle):
    def drive(self):
        print(f"🚗 {self.brand} car is driving at {self.speed} km/h")


class Bike(Vehicle):
    def drive(self):
        print(f"🏍️ {self.brand} bike is riding at {self.speed} km/h")


# ---------------- 3. Polymorphism ----------------
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def print_area(shape):
    print("Area:", shape.area())


# ---------------- 4. Abstraction ----------------
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class AbsCircle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class AbsRectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# ---------------- 5. Operator Overloading ----------------
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


# ---------------- Main Menu ----------------
def main():
    while True:
        print("\n===== OOP Mini Task Menu =====")
        print("1. Encapsulation (Bank Account)")
        print("2. Inheritance (Car & Bike)")
        print("3. Polymorphism (Shapes Area)")
        print("4. Abstraction (Abstract Shape)")
        print("5. Operator Overloading (Vector)")
        print("6. Exit")

        choice = input("Choose a concept: ")

        if choice == "1":
            acc = BankAccount("Alice", 1000)
            acc.deposit(500)
            acc.withdraw(300)
            print("Balance:", acc.get_balance())

        elif choice == "2":
            car = Car("Toyota", 120)
            bike = Bike("Yamaha", 80)
            car.drive()
            bike.drive()

        elif choice == "3":
            c = Circle(5)
            r = Rectangle(4, 6)
            print_area(c)
            print_area(r)

        elif choice == "4":
            shapes = [AbsCircle(5), AbsRectangle(4, 6)]
            for s in shapes:
                print("Area:", s.area())

        elif choice == "5":
            v1 = Vector(2, 3)
            v2 = Vector(4, 1)
            print("Vector Sum:", v1 + v2)

        elif choice == "6":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
