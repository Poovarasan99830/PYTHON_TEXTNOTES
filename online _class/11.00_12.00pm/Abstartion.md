


# ______________________________________________________________

## 🧠 **Abstraction in Python**

### 🔹 **Definition**

**Abstraction** means showing **only the essential details** and **hiding the background implementation** from the user.

It helps to reduce complexity and make code easier to maintain.

---

### 🔹 **Real-Life Example**

Think of a **TV remote** —
you press buttons like *volume up* or *change channel*,
but you don’t see how signals are sent inside the TV.

That’s abstraction — you **use the feature** without knowing **how it works internally**.

---

### 🔹 **In Python (via OOP)**

We achieve abstraction using:

1. **Abstract Classes**
2. **Abstract Methods** (methods without implementation)

---

### 🔹 **Using the `abc` module**

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):       # Abstract class
    @abstractmethod
    def start(self):
        pass               # Abstract method (no body)

class Car(Vehicle):       # Concrete class
    def start(self):
        print("Car engine started 🚗")

# object = Vehicle()  ❌ Can't create object of abstract class
obj = Car()
obj.start()
```

---

### 🔹 **Output**

```
Car engine started 🚗
```

---

### 🔹 **Why Use Abstraction?**

✅ Hides complex details
✅ Focuses on “what to do,” not “how to do it”
✅ Improves code security and readability
✅ Supports modular and scalable design


# ________________________________________________________________


## ⚙️ **Methods in Python Classes**

Python supports **three types of methods** inside a class:
1️⃣ Instance Method
2️⃣ Class Method
3️⃣ Static Method

---

### 🔹 **1. Instance Method**

* Works **with object (instance)** data.
* Needs `self` as the first parameter.
* Can **access and modify instance variables**.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):   # Instance Method
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Rahul", 85)
s1.show()
```

**Output:**

```
Name: Rahul, Marks: 85
```

---

### 🔹 **2. Class Method**

* Works **with class-level (shared)** data.
* Uses a decorator `@classmethod`.
* Takes `cls` (class) as the first parameter instead of `self`.
* Can **access or modify class variables**, but not instance variables directly.

```python
class Student:
    school_name = "ABC School"   # Class variable

    @classmethod
    def show_school(cls):
        print(f"School Name: {cls.school_name}")

Student.show_school()
```

**Output:**

```
School Name: ABC School
```

---

### 🔹 **3. Static Method**

* Doesn’t need `self` or `cls`.
* Used when a method **doesn’t depend on object or class data**.
* Acts like a **utility function inside the class**.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 10))
```

**Output:**

```
15
```

---

### 🧩 **Summary Table**

| Method Type     | Uses `self` | Uses `cls` | Access Instance Data | Access Class Data | Decorator       |
| --------------- | ----------- | ---------- | -------------------- | ----------------- | --------------- |
| Instance Method | ✅ Yes       | ❌ No       | ✅ Yes                | ✅ Yes (via class) | —               |
| Class Method    | ❌ No        | ✅ Yes      | ❌ No                 | ✅ Yes             | `@classmethod`  |
| Static Method   | ❌ No        | ❌ No       | ❌ No                 | ❌ No              | `@staticmethod` |

\