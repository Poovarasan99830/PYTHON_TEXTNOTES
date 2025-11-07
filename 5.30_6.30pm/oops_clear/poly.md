

## 🧩 **Python OOPs — Polymorphism (From First Principles)**



### **1️⃣ Definition (First Principles Rebuild)**

**Polymorphism** comes from Greek — *poly* = “many”, *morph* = “forms.”
In programming, it means: **one interface, many implementations.**

In **OOP**, **polymorphism** lets different objects respond to the **same function or method name** in **their own way**.

✅ **Core Idea:**

> “Different classes can define methods with the same name — but behave differently.”

This creates **flexibility** and **interchangeability** — key principles of scalable software design.

Example idea:

* `Dog.speak()` → “Woof”
* `Cat.speak()` → “Meow”
* `Bird.speak()` → “Tweet”

All have the same **method name**, but **different behavior** — this is **Polymorphism**.

---

### **2️⃣ Industry Use Cases**

| Use Case                        | Description                                                                                                              |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Django ORM Models**           | All models implement a `.save()` method but each model can override it to handle unique logic (signals, pre-save hooks). |
| **API Serializers (DRF)**       | Same method name `.serialize()` behaves differently for different models.                                                |
| **Payment Gateway Integration** | `Payment.process()` → Stripe, Razorpay, PayPal all have their own logic.                                                 |
| **Machine Learning Models**     | All ML models have `.fit()` and `.predict()`, but each behaves differently (Linear, SVM, RandomForest).                  |
| **UI Components / Widgets**     | All components have a `.render()` method — different visuals per widget.                                                 |
| **Authentication Systems**      | Multiple user types share `.authenticate()` but with custom credential logic.                                            |

---

### **3️⃣ Example Code (Multiple Examples)**

#### 🧠 Example 1 — Basic Polymorphism with Classes

```python
class Dog:
    def speak(self):
        return "Woof 🐶"

class Cat:
    def speak(self):
        return "Meow 🐱"

for animal in [Dog(), Cat()]:
    print(animal.speak())
```

**Output:**

```
Woof 🐶
Meow 🐱
```

---

#### ⚙️ Example 2 — Polymorphism in Inheritance (Method Overriding)

```python
class Vehicle:
    def start(self):
        return "Vehicle starting..."

class Car(Vehicle):
    def start(self):
        return "Car engine starting... 🚗"

class Bike(Vehicle):
    def start(self):
        return "Bike ignition ON 🏍️"

for v in [Car(), Bike()]:
    print(v.start())
```

---

#### 🧩 Example 3 — Built-in Polymorphism

```python
print(len("Uniq"))          # String length
print(len([10, 20, 30]))    # List length
print(len({"a": 1, "b": 2})) # Dict length
```

All use `len()`, but Python automatically handles it **polymorphically**.

---

#### 🧠 Example 4 — Polymorphism with Functions

```python
def add(a, b):
    return a + b

print(add(10, 5))        # int addition
print(add("Hello ", "AI"))  # string concatenation
```

---

### **4️⃣ Tasks / Questions**

1. Create a base class `Shape` with a method `area()`, and subclasses `Circle`, `Rectangle` implementing it differently.
2. Write a class `Employee` and subclass `Manager`, both with a `get_role()` method showing different messages.
3. Demonstrate polymorphism using built-in methods (`len`, `max`, `min`).
4. Use a loop to call the same method name (`speak`, `move`, etc.) on different objects.
5. Create a `Payment` base class and subclasses `UPIPayment`, `CardPayment`, `WalletPayment`, each overriding a `.process()` method.

---

### **5️⃣ Important Methods + Real-World Usage**

| Concept / Method                | Description                                                                  | Real-World Usage                                |
| ------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------- |
| **Method Overriding**           | Subclass defines a method with the same name as parent                       | Custom logic in Django models or API views      |
| **Duck Typing**                 | “If it looks like a duck and quacks like a duck…” — no need for strict types | Python treats objects by behavior, not type     |
| **Operator Overloading**        | Define how operators (`+`, `-`, etc.) work on custom objects                 | Adding ML models, Money objects, Vectors        |
| **Abstract Base Classes (ABC)** | Enforce subclasses to implement specific methods                             | Used in DRF serializers, payment interfaces     |
| **`super()`**                   | Calls overridden parent method                                               | Combine old and new logic in overridden methods |
| **Polymorphic Iteration**       | Iterate over different objects sharing same interface                        | Dynamic object processing in APIs, ML pipelines |

---

### **6️⃣ Advanced Concept + Developer Point of View (Project Use Case)**

#### 💡 Where Polymorphism Appears in Real Frameworks

| Project Area                    | Example Usage                                                                                                    |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Django Models**               | `.save()` and `.delete()` methods overridden per model to handle business logic (like logging or validation).    |
| **Django REST Framework (DRF)** | Serializers and Views use the same `.validate()` or `.perform_create()` method with custom implementations.      |
| **Authentication Systems**      | Different user types (Admin, Staff, Customer) override `.authenticate()` to handle role-based logic.             |
| **ORM Design**                  | All models share base ORM behavior but override `__str__` or validation logic differently.                       |
| **Machine Learning Systems**    | All models (NeuralNet, RandomForest, SVM) share `.fit()` / `.predict()` interfaces — but with unique algorithms. |
| **Automation Frameworks**       | BaseBot defines `.run_task()`; subclasses implement scraping, parsing, or testing behaviors.                     |

🧠 **Developer Insight:**
Polymorphism keeps your **interfaces consistent** and your **code scalable** — it allows **plug-and-play behavior**, especially in large frameworks where different entities share a common contract.

---

### **7️⃣ Real-World Inspired Example**

#### 🌍 Example: Payment Processing System (Like Razorpay / Stripe)

```python
class Payment:
    def process(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class CardPayment(Payment):
    def process(self, amount):
        return f"Processing ₹{amount} through Card 💳"

class UPIPayment(Payment):
    def process(self, amount):
        return f"Processing ₹{amount} through UPI 📱"

class WalletPayment(Payment):
    def process(self, amount):
        return f"Processing ₹{amount} through Wallet 💰"

# Polymorphic behavior
payments = [CardPayment(), UPIPayment(), WalletPayment()]

for method in payments:
    print(method.process(1500))
```

**Output:**

```
Processing ₹1500 through Card 💳
Processing ₹1500 through UPI 📱
Processing ₹1500 through Wallet 💰
```







---

## 🧠 **Python Polymorphism (From First Principles)**

### *(Write Once — Work for Many Types)*

---

### **1️⃣ Definition**

**Polymorphism** (Greek: *poly* = many, *morph* = forms) means **“one interface, many implementations.”**
It allows objects of different classes to **respond to the same method name in different ways**.

In simple words —

> “You can call the same function or method on different objects, and each behaves differently.”

✅ Promotes flexibility, scalability, and code reusability.
✅ Central idea behind “dynamic typing” and “duck typing” in Python.

---

### **2️⃣ Industry Use Cases**

| **Use Case**                 | **Description**                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------- |
| **Django Views & REST APIs** | Different views (ListView, DetailView) implement `get()`/`post()` differently.           |
| **ML Pipelines**             | `fit()` and `predict()` behave differently across models but share the same interface.   |
| **Game Engines**             | Common method like `move()` behaves differently for players, enemies, NPCs.              |
| **Automation Frameworks**    | Same function `run_task()` executes differently for web, API, or file tasks.             |
| **Payment Gateways**         | `process_payment()` works for CreditCard, UPI, PayPal — same interface, different logic. |
| **Plugin Systems**           | Each plugin subclass overrides a base method to handle unique actions.                   |

---

### **3️⃣ Example Codes (n+ Examples)**

#### 🧩 **Example 1: Built-in Polymorphism**

```python
print(len("Python"))     # 6 (string)
print(len([1, 2, 3]))    # 3 (list)
print(len({"a": 10}))    # 1 (dict)
```

✅ Same function `len()` → different behaviors for each type.

---

#### 🧩 **Example 2: Polymorphism with Functions and Objects**

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

for animal in [Dog(), Cat()]:
    print(animal.speak())
```

✅ Same method name → different outputs depending on object type.

---

#### 🧩 **Example 3: Method Overriding (Runtime Polymorphism)**

```python
class Employee:
    def role(self):
        return "Employee"

class Developer(Employee):
    def role(self):
        return "Writes Code"

class Manager(Employee):
    def role(self):
        return "Leads Team"

for emp in [Developer(), Manager()]:
    print(emp.role())
```

✅ Parent method redefined in child → custom behavior at runtime.

---

#### 🧩 **Example 4: Polymorphism with Abstract Base Class**

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditCard(Payment):
    def process(self, amount):
        return f"Paid ₹{amount} via Credit Card"

class UPI(Payment):
    def process(self, amount):
        return f"Paid ₹{amount} via UPI"

for method in [CreditCard(), UPI()]:
    print(method.process(500))
```

✅ Enforces method consistency across all subclasses.

---

#### 🧩 **Example 5: Operator Overloading (Compile-time Polymorphism)**

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 6)
print(v1 + v2)
```

✅ The `+` operator is **overloaded** to add vectors instead of numbers.

---

#### 🧩 **Example 6: Duck Typing (Pythonic Polymorphism)**

```python
class Laptop:
    def code(self, ide):
        ide.execute()

class PyCharm:
    def execute(self):
        print("Compiling & Running Python Code")

class VSCode:
    def execute(self):
        print("Linting, Debugging, Running Code")

lap = Laptop()
lap.code(PyCharm())
lap.code(VSCode())
```

✅ Any object with `execute()` method will work — that’s **duck typing**.

---

### **4️⃣ Tasks / Questions**

1. Write a base class `Shape` and subclasses `Circle`, `Rectangle`, each implementing `area()`.
2. Create a payment system where subclasses (`UPI`, `Card`, `Wallet`) override `process_payment()`.
3. Demonstrate operator overloading using `__mul__` or `__sub__`.
4. Implement polymorphism using an abstract base class for transport types (`Car`, `Bike`, `Bus`).
5. Show duck typing with objects having the same method but unrelated classes.

---

### **5️⃣ Important Methods + Real-World Usage**

| **Concept / Method**                   | **Description**                   | **Real-World Usage**                   |
| -------------------------------------- | --------------------------------- | -------------------------------------- |
| Method Overriding                      | Redefine parent methods           | Custom model or API logic              |
| `super()`                              | Call parent’s version of a method | Extend base method in subclass         |
| Abstract Methods (`@abstractmethod`)   | Enforce interface consistency     | Django/Flask class-based views         |
| Operator Overloading (`__add__`, etc.) | Customize built-in operators      | Vector, Matrix, Financial calculations |
| Duck Typing                            | Dynamic method execution          | Flexible frameworks and plugins        |
| Polymorphic Iteration                  | Treat objects uniformly           | Loops handling different object types  |
| `isinstance()`                         | Type-safe polymorphism            | Validation in serializers or schemas   |

---

### **6️⃣ Advanced Concept + Developer POV (Project-Level Use)**

| **Use Case**                | **Implementation / Behavior**                                                               |
| --------------------------- | ------------------------------------------------------------------------------------------- |
| **ORM Layer (Django)**      | Models use polymorphism to redefine `save()` or `delete()` for custom actions.              |
| **DRF Serializers / Views** | `get()` and `post()` behave differently in subclassed views.                                |
| **Authentication**          | Different user backends (`EmailAuth`, `OAuth`) override the same `authenticate()` method.   |
| **ML Models**               | Every estimator implements `fit()` and `predict()` differently but with the same interface. |
| **Plugin Systems**          | Each plugin subclass handles `execute()` or `run()` differently.                            |
| **Financial Systems**       | `calculate_interest()` varies across `SavingsAccount`, `LoanAccount`, `FDAccount`.          |
| **Logging / Monitoring**    | Subclasses of `Logger` implement custom log storage targets.                                |

---

### **7️⃣ Real-World Inspired Example**

#### 🔹 **Django REST Framework View Example**

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class BaseView(APIView):
    def get(self, request):
        return Response({"message": "Base GET"})

class UserView(BaseView):
    def get(self, request):
        return Response({"message": "User GET response"})

class ProductView(BaseView):
    def get(self, request):
        return Response({"message": "Product GET response"})
```

✅ Each subclass overrides `get()` method → **same name, different response.**

---

#### 🔹 **Machine Learning Example**

```python
class Model:
    def train(self, data):
        raise NotImplementedError

class LinearRegression(Model):
    def train(self, data):
        print("Training Linear Regression Model")

class RandomForest(Model):
    def train(self, data):
        print("Training Random Forest Model")

for m in [LinearRegression(), RandomForest()]:
    m.train("dataset.csv")
```

✅ Same interface `train()` → different training logic.

---

#### 🔹 **Real App Example — Payment Gateway**

```python
class PaymentGateway:
    def process(self, amount):
        raise NotImplementedError

class Stripe(PaymentGateway):
    def process(self, amount):
        return f"Stripe processed ₹{amount}"

class Razorpay(PaymentGateway):
    def process(self, amount):
        return f"Razorpay processed ₹{amount}"

def pay(gateway, amount):
    print(gateway.process(amount))

pay(Stripe(), 500)
pay(Razorpay(), 500)
```

✅ Same function `process()` → framework-independent extensibility.

---
