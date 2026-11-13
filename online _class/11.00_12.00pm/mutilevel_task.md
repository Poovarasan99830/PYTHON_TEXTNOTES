# ===========================================================
# 🧩 MULTILEVEL INHERITANCE EXAMPLES
# ===========================================================
# Each section shows:
#   Base Class → Intermediate Class → Derived Class
# ===========================================================


# ===========================================================
# 🏢 1️⃣ COMPANY HIERARCHY EXAMPLE
# ===========================================================

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def show_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.id}")


class Manager(Employee):  # Inheriting from Employee
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

    def assign_task(self):
        print(f"Manager {self.name} assigns tasks to {self.team_size} team members.")


class ProjectManager(Manager):  # Inheriting from Manager
    def __init__(self, name, emp_id, team_size, project_name):
        super().__init__(name, emp_id, team_size)
        self.project_name = project_name

    def show_project(self):
        print(f"Project Manager {self.name} manages project: {self.project_name}")


# ---- Test Section 1 ----
print("=== COMPANY HIERARCHY EXAMPLE ===")
pm = ProjectManager("Arun", 101, 10, "AI Automation")
pm.show_details()
pm.assign_task()
pm.show_project()
print("\n")


# ===========================================================
# 🚗 2️⃣ VEHICLE EXAMPLE
# ===========================================================

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"{self.brand} is driving at {self.speed} km/h.")


class Car(Vehicle):  # Inheriting from Vehicle
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def show_car_info(self):
        print(f"{self.brand} car has {self.doors} doors.")


class ElectricCar(Car):  # Inheriting from Car
    def __init__(self, brand, speed, doors, battery_capacity):
        super().__init__(brand, speed, doors)
        self.battery_capacity = battery_capacity

    def charge_battery(self):
        print(f"{self.brand} battery capacity is {self.battery_capacity} kWh. Charging...")


# ---- Test Section 2 ----
print("=== VEHICLE EXAMPLE ===")
ec = ElectricCar("Tesla", 200, 4, 85)
ec.drive()
ec.show_car_info()
ec.charge_battery()
print("\n")


# ===========================================================
# 🎓 3️⃣ EDUCATION SYSTEM EXAMPLE
# ===========================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


class Student(Person):  # Inheriting from Person
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def study(self):
        print(f"Student {self.name} (Roll No: {self.roll_number}) is studying.")


class GraduateStudent(Student):  # Inheriting from Student
    def __init__(self, name, age, roll_number, research_topic):
        super().__init__(name, age, roll_number)
        self.research_topic = research_topic

    def research(self):
        print(f"Graduate student {self.name} is researching on '{self.research_topic}'.")


# ---- Test Section 3 ----
print("=== EDUCATION SYSTEM EXAMPLE ===")
gs = GraduateStudent("Kavya", 24, "CS101", "Artificial Intelligence")
gs.introduce()
gs.study()
gs.research()
print("\n")


# ===========================================================
# 🏦 4️⃣ BANKING SYSTEM EXAMPLE
# ===========================================================

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining Balance: ₹{self.balance}")
        else:
            print("Insufficient balance!")


class SavingsAccount(Account):  # Inheriting from Account
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added ₹{interest}. New Balance: ₹{self.balance}")


class SeniorCitizenSavingsAccount(SavingsAccount):  # Inheriting from SavingsAccount
    def __init__(self, account_number, balance, interest_rate, extra_benefit):
        super().__init__(account_number, balance, interest_rate)
        self.extra_benefit = extra_benefit

    def apply_benefits(self):
        print(f"Extra benefit applied: {self.extra_benefit}")


# ---- Test Section 4 ----
print("=== BANKING SYSTEM EXAMPLE ===")
acc = SeniorCitizenSavingsAccount(987654321, 50000, 5, "Free Health Insurance")
acc.deposit(10000)
acc.add_interest()
acc.apply_benefits()
acc.withdraw(20000)
print("\n")

# ===========================================================
# END OF FILE
# ===========================================================
