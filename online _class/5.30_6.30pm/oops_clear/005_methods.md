
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
