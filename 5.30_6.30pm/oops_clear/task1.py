# class Parent:
#     def __init__(self, name, age):
#         print("Parent init called")
#         self.name = name
#         self.age = age

# class Child(Parent):
#     def __init__(self, name, age, grade):
#         print("Child init called")
#         super().__init__(name, age)
#         self.grade = grade
       
        

# c = Child("Alice", 12, "7th")

# print(c.grade)  # Works
# print(c.name)   # ❌ AttributeError: 'Child' object has no attribute 'name'




# class A:
#     def __init__(self):
#         print("Feature A")

# class B(A):
#     def __init__(self):
#         print("Feature B")
#         super().__init__() 
       
# class E(A):
#     def __init__(self):
#         print("Feature E")
#         super().__init__()
        

# class C(B,E):
#     def __init__(self):
#         print("Feature C")
#         super().__init__()
        

# # obj = C()
# # obj.featureA()
# # obj.featureB()
# # print(C.mro())
# obj=C()
# print(C.__mro__)




# import datetime

# class BaseModel:
#     def __init__(self):
#         self.created_at = datetime.datetime.now()

#     def save(self):
#         print(f"Record saved at {self.created_at}")

# class User(BaseModel):
#     def __init__(self, username):
#         super().__init__()
#         self.username = username

#     def __str__(self):
#         return f"welcome {self.username}"

# user = User("poovarasan")
# print(user)
# user.save()



# class Employee:
#     def role(self):
#         return "Employee"

# class Developer(Employee):
#     def role(self):
#         super().role()
#         return "Writes Code"

# class Manager(Employee):
#     def role(self):
#         super().role()
#         return "Leads Team"

# for emp in [Developer(), Manager()]:
#     print(emp.role())



# class Employee:
#     def role(self):
#         print("General Employee")

# class Developer(Employee):
#     def developer_role(self):
#         print("Writes Code")

# class Manager(Employee):
#     def manager_role(self):
#         print("Leads Team")




# for emp in [Employee(), Developer(), Manager()]:
#     # Different method names — need manual checks
#     if isinstance(emp, Manager):
#         emp.manager_role()
#     elif isinstance(emp, Developer):
#         emp.developer_role()
#     else:
#         emp.role()



# class Vector:
#     def __init__(self, x, y):
#         self.x, self.y = x, y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"({self.x}, {self.y})"

# v1 = Vector(2, 3)
# v2 = Vector(5, 6)
# print(v1 + v2)


# v1.__add__(v2)




# from abc import ABC, abstractmethod

# # Abstract Class
# class Payment(ABC):

#     @abstractmethod
#     def make_payment(self, amount):
#         pass  # Only defines WHAT to do, not HOW


# # Concrete Class
# class CreditCardPayment(Payment):
#     def make_payment(self, amount):
#         print(f"Payment of ₹{amount} made using Credit Card.")


# class UPIBasedPayment(Payment):
#     def make_payment(self, amount):
#         print(f"Payment of ₹{amount} made using UPI.")


# Using the abstraction
# payment1 = CreditCardPayment()
# payment1.make_payment(1000)

# payment2 = UPIBasedPayment()
# payment2.make_payment(500)


# obj=Payment()





# programming language:
#     variable    ===>empty box
    
#     data       ===>infomation 
                                #  ==>types:
                                # text --->string
#                      #         number --->int,float,complex

#                      #         boolean --->True,False
#                      #         list --->[1,2,3]
#                      #         tuple --->(1,2,3)
#                      #         set --->{1,2,3}
#                      #         dict --->{"key": "value"}



#     opearators ==>perform the operation

    
#     function  ===>to perform the specific task
    

#     keywords ==>reserved words in programming language which have special meaning



# class Product:
#     def __init__(self, price):
#         self.__price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value > 0:
#             self.__price = value
#         else:
#             print("Invalid Price")

# item = Product(100)
# print(item.price)
# item.price = 250
# print(item.price)

# item.price = -50  # Invalid Price





# class Product:
#     def __init__(self, price):
#         self.__price = price

#     @property
#     def price(self,arg=None):
#         if arg is not None:
#             self.__price=arg
#         return f"The price is {self.__price}"

#     @price.setter
#     def price(self, value):
#         if value > 0:
#             self.__price = value
#         else:
#             print("Invalid Price")

# item = Product(100)
# item.price=6789
# print(item.price)

# print(item.price)   # ✅ Calls getter
# item.price = 250    # ✅ Calls setter
# print(item.price)
# item.price = -50    # ❌ Invalid Price


# We use the same function name for getter and setter because both represent the same logical attribute, just with different behaviors (read/write).
# Python binds them under one “property” name to make your code clean, natural, and safe.





# Perfect 👍 — let’s understand **why getter and setter use the same name** through a **real-world analogy** that makes it crystal clear.

# ---

# # 🏠 **Real-World Analogy — “Smart Door Lock”**

# ---

# ## **Imagine a Smart Door at Your Home 🏡**

# The door has **one name** — let’s call it **“main_door”**.

# But this one door can perform **two different actions** depending on what you do:

# | Action             | What You Do                        | What Happens                         |
# | ------------------ | ---------------------------------- | ------------------------------------ |
# | 🔓 **Get (Read)**  | You **open** the door              | You can **see inside the house**     |
# | 🔒 **Set (Write)** | You **lock** or **close** the door | You **change the state** of the door |

# ---

# Even though you perform **two different actions**,
# you’re still using **the same door** — the **“main_door.”**

# You don’t say:

# * “open_main_door()”
# * “close_main_door()”

# You just interact with **main_door** intuitively:

# ```text
# main_door → open
# main_door → close
# ```

# ---

# ## 🧠 **Now Relate This to Python**

# | Real World                           | Python Code                      |
# | ------------------------------------ | -------------------------------- |
# | The door is the “property”           | `price`                          |
# | Looking inside the house             | `@property` (getter)             |
# | Locking or changing the door’s state | `@price.setter` (setter)         |
# | Both share the same name “main_door” | Both share the same name `price` |

# ---

# ### ✅ Analogy in Action

# ```python
# class Product:
#     def __init__(self, price):
#         self.__price = price

#     @property
#     def price(self):
#         # Opening the door — reading value
#         return self.__price

#     @price.setter
#     def price(self, value):
#         # Locking the door safely — updating value
#         if value > 0:
#             self.__price = value
#         else:
#             print("Invalid Price")
# ```

# So:

# ```python
# item.price        # You’re “looking inside” (getter)
# item.price = 250  # You’re “changing the state” (setter)
# ```

# But in both cases, you’re dealing with **the same property: `price`**
# Just like you deal with the same **door** that can **open or close**.

# ---

# ## 🧩 **In One Line Summary**

# > Using the same name for getter and setter is like having **one smart door** with **two modes** —
# > you open it to **see inside (getter)** and close it to **change its state (setter)** —
# > but it’s still **one door**, not two different ones.

# ---

# Would you like me to give one more analogy from **real-life apps** (like bank balance or volume control)?





class Person:
    def __init__(self, name):
        self.__name = name
        self._address="chennai"
        self.age=56

    @property
    def get_name(self):
        return self.__name
    
    @get_name.setter
    def get_name(self, new_name):
        if len(new_name) > 2:
            self.__name = new_name

p = Person("Abi")
print(p.get_name)

p.get_name="sam"
print(p.get_name)





# class Product:
#     def __init__(self, price):
#         self.__price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value > 0:
#             self.__price = value
#         else:
#             print("Invalid Price")


# item = Product(100)
# print(item.price)
# item.price = 250
# print(item.price)
