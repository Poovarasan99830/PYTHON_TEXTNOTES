


#____________________________________________________________________________________




##1. Duck Typing (Dynamic Polymorphism)

Python uses **dynamic typing** — you don't need to declare variable types.

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog())   # Woof!
animal_sound(Cat())   # Meow!
```

🔸 Both `Dog` and `Cat` have a `.speak()` method.
🔸 The function doesn't care what type the object is, as long as it implements `speak()`.

#_________________________________________________________________________________________

## ✅ 2. Method Overriding (Inheritance Polymorphism)

Subclasses override methods from a parent class.


class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

for animal in (Dog(), Cat()):
    print(animal.speak())

✔️ Here, the same method `speak()` behaves differently depending on the class.

#_________________________________________________________________________________________


#3. Operator Overloading (Compile-Time Polymorphism)

You can define what `+`, `*`, etc.
mean for your own classes.


class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

book1 = Book(100)
book2 = Book(150)
print(book1 + book2)  # 250


🔸 The `+` operator is overloaded to add `Book` objects by their `pages`.

#_________________________________________________________________________________________


## ✅ 4. Function Overloading (Simulated in Python)

Python **does not support function overloading** by default like Java or C++ — last defined function overrides earlier ones.
But we can simulate it using **default arguments** or **`*args`**:



def greet(name=None):
    if name:
        print(f"Hello, {name}")
    else:
        print("Hello!")

greet()         # Hello!
greet("Alice")  # Hello, Alice


✔️ One function behaves differently based on arguments — pseudo-overloading.

#_________________________________________________________________________________________


## ✅ 5. Built-in Polymorphic Functions

Functions like `len()` show built-in polymorphism:


print(len("Hello"))      # 5 (string)
print(len([1, 2, 3]))     # 3 (list)
print(len({1: 'a', 2: 'b'}))  # 2 (dict)


#_________________________________________________________________________________________


#Real world example:

Imagine a payment system:

class Payment:
    def pay(self):
        raise NotImplementedError

class CreditCard(Payment):
    def pay(self):
        return "Paid using credit card"

class PayPal(Payment):
    def pay(self):
        return "Paid using PayPal"

def process_payment(p: Payment):
    print(p.pay())

process_payment(CreditCard())  # Paid using credit card
process_payment(PayPal())      # Paid using PayPal


#__________________________________________________________________________________




## ✅ What is **Single Dispatch**?

**Single Dispatch** allows you to write a **generic function** and **register type-specific versions** of it based only on the **type of the first argument**.

> 📍 Provided by Python’s built-in module: `functools`

---

## 📦 How to Import It

```python
from functools import singledispatch
```

---

## 🧪 Example: Basic Single Dispatch

```python
from functools import singledispatch

@singledispatch
def greet(arg):
    print("Hello, there!")

@greet.register
def _(arg: str):
    print(f"Hello, {arg}!")

@greet.register
def _(arg: int):
    print(f"Hello, user #{arg}!")

greet("Alice")  # Hello, Alice!
greet(101)      # Hello, user #101!
greet(3.14)     # Hello, there! (default)
```

> ⚠️ `@greet.register` uses `_` for the function name because the main dispatch function is already called `greet`.

---

## 🧠 How It Works

* The **`@singledispatch`** decorator defines a **base function**.
* Then you **register specialized versions** based on **type of the first argument**.
* If no registered type matches, the **generic function** is called.

---

## ⚙️ Under the Hood

Internally, it creates a **dispatch table** (like a dictionary) where:

* Key → type (e.g. `int`, `str`)
* Value → registered function for that type

---

## 📌 Real-World Use Cases

| Use Case             | Example                                      |
| -------------------- | -------------------------------------------- |
| Logging              | Different formats for `str`, `dict`, `list`  |
| Data Serialization   | Serialize based on object type               |
| Drawing UI Elements  | Different shapes: circle, rectangle, polygon |
| Generic Data Parsers | Parse string, list, or dict differently      |

---

## 🚫 Limitations

| Limitation                               | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| Only first argument considered           | Cannot dispatch based on 2nd or 3rd arg  |
| No support for methods (without wrapper) | Must use special `@singledispatchmethod` |

---

## 🧱 Bonus: `@singledispatchmethod` for Classes

Python 3.8+ supports dispatch on **instance methods**:

```python
from functools import singledispatchmethod

class Messenger:
    @singledispatchmethod
    def send(self, data):
        print("Generic sender")

    @send.register
    def _(self, data: str):
        print(f"Sending message: {data}")

    @send.register
    def _(self, data: bytes):
        print(f"Sending binary: {data}")

m = Messenger()
m.send("Hello")
m.send(b"0101")
```

---

## 🧠 Interview Perspective

**Q: What is `singledispatch` used for?**
**A:** It enables writing polymorphic functions by overloading based on the first argument's type. It improves code readability and modularity.

**Q: How does `singledispatch` differ from `multipledispatch`?**
**A:** `singledispatch` works only on the first argument's type. `multipledispatch` (via third-party lib) supports multiple arguments.


