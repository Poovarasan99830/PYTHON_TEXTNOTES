
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
"
print(len(["python"]))    # 1 (list)

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



<!-- Imagine a remote-controlled toy.

    You don’t check whether it’s a car, boat, or drone —
    you just check if it has a .start() and .stop() button.
     If those exist, you can control it → that’s duck typing! -->

# ______________________________________________________________
## 🧩 **Example 3: Method Overriding (Runtime Polymorphism)**
# _______________________________________________________________


 # 🧩 Without Overriding:

```python
class Employee:
    def role(self):
        print("General Employee")

class Developer(Employee):
    def developer_role(self):
        print("Writes Code")

class Manager(Employee):
    def manager_role(self):
        print("Leads Team")

for emp in [Employee(), Developer(), Manager()]:
    # Different method names — need manual checks
    if isinstance(emp, Developer):
        emp.developer_role()
    elif isinstance(emp, Manager):
        emp.manager_role()
    else:
        emp.role()



# Problem:
#    You need if / elif conditions.
#    Code becomes hard to maintain when new classes come (Tester, HR, etc.)
#    You’re breaking the “write once, work for many” principle





 # 🧩 With Overriding:

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



<!-- Overriding keeps the interface same,
but allows the behavior to evolve -->

<!-- ✅ No conditions
✅ Clean and extendable
✅ If you add 10 more child classes → same method name will still work! -->


<!-- You → Dog.speak()
   → Cat.speak() -->

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
<!-- result = a + b
result = a.__add__(b) -->





```python

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.amount - other.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __str__(self):
        return f"₹{self.amount}"

m1 = Money(100)
m2 = Money(50)
print(m1 + m2)   # ₹150
print(m1 - m2)   # ₹50
print(m1 == m2)  # False







# | Operator | Special Method             |
# | :------- | :------------------------- |
# | `+`      | `__add__(self, other)`     |
# | `-`      | `__sub__(self, other)`     |
# | `*`      | `__mul__(self, other)`     |
# | `/`      | `__truediv__(self, other)` |
# | `==`     | `__eq__(self, other)`      |
# | `<`      | `__lt__(self, other)`      |
# | `>`      | `__gt__(self, other)`      |



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



<!-- | Example        | Real Analogy                                                                                     |
| :------------- | :----------------------------------------------------------------------------------------------- |
| **Dog–Cat**    | You directly talk to animals — each responds in its own way.                                     |
| **Laptop–IDE** | Laptop uses *different tools (IDE)* to do the same job (coding) — each tool behaves differently. | -->


<!-- You → Laptop.code(IDE)
           ↓
     IDE.execute() -->


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
# 🔹 **Real App Example -EMPLOYEE SALARY MANAGEMENT
# ___________________________________________________________________



```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, bonus):
        """Overload + operator to add bonus to salary"""
        return Employee(self.name, self.salary + bonus)

    def __gt__(self, other):
        """Overload > operator to compare salaries"""
        return self.salary > other.salary

    def __lt__(self, other):
        """Overload < operator"""
        return self.salary < other.salary

    def __eq__(self, other):
        """Overload == operator"""
        return self.salary == other.salary

    def __str__(self):
        return f"{self.name} earns ₹{self.salary}"

# Create Employee objects
emp1 = Employee("Rahul", 50000)
emp2 = Employee("Priya", 65000)

# Compare salaries
print(emp1 > emp2)   # False
print(emp1 < emp2)   # True
print(emp1 == emp2)  # False

# Add bonus
emp1_bonus = emp1 + 10000
print(emp1_bonus)    # Rahul earns ₹60000
