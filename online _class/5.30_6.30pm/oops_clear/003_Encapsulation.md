# ___________________________________________________________________
## 🧠 **Python Encapsulation (From First Principles)**
# ___________________________________________________________________


### *(Protect Data — Control Access — Maintain Integrity)*

---

### **1️⃣ Definition**

**Encapsulation** means **wrapping data (variables)** and **methods (functions)** into a **single unit** — typically a class.

It is one of the **four pillars of OOP** (with inheritance, abstraction, and polymorphism).



In simple words —

> “Encapsulation hides internal data and only exposes what’s necessary through controlled interfaces (getters/setters).”

✅ Protects data from unauthorized modification


✅ Enables controlled access to class attributes

✅ Improves code modularity, security, and maintainability


---

### 🔹 **Python Approach**

Unlike some strictly-typed OOP languages (like Java/C++), Python does not have s

trict access modifiers like `private` or `protected`.

Instead, it **relies on conventions and name mangling**:

| Convention    | Syntax       | Meaning                                   |
| ------------- | ------------ | ----------------------------------------- |
| **Public**    | `variable`   | Accessible from anywhere                  |
| **Protected** | `_variable`  | Intended for internal use only            |
| **Private**   | `__variable` | Name mangled to prevent accidental access |

---

# ____________________________________________________________________________
# **2️⃣ Industry Use Cases**
# ____________________________________________________________________________





| **Use Case**                   | **Description**                                                                 |
| ------------------------------ | ------------------------------------------------------------------------------- |
| **Banking Systems**            | Hide customer balance and control access via deposit/withdraw methods.          |
| **Healthcare Software**        | Protect patient records and control access through secure methods.              |
| **E-commerce Apps**            | Hide order data, allow modification only via APIs.                              |
| **Machine Learning Pipelines** | Keep model parameters private and expose only train/predict methods.            |
| **Game Development**           | Control player stats like health or score through functions, not direct access. |
| **Enterprise APIs**            | Control access to internal data models using getters and setters.               |

---

# _______________________________________________________________________________________
### **3️⃣ Example Codes (n+ Examples)**
# _______________________________________________________________________________________








#### 🧩 **Example 1: Basic Encapsulation — Public Attributes**

```python
class Student:
    def __init__(self, name, age):
        self.name = name    # public
        self.age = age      # public

s = Student("Arun", 22)
print(s.name)   # Accessible
print(s.age)    # Accessible
```

✅ Public members can be accessed anywhere.






---

#### 🧩 **Example 2: Protected Members (`_variable`)**

```python
class Employee:
    def __init__(self, name, salary):
        self._salary = salary   # protected
        self.name = name

    def show_info(self):
        return f"{self.name} earns ₹{self._salary}"

emp = Employee("Ram", 50000)
print(emp._salary)      # ⚠️ Accessible, but not recommended
print(emp.show_info())
```

✅ `_salary` should be treated as internal-only data.





---

#### 🧩 **Example 3: Private Members (`__variable`)**

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())
# print(acc.__balance)  ❌ AttributeError
```

✅ `__balance` cannot be directly accessed from outside (due to name mangling).


print(acc._BankAccount__balance)


---

#### 🧩 **Example 4: Access Private Data using Getters and Setters**

```python
class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if len(new_name) > 2:
            self.__name = new_name

p = Person("Abi")
print(p.get_name())
p.set_name("Kumar")
print(p.get_name())
```

✅ Data access controlled through methods (validation possible).





---

#### 🧩 **Example 5: Encapsulation with `@property` Decorator (Pythonic Way)**

```python
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Invalid Price")

item = Product(100)
print(item.price)
item.price = 250
print(item.price)
```

✅ Simplifies getters and setters using decorators.

---




#### 🧩 **Example 6: Encapsulation in Inheritance**

```python
class Vehicle:
    def __init__(self, brand):
        self._brand = brand

class Car(Vehicle):
    def show(self):
        return f"Brand: {self._brand}"

c = Car("Tesla")
print(c.show())
```

✅ Child class can access protected attributes of parent.

---

# ___________________________________________________________________
### **4️⃣ Tasks / Questions**
# ___________________________________________________________________


1. Create a class `Employee` with private attribute `__salary` and methods to get/set it safely.
2. Build a `Student` class that encapsulates marks and prevents negative input.
3. Implement `@property` for an `Account` class with controlled `balance` access.
4. Create a `Car` class that hides its speed variable and controls access with methods.
5. Demonstrate encapsulation with inheritance (`_protected` variable usage).

---

# ______________________________________________________________________________
## **5️⃣ Important Methods + Real-World Usage**
# _______________________________________________________________________________





| **Concept / Method**       | **Description**                                     | **Real-World Usage**                           |
| -------------------------- | --------------------------------------------------- | ---------------------------------------------- |
| `_protected_variable`      | Convention for internal data                        | Used in base classes to share within hierarchy |
| `__private_variable`       | Prevents accidental modification                    | Hide sensitive data like API keys, balance     |
| Getter / Setter            | Controlled access to variables                      | Employee salary, configuration settings        |
| `@property`                | Pythonic getter/setter syntax                       | Django models, data validation                 |
| Name Mangling              | Renames private vars internally (`_ClassName__var`) | Prevents namespace collision                   |
| Encapsulation + Validation | Add business logic before setting values            | Banking, E-commerce, IoT systems               |

---

# _______________________________________________________________________________________
## **6️⃣ Advanced Concept + Developer POV (Project-Level Use)**
# _______________________________________________________________________________________




| **Use Case**                | **Implementation / Behavior**                                           |
| --------------------------- | ----------------------------------------------------------------------- |
| **Banking Apps**            | Private account balance; modified only through deposit/withdraw methods |
| **Django ORM Models**       | Model fields are encapsulated and accessed via attributes/methods       |
| **Machine Learning Models** | Hyperparameters or weights stored privately, exposed via APIs           |
| **APIs / SDKs**             | Internal methods hidden using `_method()` conventions                   |
| **Enterprise Systems**      | Protect sensitive data (keys, credentials) using private members        |
| **IoT Applications**        | Device state variables encapsulated for safety                          |
| **Game Development**        | Player’s health/speed attributes hidden to prevent cheat access         |

---

# ___________________________________________________________________________________________
# **7️⃣ Real-World Inspired Example** ___________________________________________________________________________________________




#### 🔹 **Example 1: Banking Application**

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return f"Balance for {self.owner}: ₹{self.__balance}"

acc = BankAccount("Ravi", 10000)
acc.deposit(2500)
acc.withdraw(2000)
print(acc.get_balance())
```

✅ Internal balance is hidden; access only through controlled methods.

---




#### 🔹 **Example 2: Django Model-like Example**

```python
class User:
    def __init__(self, email, password):
        self.email = email
        self.__password = password  # private

    @property
    def password(self):
        return "*****"  # Hide actual password

    def check_password(self, pwd):
        return pwd == self.__password

u = User("admin@example.com", "secret123")
print(u.password)             # masked
print(u.check_password("secret123"))
```

✅ Real-world analogy of password hashing and secure access.

---




#### 🔹 **Example 3: Machine Learning Model**

```python
class Model:
    def __init__(self, weights):
        self.__weights = weights

    def train(self):
        print("Training using private weights...")

    def get_weights(self):
        return f"Weights (secured): {len(self.__weights)} parameters"

model = Model([0.1, 0.2, 0.3])
model.train()
print(model.get_weights())
```

✅ Model internals are encapsulated — exposed only through safe interfaces.





---

✅ **Encapsulation Summary:**

| **Feature**       | **Purpose**                   | **Example**           |
| ----------------- | ----------------------------- | --------------------- |
| Hiding Data       | Prevent external modification | `__balance`           |
| Controlled Access | Use getter/setter             | `get_salary()`        |
| Validation        | Add checks before setting     | `@property` setter    |
| Name Mangling     | Prevent accidental conflict   | `_ClassName__attr`    |
| Maintainability   | Modular, secure design        | APIs, SDKs, ML Models |




# _____________________________________________________________________________________




# 🧠 **Encapsulation with `@property` — From First Principles**

---

## **1️⃣ First, What Is Encapsulation?**

**Encapsulation** means **binding data (variables)** and **methods (functions)** that operate on that data **into a single unit (class)** — and **restricting direct access** to some parts of the object.

It’s like **putting sensitive data inside a box** and providing **controlled access** through safe doors (methods).



# _____________________________________________________________________________________

### 🔒 **Goal of Encapsulation**

* **Hide internal details**
* **Control how data is modified**
* **Protect object’s integrity**

# _____________________________________________________________________________________




## **2️⃣ The Old (Traditional) Way — Using Getters and Setters**

```python
class Product:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Invalid Price")

item = Product(100)
print(item.get_price())  # Access
item.set_price(250)      # Modify safely
print(item.get_price())
```

✅ Works fine,
❌ But it looks **un-Pythonic** and **verbose**.



# _____________________________________________________________________________________





## **3️⃣ The Pythonic Way — Using `@property` Decorator**

Python introduces the **`@property` decorator** to make encapsulation **simpler, elegant, and natural**.

---

### 🔧 How It Works Step-by-Step

#### Step 1 — Private Variable

```python
self.__price = price
```

Encapsulation begins here — `__price` is private.


# _____________________________________________________________________________________



#### Step 2 — The Getter (`@property`)

```python
@property
def price(self):
    return self.__price
```

* Acts like a **method**, but can be **used as an attribute**.
* Allows **read-only access** to private data.



# _____________________________________________________________________________________



#### Step 3 — The Setter (`@price.setter`)

```python
@price.setter
def price(self, value):
    if value > 0:
        self.__price = value
    else:
        print("Invalid Price")
```

* Provides **controlled write access**.
* Executes logic before assignment (validation, security, etc.).


# _____________________________________________________________________________________



## **4️⃣ Full Example**

```python
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Invalid Price")

item = Product(100)
print(item.price)   # ✅ Calls getter
item.price = 250    # ✅ Calls setter
print(item.price)
item.price = -50    # ❌ Invalid Price
```

# _____________________________________________________________________________________



## **5️⃣ Why `@property` Is Better**

| Feature     | Traditional Get/Set                      | `@property` Approach            |
| ----------- | ---------------------------------------- | ------------------------------- |
| Syntax      | `obj.get_price()` / `obj.set_price(100)` | `obj.price` / `obj.price = 100` |
| Readability | Verbose                                  | Clean, natural                  |
| Control     | Full                                     | Full                            |
| Style       | Java-like                                | Pythonic                        |



# _____________________________________________________________________________________

## **6️⃣ Behind the Scenes (How Python Translates It)**

```python
item.price      →  item.price()
item.price = x  →  item.price(x)
```

So even though it looks like attribute access,
Python internally **calls getter/setter methods**!



# _____________________________________________________________________________________

## **7️⃣ Real-World Analogy**

Imagine you’re in a **hotel room**:

* You **can’t access** the main control panel directly (`__private` data)
* You use a **remote control** (`@property`) to change settings safely
  (e.g., increase temperature, but not to dangerous levels)




# _____________________________________________________________________________________
## **8️⃣ In One Line Summary**

> `@property` lets you **encapsulate data** while **exposing a clean attribute-style interface** —
> protecting your class **without sacrificing simplicity**.





encapsulation:



Encapsulation hides data using access modifiers (public, protected, private) and provides controlled access through getter/setter or @property methods.




access modifires
   public
   __private        --->self.__balance --->_classname__variablename
   _protect         --->internal use  



__variable is not accessible outside directly because Python mangles (renames) the variable to protect it.
This prevents accidental modification and enforces encapsulation.

__variable not accessible outside — because of Name Mangling



getter and setter
   # traditional           
   # @property                  --->control room ---remote control
        #@property-->getter
                  -->setter










Encapsulation hides the internal data of a class, while abstraction hides the internal working and shows only essential features. They are different concepts: encapsulation = data protection, abstraction = complexity reduction.


| Feature    | Encapsulation                        | Abstraction                |
| ---------- | ------------------------------------ | -------------------------- |
| Focus      | Data hiding                          | Complexity hiding          |
| Purpose    | Protect data                         | Show only essential things |
| Tools      | Private / Protected, getters/setters | Abstract classes, methods  |
| Visibility | Restrict access                      | Reduce complexity          |
| Example    | `__balance`                          | `@abstractmethod start()`  |



Great question — many students get confused here!
**Encapsulation and Abstraction are NOT the same.**
They are different concepts, even though both help in hiding complexity.

Here is the **clearest and simplest explanation** 👇

---

# 🟦 **Encapsulation vs Abstraction — Key Differences**

## ✅ **1. Meaning**

### **Encapsulation → Hiding Data**

* Hides **how data is stored**
* Protects variables using `_protected` and `__private`
* Controls access using getter/setter

**Focus:** *Data security + controlled access*

---

### **Abstraction → Hiding Complexity**

* Hides **implementation details**
* Shows **only necessary features**
* Uses **abstract classes, methods, interfaces**

**Focus:** *Simplifying usage + showing only what is needed*

---

# 🟦 **2. Simple Real-World Example**

### **Encapsulation Example**

ATM machine:

* Balance is hidden (you cannot directly change it)
* Access only through deposit/withdraw methods
  → Protects data

---

### **Abstraction Example**

You press ATM buttons:

* You don’t know how cash is calculated internally
  → Hides complex logic, shows simple interface

---

# 🟦 **3. Python Example**

### **Encapsulation**

```python
class Bank:
    def __init__(self):
        self.__balance = 1000  # hidden data

    def deposit(self, amt):   # controlled access
        self.__balance += amt
```

---

### **Abstraction**

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
```

Hides "how start works", only says "start must exist".

---

# 🟦 **4. One-Line Exam Difference**

### **Encapsulation = Hiding Data**

### **Abstraction = Hiding Implementation**

---

# 🟩 **5. Ultimate 5-Second Difference Table**

| Feature    | Encapsulation                        | Abstraction                |
| ---------- | ------------------------------------ | -------------------------- |
| Focus      | Data hiding                          | Complexity hiding          |
| Purpose    | Protect data                         | Show only essential things |
| Tools      | Private / Protected, getters/setters | Abstract classes, methods  |
| Visibility | Restrict access                      | Reduce complexity          |
| Example    | `__balance`                          | `@abstractmethod start()`  |

---

# 🟦 **6. Short Answer (2 Marks)**

Encapsulation hides the **internal data** of a class, while abstraction hides the **internal working** and shows only essential features. They are different concepts: encapsulation = data protection, abstraction = complexity reduction.

---

If you want, I can give a **combined diagram** to remember both.
