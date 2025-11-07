Perfect set of OOP tasks 👌
Here’s the **complete implementation and explanation** (in simple, clear Python) for your **Encapsulation** and **Abstraction** tasks.

---

# 🧩 **Encapsulation Tasks**

## ✅ Task 1 — Fitness Tracker

Encapsulation = *protecting internal data from direct modification.*

```python
class FitnessTracker:
    def __init__(self):
        self.__steps = 0
        self.__calories = 0

    def add_steps(self, count):
        if count > 0:
            self.__steps += count
        else:
            print("❌ Steps cannot be negative.")

    def add_calories(self, amount):
        if amount > 0:
            self.__calories += amount
        else:
            print("❌ Calories cannot be negative.")

    def get_summary(self):
        return f"🏃‍♂️ Total Steps: {self.__steps}, 🔥 Total Calories: {self.__calories}"


# Example usage
tracker = FitnessTracker()
tracker.add_steps(5000)
tracker.add_calories(200)
tracker.add_steps(-100)   # invalid
print(tracker.get_summary())
```

🧠 **Concept:**
`__steps` and `__calories` are *private variables* (cannot be accessed directly).
Access is controlled via public methods.

---

## ✅ Task 2 — IoT Device Controller

Encapsulation + Controlled Access

```python
class SmartDevice:
    def __init__(self):
        self.__status = "OFF"

    def turn_on(self):
        if self.__status != "ON":
            self.__status = "ON"
            print("💡 Device turned ON.")
        else:
            print("Device is already ON.")

    def turn_off(self):
        if self.__status != "OFF":
            self.__status = "OFF"
            print("💤 Device turned OFF.")
        else:
            print("Device is already OFF.")

    def get_status(self):
        return f"Device status: {self.__status}"


# Example
device = SmartDevice()
device.turn_on()
device.turn_off()
print(device.get_status())
```

🧠 **Concept:**
`__status` is private — direct access from outside not allowed.
The public methods control how the value changes.

---

# 🧠 **Abstraction Tasks**

To use abstraction, we’ll use Python’s `abc` module (Abstract Base Class).

---

## ✅ Task 3 — Notification System

```python
from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def validate_receiver(self, receiver):
        pass


class EmailNotification(Notification):
    def validate_receiver(self, receiver):
        return "@" in receiver

    def send(self, message):
        print(f"📧 Sending Email: {message}")


class SMSNotification(Notification):
    def validate_receiver(self, receiver):
        return receiver.isdigit() and len(receiver) == 10

    def send(self, message):
        print(f"📱 Sending SMS: {message}")


class PushNotification(Notification):
    def validate_receiver(self, receiver):
        return len(receiver) > 5  # dummy rule

    def send(self, message):
        print(f"🔔 Sending Push Notification: {message}")


# Example usage
email = EmailNotification()
if email.validate_receiver("test@gmail.com"):
    email.send("Welcome to our service!")
```

🧠 **Concept:**
Abstract methods `send()` and `validate_receiver()` hide complex logic — subclasses define *how* it works.

---

## ✅ Task 4 — Smart Home Appliance

```python
from abc import ABC, abstractmethod

class Appliance(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def calculate_energy(self, hours, watts):
        energy = (watts * hours) / 1000
        return f"⚡ Energy Used: {energy} kWh"


class WashingMachine(Appliance):
    def turn_on(self):
        print("🧺 Washing Machine started.")

    def turn_off(self):
        print("🧺 Washing Machine stopped.")


class AirConditioner(Appliance):
    def turn_on(self):
        print("❄️ Air Conditioner cooling ON.")

    def turn_off(self):
        print("❄️ Air Conditioner OFF.")


class Refrigerator(Appliance):
    def turn_on(self):
        print("🥶 Refrigerator running.")

    def turn_off(self):
        print("🥶 Refrigerator turned OFF.")


# Example usage
ac = AirConditioner()
ac.turn_on()
print(ac.calculate_energy(5, 1500))  # 5 hours, 1500 watts
ac.turn_off()
```

🧠 **Concept:**
Abstract class defines *what must be done*; subclasses define *how it is done*.
Energy calculation is **common logic** → placed in the abstract class (shared by all).





# 🧩 **Encapsulation — Data Protection & Controlled Access**

```
                +-----------------------+
                |     FitnessTracker    |
                +-----------------------+
                |  __steps              |  ← private
                |  __calories           |  ← private
                +-----------------------+
                | + add_steps()         |  ← public (validates & updates)
                | + add_calories()      |
                | + get_summary()       |
                +-----------------------+
                          ↑
                          |
                 user calls methods
                 (cannot access private vars directly)
```

**Key Idea:**
🔒 Private data → protected inside class
✅ Public methods → control access safely
❌ Direct modification (like `obj.__steps`) → not allowed

---

```
                +-------------------+
                |    SmartDevice    |
                +-------------------+
                |  __status         |  ← private ("ON"/"OFF")
                +-------------------+
                | + turn_on()       |
                | + turn_off()      |
                | + get_status()    |
                +-------------------+
```

**Flow:**

* Only public methods can change device status.
* Encapsulation hides inner variable from user.

---

# 🧠 **Abstraction — Hide Complex Logic**

```
                    +----------------------+
                    |   Notification (ABC) |
                    +----------------------+
                    | + send(message) *    | ← abstract method
                    | + validate_receiver()*|
                    +----------^-----------+
                               |
   --------------------------------------------------------
   |                         |                          |
+----------------+   +----------------+        +----------------+
| EmailNotification |   | SMSNotification |     | PushNotification |
+----------------+   +----------------+        +----------------+
| + send()       |   | + send()       |        | + send()       |
| + validate()   |   | + validate()   |        | + validate()   |
+----------------+   +----------------+        +----------------+
```

**Key Idea:**
💡 `Notification` defines the structure (what must exist).
💬 Subclasses implement *their own logic* for sending messages.
→ Users interact with `send()` without knowing the internal code.

---

```
                 +---------------------+
                 |  Appliance (ABC)    |
                 +---------------------+
                 | + turn_on() *       |
                 | + turn_off() *      |
                 | + calculate_energy()| ← common concrete method
                 +----------^----------+
                            |
     -------------------------------------------------
     |                        |                     |
+----------------+   +----------------+   +----------------+
| WashingMachine |   | AirConditioner |   | Refrigerator   |
+----------------+   +----------------+   +----------------+
| + turn_on()    |   | + turn_on()    |   | + turn_on()    |
| + turn_off()   |   | + turn_off()   |   | + turn_off()   |
+----------------+   +----------------+   +----------------+
```

**Key Idea:**
🧩 Abstract class = blueprint
⚙️ Subclasses = real implementations
⚡ `calculate_energy()` = shared method → reusable logic for all appliances.

---

# 🔍 Summary Table

| Concept           | Purpose                                  | Example                         | Visibility                         | Who Controls Data/Logic    |
| ----------------- | ---------------------------------------- | ------------------------------- | ---------------------------------- | -------------------------- |
| **Encapsulation** | Protect data, control access             | `FitnessTracker`, `SmartDevice` | Private variables + Public methods | Class instance methods     |
| **Abstraction**   | Hide complexity, show essential features | `Notification`, `Appliance`     | Abstract base class                | Subclasses implement logic |

