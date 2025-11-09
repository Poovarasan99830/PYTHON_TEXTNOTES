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




import datetime

class BaseModel:
    def __init__(self):
        self.created_at = datetime.datetime.now()

    def save(self):
        print(f"Record saved at {self.created_at}")

class User(BaseModel):
    def __init__(self, username):
        super().__init__()
        self.username = username

    def __str__(self):
        return f"welcome {self.username}"

user = User("poovarasan")
print(user)
user.save()