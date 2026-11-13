




Absolutely! Let’s create a **complete, student-friendly, and detailed note on Encapsulation in Python**. I’ll cover theory, examples, and best practices.

---

# 🛡️ **Encapsulation in Python — Full Notes**

## 1️⃣ **What is Encapsulation?**

Encapsulation is one of the **fundamental concepts of Object-Oriented Programming (OOP)**.

**Definition:**
Encapsulation is the process of **hiding the internal details of an object** and exposing only the necessary functionalities to the outside world.

Think of it as a **capsule** or a **protective shield**: you can interact with the object, but you don’t need to know how it works inside.

**Key Idea:**

* Control access to data
* Protect data from unauthorized modification

---

## 2️⃣ **Why Encapsulation is Important**

1. **Data Hiding:** Prevents direct modification of internal object data.
2. **Security:** Sensitive information is safe from unintended changes.
3. **Improved Maintainability:** Changes inside a class do not affect outside code if the interface remains the same.
4. **Flexibility:** You can change internal implementation without affecting external code.

---

## 3️⃣ **Access Modifiers in Python**

Python uses **naming conventions** for access control:

| Modifier  | Syntax       | Access Level                         | Example          |
| --------- | ------------ | ------------------------------------ | ---------------- |
| Public    | `variable`   | Accessible everywhere                | `self.name`      |
| Protected | `_variable`  | Accessible within class & subclass   | `self._salary`   |
| Private   | `__variable` | Accessible **only inside the class** | `self.__balance` |

**Note:** Python does **not enforce strict access control**, it’s more of a convention. But name mangling helps with private variables (`_ClassName__variable`).

---

## 4️⃣ **Example of Encapsulation**

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self.__balance = balance    # Private attribute

    # Public method to access private balance
    def get_balance(self):
        return self.__balance

    # Public method to modify private balance safely
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount!")
            
# Usage
account = BankAccount("Poovarasan", 1000)
print(account.owner)          # Public access
print(account.get_balance())  # Access private via method
account.deposit(500)
account.withdraw(200)
# print(account.__balance)    # Error! Private variable
```

**Output:**

```
Poovarasan
1000
Deposited 500. New balance: 1500
Withdrew 200. New balance: 1300
```

---

## 5️⃣ **Getter and Setter Methods**

* **Getter:** Method to **read private variables**.
* **Setter:** Method to **modify private variables** safely.

```python
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks!")
```

---

## 6️⃣ **Pythonic Way: Property Decorator**

Python offers a **simpler way** to use getters and setters using `@property`:

```python
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks!")

s = Student("Poovarasan", 85)
print(s.marks)   # Getter
s.marks = 95     # Setter
print(s.marks)
```

---

## 7️⃣ **Key Points to Remember**

1. Encapsulation = **data hiding + controlled access**.
2. Use `_` for **protected**, `__` for **private** variables.
3. Always provide **methods to safely access or modify private data**.
4. `@property` makes your code **cleaner and Pythonic**.
5. Helps in **security, maintainability, and flexibility** of code.

---

## 8️⃣ **Real-life Analogy**

Think of a **TV remote**:

* You **press buttons** (interface)
* You **don’t open the TV** to change the wiring inside.
* That’s exactly **encapsulation** in programming!

---

If you want, I can also make a **diagrammatic version** of this note showing **Public, Protected, Private, Getters, Setters, and Property** visually — which makes it super easy for students to remember.

Do you want me to make that diagram?
















# ______________________________________________________________________________________





| Without `@property`   | With `@property`        |
| --------------------- | ----------------------- |
| `student.get_grade()` | `student.grade`         |
| Feels like a method   | Feels like an attribute |
| Slightly verbose      | Clean and intuitive     |











| Feature           | With `@property` | Without `@property` |
| ----------------- | ---------------- | ------------------- |
| Syntax            | `s.grade`        | `s.get_grade()`     |
| Feels like        | an attribute     | a function call     |
| Easier to read    | ✅ Yes            | ❌ No                |
| Allows validation | ✅ Yes            | ✅ Yes               |
| Pythonic design   | ✅ Recommended    | 🚫 Less modern      |







| Feature                          | Benefit             |
| -------------------------------- | ------------------- |
| Clean interface (`s.grade`)      | Easy to use         |
| Internals can change anytime     | Safe & flexible     |
| Code outside class doesn't break | Backward compatible |

| Feature                        | Benefit                         |
| ------------------------------ | ------------------------------- |
| `emp.status` remains unchanged | No refactor in external code    |
| Internals can change anytime   | Logic can be added later easily |
| Cleaner, readable interface    | `emp.status` feels natural      |


| Claim                               | Proved? | How                                                  |
| ----------------------------------- | ------- | ---------------------------------------------------- |
| Internals can change anytime        | ✅       | We switched from a static string to calculated logic |
| Logic can be added later easily     | ✅       | Just added a `@property`; external usage unchanged   |
| External code does NOT need changes | ✅       | `print(s.grade)` worked before and after             |


| **Decorator** | **Purpose**   | **Why it's useful**                                                                                         |
| ------------- | ------------- | ----------------------------------------------------------------------------------------------------------- |
| `@property`   | Read access   | Allows you to compute values dynamically (e.g., `@property def grade`)                                      |
| `@setter`     | Write access  | Add **validation or transformation** when setting values (e.g., check if name is not empty, marks in range) |
| `@deleter`    | Delete access | Add **logging, warnings, or clean-up** logic before deleting attributes                                     |


| Without Setter/Deleter        | With Setter/Deleter           |
| ----------------------------- | ----------------------------- |
| ✅ Easy and flexible           | ✅ Still flexible              |
| ❌ No validation or control    | ✅ Can add validation & safety |
| ❌ Hard to debug later         | ✅ Clean, future-proof design  |
| ❌ May break code accidentally | ✅ Prevent invalid updates     |



| **Feature**                       | **Normal Attribute (`obj.attr`)**          | **With `@property` / `@setter` / `@deleter`** |
| --------------------------------- | ------------------------------------------ | --------------------------------------------- |
| **Validation**                    | ❌ Not possible automatically               | ✅ Can validate data before assigning          |
| **Data integrity**                | ❌ Anyone can assign anything               | ✅ Only valid data is allowed                  |
| **Debugging support**             | ❌ Hard to trace bugs                       | ✅ Add logging, print, or debugging logic      |
| **Changing internal logic later** | ❌ Breaks external code if internals change | ✅ External code doesn't need to change        |
| **Encapsulation**                 | ❌ Poor — exposes internal structure        | ✅ Strong — protects internal state            |
| **Automatic updates**             | ❌ Always stores values                     | ✅ Can compute values on the fly (`@property`) |
| **Control over deletion**         | ❌ Deletes immediately                      | ✅ You can control what happens on delete      |
| **Security**                      | ❌ Exposed to tampering                     | ✅ You can restrict or log access              |
| **Readability & maintainability** | ❌ Harder to maintain safely                | ✅ Cleaner, more Pythonic design               |



Absolutely! Let’s break down **getter** and **setter** methods in Python with a **real-world example**. I’ll explain clearly and practically.

---

## **1. What are Getters and Setters?**

* **Getter**: A method used to **access** the value of a private attribute.
* **Setter**: A method used to **update or modify** the value of a private attribute.

> Think of it like a bank account:
>
> * You **can’t directly access** someone else’s bank balance.
> * You **ask the bank (getter)** to tell you the balance.
> * You **tell the bank (setter)** to deposit or withdraw money, and the bank checks rules before allowing it.

---

## **2. Real-World Example: Bank Account**

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def set_balance(self, amount):
        if amount < 0:
            print("Error: Balance cannot be negative!")
        else:
            self.__balance = amount
            print(f"Balance updated to {self.__balance}")

# Using the class
account = BankAccount("123456", 1000)

# Accessing balance using getter
print("Current Balance:", account.get_balance())  # Current Balance: 1000

# Updating balance using setter
account.set_balance(1500)  # Balance updated to 1500

# Trying invalid balance
account.set_balance(-500)  # Error: Balance cannot be negative!
```

---

### **Explanation**

1. `__balance` is **private**, so it **cannot be accessed directly**:

   ```python
   account.__balance  # ❌ This will cause an error
   ```
2. We use `get_balance()` to **read** the balance safely.
3. We use `set_balance()` to **update** the balance safely, ensuring rules (like no negative balance) are followed.

---

## **3. Pythonic Way Using @property**

Python allows a cleaner syntax using `@property`:

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Error: Balance cannot be negative!")
        else:
            self.__balance = amount
            print(f"Balance updated to {self.__balance}")

account = BankAccount("123456", 1000)

print(account.balance)  # Current balance
account.balance = 2000  # Update balance safely
account.balance = -100  # ❌ Error check
```

# ______________________________________________________________________




Got it! Let's go **step by step** with Python’s `@property` decorator, including **getter, setter, and deleter**. I’ll explain with a **real-world example** so it’s easy to understand.

---

## **1. What is `@property`?**

The `@property` decorator allows you to **access a method like an attribute**. It’s mainly used for **encapsulation** — hiding internal details while giving controlled access to a variable.

Think of it as **“smart attributes”**: you can **get, set, or delete** a value with logic behind it.

---

## **2. Basic Syntax**

```python
class Person:
    def __init__(self, name):
        self._name = name  # underscore _ indicates “private” variable

    @property
    def name(self):
        """Getter method"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter method"""
        if not value:
            raise ValueError("Name cannot be empty!")
        self._name = value

    @name.deleter
    def name(self):
        """Deleter method"""
        print("Deleting name...")
        del self._name
```

---

## **3. How It Works**

```python
p = Person("Poovarasan")

# ✅ Using getter
print(p.name)  # Output: Poovarasan

# ✅ Using setter
p.name = "Kumar"
print(p.name)  # Output: Kumar

# ❌ Setting invalid value
# p.name = ""  # Raises ValueError: Name cannot be empty!

# ✅ Using deleter
del p.name  # Output: Deleting name...
# print(p.name)  # Raises AttributeError because name is deleted
```

---

## **4. Key Points**

1. `_name` is a “private” variable. We don’t access it directly.
2. `@property` → defines the **getter**.
3. `@name.setter` → defines the **setter**.
4. `@name.deleter` → defines the **deleter**.
5. Using these, you can **add validation** and **encapsulation** without changing how the attribute is accessed.

---

### **5. Real-World Example**

Imagine a **bank account**:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self._balance = amount

    @balance.deleter
    def balance(self):
        print("Deleting balance...")
        del self._balance
```

```python
acct = BankAccount(500)
print(acct.balance)  # 500
acct.balance = 1000  # Update balance
# acct.balance = -100  # ❌ Error
del acct.balance      # Deletes balance
```

---

✅ **Summary Table:**

| Decorator      | Purpose                    |
| -------------- | -------------------------- |
| `@property`    | Getter (read the value)    |
| `@xxx.setter`  | Setter (update the value)  |
| `@xxx.deleter` | Deleter (delete the value) |

---

If you want, I can make a **super simple diagram** showing **getter, setter, and deleter flow** — it makes this concept **stick visually**.

Do you want me to do that?
