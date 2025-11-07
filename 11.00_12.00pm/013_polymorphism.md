

## 🦆 1) **Duck Typing** → *Dynamic behavior based on methods, not types*

> “If it quacks like a duck, I don’t care what it is.”

### 🧾 **Real-World Example: Generating invoices from different sources**

We have multiple objects that can generate an **invoice** — but they’re not subclasses of each other.
As long as they implement `.generate_invoice()`, our function doesn’t care what their actual type is.

```python
class OnlineOrder:
    def generate_invoice(self):
        return "Generated invoice for online order"

class StorePurchase:
    def generate_invoice(self):
        return "Generated invoice for store purchase"

class Subscription:
    def generate_invoice(self):
        return "Generated invoice for subscription billing"

def process_invoice(order):
    # Duck typing: assume the object has generate_invoice()
    print(order.generate_invoice())

# Real usage
orders = [OnlineOrder(), StorePurchase(), Subscription()]
for o in orders:
    process_invoice(o)
```

✅ Even though they are unrelated classes, `process_invoice` works for all — **behavior > type**.

---

## 🧬 2) **Method Overriding** → *Subclass replaces parent behavior*

> “Child class changes how it does something inherited from the parent.”

### 🚚 **Real-World Example: Shipping cost calculation**

We have a base class `Shipping` that provides a generic `calculate_cost`.
Different shipping methods override it to apply their own pricing logic.

```python
class Shipping:
    def calculate_cost(self, weight):
        return 5 * weight  # base cost

class ExpressShipping(Shipping):
    def calculate_cost(self, weight):
        return 10 * weight + 50  # extra express charge

class InternationalShipping(Shipping):
    def calculate_cost(self, weight):
        return 15 * weight + 100  # customs fee

shipments = [
    ExpressShipping(),
    InternationalShipping()
]

for s in shipments:
    print(f"Cost: ₹{s.calculate_cost(10)}")
```

✅ All subclasses **override** the method to provide their own calculation rules — classic inheritance polymorphism.

---

## ➕ 3) **Operator Overloading** → *Same operator, different meaning*

> “Teach Python operators to work with your custom objects in a meaningful way.”

### 📚 **Real-World Example: Combining booklets to find total pages**

```python
class Booklet:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Booklet(self.pages + other.pages)

    def __repr__(self):
        return f"<Booklet: {self.pages} pages>"

b1 = Booklet(40)
b2 = Booklet(60)
total = b1 + b2   # uses __add__
print(total)      # <Booklet: 100 pages>
```

✅ Here, the `+` operator is **overloaded** to mean “combine booklets by adding their pages.”
You could also overload `*` to mean “duplicate copies,” etc.

---

## 🧠 4) **Function Overloading** → *Simulate multiple ways to call one function*

> Python doesn’t have true function overloading, but we can **simulate** it using:

* default arguments
* `*args` / `**kwargs`
* or `functools.singledispatch`

### 📅 **Real-World Example: Customer greeting system**

You want to greet a customer differently depending on whether:

* You only know their name
* You also know their age
* You have no info

```python
def greet(name=None, age=None):
    if name and age:
        print(f"Hello {name}, {age} years young!")
    elif name:
        print(f"Hello {name}!")
    else:
        print("Hello, valued customer!")

greet()                     # Hello, valued customer!
greet("Alice")              # Hello Alice!
greet("Bob", age=30)        # Hello Bob, 30 years young!
```

✅ One function, **multiple behaviors** based on arguments — simulated overloading.

👉 Alternatively, `functools.singledispatch` can do type-based dispatch in a cleaner way.

---

## 🧰 5) **Built-in Polymorphism** → *One built-in function works for many types*

> “Python functions like `len()`, `sum()`, `max()`, `sorted()` adapt their behavior to the object’s interface.”

### 🗂️ **Real-World Example: Counting elements in different collections**

```python
products = ["Pen", "Pencil", "Notebook"]
categories = {"Stationery": 10, "Electronics": 5}
message = "Thank you!"

print(len(products))    # 3 → number of products
print(len(categories))  # 2 → number of categories
print(len(message))     # 10 → number of characters
```

✅ `len()` is polymorphic:

* For lists, it counts items
* For dicts, it counts keys
* For strings, it counts characters

👉 This works because each type implements the **`__len__`** method.

---

## 📝 Quick Recap Table

| Type                     | Real-World Context          | Key Idea                                                        |
| ------------------------ | --------------------------- | --------------------------------------------------------------- |
| 🦆 Duck Typing           | Invoicing system            | Different classes share same method name, no inheritance needed |
| 🧬 Method Overriding     | Shipping cost calculation   | Child modifies parent’s method behavior                         |
| ➕ Operator Overloading   | Booklet total pages         | Custom meaning for `+`                                          |
| 🧠 Function Overloading  | Greeting customers          | One function, different logic depending on arguments            |
| 🧰 Built-in Polymorphism | len() on list, dict, string | Built-ins adapt to the object’s protocol                        |

🧠💻








Perfect! Let’s expand this **real-world, practical examples** format for **more Python polymorphism scenarios**, just like your original style 🏪✨

---

## 🦆 1) **Duck Typing** → *Dynamic behavior based on methods, not types*

> “If it quacks like a duck, I don’t care what it is.”

### 🧾 **Real-World Example: Payment System**

```python
class CreditCardPayment:
    def pay(self):
        return "Paid using Credit Card"

class PayPalPayment:
    def pay(self):
        return "Paid using PayPal"

class CryptoPayment:
    def pay(self):
        return "Paid using Bitcoin"

def process_payment(payment):
    print(payment.pay())

payments = [CreditCardPayment(), PayPalPayment(), CryptoPayment()]
for p in payments:
    process_payment(p)
```

✅ Different classes, same method name `.pay()`, function works for all — **behavior > type**

---

## 🧬 2) **Method Overriding** → *Subclass replaces parent behavior*

> “Child class changes how it does something inherited from the parent.”

### 🚚 **Real-World Example: Employee Salary Calculation**

```python
class Employee:
    def calculate_salary(self, base):
        return base

class Manager(Employee):
    def calculate_salary(self, base):
        return base + 5000  # bonus for manager

class Intern(Employee):
    def calculate_salary(self, base):
        return base - 1000  # unpaid leave deduction

staff = [Manager(), Intern()]
for s in staff:
    print(s.calculate_salary(20000))
```

✅ Same method `.calculate_salary()`, behaves differently based on subclass

---

## ➕ 3) **Operator Overloading** → *Same operator, different meaning*

> “Teach Python operators to work with your custom objects in a meaningful way.”

### 📚 **Real-World Example: Shopping Cart Quantities**

```python
class CartItem:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return CartItem(self.quantity + other.quantity)

    def __repr__(self):
        return f"<CartItem: {self.quantity} pcs>"

item1 = CartItem(3)
item2 = CartItem(5)
total_items = item1 + item2
print(total_items)  # <CartItem: 8 pcs>
```

✅ `+` operator now adds **quantities** of custom objects

---

## 🧠 4) **Function Overloading** → *Simulate multiple ways to call one function*

> Python doesn’t have true overloading — we use default args, `*args`, or `singledispatch`.

### 📅 **Real-World Example: Notifications System**

```python
def notify(user=None, message=None):
    if user and message:
        print(f"Notify {user}: {message}")
    elif user:
        print(f"Notify {user}: You have a new message!")
    else:
        print("Notify all users: System maintenance scheduled!")

notify()                   # Notify all users
notify("Alice")            # Notify Alice: default message
notify("Bob", "Order ready")  # Notify Bob: Order ready
```

✅ Same function, different behavior based on arguments — simulated overloading

---

## 🧰 5) **Built-in Polymorphism** → *One built-in function works for many types*

> Python built-ins like `len()`, `sum()`, `sorted()` adapt to object interface.

### 🗂️ **Real-World Example: Analyzing Sales Data**

```python
daily_sales = [100, 200, 150, 50]
monthly_sales = {"Jan": 3000, "Feb": 3500, "Mar": 2800}
sales_message = "Total sales report"

print(len(daily_sales))     # 4 → days
print(len(monthly_sales))   # 3 → months
print(len(sales_message))   # 18 → characters in string
```

✅ `len()` works on **lists, dicts, strings** — polymorphism in built-ins

---

## 📝 Expanded Recap Table

| Type                     | Real-World Context            | Key Idea                                                        |
| ------------------------ | ----------------------------- | --------------------------------------------------------------- |
| 🦆 Duck Typing           | Payment system                | Different classes share same method name, no inheritance needed |
| 🧬 Method Overriding     | Employee salary calculation   | Child modifies parent’s method behavior                         |
| ➕ Operator Overloading   | Shopping cart item quantities | Custom meaning for `+`                                          |
| 🧠 Function Overloading  | Notifications system          | One function, different logic depending on arguments            |
| 🧰 Built-in Polymorphism | Analyzing sales data          | Built-ins adapt to the object’s protocol                        |






Perfect! Let’s add **5 more real-world examples** in the **same Python + practical style** so you have **10+ total polymorphism examples** 🏪✨

---

## 🦆 6) **Duck Typing** → *Dynamic behavior based on methods, not types*

### 📦 **Example: Notification Sender (Email, SMS, Push)**

```python
class EmailSender:
    def send(self):
        return "Email sent"

class SMSSender:
    def send(self):
        return "SMS sent"

class PushSender:
    def send(self):
        return "Push notification sent"

def notify(sender):
    print(sender.send())

senders = [EmailSender(), SMSSender(), PushSender()]
for s in senders:
    notify(s)
```

✅ Different classes, same `.send()` method → Python treats all as “sendable”

---

## 🧬 7) **Method Overriding** → *Subclass replaces parent behavior*

### 🏨 **Example: Hotel Room Pricing**

```python
class Room:
    def price(self):
        return 1000

class DeluxeRoom(Room):
    def price(self):
        return 2000

class SuiteRoom(Room):
    def price(self):
        return 5000

rooms = [DeluxeRoom(), SuiteRoom()]
for r in rooms:
    print(r.price())
```

✅ Same method `.price()`, behaves differently for each room type

---

## ➕ 8) **Operator Overloading** → *Same operator, different meaning*

### 🍎 **Example: Fruit Basket Weight**

```python
class Fruit:
    def __init__(self, weight):
        self.weight = weight

    def __add__(self, other):
        return Fruit(self.weight + other.weight)

    def __repr__(self):
        return f"<Fruit: {self.weight} kg>"

basket1 = Fruit(2)
basket2 = Fruit(3)
total_basket = basket1 + basket2
print(total_basket)  # <Fruit: 5 kg>
```

✅ `+` operator adds **weights** of custom objects

---

## 🧠 9) **Function Overloading** → *Simulate multiple ways to call one function*

### 🛒 **Example: Product Discount Calculator**

```python
def discount(price, percent=None):
    if percent:
        return price - (price * percent / 100)
    else:
        return price - 50  # default discount

print(discount(500))        # default discount → 450
print(discount(500, 20))    # 20% discount → 400
```

✅ One function, multiple behaviors based on arguments

---

## 🧰 10) **Built-in Polymorphism** → *One built-in function works for many types*

### 🎓 **Example: Students & Scores**

```python
names = ["Alice", "Bob", "Charlie"]
scores = {"Math": 90, "Science": 85}
message = "Welcome Students"

print(len(names))    # 3
print(len(scores))   # 2
print(len(message))  # 15
```

✅ `len()` adapts to list, dict, string — built-in polymorphism

---

## 📝 Updated Recap Table (10 Examples)

| Type                     | Real-World Context                   | Key Idea                                                        |
| ------------------------ | ------------------------------------ | --------------------------------------------------------------- |
| 🦆 Duck Typing           | Payment system / Notification Sender | Different classes share same method name, no inheritance needed |
| 🧬 Method Overriding     | Employee salary / Hotel room pricing | Child modifies parent’s method behavior                         |
| ➕ Operator Overloading   | Shopping cart / Fruit basket         | Custom meaning for `+`                                          |
| 🧠 Function Overloading  | Notifications / Discount calculator  | One function, different logic depending on arguments            |
| 🧰 Built-in Polymorphism | Sales data / Students & Scores       | Built-ins adapt to the object’s protocol                        |

---

If you want, I can **create 5 MORE examples** using **e-commerce, booking systems, library management, and transportation apps** — so you have a **full 15+ super practical examples** all in this format.

Do you want me to do that next?

