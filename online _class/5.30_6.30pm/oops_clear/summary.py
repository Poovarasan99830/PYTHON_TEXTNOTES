
# _______________________________________
#                 OOPS
# ________________________________________




# Inheritance = Reuse structure

# Polymorphism = Reuse interface

# super() = Bridge between parent & child

# ABCs = Enforce method consistency

# Duck typing = Trust behavior, not type







# _______________________________________
#                 oops
# ________________________________________


# Inheritance shares structure,

# Polymorphism shares behavior,

# super() connects both,

# ABCs enforce discipline,

# and Duck Typing gives flexibility.”


# _______________________________________
#                 OOPS
# ________________________________________

# | 🧩 **Concept**                                                   | 💡 **Definition (Core Idea)**                       | 🌍 **Real-World Analogy / Example**                                                                               | 💬 **How to Say in Interview**                                                                                                          |
# | ---------------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
# | 🧬 **Inheritance = Reuse structure**                             | Child class reuses parent’s data and logic          | 👨‍👩‍👦 *Family genetics:* A child inherits DNA, eye color, or habits from parents — no need to “recreate” them. | “Just like a child inherits traits from parents, subclasses reuse logic from base classes — that’s inheritance.”                        |
# | 🎭 **Polymorphism = Reuse interface**                            | Same method name, different behaviors               | 🖱️ *TV Remote:* Same “power” button works for TV, AC, or speaker — action differs by device.                     | “Polymorphism lets different objects respond to the same method in their own way — like pressing the same button on different remotes.” |
# | 🪜 **super() = Bridge between parent & child**                   | Calls parent’s version of a method                  | 👨‍👦 *Family Business:* Child continues the business but still calls parent’s advice when needed.                | “`super()` acts as a bridge — it allows child classes to use or extend the parent’s setup or logic.”                                    |
# | 🧱 **ABCs (Abstract Base Classes) = Enforce method consistency** | Define a *template* that all subclasses must follow | 🏗️ *Construction Contract:* All builders must include kitchen, hall, bedroom — exact design may differ.          | “ABCs ensure every subclass implements the required methods — like enforcing a project blueprint.”                                      |
# | 🦆 **Duck Typing = Trust behavior, not type**                    | Don’t check *who* it is, check *what it can do*     | 🦆 *If it quacks and walks like a duck — treat it as one!*                                                        | “In Python, we don’t care about the object’s class — if it has the required method, we just use it.”                                    |







# ____________________________________________________
#  *decorators** that belong to the **OOP 
# __________________________________________________


# @property`, 
# `@name.setter`,
# `@staticmethod`,
# `@classmethod`
# `@abstractmethod`



# But Python actually has **two broad categories of decorators**:


# ____________________________________________________
# ## 🧩 **1️⃣ Built-in OOP Decorators**
# ____________________________________________________





# These are directly related to **class and object behavior** — they modify how methods and attributes behave *inside a class*.

# | **Decorator**     | **Belongs To**                   | **Purpose / Behavior**                                                 | **Mini Example**                                |
# | ----------------- | -------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------- |
# | `@property`       | OOP (Encapsulation)              | Makes a method act like an attribute (getter).                         | `obj.name` instead of `obj.get_name()`          |
# | `@x.setter`       | OOP                              | Defines how to modify a “protected” variable.                          | `obj.name = "John"`                             |
# | `@x.deleter`      | OOP                              | Defines delete behavior of a property.                                 | `del obj.name`                                  |
# | `@classmethod`    | OOP                              | Method bound to **class**, not object. Gets `cls` instead of `self`.   | `MyClass.from_json()`                           |
# | `@staticmethod`   | OOP                              | Method bound to **neither class nor object** — a utility inside class. | `MathUtils.add(3, 4)`                           |
# | `@abstractmethod` | OOP (Inheritance + Polymorphism) | Enforces that child classes must override this method.                 | `class Shape(ABC): @abstractmethod def area():` |






# ____________________________________________________
# ## 🧠 **2️⃣ Functional / General-Purpose Decorators**
# ____________________________________________________






# These aren’t tied to OOP — they’re used for *wrapping functions or methods* with additional logic (e.g., logging, timing, access control, caching, etc.).

# | **Decorator**                   | **Belongs To**    | **Purpose**                                   | **Example Use Case**            |
# | ------------------------------- | ----------------- | --------------------------------------------- | ------------------------------- |
# | `@staticmethod`, `@classmethod` | OOP               | Behavior modifiers for class methods          | As above                        |
# | `@abstractmethod`               | OOP               | Enforce structure                             | Abstract Base Classes           |
# | `@functools.lru_cache`          | Functional        | Cache function results                        | Optimization in recursive calls |
# | `@functools.wraps`              | Functional        | Preserve metadata of wrapped function         | Custom decorators               |
# | `@dataclass`                    | OOP + Functional  | Auto-generate `__init__`, `__repr__`, etc.    | Clean data containers           |
# | `@contextmanager`               | Functional        | Simplify context managers (`with` statements) | Resource management             |
# | `@staticmethod`, `@classmethod` | OOP               | Change how methods bind                       | Common in frameworks            |
# | **Custom Decorators**           | Functional or OOP | Add logging, auth, retry, etc.                | `@login_required`, `@retry(3)`  |

# ---


# ____________________________________________________
# ## 🧩 **Classification Summary**
# ____________________________________________________





# | **Category**                      | **Decorators**                                      | **Concept Related To**   |
# | --------------------------------- | --------------------------------------------------- | ------------------------ |
# | 🔹 **Encapsulation**              | `@property`, `@x.setter`, `@x.deleter`              | Attribute control        |
# | 🔹 **Inheritance / Polymorphism** | `@abstractmethod`                                   | Enforcing subclass rules |
# | 🔹 **Class Behavior**             | `@classmethod`, `@staticmethod`                     | Class-level logic        |
# | 🔹 **Functional Programming**     | `@functools.wraps`, `@lru_cache`, `@contextmanager` | Function wrapping        |
# | 🔹 **Data Handling**              | `@dataclass`                                        | Boilerplate reduction    |
# | 🔹 **Custom Decorators**          | User-defined `@logger`, `@timer`, etc.              | Cross-cutting logic      |

# ---



# ____________________________________________________
# ### 💬 Interview Tip
# ____________________________________________________





# If asked:

# > “Are decorators part of OOP in Python?”

# ✅ Say:

# > “Some decorators — like 
# 
# `@property`,
# `@classmethod`, 
# `@staticmethod`,
# `@abstractmethod` 
# 
# — are OOP-related, as they change how methods and attributes behave in class design.
# > Others like `@lru_cache` or custom decorators belong to functional programming.”




#  compare **normal methods**, **@classmethod**, and **@staticmethod** with **three different examples** — each highlighting their distinct purpose.

# ---

# ____________________________________________________
# # 🧩 COMPARISON: `Normal` vs `@classmethod` vs `@staticmethod`
# ____________________________________________________







# ---

# ## ⚙️ **Example 1️⃣ — Car Factory (Who Calls It Matters)**

# ### 🚗 Normal Method → works on **individual objects**


#______________________________________________________________________

# class Car:
#     def __init__(self, model):
#         self.model = model

#     def show_model(self):         # Regular method → needs self
#         print(f"This car model is {self.model}")

# c1 = Car("Tesla")
# c1.show_model()   # ✅ Works — uses instance data
# ```

# 🧠 Behind the scenes: `Car.show_model(c1)`
# 👉 The **instance** (`self`) is automatically passed.





##______________________________________________________________________





# ### 🏭 Class Method → works on the **class itself**

# ```python
# class Car:
#     cars_built = 0

#     def __init__(self, model):
#         Car.cars_built += 1
#         self.model = model

#     @classmethod
#     def total_cars(cls):          # Bound to class, not instance
#         print(f"Total cars built: {cls.cars_built}")

# Car("Tesla")
# Car("BMW")
# Car.total_cars()   # ✅ Works — no instance needed
# ```

# 🧠 Behind the scenes: `Car.total_cars(Car)`
# 👉 The **class** (`cls`) is passed automatically.
# 


##______________________________________________________________________ 

# ### ⚙️ Static Method → just a **utility tool**

# ```python
# class Car:
#     @staticmethod
#     def check_wheels(count):      # No self, no cls
#         return count == 4

# print(Car.check_wheels(4))   # ✅ True
# ```

# 🧠 It doesn’t depend on the object or class.
# 👉 Just lives **inside** the class for logical grouping.

# ---

# ### 🧩 Summary (Factory Analogy)

# | Type          | Bound To | Purpose          | Real-World Analogy              |
# | ------------- | -------- | ---------------- | ------------------------------- |
# | Normal method | Instance | Acts on one car  | “Check this car’s model”        |
# | Class method  | Class    | Acts on all cars | “How many cars built?”          |
# | Static method | None     | Helper tool      | “Check if 4 wheels = valid car” |

# ---

# ## ⚙️ **Example 2️⃣ — Student Admission (Who Owns Data)**

# ```python
# class Student:
#     school = "ABC School"

#     def __init__(self, name):
#         self.name = name

#     def introduce(self):                 # Normal
#         print(f"I’m {self.name} from {self.school}")

#     @classmethod
#     def change_school(cls, new_name):    # Class method
#         cls.school = new_name

#     @staticmethod
#     def is_eligible(age):                # Static method
#         return age >= 5
# ```

# ---

# ### 🎯 Usage:

# ```python
# # Create instances
# s1 = Student("John")
# s2 = Student("Emma")

# # 1️⃣ Regular method — uses instance data
# s1.introduce()    # I'm John from ABC School

# # 2️⃣ Class method — changes class-level data
# Student.change_school("XYZ School")
# s2.introduce()    # I'm Emma from XYZ School

# # 3️⃣ Static method — independent utility
# print(Student.is_eligible(6))  # ✅ True
# print(Student.is_eligible(3))  # ❌ False
# ```

# ---

# ### 🧠 What’s happening:

# | Type              | Receives | Can Access       | Example                |
# | ----------------- | -------- | ---------------- | ---------------------- |
# | `introduce()`     | `self`   | instance + class | `s1.name`, `s1.school` |
# | `change_school()` | `cls`    | class only       | `cls.school`           |
# | `is_eligible()`   | —        | nothing          | logic only             |

# ---

# ## ⚙️ **Example 3️⃣ — Bank Account (Different Purpose, Same Class)**

# ```python
# class BankAccount:
#     interest_rate = 5.0  # class variable

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     # Normal method
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{self.owner}'s new balance: {self.balance}")

#     # Class method
#     @classmethod
#     def set_interest(cls, rate):
#         cls.interest_rate = rate
#         print(f"Updated interest rate: {cls.interest_rate}%")

#     # Static method
#     @staticmethod
#     def calculate_interest(amount, rate):
#         return amount * rate / 100
# ```

# ---

# ### 🧩 Usage:

# ```python
# a1 = BankAccount("Alice", 1000)
# a1.deposit(500)  # Uses instance data

# BankAccount.set_interest(6.5)  # Affects all accounts

# print(BankAccount.calculate_interest(2000, 6.5))  # 130.0
# ```

# ---

# ### 💡 Real-World View

# | Type   | Belongs To   | Think Of It As   | Example Action       |
# | ------ | ------------ | ---------------- | -------------------- |
# | Normal | Object       | Personal Account | Deposit, withdraw    |
# | Class  | Organization | Bank policy      | Update interest rate |
# | Static | Utility      | Calculator       | Interest formula     |

# ---

# ## 🧠 FINAL SUMMARY TABLE

# | Feature         | Normal Method         | Class Method         | Static Method            |
# | --------------- | --------------------- | -------------------- | ------------------------ |
# | Decorator       | ❌ None                | ✅ `@classmethod`     | ✅ `@staticmethod`        |
# | First Arg       | `self`                | `cls`                | none                     |
# | Bound To        | Instance              | Class                | Nothing                  |
# | Access Instance | ✅                     | ❌                    | ❌                        |
# | Access Class    | ✅ (through self)      | ✅                    | ❌                        |
# | Purpose         | Work with object data | Work with class data | Independent helper logic |
# | Example         | `deposit()`           | `set_interest()`     | `calculate_interest()`   |






# ## 🔬 5️⃣ Summary Table (Behind the Scenes View)

# | Feature          | Regular Method    | Class Method                       | Static Method   |
# | ---------------- | ----------------- | ---------------------------------- | --------------- |
# | Decorator        | None              | `@classmethod`                     | `@staticmethod` |
# | First Argument   | `self` (instance) | `cls` (class)                      | None            |
# | Bound To         | Instance          | Class                              | Nothing         |
# | Access Instance? | ✅ Yes             | ❌ No                               | ❌ No            |
# | Access Class?    | ✅ Indirectly      | ✅ Directly                         | ❌ No            |
# | Defined As       | `def func(self):` | `def func(cls):`                   | `def func():`   |
# | Called By        | `obj.func()`      | `obj.func()` or `Class.func()`     | Either one      |
# | Typical Use      | Object behavior   | Factory / alternative constructors | Utility logic   |













# ____________________________________________________
   # behind the scenes** with # `@classmethod` and `@staticmethod`.
# ____________________________________________________




# We’ll rebuild both **from first principles** — step-by-step — to understand *how* and *why* they work differently.

# ---

# # 🧩 FIRST PRINCIPLES — `@classmethod` vs `@staticmethod`

# ---

# ## ⚙️ 1️⃣ The Problem They Solve



# Normally, when you define a method in a class:

# ```python
# class Car:
#     def info(self):
#         print("Car method")
# ```

# When you call:

# ```python
# Car().info()
# ```





# 👉 Python automatically passes the **instance** as the **first argument** (`self`).

# That’s why you write:

# ```python
# def info(self):
#     ...
# ```








# But sometimes, you want:

# * a method that should work on the **class itself** (`Car`, not on `Car()`)
# * a method that **doesn’t need** access to either instance or class

# Hence —
# 🔹 `@classmethod` → bound to **class**
# 🔹 `@staticmethod` → bound to **nothing**

# ---




# ## 🧠 2️⃣ How Python Normally Binds Methods

# When you access a method through an object:

# ```python
# Car().info
# ```

# Python looks up `info` in the class dictionary and **binds** it to the instance.
# That’s why inside, `self` automatically refers to the calling object.

# Internally, it works like:

# ```python
# Car.info.__get__(car_instance, Car)
# ```

# That `__get__` method is part of the **descriptor protocol**.

# ---






# ## 🔍 3️⃣ Enter `@classmethod`

# When you define:

# ```python
# class Car:
#     @classmethod
#     def show(cls):
#         print(cls)
# ```

# Python wraps the function `show` inside a `classmethod` object:

# ```python
# Car.__dict__['show'] = classmethod(show)
# ```

# When you call:

# ```python
# Car.show()
# ```

# Internally, `classmethod.__get__` intercepts this and **passes the class itself (`Car`)** as the first argument — instead of an instance.

# So it’s equivalent to:

# ```python
# Car.show(Car)
# ```






# ✅ **Behind the scenes:**

# ```python
# class Car:
#     def show(cls):
#         ...
# show = classmethod(show)
# ```

# So when you call `Car.show()` or `Car().show()`, both pass `cls = Car`.

# ---





# ### ⚙️ Internal Mechanism (Simplified)

# ```python
# class classmethod:
#     def __init__(self, func):
#         self.func = func
#     def __get__(self, obj, cls=None):
#         return lambda *args, **kwargs: self.func(cls, *args, **kwargs)
# ```

# That’s literally what Python does under the hood.

# ---





# ### 💡 Use Case

# Factory methods that create objects in different ways:

# ```python
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_string(cls, data):
#         name, age = data.split('-')
#         return cls(name, int(age))

# s = Student.from_string("John-21")
# ```

# 👉 Here `cls` ensures that if you subclass `Student`, the right class is instantiated.

# ---





# ## ⚙️ 4️⃣ `@staticmethod` — “No Binding at All”

# When you define:

# ```python
# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b
# ```

# Python wraps it with a `staticmethod` object:

# ```python
# Math.__dict__['add'] = staticmethod(add)
# ```

# Now when you call:

# ```python
# Math.add(3, 4)
# ```

# There’s **no binding at all** — no `self`, no `cls`.
# It’s just a plain function stored *inside a class namespace*.

# So internally:

# ```python
# Math.add == add  ✅  (a plain function, no automatic argument)
# ```

# ---

# ### ⚙️ Internal Mechanism (Simplified)

# ```python
# class staticmethod:
#     def __init__(self, func):
#         self.func = func
#     def __get__(self, obj, cls=None):
#         return self.func
# ```

# Unlike `classmethod`, it just returns the function itself — no auto `cls` or `self`.

# ---

# ### 💡 Use Case

# Utility or helper functions that conceptually belong to the class,
# but don’t touch instance or class data.

# ```python
# class Math:
#     @staticmethod
#     def is_even(n):
#         return n % 2 == 0
# ```

# You can call:

# ```python
# Math.is_even(10)   # ✅
# Math().is_even(10) # ✅ same thing
# ```

# ---

# ## 🔬 5️⃣ Summary Table (Behind the Scenes View)

# | Feature          | Regular Method    | Class Method                       | Static Method   |
# | ---------------- | ----------------- | ---------------------------------- | --------------- |
# | Decorator        | None              | `@classmethod`                     | `@staticmethod` |
# | First Argument   | `self` (instance) | `cls` (class)                      | None            |
# | Bound To         | Instance          | Class                              | Nothing         |
# | Access Instance? | ✅ Yes             | ❌ No                               | ❌ No            |
# | Access Class?    | ✅ Indirectly      | ✅ Directly                         | ❌ No            |
# | Defined As       | `def func(self):` | `def func(cls):`                   | `def func():`   |
# | Called By        | `obj.func()`      | `obj.func()` or `Class.func()`     | Either one      |
# | Typical Use      | Object behavior   | Factory / alternative constructors | Utility logic   |

# ---

# ## 🧩 6️⃣ Real-World Analogy

# | Decorator          | Analogy                                                                |
# | ------------------ | ---------------------------------------------------------------------- |
# | **Regular method** | Employee method: works only when you hire them (instance)              |
# | **Class method**   | HR manual: rules that apply to all employees (class)                   |
# | **Static method**  | Calculator kept in the office: anyone can use, no employee data needed |

# ---

# Would you like me to show a **visual flow diagram** of how the `__get__` descriptor works for
# these three methods (self → cls → none)? It makes the internal binding crystal clear.



# Perfect 👏 — let’s visualize what happens *under the hood* when you call a **regular method**, **classmethod**, or **staticmethod** in Python.

# Below is a **conceptual diagram** showing how Python binds methods behind the scenes using the **descriptor protocol**.

# ---

# # 🧩 **Visual Flow — Method Binding Behind the Scenes**

# ```
# ────────────────────────────────────────────
#            CLASS DEFINITION STAGE
# ────────────────────────────────────────────
# class MyClass:
#     def normal(self): ...
#     @classmethod
#     def cls_method(cls): ...
#     @staticmethod
#     def static_method(): ...
# ────────────────────────────────────────────
# When Python loads the class:
# MyClass.__dict__ becomes:
# {
#   'normal': function normal(self),
#   'cls_method': classmethod(cls_method),
#   'static_method': staticmethod(static_method)
# }
# ────────────────────────────────────────────
# ```

# Now let’s see what happens when you **access** these methods 👇

# ---

# ## 🧠 **1️⃣ Regular Method Access**

# ```
# obj = MyClass()
# obj.normal()
#         │
#         ▼
# LOOKUP: MyClass.__dict__['normal'] → <function normal>
#         │
#         ▼
# PYTHON CALLS function.__get__(obj, MyClass)
#         │
#         ▼
# RETURNS a "bound method" that passes:
#     self = obj
#         │
#         ▼
# → normal(obj)
# ```

# ✅ **Bound to instance**

# ---

# ## 🧩 **2️⃣ Class Method Access**

# ```
# MyClass.cls_method()
#         │
#         ▼
# LOOKUP: MyClass.__dict__['cls_method'] → <classmethod object>
#         │
#         ▼
# CALLS classmethod.__get__(None, MyClass)
#         │
#         ▼
# RETURNS a wrapper that passes:
#     cls = MyClass
#         │
#         ▼
# → cls_method(MyClass)
# ```

# ✅ **Bound to class (cls)**
# No instance needed — even if called as `obj.cls_method()`, it still gets the class.

# ---

# ## ⚙️ **3️⃣ Static Method Access**

# ```
# MyClass.static_method()
#         │
#         ▼
# LOOKUP: MyClass.__dict__['static_method'] → <staticmethod object>
#         │
#         ▼
# CALLS staticmethod.__get__(None, MyClass)
#         │
#         ▼
# RETURNS the original function itself
# (No self, no cls)
#         │
#         ▼
# → static_method()
# ```

# ✅ **Not bound to anything** — acts like a plain function living inside the class namespace.

# ---

# ## 🧩 **Summary Diagram (Binding Flow)**

# ```
# ──────────────────────────────────────────────
# | Method Type   | Who Gets Passed Automatically? |
# ──────────────────────────────────────────────
# | normal()      |  self  → instance              |
# | cls_method()  |  cls   → class                 |
# | static_method()|  ❌ nothing                   |
# ──────────────────────────────────────────────
# ```

# ---

# ## 💬 Real-World Analogy

# | Type            | Analogy                           | Example                                |
# | --------------- | --------------------------------- | -------------------------------------- |
# | `def normal()`  | Employee’s personal task          | Needs their own desk (instance)        |
# | `@classmethod`  | HR policy shared by all employees | Applies to company as a whole          |
# | `@staticmethod` | Tool in office (calculator)       | Works independently of people or rules |

# ---

# Would you like me to **generate a visual flowchart image** version of this —
# (showing arrows from `obj` or `Class` to `self / cls / none`)?
# It’ll make the binding paths visually clear in one glance.






# Here is a **super clean, confident, professional script** you can *speak directly* to your boss when explaining any code — especially your getter/setter example.

# Use it like a dialogue.
# No technical overload.
# Boss-friendly.
# Clear & structured.

# ---

# # 🎤 **CONFIDENT SPEAKING SCRIPT (Use for ANY CODE)**

# ## **1️⃣ PURPOSE (Start here)**

# “First, let me explain the purpose.
# This code is written to give us better control over how the value is stored and accessed.
# Instead of exposing the variable directly, we manage it safely.”

# ---

# ## **2️⃣ CONCEPT (Introduce the idea simply)**

# “The concept is simple:
# A *getter* is used to read a value, and a *setter* is used to update a value.
# This keeps the internal data protected.”

# ---

# ## **3️⃣ CODE BREAKDOWN (Explain piece-by-piece)**

# “Inside the class, the `@property` decorator makes the method behave like an attribute.
# So when we call `p.price`, Python runs the getter method and returns the internal value.

# Next, the `@price.setter` method is responsible for updating the value.
# Here, we store the new value in a private attribute called `_price`.
# This prevents accidental misuse and allows us to add validations later.”

# ---

# ## **4️⃣ FLOW (Explain how the program runs)**

# “When I write `p.price = 100`, the setter runs and stores the value internally.
# When I write `print(p.price)`, the getter runs and retrieves the stored value.”

# ---

# ## **5️⃣ RESULT (Show output)**

# “So in this example, the final output will be **100**.”

# ---

# ## **6️⃣ BENEFIT (End with value impact)**

# “The advantage of this structure is that we maintain clean code, strong data protection, and we can easily add rules or validation in the future without changing how the class is used.”

# ---

# # ⭐ **Full Script in One Flow (Natural Speech)**

# Here is the full thing combined — you can speak it directly:

# > “Let me explain this code step-by-step.
# >
# > The purpose of this code is to control how the price is stored and accessed so that we have full safety and flexibility.
# >
# > The concept is simple: a getter reads the value and a setter updates it.
# > Using this makes our internal data protected and gives us room for validation later.
# >
# > In the code, `@property` turns the `price` method into a readable attribute.
# > So when we access `p.price`, the getter runs automatically and returns the internal `_price`.
# >
# > The `@price.setter` method handles updates.
# > When we assign `p.price = 100`, the setter stores that value in `_price`.
# >
# > The flow is:
# > assign value → setter runs
# > read value → getter runs.
# >
# > The final output for this example will be 100.
# >
# > The main benefit is that this approach gives us clean code, proper encapsulation, and full control over the data, which is important for scaling or adding validations in the future.”





# Here are both versions — **10-second** and **interview-style** — short, sharp, and confident.

# ---

# # ⚡ **10-Second Version**

# > “Getter lets us read the price safely, setter updates it and stores it in a private variable.
# > `p.price = 100` calls the setter, `p.price` reads it.
# > This keeps the code clean and controlled.”

# ---

# # 🎙️ **Interview-Style Version (Very Professional)**

# > “I used a getter and setter to control access to the `price` attribute.
# > The getter returns the internal `_price`, and the setter updates it safely with room for validation.
# > Using `p.price = value` triggers the setter, and reading `p.price` triggers the getter.
# > This ensures clean, maintainable, and secure object design.”

# ---




# Here is a **crisp 20-second version** you can speak confidently:

# ---

# # 🎤 **20-Second Explanation Script**

# > “This code controls how the price is stored and accessed.
# > The getter, using `@property`, lets us read the price safely.
# > The setter updates the price and stores it in a private variable `_price`, which prevents mistakes and allows validation later.
# > When we do `p.price = 100`, the setter runs, and when we print `p.price`, the getter returns the value.
# > This keeps the code clean, safe, and easy to maintain.”

# ---

# If you want, I can give **10-second** or **interview-style** versions too.
