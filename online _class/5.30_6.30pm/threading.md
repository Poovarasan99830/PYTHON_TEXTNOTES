


# ____________________________________________
**Concurrency** vs **Parallelism**
# _____________________________________________


* Concurrency → *Dealing with* multiple things at once (can be single-core).
* Parallelism → *Doing* multiple things at once (requires multi-core).



#Example:
one staff multiple subject  --python ,java,dot net
multiple staff multiple subject -->python,java,dot net


Concurrency ──► Multithreading ──► Shares memory, GIL limits CPU-bound performance
             └─► Asyncio ──► Single thread, non-blocking I/O

Parallelism ──► Multiprocessing ──► Multiple processes, true parallel execution, bypasses GIL


**Multithreading**   
**Multiprocessing**  
**Asynchronous Programming**  


# ______________________________________
**Multithreading**
# _______________________________________

   → Definition 
  → Real-time example
  ->N number Examples
  → Tasks 
  → Task Explanation 
  ->Advanced Concept 
  → Where Used 

  → Levels (Beginner, Intermediate, Advanced, General)**. 





# ________________________________________
  → Definition 
# _________________________________________



### ✅ Definition


**Threading** in Python means running multiple tasks **concurrently** within the same process.
**Multithreading** allows multiple threads to run at the same time, improving efficiency for tasks that can run **independently**.



* Good for **I/O tasks** (sleep, downloads, DB calls)
* Not good for **heavy CPU tasks**
* Especially useful when our program is doing **waiting work**



# **KEY FUNCTIONS**

| Function   | Meaning                              |
| ---------- | ------------------------------------ |
| `Thread()` | Create a thread                      |
| `.start()` | Begin thread execution               |
| `.join()`  | Wait until thread finishes           |
| `Lock()`   | Stop threads from fighting over data |


# _______________________________________________________
  → Real-time example
# _______________________________________________________

1. **Flipkart Product Categories:**
   Loading Electronics, Mobiles, Laptops, and Clothing categories **simultaneously** instead of sequentially.

2. **Zomato / Swiggy Menu:**
   Fetching South Indian, North Indian, Chinese dishes **concurrently** for faster display.




# _______________________________________________________
  →N number of  Examples
# _______________________________________________________


# _______________________________________________________
EXAMPLE 1 -->Normal Vs Threading(FUNCTION BASED)
# _______________________________________________________


**1. NORMAL (NO THREADS) — Flipkart search is slow**
  ---->  All services are called **one-by-one**.


```python

import time

def fetch_service(name, delay):
    print(f"Fetching {name}...")
    time.sleep(delay)   # simulating API delay
    print(f"Completed {name}")

start = time.time()

fetch_service("Product Data", 2)
fetch_service("Price Details", 2)
fetch_service("Ratings", 2)
fetch_service("Reviews", 2)
fetch_service("Images", 2)

end = time.time()
print("Total time:", end - start)


➡️ 5 tasks × 2 sec = **10 seconds**
➡️ Flipkart would feel **very slow**.



# _______________________________________________________

#  **2. WITH THREADS — Flipkart becomes FAST**
---->     All services fetched **parallel-aa**.



```python
import threading
import time

def fetch_service(name, delay):
    print(f"Fetching {name}...")
    time.sleep(delay)
    print(f"Completed {name}")

start = time.time()

services = [
    ("Product Data", 2),
    ("Price Details", 2),
    ("Ratings", 2),
    ("Reviews", 2),
    ("Images", 2)
]

threads = []

for name, d in services:
    t = threading.Thread(target=fetch_service, args=(name, d))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()
print("Total time:", end - start)

```

➡️ All services respond at same time
➡️ Total time = **2 seconds**, NOT 10 seconds
➡️ Flipkart search becomes **very fast**





### 🔥 Multi-threading (Parallel)

* product + price + rating + review + image
  **all start at same time**
* Wait 2 seconds only
* UI = super fast ⚡
* Customer happy 😍





# _______________________________________________________
EXAMPLE 2 -->Normal Vs Threading (CLASS BASED)
# _______________________________________________________



# **1️⃣ NORMAL PROGRAM (No Threading – Slow)**

→ Runs **one-by-one**
→ Next seller starts **only after previous finishes**

```python
import time
import random

def fetch_price(seller):
    print(f"{seller} → Checking price...")
    time.sleep(2)
    price = random.randint(500, 1500)
    print(f"{seller} → Price: ₹{price}")

# Normal (Sequential)
fetch_price("Seller A")
fetch_price("Seller B")
fetch_price("Seller C")




⛔ Takes **6 seconds** (2+2+2)
⛔ Slow user experience



# __________________________________________________________

# **2️⃣ THREADING PROGRAM (Fast – Parallel Fetch)**



→ All sellers checked **at the same time**
→ CPU switches threads → **concurrency**



```python


import threading
import time
import random


class Flipkart:
    def fetch_price(self, seller):
        print(f"{seller} → Checking price...")
        time.sleep(2)
        price = random.randint(500, 1500)
        print(f"{seller} → Price: ₹{price}")

    def start_thread(self, seller):
        t = threading.Thread(target=self.fetch_price, args=(seller,))
        t.start()
        return t

f = Flipkart()

t1 = f.start_thread("Seller A")
t2 = f.start_thread("Seller B")
t3 = f.start_thread("Seller C")





⏳ Takes **only 2 seconds total**
✔ ALL sellers checked **concurrently**
✔ Faster like Flipkart backend




#  Final Summary Table

| Feature                | Normal     | Multithreaded |
| ---------------------- | ---------- | ------------- |
| Execution              | Sequential | Parallel      |
| Speed                  | Slow       | Fast          |
| Number of APIs fetched | One-by-one | All at once   |
| User Experience        | Laggy      | Smooth        |




🔹 

# _______________________________________________________
EXAMPLE 3 -->**GIL (Global Interpreter Lock) With Threading
# _______________________________________________________



### ✅  **Why Python has GIL?**

* Makes **memory management simpler**.
* Prevents **race conditions** (when multiple threads modify data simultaneously).
* Python objects (like lists, dictionaries) become **thread-safe** without extra locks.

**Analogy:**

> If two students write in the same notebook at the same time, content may get mixed up.
> GIL ensures that **one student finishes writing before the next one starts**.



### ✅ **Race Condition**

* A **race condition** occurs when **two or more threads try to modify the same data simultaneously**.
* The result becomes **unpredictable** — sometimes correct, sometimes wrong.
* In Python, using * and **locks** can help **avoid race conditions**.



### ✅ **Default Thread Safety in Python**

* Python’s **GIL** makes **simple operations thread-safe**.
* By default, **race conditions are rare** for small operations.
* **However**, for **complex operations or multiple-step processes**, race conditions **can still occur**, and using **locks is necessary**.



# _______________________________________________________
#  Thread Working Flow with Main Thread With Child Thread
# _______________________________________________________




Python Process
│
├── Main Thread  ← starts first
│     └── creates other threads
│
├── Product Data Thread
├── Price Thread
├── Ratings Thread
├── Reviews Thread
└── Images Thread


Main Thread = Appa (Parent)
Worker Threads = 5 kids


Appa (main thread) says:

Nee Product Data fetch pannu
Nee Price fetch pannu
Nee Ratings fetch pannu
Nee Reviews fetch pannu
Nee Images fetch pannu
Kids do the work independently, not inside Appa's body.

But they all live in the same house (same process memory).





# ______________________________
#  Thread Working Flow With GIL 
# _____________________________



A) Code run
       ↓
B) Main Thread starts execution
       ↓
C) Main Thread acquires GIL
       ↓
D) Main Thread creates:
        - Product Data Thread
        - Price Thread
        - Ratings Thread
        - Reviews Thread
        - Images Thread
       ↓
E) Each worker thread starts and prints:
        "Fetching Product Data..."
        "Fetching Price..."
        "Fetching Ratings..."
        "Fetching Reviews..."
        "Fetching Images..."
       ↓
F) All 5 worker threads call time.sleep(2) → I/O wait
       ↓
G) All 5 threads BLOCK and release GIL
       ↓
H) After 2 seconds, scheduler picks any thread that wakes up
       ↓
I) For example: Product Data Thread wakes up first
       ↓
J) Product Data Thread acquires GIL
       ↓
K) Product Data Thread prints:
        "Completed Product Data"
       ↓
L) Product Data Thread finishes and releases GIL
       ↓
M) Scheduler picks the next thread that woke up:
        maybe Price Thread, Ratings Thread, etc.
       ↓
N) Each thread, one by one, acquires GIL and prints:
        "Completed Price"
        "Completed Ratings"
        "Completed Reviews"
        "Completed Images"
       ↓
O) All 5 worker threads finish → Main Thread’s join() unblocks → program ends










# _______________________________________________________
     EXAMPLE 4:Without Lock vs With Lock
# _______________________________________________________



# Threaded version WITHOUT Lock

```python

import threading
import time

order_status = ""   # shared variable (dangerous without lock)

def update_status(status):
    global order_status
    order_status = status
    # Small sleep increases race condition effect
    time.sleep(0.1)
    print("Updated:", order_status)

threads = [
    threading.Thread(target=update_status, args=("Order Confirmed",)),
    threading.Thread(target=update_status, args=("Payment Success",)),
    threading.Thread(target=update_status, args=("Delivery Partner Assigned",))
]

for t in threads:
    t.start()

for t in threads:
    t.join()




Updated: Payment Success
Updated: Delivery Partner Assigned
Updated: Delivery Partner Assigned   <-- overwritten incorrectly

Thread-1 writes "Order Confirmed"
Same time Thread-2 writes "Payment Success"
Same time Thread-3 writes "Delivery Partner Assigned"

All three run concurrently, so:

Updates overlap
Output becomes unpredictable
Final status becomes random

This is called Race Condition.


#_________________________________________________________________________

# Threaded version With Lock
     Multiple threads are trying to update the same shared variable (order_status).
     To prevent data corruption or mixed outputs, we use a lock.
     ➡ Ensures only one thread updates at a time.




# Threaded version With Lock Code

import threading

order_status = ""
lock = threading.Lock()

def update_status(status):
    global order_status
    with lock:
        order_status = status
        print("Updated:", order_status)

threads = [
    threading.Thread(target=update_status, args=("Order Confirmed",)),
    threading.Thread(target=update_status, args=("Payment Success",)),
    threading.Thread(target=update_status, args=("Delivery Partner Assigned",))
]

for t in threads:
    t.start()

for t in threads:
    t.join()




#CODE Explanation

Purpose: Protect shared data (order_status) from being changed by multiple threads at the same time.
Concept: A lock allows only one thread to update the variable, avoiding race conditions.
Code: Each thread calls update_status(), and with lock: ensures safe, one-by-one execution.
Flow: Thread A updates → releases lock → Thread B updates → Thread C updates.
Output: Three clean updates printed without mixing or corruption.
Benefit: Makes multi-threading safe, predictable, and consistent.



# Now updates happen one-by-one, safely.


# | Version                      | Safe?    | Why                                               |
# | ---------------------------- | -------- | ------------------------------------------------- |
# | **Threads WITHOUT Lock**     | ❌ Unsafe | Multiple threads write same variable at same time |
# | **Threads WITH Lock**        | ✔ Safe   | Threads update one-by-one                         |
# | **Normal code (no threads)** | ✔ Safe   | Only one flow, no concurrency                     |


#_________________________________________________________________________




#________________________________________________________________
EXAMPLE 5:Thread Pool (Normal Thread VS Thread Pool)
# ______________________________________________________________



# Normal Thread Code (Tea Shop)


import threading
import time

def make_tea(order_no):
    print(f"Tea {order_no} start pannuren (new worker)...")
    time.sleep(2)
    print(f"Tea {order_no} ready!")

threads = []

for i in range(1, 11):  # 10 orders
    t = threading.Thread(target=make_tea, args=(i,))
    t.start()
    threads.append(t)

# for t in threads:
    t.join()


# _________________________________________________________


# Thread Pool

Thread Pool = Set of reusable worker threads that execute multiple tasks efficiently without creating new threads every time.



# Thread Pool Code (Tea Shop)

from concurrent.futures import ThreadPoolExecutor
import time

def make_tea(order_no):

    print(f"Tea {order_no} start pannuren (pool worker)...")

    time.sleep(2)

    print(f"Tea {order_no} ready!")

    return order_no

# Create a pool of 5 workers

with ThreadPoolExecutor(max_workers=5) as pool:
    pool.map(make_tea, range(1, 11))



#CODE Explanation

Purpose: Run many tasks (10 tea orders) efficiently.
Concept: Use 5 fixed threads and reuse them for all tasks.
Code: ThreadPoolExecutor(max_workers=5) creates 5 workers; pool.map() assigns tasks.
Flow: 5 orders run first → worker frees → next order runs → continues until all 10 are done.
Output: Always 5 teas preparing at a time; all finish in batches.
Benefit: Faster, efficient, controlled threading without overload.



# Why Thread Pool is Useful? 

Thread Pool — Summary

Fast: No need to create a new thread for every task.
Efficient: Same set of threads are reused.
Easy: Simple API to manage multiple tasks.
Safe: Prevents the system from creating too many threads and crashing.


Fast → Ovoru task-kum pudhusa thread create panna time pogadhu
Efficient → Threads reuse aagum
Easy → Simple code
Safe → OS-ku overload varadhu



“Thread = worker”
“Process = company”
“Thread Pool = staff room full of ready workers”


# ______________________________________________________________
⭐ FINAL SUMMARY TABLE
# ______________________________________________________________


| Concept         | Simple Meaning                                   |
| --------------- | ------------------------------------------------ |
| Thread          | Small worker inside a program                    |
| Concurrency     | Many tasks in progress                           |
| Parallelism     | Many tasks truly running at the same time        |
| GIL             | Python allows only one thread to run Python code |
| Good for        | I/O tasks (network, file, API calls)             |
| Bad for         | CPU-heavy tasks (math, loops, processing)        |
| Race Condition  | Two threads updating shared data incorrectly     |
| Lock            | Protects shared data; prevents clashes           |
| **Thread Pool** | Reuses a fixed number of threads for many tasks  |


# ________________________________________
### 🎯 Tasks
#__________________________________________

1. Create a thread to print numbers from 1 to 10.
2. Create a thread to print squares of numbers from 1 to 5.
3. Create threads to traverse nested menu structures.
4. Create threads to download multiple files concurrently.



# ________________________________________
### 🎯 Tasks Explanation
#__________________________________________
#____________________________________________________________________
#Task 1: 1. Create a thread to print numbers from 1 to 10.
#____________________________________________________________________


import threading
import time


def print_numbers(i):
    print(f"Process_memory-I[Thread{i}(Worker)-doing ->work{i}]:")
    print(f"work loading...{i}")
    time.sleep(2)
    print(f"process_memory-I[Thread{i}(worker)-->completed work {i}]")
    

threads = []

for i in range(1, 6):
    t = threading.Thread(target=print_numbers, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Process Memory-I[ Main Thread completed].")



# When Python program starts → Python creates one main thread.
# This main thread executes all top-level code (the lines outside any function).
# It creates the worker thread t1.
# It calls t1.start() → worker thread begins.
# Then main thread waits using join().




#____________________________________________________________________
#Task 2:2. Create a thread to print squares of numbers from 1 to 5.
#____________________________________________________________________

import threading
import time


def print_square():
    print("""Process_memory-II[Square-Thread(Worker)-doing ->work]:""")
    for i in range(1, 6):
        print(f"Square of {i} is {i*i}")
        time.sleep(1)   
    print("Process_memory-II[Square-Thread(Worker)-->completed work]")

threads = []
t = threading.Thread(target=print_square)
threads.append(t)
t.start()
t.join()

print("Process Memory-II[ Main Thread completed].")

#____________________________________________________________________
#    Task 3:3.Threads to Traverse Nested Menu
#____________________________________________________________________

# import threading

menu = {
    "Food": ["Pizza", "Burger", "Pasta"],
    "Drinks": ["Coke", "Juice"],
    "Desserts": ["Ice Cream", "Cake"]
}

def traverse(category, items):
    print(f"""Process_memory-I [-Thread(Worker)-doing ->work{category}]:""")
    print(f"Work {category} Loading..... :")
    time.sleep(1)
    print(f"""Process_memory-I [-Thread(Worker)-->completed work{category} --->{menu[category]}""")

threads = []
for category, items in menu.items():
    t = threading.Thread(target=traverse, args=(category, items))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


print("All categories traversed.")    





# 1️⃣ Purpose → To process multiple menu categories faster using threads.
# 2️⃣ Concept → Each category runs in a separate thread inside the same process.
# 3️⃣ Code → Creates threads using threading.Thread() and runs traverse() function.
# 4️⃣ Flow → Main thread → creates worker threads → workers process items → join → finish.
# 5️⃣ Output → Each category prints “loading + completed” messages in parallel.
# 6️⃣ Benefit → Saves time by doing concurrent work instead of sequential work.


#____________________________________________________________________
#    Task 4:4. Create threads to download multiple files concurrently.
#____________________________________________________________________


import threading
import time

def download_file(file_name):
    print(f"Starting download → {file_name}")
    time.sleep(2)   # simulate a download
    print(f"Completed download → {file_name}")

files = ["file1.pdf", "file2.jpg", "file3.mp4", "file4.zip"]

threads = []

# Create a thread for each file
for f in files:
    t = threading.Thread(target=download_file, args=(f,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("📥 All files downloaded.")




#_____________END_____________________________




