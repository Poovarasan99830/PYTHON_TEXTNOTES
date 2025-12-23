



# __________________________________________________________________________________
### **1️⃣ Definition**
# __________________________________________________________________________________

A **constructor** is a special method in Python used to **initialize** objects when they are created from a class.
In Python, the constructor method is defined using **`__init__()`**.

It is automatically called **every time an object is created**, and is typically used to set up **initial values for attributes** or run **setup code**.


# __________________________________________________________________________________
🧠 **Syntax:**
# __________________________________________________________________________________

## **Python Constructors (`__init__()` Method)**

def __init__(self, parameters):
    # initialization code


# __________________________________________________________________________________
### **2️⃣ Industry Use Cases**
# __________________________________________________________________________________


| Domain                       | Real-World Use Case                                                        |
| ---------------------------- | -------------------------------------------------------------------------- |
| **Web Development (Django)** | Automatically initialize model fields like `user`, `created_at`, etc.      |
| **E-commerce Systems**       | Set up product details, inventory info, or cart totals at object creation. |
| **Banking/FinTech**          | Initialize user account balances and transaction histories.                |
| **Automation Scripts**       | Store configuration details (URLs, credentials, file paths).               |
| **AI/ML Applications**       | Initialize model parameters, dataset paths, or hyperparameters.            |
| **Gaming Applications**      | Set up player attributes like health, score, and position at start.        |

# __________________________________________________________________________________

### **3️⃣ Example Code (Multiple Examples)**
# __________________________________________________________________________________




#### 🧩 **Example 1: Basic Constructor**

```python
class Student:
    def __init__(self, name, grade):
        self.name = name    #instance variable..
        self.grade = grade

s1 = Student("Poovarasan", "A+")







**Output:**

```
Poovarasan A+
```

# __________________________________________________________________________________

#### ⚙️ **Example 2: Constructor with Default Values**


class Car:
    def __init__(self, brand="Tesla", model="Model 3"):
        self.brand = brand
        self.model = model



c1 = Car()
c2 = Car("BMW", "i8")

print(c1.brand, c1.model)
print(c2.brand, c2.model)


**Output:**

```
Tesla Model 3
BMW i8
```

# __________________________________________________________________________________

#### 🏦 **Example 3: Constructor with Logic**

```python
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance if balance >= 0 else 0

acc1 = BankAccount("Poovarasan", 10000)
acc2 = BankAccount("Nandhini", -500)

print(acc1.balance, acc2.balance)  # Output: 10000, 0
```

# __________________________________________________________________________________

#### 🧠 **Example 4: Constructor Calling Another Method**


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
        self.fahrenheit = self.another()

    def another(self):
        return "welcome python"

t1 = Temperature(25)

print(t1.fahrenheit)  # Output: "welcome python"



# __________________________________________________________________________________
#### 🧠 **Example   5   : Constructor Chaining Method**

## 1️⃣ What actually happens when you create an object

When you write:

```python
child = Child("Alice", 12, "7th")
```

Python does roughly this:

1. **Allocate memory** for a new `Child` object (`self`).
2. **Look up** `__init__` in `Child`’s class (method resolution order — MRO).
3. **Call that `__init__` method** with the arguments you gave.

---

## 2️⃣ MRO in action

For your case:

```python
class Parent:
    def __init__(self, name, age):
        ...

class Child(Parent):
    def __init__(self, name, age, grade):
        self.grade = grade
```

The **MRO** for `Child` is:

```
[Child, Parent, object]
```

When you call `Child(...)`:

* Python looks at the **first class in MRO (`Child`)** for `__init__`.
* It **finds it there**, so it **does NOT** automatically look at `Parent.__init__` unless you explicitly call it.

This means **Parent’s constructor is never run** unless you say so.

---

## 3️⃣ Why `self.name` and `self.age` don’t exist

The attributes `self.name` and `self.age` are **created inside `Parent.__init__`**.
If `Parent.__init__` never runs, then:

* No code assigns `self.name = ...`
* No code assigns `self.age = ...`
* So those attributes simply **don’t exist** in the object.

---

## 4️⃣ Demonstration

```python
class Parent:
    def __init__(self, name, age):
        print("Parent init called")
        self.name = name
        self.age = age

class Child(Parent):
    def __init__(self, name, age, grade):
        print("Child init called")
        self.grade = grade

c = Child("Alice", 12, "7th")

print(c.grade)  # Works
print(c.name)   # ❌ AttributeError: 'Child' object has no attribute 'name'
```

---

## 5️⃣ The logic behind the rule

* **If a class defines `__init__`, Python assumes you want to handle all initialization yourself.**

* It will **not** run any parent constructors automatically (unlike Java or C# where `super()` is sometimes implicit).

* This gives you full control but means you must remember to chain constructors if needed.

---

✅ **Bottom line:**
In Python, constructor chaining is **manual**. If you override `__init__` in a child class, the parent’s `__init__` will not be called unless 

you explicitly tell Python to call it (usually via `super().__init__()`).




# __________________________________________________________________________________
### **4️⃣ Tasks / Questions**
# __________________________________________________________________________________




1. Create a `Book` class with title, author, and price using a constructor.
2. Write a `Rectangle` class that calculates area and perimeter during initialization.
3. Create a `Student` class with constructor validation (grade must be between 0–100).
4. Build a `Laptop` class that auto-calculates GST price inside constructor.
5. Make an `Employee` class that takes hourly rate and hours worked and computes salary automatically.





# __________________________________________________________________________________
# **5️⃣ Important Methods + Real-World Usage**
# __________________________________________________________________________________



| Method / Concept                            | Description                                         | Real-World Usage                                       |
| ------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------ |
| `__init__()`                                | Initializes class attributes when object is created | Initialize database models, user sessions              |
| `__del__()`                                 | Destructor, called when object is deleted           | Close connections, cleanup resources                   |
| Default Constructor                         | No parameters, initializes default values           | Used for static objects like “AppConfig”               |
| Parameterized Constructor                   | Accepts arguments                                   | Used for user-defined data like Employee(name, salary) |
| Constructor Chaining (`super().__init__()`) | Call parent constructor                             | Used in inheritance and Django model extensions        |
| Initialization Logic                        | Run setup code                                      | Validate, preprocess, or auto-calculate values         |




# __________________________________________________________________________________
# **6️⃣ Advanced Concept + Developer Point of View (Project Use Case)**
# __________________________________________________________________________________






#### 💼 **a) Django ORM Models**

Every Django model automatically calls a constructor when an instance is created.

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"🧱 Product object created: {self.name}")
```



# __________________________________________________________________________________

#### 🔐 **b) Authentication (Django / Flask)**

Constructors are used in service classes to set up session data or tokens.

```python
class AuthManager:
    def __init__(self, username, token):
        self.username = username
        self.token = token

    def is_authenticated(self):
        return self.token is not None
```


# __________________________________________________________________________________

#### 🧩 **c) API or Utility Classes**

Initialize configurations, endpoints, and API keys.

```python
class APIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        print(f"Connected to API: {self.base_url}")
```


# __________________________________________________________________________________

#### 🤖 **d) Machine Learning Pipeline**

Constructors are used to initialize data paths and model configs.

```python
class ModelTrainer:
    def __init__(self, model, data_path):
        self.model = model
        self.data_path = data_path
        self.dataset = self.load_data()

    def load_data(self):
        print(f"Loading data from {self.data_path}")
        return [1, 2, 3, 4, 5]



# _________________________________________________________________________________

# **7️⃣ Real-World Inspired Example**
# __________________________________________________________________________________



#### 🌍 Example1 : User Profile Creations



class UserProfile:
    def __init__(self, username, email, is_admin=False):
        self.username = username
        self.email = email
        self.is_admin = is_admin
        self.permissions = self.set_permissions()

    def set_permissions(self):
        if self.is_admin:
            return ["add_user", "delete_user", "view_reports"]
        else:
            return ["view_profile"]

    def display_profile(self):
        return f"👤 {self.username} | Email: {self.email} | Permissions: {self.permissions}"

# Object creation
user1 = UserProfile("poovarasan", "poo@example.com")
admin = UserProfile("admin_user", "admin@example.com", True)

print(user1.display_profile())
print(admin.display_profile())
```

**Output:**

```
👤 poovarasan | Email: poo@example.com | Permissions: ['view_profile']
👤 admin_user | Email: admin@example.com | Permissions: ['add_user', 'delete_user', 'view_reports']
```

# __________________________________________________________________________________
### 🌍 Example 2: API Client Constructor in Real Project






```python
class APIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {api_key}"}
        print("API Client initialized!")

    def get_user(self, user_id):
        return f"GET {self.base_url}/users/{user_id} with {self.headers}"

client = APIClient("https://api.github.com", "xyz123apikey")
print(client.get_user("poovarasan"))
```

**Output:**

```
API Client initialized!
GET https://api.github.com/users/poovarasan with {'Authorization': 'Bearer xyz123apikey'}
```
