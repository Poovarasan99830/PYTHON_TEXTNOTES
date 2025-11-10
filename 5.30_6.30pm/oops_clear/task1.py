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
        

# class C(B, E):
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



class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 6)
print(v1 + v2)


# v1.__add__(v2)