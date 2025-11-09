
# ___________________________________________________________________
## 🧠 **Python Polymorphism (From First Principles)**
# ___________________________________________________________________



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



# ____________________________________________________________________________
### **2️⃣ Industry Use Cases**
# ____________________________________________________________________________





| **Use Case**                 | **Description**                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------- |
| **Django Views & REST APIs** | Different views (ListView, DetailView) implement `get()`/`post()` differently.           |
| **ML Pipelines**             | `fit()` and `predict()` behave differently across models but share the same interface.   |
| **Game Engines**             | Common method like `move()` behaves differently for players, enemies, NPCs.              |
| **Automation Frameworks**    | Same function `run_task()` executes differently for web, API, or file tasks.             |
| **Payment Gateways**         | `process_payment()` works for CreditCard, UPI, PayPal — same interface, different logic. |
| **Plugin Systems**           | Each plugin subclass overrides a base method to handle unique actions.                   |

---




# _______________________________________________________________________________________
### **3️⃣ Example Codes (n+ Examples)**
# _______________________________________________________________________________________






#### 🧩 **Example 1: Built-in Polymorphism**

```python
print(len("Python"))     # 6 (string)
print(len([1, 2, 3]))    # 3 (list)
print(len({"a": 10}))    # 1 (dict)
```

✅ Same function `len()` → different behaviors for each type.





# ______________________________________________________________
#### 🧩 **Example 2: Polymorphism with Functions and Objects**
# _______________________________________________________________




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





# ______________________________________________________________
## 🧩 **Example 3: Method Overriding (Runtime Polymorphism)**
# _______________________________________________________________




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






# ______________________________________________________________
#### 🧩 **Example 4: Polymorphism with Abstract Base Class**
# _______________________________________________________________



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





# ___________________________________________________________________
## 🧩 **Example 5: Operator Overloading (Compile-time Polymorphism)**
# ___________________________________________________________________



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


# ___________________________________________________________________
#### 🧩 **Example 6: Duck Typing (Pythonic Polymorphism)**
# ___________________________________________________________________




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





# ___________________________________________________________________
# **4️⃣ Tasks / Questions**
# ___________________________________________________________________

1. Write a base class `Shape` and subclasses `Circle`, `Rectangle`, each implementing `area()`.
2. Create a payment system where subclasses (`UPI`, `Card`, `Wallet`) override `process_payment()`.
3. Demonstrate operator overloading using `__mul__` or `__sub__`.
4. Implement polymorphism using an abstract base class for transport types (`Car`, `Bike`, `Bus`).
5. Show duck typing with objects having the same method but unrelated classes.





# ______________________________________________________________________________
## **5️⃣ Important Methods + Real-World Usage**
# _______________________________________________________________________________




| **Concept / Method**                   | **Description**                   | **Real-World Usage**                   |
| -------------------------------------- | --------------------------------- | -------------------------------------- |
| Method Overriding                      | Redefine parent methods           | Custom model or API logic              |
| `super()`                              | Call parent’s version of a method | Extend base method in subclass         |
| Abstract Methods (`@abstractmethod`)   | Enforce interface consistency     | Django/Flask class-based views         |
| Operator Overloading (`__add__`, etc.) | Customize built-in operators      | Vector, Matrix, Financial calculations |
| Duck Typing                            | Dynamic method execution          | Flexible frameworks and plugins        |
| Polymorphic Iteration                  | Treat objects uniformly           | Loops handling different object types  |
| `isinstance()`                         | Type-safe polymorphism            | Validation in serializers or schemas   |






# _______________________________________________________________________________________
# **6️⃣ Advanced Concept + Developer POV (Project-Level Use)**
# _________________________________________________________________________________________





| **Use Case**                | **Implementation / Behavior**                                                               |
| --------------------------- | ------------------------------------------------------------------------------------------- |
| **ORM Layer (Django)**      | Models use polymorphism to redefine `save()` or `delete()` for custom actions.              |
| **DRF Serializers / Views** | `get()` and `post()` behave differently in subclassed views.                                |
| **Authentication**          | Different user backends (`EmailAuth`, `OAuth`) override the same `authenticate()` method.   |
| **ML Models**               | Every estimator implements `fit()` and `predict()` differently but with the same interface. |
| **Plugin Systems**          | Each plugin subclass handles `execute()` or `run()` differently.                            |
| **Financial Systems**       | `calculate_interest()` varies across `SavingsAccount`, `LoanAccount`, `FDAccount`.          |
| **Logging / Monitoring**    | Subclasses of `Logger` implement custom log storage targets.                                |








# ___________________________________________________________________________________________
### **7️⃣ Real-World Inspired Example**
# ___________________________________________________________________________________________






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






# ___________________________________________________________________
#### 🔹 **Machine Learning Example**
# ___________________________________________________________________



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




# ___________________________________________________________________
#### 🔹 **Real App Example — Payment Gateway**
# ___________________________________________________________________






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




# ___________________________________________________________________
