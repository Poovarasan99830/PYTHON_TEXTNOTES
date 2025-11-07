

## **Python Constructors (`__init__()` Method)**

# __________________________________________________________________________________

### **1️⃣ Definition**

A **constructor** is a special method in Python used to **initialize** objects when they are created from a class.
In Python, the constructor method is defined using **`__init__()`**.

It is automatically called **every time an object is created**, and is typically used to set up **initial values for attributes** or run **setup code**.


# __________________________________________________________________________________

🧠 **Syntax:**


def __init__(self, parameters):
    # initialization code


# __________________________________________________________________________________

### **2️⃣ Industry Use Cases**

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

### **4️⃣ Tasks / Questions**

1. Create a `Book` class with title, author, and price using a constructor.
2. Write a `Rectangle` class that calculates area and perimeter during initialization.
3. Create a `Student` class with constructor validation (grade must be between 0–100).
4. Build a `Laptop` class that auto-calculates GST price inside constructor.
5. Make an `Employee` class that takes hourly rate and hours worked and computes salary automatically.

# __________________________________________________________________________________

### **5️⃣ Important Methods + Real-World Usage**

| Method / Concept                            | Description                                         | Real-World Usage                                       |
| ------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------ |
| `__init__()`                                | Initializes class attributes when object is created | Initialize database models, user sessions              |
| `__del__()`                                 | Destructor, called when object is deleted           | Close connections, cleanup resources                   |
| Default Constructor                         | No parameters, initializes default values           | Used for static objects like “AppConfig”               |
| Parameterized Constructor                   | Accepts arguments                                   | Used for user-defined data like Employee(name, salary) |
| Constructor Chaining (`super().__init__()`) | Call parent constructor                             | Used in inheritance and Django model extensions        |
| Initialization Logic                        | Run setup code                                      | Validate, preprocess, or auto-calculate values         |

# __________________________________________________________________________________

### **6️⃣ Advanced Concept + Developer Point of View (Project Use Case)**

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


# __________________________________________________________________________________

### **7️⃣ Real-World Inspired Example**

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


## 🧱 **Python Constructors — From First Principles**

---

### **1️⃣ Definition (First Principles Rebuild)**

Before we jump into code, think of **constructors** as the **DNA of an object’s creation**.
When you say:

```python
car = Car("Tesla", "Model S")
```

Something *automatically happens* inside the class — Python prepares a new object, assigns memory, and **calls a special method `__init__()`** to set initial values (brand, model, etc.).

✅ **So, the constructor’s job:**
Initialize the **state** (attributes) of an object when it’s created.

**Key Idea:**

> “A constructor is a method that runs automatically when you create an object — giving it initial data and structure.”

---

### **2️⃣ Industry Use Cases**

| Use Case                       | Description                                                                                                       |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| **Django ORM Models**          | When a record (e.g., `User(username="poovarasan")`) is created, the constructor assigns default values to fields. |
| **Authentication Systems**     | User objects are initialized with credentials, roles, and session info using constructors.                        |
| **API Services**               | Request handlers initialize with API keys, URLs, and configurations automatically.                                |
| **Machine Learning Pipelines** | Model classes initialize with hyperparameters (learning_rate, epochs, etc.) at creation time.                     |
| **Automation Scripts / Bots**  | Configurations like browser session, login token, or base URL are set in constructor.                             |
| **Game Development**           | Each player or enemy is born (constructed) with health, speed, and weapon attributes.                             |

---

### **3️⃣ Example Code (Multiple Examples)**

#### 🧩 Example 1 — Basic Constructor

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Tesla", "Model S")
print(car1.brand, car1.model)
```

---

#### ⚙️ Example 2 — Default Constructor

```python
class Greeting:
    def __init__(self):
        print("Welcome to Python OOPs!")

msg = Greeting()
```

---

#### 🏗️ Example 3 — Constructor with Default Values

```python
class Employee:
    def __init__(self, name, role="Intern"):
        self.name = name
        self.role = role

e1 = Employee("Poovarasan", "Developer")
e2 = Employee("Nandhini")  # uses default "Intern"
print(e1.role, e2.role)
```

---

#### 💾 Example 4 — Constructor with Initialization Logic

```python
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "a")  # open file on creation

    def write(self, text):
        self.file.write(text + "\n")

handler = FileHandler("log.txt")
handler.write("System started")
```

---

#### 🧠 Example 5 — Constructor in Inheritance

```python
class User:
    def __init__(self, username):
        self.username = username

class Admin(User):
    def __init__(self, username, permissions):
        super().__init__(username)   # call parent constructor
        self.permissions = permissions
```

---

### **4️⃣ Tasks / Questions**

1. Write a class `Student` that takes name, age, and marks in its constructor.
2. Create a `Product` class where price has a default value if not passed.
3. Design a `Database` class that connects automatically to SQLite when created.
4. Use `super()` in inheritance to call the parent class constructor.
5. Create a `Robot` class where each robot has a unique ID assigned at creation.

---

### **5️⃣ Important Methods + Real-World Usage**

| Method / Concept     | Description                                   | Example Usage                                 |
| -------------------- | --------------------------------------------- | --------------------------------------------- |
| `__init__()`         | Primary constructor called at object creation | `User("poovarasan")`                          |
| `self`               | Refers to current instance                    | Access instance attributes inside constructor |
| `super().__init__()` | Calls parent constructor in child class       | Inheritance (e.g., Django models)             |
| Default arguments    | Predefine common attribute values             | `def __init__(self, x=0)`                     |
| Initialization logic | Perform setup actions                         | File open, DB connect, token load             |
| Resource allocation  | Initialize connections or sessions            | API clients, DB connectors                    |

---

### **6️⃣ Advanced Concept + Developer Point of View (Project Use Case)**

#### 💡 In Real Projects:

Constructors are critical in frameworks like **Django**, **Flask**, and **FastAPI** because they manage initialization automatically.

| Project Area                | Example Usage                                                             |
| --------------------------- | ------------------------------------------------------------------------- |
| **ORM (Django)**            | `class User(models.Model)` → constructor auto-initializes all field data. |
| **Authentication Systems**  | `UserSession(user, token)` → constructor stores session info.             |
| **REST API Clients**        | `APIClient(base_url, api_key)` → sets up headers and URL templates.       |
| **Machine Learning Models** | `Model(learning_rate=0.01, epochs=10)` → sets training params.            |
| **Automation Frameworks**   | `Bot(driver, credentials)` → initializes Selenium driver & credentials.   |

🧠 **Developer Tip:**
Use constructors for **setup, validation, and dependency injection** — avoid heavy logic.
Let constructors prepare objects *ready for action*.

---

### **7️⃣ Real-World Inspired Example**

#### 🌍 Example: API Client Constructor in Real Project

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
