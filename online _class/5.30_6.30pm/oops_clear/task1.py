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
#     def make_payment(self):
#         print(f"Payment of ₹{amount} made using Credit Card.")


# class UPIBasedPayment(Payment):
#     def make_payment(self, amount):
#         print(f"Payment of ₹{amount} made using UPI.")


# # Using the abstraction
# payment1 = CreditCardPayment()
# payment1.make_payment()

# payment2 = UPIBasedPayment()
# payment2.make_payment()


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





# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self._address="chennai"
#         self.age=56

#     @property
#     def get_name(self):
#         return self.__name
    
#     @get_name.setter
#     def get_name(self, new_name):
#         if len(new_name) > 2:
#             self.__name = new_name

# p = Person("Abi")
# print(p.get_name)

# p.get_name="sam"
# print(p.get_name)





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



# class Car:
#     discount="50%"

#     def __init__(self):
#         self.model = "BMW"
#         print(Car.discount)
#         print(f"Car model is {self.model}")

   
#     # @classmethod
#     # def show_model(cls):
#     #     print(Car.discount)
#     #     print(f"This car model is....")


#     @classmethod
#     def display(cls):
#         print(f"Car model is {cls.discount}")

#     @staticmethod
#     def main(self):
        



# obj=Car()
# Car.display()
# obj.main()

# Car.display("sam")


# Car.main("SAM")






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





# import threading

# lock = threading.Lock()
# count = 0

# def increment():
#     global count
#     for _ in range(2):
#         with lock:
#             count += 1

# threads = [threading.Thread(target=increment) for _ in range(5)]

# for t in threads: t.start()
# for t in threads: t.join()

# print(count)




# import threading
# import time

# order_status = ""   # shared variable (dangerous without lock)

# def update_status(status):
#     global order_status
#     order_status = status
#     # Small sleep increases race condition effect
#     time.sleep(0.1)
#     print("Updated:", order_status)

# threads = [
#     threading.Thread(target=update_status, args=("Order Confirmed",)),
#     threading.Thread(target=update_status, args=("Payment Success",)),
#     threading.Thread(target=update_status, args=("Delivery Partner Assigned",))
# ]

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()



# import threading

# order_status = ""
# lock = threading.Lock()

# def update_status(status):
#     global order_status
#     with lock:
#         order_status = status
#         print("Updated:", order_status)

# threads = [
#     threading.Thread(target=update_status, args=("Order Confirmed",)),
#     threading.Thread(target=update_status, args=("Payment Success",)),
#     threading.Thread(target=update_status, args=("Delivery Partner Assigned",))
# ]

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()


# import threading
# import time
# import random

# class Flipkart:
#     def fetch_price(self, seller):
#         print(f"{seller} → Checking price...")
#         time.sleep(2)
#         price = random.randint(500, 1500)
#         print(f"{seller} → Price: ₹{price}")

#     def start_thread(self, seller):
#         t = threading.Thread(target=self.fetch_price, args=(seller,))
#         t.start()
#         return t

# f = Flipkart()

# t1 = f.start_thread("Seller A")
# t2 = f.start_thread("Seller B")
# t3 = f.start_thread("Seller C")


# import threading
# import time

# def fetch_service(name, delay):
#     print(f"Fetching {name}...")
#     time.sleep(delay)
#     print(f"Completed {name}")

# start = time.time()

# services = [
#     ("Product Data", 2),
#     ("Price Details", 2),
#     ("Ratings", 2),
#     ("Reviews", 2),
#     ("Images", 2)
# ]

# threads = []

# for name, d in services:
#     t = threading.Thread(target=fetch_service, args=(name, d))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# end = time.time()
# print("Total time:", end - start)





# import threading
# import time

# order_status = ""   # shared variable (dangerous without lock)

# def update_status(status):
#     global order_status
#     order_status = status
#     # Small sleep increases race condition effect
#     time.sleep(2)
#     print("Updated:", order_status)

# threads = [
#     threading.Thread(target=update_status, args=("Order Confirmed",)),
#     threading.Thread(target=update_status, args=("Payment Success",)),
#     threading.Thread(target=update_status, args=("Delivery Partner Assigned",))
# ]

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()



# import threading

# order_status = ""
# lock = threading.Lock()

# def update_status(status):
#     global order_status
#     with lock:
#         order_status = status
#         print("Updated:", order_status)

# threads = [
#     threading.Thread(target=update_status, args=("Order Confirmed",)),
#     threading.Thread(target=update_status, args=("Payment Success",)),
#     threading.Thread(target=update_status, args=("Delivery Partner Assigned",))
# ]

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()


# import threading
# import time

# def make_tea(order_no):
#     print(f"Tea {order_no} start pannuren (new worker)...")
#     time.sleep(2)
#     print(f"Tea {order_no} ready!")

# threads = []

# for i in range(1, 11):  # 10 orders
#     t = threading.Thread(target=make_tea, args=(i,))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()



# from concurrent.futures import ThreadPoolExecutor
# import time

# def make_tea(order_no):

#     print(f"Tea {order_no} start pannuren (pool worker)...")

#     time.sleep(2)

#     print(f"Tea {order_no} ready!")

#     return order_no

# # Create a pool of 5 workers

# with ThreadPoolExecutor(max_workers=5) as pool:
#     pool.map(make_tea, range(1, 11))



#__________________________________________________

#topic = Task Explanation Threading and Process Memory



#____________________________________________________________________
#Task 1: 1. Create a thread to print numbers from 1 to 10.
#____________________________________________________________________


# import threading
# import time


# def print_numbers(i):
#     print(f"Process_memory-I[Thread{i}(Worker)-doing ->work{i}]:")
#     print(f"work loading...{i}")
#     time.sleep(2)
#     print(f"process_memory-I[Thread{i}(worker)-->completed work {i}]")
    

# threads = []

# for i in range(1, 6):
#     t = threading.Thread(target=print_numbers, args=(i,))
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()

# print("Process Memory-I[ Main Thread completed].")



# When Python program starts → Python creates one main thread.
# This main thread executes all top-level code (the lines outside any function).
# It creates the worker thread t1.
# It calls t1.start() → worker thread begins.
# Then main thread waits using join().







# MAIN THREAD
#     |
#     |---> creates t1
#     |---> starts t1
#     |---> waits (join)
    
# WORKER THREAD (t1)
#     |
#     |---> executes print_numbers()
#     |---> prints 1 to 10






# ⭐ Explanation

### **1. PROCESS**

# * The Python program starts inside a **process**.
# * Process = memory + interpreter + one main thread.

### **2. MAIN THREAD**

# * Executes your top-level code.
# * Creates **5 child threads** inside the loop.
# * Calls `.join()` to wait for them.
# * After all child threads finish → prints final message.

### **3. CHILD THREADS**

# Each child thread runs:

# ```
# print_numbers(i)
# ```

# So child threads perform:

# * Worker 1 → work 1
# * Worker 2 → work 2
# * Worker 3 → work 3
# * Worker 4 → work 4
# * Worker 5 → work 5

# All run concurrently.





# ____________________________________________________________________________

# 🏢 **Real-World Analogy (Flipkart Warehouse Example)**

### Process = Flipkart Warehouse System

    #   → The entire logistics, database, control room



### Main Thread = Warehouse Manager

    #   → Gets the customer order request
    #   → Decides what tasks should be done
    #   → Creates multiple workers to do tasks in parallel
    #     One main manager in charge of handling your order request.*



### Child Threads = Workers

# Each worker does one job in parallel:

# * Worker 1 → Get product info
# * Worker 2 → Fetch images
# * Worker 3 → Fetch review sheet
# * Worker 4 → Find similar products
# * Worker 5 → Check delivery availability

# They all report back to the manager.
# Manager (Main Thread) combines everything and sends it to the customer.





# 🧩 **If this was Python Code (similar to your program)**

# ```python
# import threading
# import time

# def flipkart_task(name):
#     print(f"{name} started...")
#     time.sleep(2)
#     print(f"{name} completed...")

# print("Process Started (Flipkart Backend)")

# threads = []
# tasks = ["Product Details", "Images", "Reviews", "Similar Items", "Delivery Availability"]

# # Main Thread creates child threads
# for t in tasks:
#     thread = threading.Thread(target=flipkart_task, args=(t,))
#     threads.append(thread)
#     thread.start()

# # Main Thread waiting for child threads
# for thread in threads:
#     thread.join()

# print("Main Thread: All Flipkart tasks completed. Sending response to user.")
# # ```

# ---

# # 🎯 Summary (Easy to Remember)

# | Concept           | Flipkart Example                                     |
# | ----------------- | ---------------------------------------------------- |
# | **Process**       | Entire Flipkart backend program                      |
# | **Main Thread**   | Handles the user request                             |
# | **Child Threads** | Fetch different data parts (images, reviews, price…) |

# ---






# 🛒 **Flipkart Web App — Threading Comparison**

         # Think Flipkart as a big company (Process).
         # Inside it, one main manager (Main Thread) controls multiple workers (Child Threads).



#  **PROCESS (Flipkart Web App Backend Server)**

         #   ✔ The entire Flipkart backend running on a Python program
         #   ✔ Holds memory, database connections, cache, APIs, etc.

         # **Real-world analogy:**
               #   *Flipkart company building* → Everything happens inside this building.



# 🧵 **MAIN THREAD (Flipkart Request Handler)**

         #When a user opens the Flipkart website:

        #* One *main thread* starts to handle the request.
         #* It coordinates all work:
         #  ✔ Fetch products
         #  ✔ Fetch user profile
         #  ✔ Fetch offers
         #  ✔ Fetch cart details

      #**Analogy:**
         #*One main manager in charge of handling your order request.*



# **CHILD THREADS (Parallel Tasks for Faster Page Loading)**

       #Flipkart loads data from **multiple services** at the same time for speed.

### Example:

         #When one user opens a product page:

### The **Main Thread** creates multiple **Child Threads**:

# | Child Thread | What It Does (Flipkart Work)        |
# | ------------ | ----------------------------------- |
# | Thread-1     | Fetch product details (name, price) |
# | Thread-2     | Fetch product images                |
# | Thread-3     | Fetch reviews & ratings             |
# | Thread-4     | Fetch similar products              |
# | Thread-5     | Fetch delivery availabilit




# Here is the **short, clean, interview-style summary** 👇

# ---

# # ✅ **Process → Main Thread → Child Threads (Flipkart Example Summary)**

# ### **1. PROCESS = Flipkart Backend System**

# * The entire Flipkart Python program running in memory.
# * Holds all services: products, reviews, images, delivery, cart, offers.

# **Analogy:**
# 🏢 Flipkart company building → everything happens inside it.

# ---

# ### **2. MAIN THREAD = Request Manager**

# * Starts automatically when the Python program runs.
# * Handles the user request (ex: open product page).
# * Creates child threads to do work faster.

# **Analogy:**
# 👨‍💼 Warehouse manager who receives the customer request.

# ---

# ### **3. CHILD THREADS = Workers**

# Main thread creates multiple worker threads to load the page:

# * Thread-1 → Fetch product details
# * Thread-2 → Fetch images
# * Thread-3 → Fetch reviews
# * Thread-4 → Fetch similar products
# * Thread-5 → Check delivery availability

# All run **together (concurrently)**.

# **Analogy:**
# 👷 Each worker does one task and reports back to the manager.

# ---

# # 🎯 **One-Line Summary**

# **Process is the whole Flipkart system →
# Main Thread is the manager →
# Child Threads are workers doing parts of the work in parallel.**

# ---

# If you want, I can also give a **memory diagram** in simple boxes.






#____________________________________________________________________
#Task 1:2. Create a thread to print squares of numbers from 1 to 5.
#____________________________________________________________________

import threading
import time


# def print_square():
#     print("""Process_memory-II[Square-Thread(Worker)-doing ->work]:""")
#     for i in range(1, 6):
#         print(f"Square of {i} is {i*i}")
#         time.sleep(1)   
#     print("Process_memory-II[Square-Thread(Worker)-->completed work]")

# threads = []
# t = threading.Thread(target=print_square)
# threads.append(t)
# t.start()
# t.join()

# print("Process Memory-II[ Main Thread completed].")

#____________________________________________________________________
#    Task 3:3.Threads to Traverse Nested Menu
#____________________________________________________________________

# # import threading

# menu = {
#     "Food": ["Pizza", "Burger", "Pasta"],
#     "Drinks": ["Coke", "Juice"],
#     "Desserts": ["Ice Cream", "Cake"]
# }

# def traverse(category, items):
#     print(f"""Process_memory-I [-Thread(Worker)-doing ->work{category}]:""")
#     print(f"Work {category} Loading..... :")
#     time.sleep(1)
#     print(f"""Process_memory-I [-Thread(Worker)-->completed work{category} --->{menu[category]}""")

# threads = []
# for category, items in menu.items():
#     t = threading.Thread(target=traverse, args=(category, items))
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()


# print("All categories traversed.")    



# 1️⃣ Purpose → To process multiple menu categories faster using threads.
# 2️⃣ Concept → Each category runs in a separate thread inside the same process.
# 3️⃣ Code → Creates threads using threading.Thread() and runs traverse() function.
# 4️⃣ Flow → Main thread → creates worker threads → workers process items → join → finish.
# 5️⃣ Output → Each category prints “loading + completed” messages in parallel.
# 6️⃣ Benefit → Saves time by doing concurrent work instead of sequential work.


# Main Thread  
#     ↓  
# Creates thread for 'Food'  
#     ↓  
# Creates thread for 'Drinks'  
#     ↓  
# Creates thread for 'Desserts'  
#     ↓  
# Each child thread loads its category concurrently  
#     ↓  
# Child threads print completed work  
#     ↓  
# Main thread waits (join)  
#     ↓  
# Main thread prints “All categories traversed.”



# Here is the **FULL SUMMARY FORMAT** for your menu-thread program — clean, simple, interview-ready.

# ---

# # ✅ **1️⃣ Purpose – Why we need this**

# To process **multiple categories at the same time** (Food, Drinks, Desserts) instead of one-by-one.
# This makes the program **faster and concurrent**.

# ---

# # ✅ **2️⃣ Concept – What it does**

# * Uses **Multithreading**
# * Each category runs in a **separate thread (worker)**
# * Threads execute **concurrently** → faster results
# * Main thread waits using **join()**

# ---

# # ✅ **3️⃣ Code – How it works**

# * Create a dictionary with categories
# * For each category → create a **thread**
# * Thread executes the `traverse()` function
# * Inside the function:

#   * Simulates work using `sleep()`
#   * Prints start and completion message
# * Main thread waits until all threads finish

# ---

# # ✅ **4️⃣ Flow – Step-by-Step**

# ```
# Main Thread  
#     ↓  
# Creates thread for 'Food'  
#     ↓  
# Creates thread for 'Drinks'  
#     ↓  
# Creates thread for 'Desserts'  
#     ↓  
# Each child thread loads its category concurrently  
#     ↓  
# Child threads print completed work  
#     ↓  
# Main thread waits (join)  
#     ↓  
# Main thread prints “All categories traversed.”
# ```

# ---

# # ✅ **5️⃣ Output – Final result**

# Each category prints:

# * Start of work
# * Loading
# * Completed with item list

# All three categories run **parallel (order may vary)**
# Finally:

# ```
# All categories traversed.
# ```

# ---

# # ✅ **6️⃣ Benefit – Why it’s good**

# ✔ **Faster** → processes multiple menu sections at same time
# ✔ **Concurrent** → no waiting for each category
# ✔ **Real-world simulation** → like Zomato/Swiggy fetching Food/Offers/Images at once
# ✔ **Better CPU usage** (especially for I/O tasks)
# ✔ **Main thread stays free** until everything done


#____________________________________________________________________
#    Task 4:4. Create threads to download multiple files concurrently.
#____________________________________________________________________





# **📌 1. Code Example (Threaded Multi-Download)**

# ```python
# import threading
# import time

# def download_file(file_name):
#     print(f"Starting download → {file_name}")
#     time.sleep(2)   # simulate a download
#     print(f"Completed download → {file_name}")

# files = ["file1.pdf", "file2.jpg", "file3.mp4", "file4.zip"]

# threads = []

# # Create a thread for each file
# for f in files:
#     t = threading.Thread(target=download_file, args=(f,))
#     threads.append(t)
#     t.start()

# # Wait for all threads to finish
# for t in threads:
#     t.join()

# print("📥 All files downloaded.")
# ```





# Concept → Each file download runs in a separate child thread inside one Python process.
# Code → Uses threading.Thread() to start multiple download worker functions at the same time.
# Flow → Main thread → creates worker threads → each thread downloads a file → join → all complete.
# Output → Multiple downloads happening concurrently, each printing progress independently.
# Benefit → Total download time reduces because files download in parallel instead of sequential


#____________________________________________________________________
#    Task 5:5. Create threads to process multiple JSON objects at the same time.
#____________________________________________________________________






# import threading
# import time

# def cpu_work():
#     total = 0
#     for i in range(50_000_00):
#         total += i*i

# start = time.time()

# t1 = threading.Thread(target=cpu_work)
# t2 = threading.Thread(target=cpu_work)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Thread time:", time.time() - start)



# import multiprocessing
# import time

# def cpu_work():
#     total = 0
#     for i in range(50_000_00):
#         total += i*i
#     print(total)

# if __name__ == "__main__":
#     start = time.time()

#     p1 = multiprocessing.Process(target=cpu_work)
#     p2 = multiprocessing.Process(target=cpu_work)

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print("Process time:", time.time() - start)


# import threading
# import time, random

# class PriceEngine:
#     def calculate(self, seller):
#         print(f"{seller} → calculating price...")
#         time.sleep(2)
#         print(f"{seller} → Price: {random.randint(200, 500)}")

#     def start_task(self, seller):
#         t = threading.Thread(target=self.calculate, args=(seller,))
#         t.start()
#         return t

# if __name__ == "__main__":
#     start = time.time()   # ⏱ START TIMER

#     engine = PriceEngine()

#     tasks = [
#         engine.start_task("Seller A"),
#         engine.start_task("Seller B"),
#         engine.start_task("Seller C"),
#     ]

#     for t in tasks:
#         t.join()

#     print("Threading Time:", time.time() - start)




# from multiprocessing import Process
# import time, random

# class PriceEngine:
#     def calculate(self, seller):
#         print(f"{seller} → calculating price...")
#         time.sleep(2)
#         print(f"{seller} → Price: {random.randint(200, 500)}")

#     def start_task(self, seller):
#         p = Process(target=self.calculate, args=(seller,))
#         p.start()
#         return p




# if __name__ == "__main__":
#     start = time.time()   # ⏱ START TIMER

#     engine = PriceEngine()

#     tasks = [
#         engine.start_task("Seller A"),
#         engine.start_task("Seller B"),
#         engine.start_task("Seller C"),
#         engine.start_task("seller D"),
#     ]

#     for t in tasks:
#         t.join()

#     print("Multiprocessing Time:", time.time() - start)






# from multiprocessing import cpu_count

# print("Total CPU Cores =", cpu_count())


# from multiprocessing import cpu_count

# print("Total CPU Cores =", cpu_count())


# from multiprocessing import Pool

# def square(n):
#     return n * n

# if __name__ == "__main__":
#     with Pool(processes=4) as p:
#         result = p.map(square, [1,2,3,4,5,6,7,8])
#         print(result)


# from concurrent.futures import ThreadPoolExecutor
# import time

# def make_tea(order_no):

#     print(f"Tea {order_no} start pannuren (pool worker)...")

#     time.sleep(2)

#     print(f"Tea {order_no} ready!")

#     return order_no

# # Create a pool of 5 workers

# with ThreadPoolExecutor(max_workers=5) as pool:
#     g=pool.map(make_tea, range(1, 11))
#     print(list(g))



# from multiprocessing import Pool
# import math

# def compute_factorial(n):
#     return math.factorial(n)

# numbers = [50000, 60000, 70000, 80000]

# if __name__ == "__main__":
#     with Pool() as pool:
#         result = pool.map(compute_factorial, numbers)
        
#         print("Done")


# import multiprocessing
# import time

# def cpu_work():
#     total = 0
#     for i in range(50_000_00):
#         total += i*i
#     print(total)

# start = time.time()

# t1 = multiprocessing.Process(target=cpu_work)
# t2 = multiprocessing.Process(target=cpu_work)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Thread time:", time.time() - start)



# import multiprocessing 
# import time, random

# class PriceEngine:
#     def calculate(self, seller):
#         print(f"{seller} → calculating price...")
#         time.sleep(2)
#         print(f"{seller} → Price: {random.randint(200, 500)}")

#     def start_task(self, seller):
#         p = multiprocessing.Process(target=self.calculate, args=(seller,))
#         p.start()
#         return p

# engine = PriceEngine()

# tasks = [
#     engine.start_task("Seller A"),
#     engine.start_task("Seller B"),
#     engine.start_task("Seller C"),
# ]

# for t in tasks:
#     t.join()




