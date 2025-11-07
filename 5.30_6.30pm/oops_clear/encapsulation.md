Perfect 💪 — continuing your **OOP Mastery Series**, here’s the next complete concept:

# 🧠 **Encapsulation in Python (From First Principles)**

### *(Data Protection + Controlled Access — The Core of Secure OOP Design)*

---

### **1️⃣ Definition**

**Encapsulation** means **binding data (attributes)** and **behavior (methods)** together inside a class and **restricting direct access** to some components.

It hides the internal representation of an object and **protects its data from unauthorized access or modification**.

In essence:

> “Encapsulation keeps your data safe and your code clean — only the class decides how its data is used.”

✅ Prevents unintended interference
✅ Improves code maintainability
✅ Enforces controlled access via getters/setters

---

### **2️⃣ Industry Use Cases**

| **Use Case**                    | **Description**                                                                        |
| ------------------------------- | -------------------------------------------------------------------------------------- |
| **Banking / FinTech Apps**      | Hide account balances, expose only deposit/withdraw methods.                           |
| **User Authentication Systems** | Protect passwords using private attributes and property decorators.                    |
| **E-commerce**                  | Product prices and discounts controlled via class methods, not direct variable access. |
| **API Security**                | Private configuration keys stored in encapsulated objects.                             |
| **Machine Learning Models**     | Hyperparameters and weights encapsulated with controlled update methods.               |
| **IoT Devices**                 | Sensor readings hidden; accessible only through defined APIs.                          |
| **ORM / Data Layers**           | Encapsulation ensures DB fields are validated before saving.                           |

---

### **3️⃣ Example Codes (n+ Examples)**

#### 🧩 **Example 1: Basic Encapsulation**

```python
class Student:
    def __init__(self, name, grade):
        self.name = name      # public attribute
        self.__grade = grade  # private attribute

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade!")

s = Student("Poovarasan", 85)
print(s.get_grade())   # ✅ Access via getter
s.set_grade(95)
print(s.get_grade())
```

---

#### 🧩 **Example 2: Name Mangling**

```python
class Demo:
    def __init__(self):
        self.__hidden = "Secret Data"

obj = Demo()
# Direct access not allowed
# print(obj.__hidden) ❌ AttributeError
print(obj._Demo__hidden)  # ✅ Access using name mangling (not recommended)
```

---

#### 🧩 **Example 3: Encapsulation with Getters/Setters (`@property`)**

```python
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            raise ValueError("Salary must be positive")

emp = Employee(50000)
emp.salary = 60000
print(emp.salary)
```

---

#### 🧩 **Example 4: Partial Encapsulation (Protected Members)**

```python
class Vehicle:
    def __init__(self):
        self._speed = 0   # Protected attribute

class Car(Vehicle):
    def accelerate(self):
        self._speed += 10
        print("Speed:", self._speed)

c = Car()
c.accelerate()
```

---

#### 🧩 **Example 5: Real Security Example — Bank Account**

```python
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. Remaining: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount!")

acc = BankAccount("Poovarasan", 10000)
acc.deposit(2000)
acc.withdraw(5000)
```

---

#### 🧩 **Example 6: Encapsulation with Property Validation**

```python
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative!")
        self._price = value

p = Product(1500)
p.price = 2000
print(p.price)
```

---

### **4️⃣ Tasks / Questions**

1. Create a `BankAccount` class that allows deposit and withdrawal but hides balance.
2. Implement `Student` class with a private attribute `__marks` and validation.
3. Demonstrate name mangling using private variables.
4. Use `@property` and setter for employee salary validation.
5. Implement a `Product` class where price changes are logged using setter methods.

---

### **5️⃣ Important Methods + Real-World Usage**

| **Concept / Method**       | **Description**                     | **Real-World Usage**                  |
| -------------------------- | ----------------------------------- | ------------------------------------- |
| `_protected`               | Indicates internal use only         | Used for semi-private attributes      |
| `__private`                | Name-mangled, inaccessible outside  | Prevents direct data modification     |
| `@property`                | Makes method behave like attribute  | Used in Django ORM fields, validation |
| `@<property>.setter`       | Controls modification access        | Protects internal data updates        |
| Getters/Setters            | Explicit data access methods        | Salary, Balance, Config parameters    |
| Name Mangling              | Access private variables internally | Debugging / advanced inheritance      |
| Encapsulation + Validation | Data protection with checks         | Form input validation, API security   |

---

### **6️⃣ Advanced Concept + Developer POV (Project Use Case)**

| **Use Case**                | **Implementation / Behavior**                                                  |
| --------------------------- | ------------------------------------------------------------------------------ |
| **ORM Models (Django)**     | Field access via getters/setters; prevents invalid DB writes.                  |
| **Authentication**          | Passwords stored as private variables; accessible via `check_password()` only. |
| **Config Management**       | API keys stored in encapsulated config objects.                                |
| **REST APIs**               | Request/response objects encapsulate internal state.                           |
| **Machine Learning Models** | Hyperparameters protected; only adjusted via methods.                          |
| **Logging / Monitoring**    | Internal counters, states encapsulated to avoid tampering.                     |
| **Encapsulated Services**   | Base classes hide DB/session logic from API layers.                            |

---

### **7️⃣ Real-World Inspired Example**

#### 🔹 **Django ORM (Encapsulation in Models)**

```python
class User(models.Model):
    username = models.CharField(max_length=100)
    _password = models.CharField(max_length=255)  # protected

    def set_password(self, raw_password):
        self._password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self._password)
```

✅ Real password is never exposed; only accessible via controlled methods.

---

#### 🔹 **FastAPI / Flask Config Object**

```python
class Config:
    def __init__(self, api_key):
        self.__api_key = api_key

    def get_api_key(self):
        return "****"  # never reveal original key

    def _connect(self):
        return f"Connecting with {self.__api_key}"

cfg = Config("SECRET12345")
print(cfg.get_api_key())
```

✅ Sensitive info encapsulated; visible only within class.

---

#### 🔹 **Machine Learning Example**

```python
class ModelConfig:
    def __init__(self):
        self.__learning_rate = 0.01

    @property
    def learning_rate(self):
        return self.__learning_rate

    @learning_rate.setter
    def learning_rate(self, lr):
        if 0 < lr <= 1:
            self.__learning_rate = lr
        else:
            raise ValueError("Invalid learning rate")

cfg = ModelConfig()
cfg.learning_rate = 0.05
print(cfg.learning_rate)
```

✅ Prevents invalid hyperparameter updates.

---

✅ **Encapsulation is the backbone of data integrity** — every secure, large-scale Python app (Django, ML, FinTech, API, etc.) uses it extensively.

