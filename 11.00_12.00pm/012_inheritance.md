

# 🔹 **Inheritance in Python OOP**


## ✅ 1. Definition

**Inheritance** is an **OOP concept** where a **child class** (subclass) can **inherit attributes and methods** from a **parent class** (superclass).

It helps in **reusing code**, **extending functionality**, and **organizing programs** logically.

**Key Points:**

* Promotes **code reusability**.
* Reduces duplication.
* Child can **override** parent methods.
* Supports **multiple inheritance**.

---

## 🔹 2. Syntax

```python
class Parent:
    def display(self):
        print("This is Parent class")

class Child(Parent):
    pass
```

**Explanation:**

* `Parent` → Base (superclass).
* `Child` → Derived (subclass) that inherits methods and attributes.
* `Child` object can access both parent and its own members.

---

## 🔹 3. Real-Time Examples

1. **Student System** → Base: Person, Derived: Student.
2. **Banking System** → Base: Account, Derived: SavingsAccount, CurrentAccount.
3. **E-Commerce** → Base: Product, Derived: Electronics, Clothing.
4. **Game Development** → Base: Character, Derived: Warrior, Mage, Archer.

---

## 🔹 4. Fun / Analogical Examples

1. **Family Tree Analogy:**
   Child inherits traits (attributes) and habits (methods) from parents.

2. **Company Hierarchy:**
   Employee (base), Manager and Developer (derived).

3. **Vehicles:**
   Base: Vehicle → Derived: Car, Bike, Bus.

---

## 🔹 5. Demo Code – Basic Inheritance

```python
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

s = Student("Alice", 101)
s.show()
s.display()
```

✅ Features:

* Child class uses parent constructor via `super()`.
* Student inherits attributes from Person.

---

## 🔹 6. Types of Inheritance

### 6.1. **Single Inheritance**

One parent → One child.

```python
class A:
    def methodA(self):
        print("Method in A")

class B(A):
    def methodB(self):
        print("Method in B")

obj = B()
obj.methodA()
obj.methodB()
```

---

### 6.2. **Multilevel Inheritance**

Grandparent → Parent → Child.

```python
class A:
    def methodA(self):
        print("A method")

class B(A):
    def methodB(self):
        print("B method")

class C(B):
    def methodC(self):
        print("C method")

obj = C()
obj.methodA()
obj.methodB()
obj.methodC()
```

---

### 6.3. **Multiple Inheritance**

Child inherits from multiple parents.

```python
class A:
    def featureA(self):
        print("Feature A")

class B:
    def featureB(self):
        print("Feature B")

class C(A, B):
    pass

obj = C()
obj.featureA()
obj.featureB()
```

---

### 6.4. **Hierarchical Inheritance**

One parent → multiple children.

```python
class Parent:
    def feature(self):
        print("Parent feature")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()
c1.feature()
c2.feature()
```

---

### 6.5. **Hybrid Inheritance**

Combination of multiple types.
(Python uses **MRO - C3 Linearization** to resolve conflicts.)

```python
class A:
    def show(self):
        print("A class")

class B(A):
    def show(self):
        print("B class")

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.show()  # B class (MRO decides)
```

---

## 🔹 7. Method Overriding

Child can redefine parent methods.

```python
class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

obj = Dog()
obj.sound()   # Output: Dog barks
```

---

## 🔹 8. Constructor in Inheritance

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)   # Call parent constructor
        self.age = age

c = Child("Alice", 20)
print(c.name, c.age)
```

---

## 🔹 9. Real-Life Use Cases

* **Banking** → Different account types inherit base account.
* **Games** → Characters inherit base character.
* **E-commerce** → Different product categories inherit base Product.
* **IoT** → Different devices inherit common Device class.
* **ERP** → Inventory categories inherit common Item class.

---

## 🔹 10. Tasks / Exercises

1. Create a `Vehicle` (parent) and `Car` (child) class, with methods.
2. Create a `Person` → `Employee` → `Manager` (multilevel inheritance).
3. Demonstrate **multiple inheritance** with two parent classes.
4. Override parent method in child class.
5. Show how `super()` works with constructors.

---

## 🔹 11. Task Explanation

| Task       | Explanation                                          |
| ---------- | ---------------------------------------------------- |
| Vehicle    | Car inherits features from Vehicle.                  |
| Multilevel | Person → Employee → Manager shows chain inheritance. |
| Multiple   | Demonstrates accessing methods from both parents.    |
| Overriding | Child customizes parent method.                      |
| super()    | Calls parent constructor explicitly.                 |

---

## 🔹 12. Best Practices

* Use `super()` to call parent methods/constructors.
* Avoid deep inheritance trees (hard to maintain).
* Prefer **composition over inheritance** in complex systems.
* Understand **MRO** for multiple inheritance.
* Keep parent class generic and reusable.

---

## 🔹 13. Beginner → Advanced Levels

**Beginner:** Single inheritance, constructors, methods.
**Intermediate:** Multilevel, hierarchical inheritance, method overriding.
**Advanced:** Multiple, hybrid inheritance, MRO, `super()`, diamond problem.

---

## 🔹 14. General Real-Life Applications

1. **Web Apps** → User → Admin, Customer, Vendor classes.
2. **IoT Devices** → Base Device → Sensors, Actuators.
3. **Games** → Character → Warrior, Mage, Archer.
4. **Banking** → Account → SavingsAccount, CurrentAccount.
5. **E-Commerce** → Product → Electronics, Furniture, Clothing.

---

✅ This covers **everything about inheritance**:

* Basics → Syntax & Types
* Real-life examples & analogies
* Demo code & tasks
* Advanced scenarios → overriding, constructors, multiple inheritance
* Best practices & usage

