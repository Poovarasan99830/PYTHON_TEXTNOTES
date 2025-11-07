

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






## 🔹 1. **Single Inheritance**

👉 One base class → One derived class.

### Example: School System

**Teacher (Base Class)**

* Attributes: `name`, `subject`
* Methods: `teach()`

**MathTeacher (Derived Class)**

* Inherits `Teacher`
* Extra Attribute: `specialization`
* Method: `solve_problem()`

---

## 🔹 2. **Multilevel Inheritance**

👉 Chain of inheritance: Grandparent → Parent → Child.
## 5️⃣ E-commerce Example – Multilevel Inheritance

### Structure:

**Product (Base Class)**

* Attributes: `product_id`, `price`
* Methods: `show_product()`

**Electronics (Intermediate Class)**

* Inherits `Product`
* Extra Attribute: `warranty`
* Method: `show_warranty()`

**Mobile (Derived Class)**

* Inherits `Electronics`
* Extra Attribute: `ram_size`
* Method: `show_mobile_specs()`
---

## 🔹 3. **Hierarchical Inheritance**

👉 One base class → multiple derived classes.

### Example: Animal System

**Animal (Base Class)**

* Attributes: `name`, `age`
* Methods: `eat()`, `sleep()`

**Dog (Derived Class 1)**

* Inherits `Animal`
* Extra Attribute: `breed`
* Method: `bark()`

**Cat (Derived Class 2)**

* Inherits `Animal`
* Extra Attribute: `color`
* Method: `meow()`

---

## 🔹 4. **Multiple Inheritance**

👉 A class inherits from **more than one base class**.

### Example: Smart Device

**Camera (Base Class 1)**

* Attribute: `resolution`
* Method: `take_photo()`

**Phone (Base Class 2)**

* Attribute: `number`
* Method: `make_call()`

**SmartPhone (Derived Class)**

* Inherits `Camera` + `Phone`
* Extra Attribute: `os`
* Method: `install_app()`

---

## 🔹 5. **Hybrid Inheritance**

👉 Combination of two or more inheritance types.

### Example: Education Hybrid System

**Person (Base Class)**

* Attributes: `name`, `age`
* Method: `introduce()`

**Student (Derived Class 1 – Single from Person)**

* Inherits `Person`
* Attribute: `roll_number`
* Method: `study()`

**Teacher (Derived Class 2 – Single from Person)**

* Inherits `Person`
* Attribute: `subject`
* Method: `teach()`

**TeachingAssistant (Derived Class – Multiple)**

* Inherits `Student` + `Teacher`
* Attribute: `hours`
* Method: `assist()`

---

✅ So in summary, Python supports:

1. Single Inheritance
2. Multilevel Inheritance
3. Hierarchical Inheritance
4. Multiple Inheritance
5. Hybrid Inheritance



Perfect 👍 You’ve listed all **5 inheritance types in Python OOP** with real-life examples.
Here’s the **Python code implementation** for each of them:

```python
# ----------------------------------------
# 1️⃣ Single Inheritance Example: School System
# ----------------------------------------

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

class MathTeacher(Teacher):  # Single Inheritance
    def __init__(self, name, subject, specialization):
        super().__init__(name, subject)
        self.specialization = specialization

    def solve_problem(self):
        print(f"{self.name} is solving {self.specialization} problems.")

# Usage
mt = MathTeacher("Mr. Sharma", "Mathematics", "Algebra")
mt.teach()
mt.solve_problem()


# ----------------------------------------
# 2️⃣ Multilevel Inheritance Example: E-commerce
# ----------------------------------------

class Product:
    def __init__(self, product_id, price):
        self.product_id = product_id
        self.price = price

    def show_product(self):
        print(f"Product ID: {self.product_id}, Price: ₹{self.price}")

class Electronics(Product):  # Inherits from Product
    def __init__(self, product_id, price, warranty):
        super().__init__(product_id, price)
        self.warranty = warranty

    def show_warranty(self):
        print(f"Warranty: {self.warranty} years")

class Mobile(Electronics):  # Inherits from Electronics
    def __init__(self, product_id, price, warranty, ram_size):
        super().__init__(product_id, price, warranty)
        self.ram_size = ram_size

    def show_mobile_specs(self):
        print(f"Mobile Specs → RAM: {self.ram_size}GB")

# Usage
mob = Mobile(101, 25000, 2, 8)
mob.show_product()
mob.show_warranty()
mob.show_mobile_specs()


# ----------------------------------------
# 3️⃣ Hierarchical Inheritance Example: Animal System
# ----------------------------------------

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):  # Derived from Animal
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking! Woof Woof!")

class Cat(Animal):  # Derived from Animal
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def meow(self):
        print(f"{self.name} is meowing! Meow Meow!")

# Usage
dog = Dog("Tommy", 5, "German Shepherd")
cat = Cat("Kitty", 3, "White")

dog.eat()
dog.bark()
cat.sleep()
cat.meow()


# ----------------------------------------
# 4️⃣ Multiple Inheritance Example: Smart Device
# ----------------------------------------

class Camera:
    def __init__(self, resolution):
        self.resolution = resolution

    def take_photo(self):
        print(f"Taking photo with {self.resolution}MP camera.")

class Phone:
    def __init__(self, number):
        self.number = number

    def make_call(self):
        print(f"Calling {self.number}...")

class SmartPhone(Camera, Phone):  # Multiple Inheritance
    def __init__(self, resolution, number, os):
        Camera.__init__(self, resolution)
        Phone.__init__(self, number)
        self.os = os

    def install_app(self, app):
        print(f"Installing {app} on {self.os} smartphone.")

# Usage
sp = SmartPhone(108, "9876543210", "Android")
sp.take_photo()
sp.make_call()
sp.install_app("WhatsApp")


# ----------------------------------------
# 5️⃣ Hybrid Inheritance Example: Education System
# ----------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I am {self.name}, {self.age} years old.")

class Student(Person):  # Single from Person
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def study(self):
        print(f"{self.name} is studying. Roll No: {self.roll_number}")

class Teacher(Person):  # Single from Person
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

class TeachingAssistant(Student, Teacher):  # Multiple (Hybrid)
    def __init__(self, name, age, roll_number, subject, hours):
        Student.__init__(self, name, age, roll_number)
        Teacher.__init__(self, name, age, subject)
        self.hours = hours

    def assist(self):
        print(f"{self.name} assists {self.subject} class for {self.hours} hours.")

# Usage
ta = TeachingAssistant("Raj", 22, 101, "Physics", 5)
ta.introduce()
ta.study()
ta.teach()
ta.assist()
```

---

✅ This code covers:

* **Single** → Teacher & MathTeacher
* **Multilevel** → Product → Electronics → Mobile
* **Hierarchical** → Animal → Dog, Cat
* **Multiple** → Camera + Phone → SmartPhone
* **Hybrid** → Person → Student/Teacher → TeachingAssistant

Do you also want me to **draw UML diagrams** (class diagrams) for each inheritance type so students can visually understand them?




























Got it 👍 You want **all real-time multilevel inheritance examples** explained in the **same structured format** like the banking system one.

Here’s the list rewritten in that format:

---

## 1️⃣ Company Hierarchy Example – Multilevel Inheritance

### Structure:

**Employee (Base Class)**

* Attributes: `name`, `id`
* Methods: `show_details()`

**Manager (Intermediate Class)**

* Inherits `Employee`
* Extra Attribute: `team_size`
* Method: `assign_task()`

**ProjectManager (Derived Class)**

* Inherits `Manager`
* Extra Attribute: `project_name`
* Method: `show_project()`

---

## 2️⃣ Vehicle Example – Multilevel Inheritance

### Structure:

**Vehicle (Base Class)**

* Attributes: `brand`, `speed`
* Methods: `drive()`

**Car (Intermediate Class)**

* Inherits `Vehicle`
* Extra Attribute: `doors`
* Method: `show_car_info()`

**ElectricCar (Derived Class)**

* Inherits `Car`
* Extra Attribute: `battery_capacity`
* Method: `charge_battery()`

---

## 3️⃣ Education System Example – Multilevel Inheritance

### Structure:

**Person (Base Class)**

* Attributes: `name`, `age`
* Methods: `introduce()`

**Student (Intermediate Class)**

* Inherits `Person`
* Extra Attribute: `roll_number`
* Method: `study()`

**GraduateStudent (Derived Class)**

* Inherits `Student`
* Extra Attribute: `research_topic`
* Method: `research()`

---

## 4️⃣ Banking System Example – Multilevel Inheritance

### Structure:

**Account (Base Class)**

* Attributes: `account_number`, `balance`
* Methods: `deposit()`, `withdraw()`

**SavingsAccount (Intermediate Class)**

* Inherits `Account`
* Extra Attribute: `interest_rate`
* Method: `add_interest()`

**SeniorCitizenSavingsAccount (Derived Class)**

* Inherits `SavingsAccount`
* Extra Attribute: `extra_benefit`
* Method: `apply_benefits()`

---

## 5️⃣ E-commerce Example – Multilevel Inheritance

### Structure:

**Product (Base Class)**

* Attributes: `product_id`, `price`
* Methods: `show_product()`

**Electronics (Intermediate Class)**

* Inherits `Product`
* Extra Attribute: `warranty`
* Method: `show_warranty()`

**Mobile (Derived Class)**

* Inherits `Electronics`
* Extra Attribute: `ram_size`
* Method: `show_mobile_specs()`

---

👉 Each of these follows the **Base → Intermediate → Derived chain** (Grandparent → Parent → Child).

Would you like me to also **write Python code implementations** for all these 5 examples (like the Banking one), or just keep them in this **structured explanation format** for teaching?



Perfect 👍 Let’s build a **detailed case study example** with **Multilevel Inheritance** that your students can easily relate to.

I’ll take the **Banking System** (since it’s real-life, practical, and structured).

---














## 🏦 Banking System Example – Multilevel Inheritance

### Structure:

1. **Account (Base Class)**

   * Attributes: `account_number`, `balance`
   * Methods: `deposit()`, `withdraw()`

2. **SavingsAccount (Intermediate Class)**

   * Inherits `Account`
   * Extra Attribute: `interest_rate`
   * Method: `add_interest()`

3. **SeniorCitizenSavingsAccount (Derived Class)**

   * Inherits `SavingsAccount`
   * Extra Attribute: `extra_benefit`
   * Method: `apply_benefits()`

---

### 📝 Code Implementation

```python
# Base class
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. Current Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Current Balance: ₹{self.balance}")
        else:
            print("Insufficient Balance!")

# Intermediate class
class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.04):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of ₹{interest:.2f} added. New Balance: ₹{self.balance:.2f}")

# Derived class
class SeniorCitizenSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.05, extra_benefit="Free Health Insurance"):
        super().__init__(account_number, balance, interest_rate)
        self.extra_benefit = extra_benefit

    def apply_benefits(self):
        print(f"Special Benefit for Senior Citizen: {self.extra_benefit}")

# ---------- Usage ----------
print("🏦 Senior Citizen Banking Example")
account1 = SeniorCitizenSavingsAccount(1001, 5000)

account1.deposit(2000)
account1.withdraw(1500)
account1.add_interest()
account1.apply_benefits()
```

---

### ✅ Sample Output

```
🏦 Senior Citizen Banking Example
Deposited ₹2000. Current Balance: ₹7000
Withdrew ₹1500. Current Balance: ₹5500
Interest of ₹275.00 added. New Balance: ₹5775.00
Special Benefit for Senior Citizen: Free Health Insurance
```

---

🔹 This shows:

* **Account** → general banking features.
* **SavingsAccount** → adds interest features.
* **SeniorCitizenSavingsAccount** → adds extra perks (benefits).

---

Would you like me to also prepare a **diagram (like UML/class hierarchy)** for this example so you can explain it visually to your students?
