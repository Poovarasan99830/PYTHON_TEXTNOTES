 **Python Threading/Multithreading lesson structure** 




---_____________________________________________________________________________
  → Definition 
  → Real-time example with code
  → Tasks 
  → Task Explanation 
  → Where Used 
  → Levels (Beginner, Intermediate, Advanced, General)**. 



---_____________________________________________________________________________

# 🔹 1. **Threading / Multithreading in Python**

---

### ✅ Definition

**Threading** in Python means running multiple tasks **concurrently** within the same process.

**Multithreading** allows multiple threads to run at the same time, improving efficiency for tasks that can run **independently**.

**Key points:**

* **Thread:** Smallest unit of execution inside a program.

* **Multithreading:** Multiple threads running **concurrently** in the same program.

* Useful for **I/O-bound tasks** (file read/write, network calls, menus traversal).

---


---_____________________________________________________________________________

### 🔹 Real-Time Example

1. **Flipkart Product Categories:**
   Loading Electronics, Mobiles, Laptops, and Clothing categories **simultaneously** instead of sequentially.

2. **Zomato / Swiggy Menu:**
   Fetching South Indian, North Indian, Chinese dishes **concurrently** for faster display.

3. **File Explorer:**
   Searching multiple folders at the same time using threads instead of opening one folder after another.





---_____________________________________________________________________________

### 🔹 Fun / Interesting Examples Before Tasks

1. **Coffee Shop Analogy (Parallel Tasks):**
   Imagine a coffee shop where the barista, cashier, and waiter all work **simultaneously**.

   * Barista prepares coffee → takes 2 mins
   * Cashier takes orders → takes 1 min
   * Waiter serves customers → takes 3 mins

   If done **sequentially**, the first customer waits 6 minutes.

   With **threads**, all tasks happen concurrently → the customer gets served faster.

   ✅ This is exactly how **multithreading** helps programs run multiple independent tasks at the same time.

---_____________________________________________________________________________


2. **Social Media Feed Loading:**
   When you open Facebook or Instagram, multiple feeds (posts, stories, notifications) load **simultaneously**.

   * Each feed is a separate **thread**, so you don’t have to wait for one feed to load before seeing the next.

   ✅ Multithreading makes apps **responsive and faster**, just like real-life apps.

---_____________________________________________________________________________


3. **Restaurant Menu Example:**
   Imagine Zomato wants to show South Indian, North Indian, Chinese menus **at the same time**.

   * Without threads: Menus load one by one → takes more time.
   * With threads: Each cuisine loads in a separate thread → menus appear **simultaneously** for the user.

---

4. **File Download Manager:**
   Downloading 5 large files sequentially takes 10 minutes.
   Using **threads**, all files download concurrently → overall time reduced drastically.





import threading
import time
import random

# ---------------------------
# FUN / INTERESTING EXAMPLES BEFORE TASKS
# ---------------------------

# 1️⃣ Coffee Shop Analogy
def barista():
    print("[Barista] Preparing coffee...")
    time.sleep(2)
    print("[Barista] Coffee ready!")

def cashier():
    print("[Cashier] Taking orders...")
    time.sleep(1)
    print("[Cashier] Order taken!")

def waiter():
    print("[Waiter] Serving customers...")
    time.sleep(3)
    print("[Waiter] Customers served!")

print("\n--- Coffee Shop Demo ---\n")
t1 = threading.Thread(target=barista)
t2 = threading.Thread(target=cashier)
t3 = threading.Thread(target=waiter)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("\nAll tasks done concurrently in the coffee shop!\n")

# ---------------------------
# 2️⃣ Social Media Feed Loading
def load_posts():
    print("[Feed] Loading posts...")
    time.sleep(random.uniform(1, 2))
    print("[Feed] Posts loaded!")

def load_stories():
    print("[Stories] Loading stories...")
    time.sleep(random.uniform(0.5, 1.5))
    print("[Stories] Stories loaded!")

def load_notifications():
    print("[Notifications] Loading notifications...")
    time.sleep(random.uniform(0.3, 1))
    print("[Notifications] Loaded!")

print("\n--- Social Media Feed Demo ---\n")
threads = []
for func in [load_posts, load_stories, load_notifications]:
    t = threading.Thread(target=func)
    t.start()
    threads.append(t)
for t in threads:
    t.join()

print("\nAll social media feeds loaded concurrently!\n")

# ---------------------------
# 3️⃣ Restaurant Menu Loading
def load_cuisine(cuisine):
    print(f"[Menu] Loading {cuisine} menu...")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"[Menu] {cuisine} menu loaded!")

print("\n--- Restaurant Menu Demo ---\n")
cuisines = ["South Indian", "North Indian", "Chinese"]
threads = []
for c in cuisines:
    t = threading.Thread(target=load_cuisine, args=(c,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()

print("\nAll cuisines loaded concurrently!\n")

# ---------------------------
# 4️⃣ File Download Manager Demo
def download_file(file_name):
    print(f"[Download] {file_name} started...")
    time.sleep(random.uniform(1, 3))
    print(f"[Download] {file_name} completed!")

print("\n--- File Download Demo ---\n")
files = ["File1.zip", "File2.zip", "File3.zip"]
threads = []
for f in files:
    t = threading.Thread(target=download_file, args=(f,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()

print("\nAll files downloaded concurrently!\n")



✅ Features of this Demo Code

Coffee Shop Demo: Barista, cashier, and waiter work concurrently.

Social Media Feed Demo: Posts, stories, and notifications load simultaneously.

Restaurant Menu Demo: Multiple cuisines loaded in parallel threads.

File Download Demo: Multiple files downloading at the same tim

---_____________________________________________________________________________




### 🎯 Tasks

1. Create a thread to print numbers from 1 to 10.
2. Create a thread to print squares of numbers from 1 to 5.
3. Create threads to traverse nested menu structures.
4. Create threads to download multiple files concurrently.
5. Create threads to process multiple JSON objects at the same time.

---_____________________________________________________________________________


### 🔹 Task Explanation

| Task            | Explanation                                                |
| --------------- | ---------------------------------------------------------- |
| Print numbers   | Each thread prints numbers independently.                  |
| Print squares   | Thread computes squares in parallel.                       |
| Menu traversal  | Each branch of the menu runs in a separate thread.         |
| Download files  | Threads allow simultaneous download of multiple files.     |
| JSON processing | Each JSON object processed by a separate thread for speed. |

---_____________________________________________________________________________


### 🔹 Where Used

* **Flipkart:** Product categories → Electronics → Mobiles → Smartphones → Brands
* **Zomato/Swiggy:** Food categories → Cuisines → South Indian → Idli → Variants
* **File Explorer:** Nested folders searched concurrently
* **Web Crawlers:** Crawling multiple URLs at the same time
* **Network Requests:** Fetching data from multiple APIs concurrently

➡️ Real life: **Tree structures, menus, folder search, network requests, or any independent tasks** that can be performed simultaneously.

---_____________________________________________________________________________


### 🔹 Beginner Level

1. Print numbers from 1 to 10 using threads.
2. Print squares of numbers from 1 to N using threads.
3. Print even and odd numbers using separate threads.
4. Fetch multiple URLs using threads (simple simulation with `time.sleep()`).

---

### 🔹 Intermediate Level

5. Traverse a nested menu structure using threads for each branch.
6. Read multiple files concurrently using threads.
7. Count total files in multiple folders simultaneously.
8. Process multiple JSON objects concurrently.
9. Simulate multiple bank transactions using threads.

---

### 🔹 Advanced Level

10. Download multiple large files concurrently with progress tracking.
11. Web scraping multiple pages using threads.
12. Implement producer-consumer problem using threads and queues.
13. Real-time stock price monitoring using threads for multiple stocks.
14. Thread-safe logging system for multiple threads writing to the same file.

---

### 🔹 General Real-Life Task

1. Load product categories in an e-commerce website concurrently.
2. Process multiple user requests in web servers simultaneously.
3. Perform background tasks (sending emails, notifications) using threads.
4. Concurrently check the status of multiple IoT devices.
5. Real-time game event handling (multiple players/events concurrently).

---_____________________________________________________________________________







# 🔹 **GIL (Global Interpreter Lock) – English Explanation**



# _______________________________________________________________________

### ✅ 1. **What is GIL?**

* **GIL** = Global Interpreter Lock
* In Python (CPython), there is a **mutex/lock**.
* It ensures that **only one thread can execute Python bytecode at a time**.

**Example:**

> Imagine a classroom with 10 students (threads), but **only one student can write on the board at a time**. The other students must wait.






# _______________________________________________________________________

### ✅ 3. **Effect of GIL on Multithreading**

#### a) **I/O-bound tasks**

* Tasks like file read/write, network requests, database queries.
* Threads spend most of the time **waiting**, so GIL has **minimal impact**.

```python
import threading, time

def fetch_data(n):
    print(f"Thread {n} start")
    time.sleep(2)  # Simulate I/O wait
    print(f"Thread {n} done")

threads = [threading.Thread(target=fetch_data, args=(i,)) for i in range(3)]
for t in threads: t.start()
for t in threads: t.join()
```

**Explanation:**

* Threads overlap while waiting, reducing total execution time.

---

#### b) **CPU-bound tasks**

* Tasks like math calculations, heavy loops, image processing.
* Threads **cannot run Python code truly in parallel** because of the GIL.
* Multi-core CPU usage is **limited**.

```python
import threading

def count(n):
    for i in range(n):
        pass

threads = [threading.Thread(target=count, args=(10000000,)) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
```

**Explanation:**

> 4 threads exist, but **Python executes them one by one** due to the GIL. Multi-core CPU cannot be fully utilized.




# _______________________________________________________________________

1️⃣ GIL is automatic

     In CPython (the standard Python implementation), the GIL is always there by default.
     You cannot manually “activate” or “deactivate” it in regular Python code.
     Every Python process using threads runs under the GIL automatically.

2️⃣ What it affects

     CPU-bound threads: Only one thread executes Python bytecode at a time because of GIL → no true parallelism.

     I/O-bound threads: Threads can still appear to run concurrently because GIL is released during I/O operations.

3️⃣ When you create multithreading

      You just create threads using threading.Thread() → GIL is automatically in effect.
      You don’t need to do anything manually.





# ___________________________________________________________________________________________________



### **I/O-bound threads and the GIL**

1. **GIL normally:**

   * Python allows **only one thread to run Python code at a time** because of the Global Interpreter Lock (GIL).
   * This blocks multiple threads from running CPU-bound tasks simultaneously.

2. **I/O operations:**

   * I/O tasks like `time.sleep()`, file read/write, or network calls **don’t need the CPU** while waiting.
   * Python **automatically releases the GIL** when a thread is waiting for I/O.

3. **Effect:**

   * While one thread is waiting (sleeping or reading a file), **another thread can acquire the GIL and run Python code**.
   * This allows multiple I/O-bound threads to run **concurrently**, even in Python with GIL.

---

### **Analogy**

* Imagine a single cashier (GIL) in a shop.
* CPU-bound tasks → customer needs help immediately → cashier busy → others wait.
* I/O-bound tasks → customer waits for delivery (sleep/network) → cashier is free → next customer can be served.

---

So, **the key point:**

> Python **releases the GIL automatically during I/O waits**, letting other threads run. This is why threading helps I/O-bound tasks.

---

If you want, I can make a **tiny timing diagram showing GIL release during I/O**—it will make it very clear visually.




# _______________________________________________________________________


1️⃣ GIL vs threading.Lock()

         GIL (Global Interpreter Lock) only prevents multiple Python bytecodes from executing at the exact same time in CPython.

         GIL does NOT protect shared data from race conditions.

         Example: Two threads updating a shared list or variable simultaneously.

         Even with GIL, operations that are not atomic (like x += 1) can get interrupted between bytecodes.

         threading.Lock() is a manual way to protect critical sections.

         Ensures that only one thread at a time can execute that block of code.



# ___________________________________________


### 2️⃣ Example

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        # Without lock: race condition possible
        # With lock: thread-safe
        with lock:
            counter += 1

threads = []
for i in range(2):
    t = threading.Thread(target=increment)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(counter)  # Always 200000 with lock, may be less without
```

* Even though **GIL exists**, `counter += 1` is **not atomic**.
* Without `Lock`, threads can **read-modify-write simultaneously**, causing wrong results.

---

### 3️⃣ Key points

* **GIL**: prevents true parallel execution of Python bytecode.
* **Lock**: prevents **race conditions on shared resources**.
* CPU-bound threads still need locks if they share data.
* I/O-bound threads also need locks if they modify shared data.

---

💡 **Rule of Thumb:**

* Use `Lock` anytime **multiple threads share mutable data**.
* Don’t rely on GIL for thread safety.



# ___________________________________________


##total=0
##lock=threading.Lock()
##def add_amount():
##    global total
##    for i in range(5):
##        lock.acquire()
##        total=total+1
##        lock.release()
##
##   
##emty=[]
##for i in range(2):
##    data=threading.Thread(target=add_amount)
##    emty.append(data)
##    data.start()
##   
##for i in emty:
##    i.join()

##    

##print(total)
# _______________________________________________________________________


### ✅ 2. **Why Python has GIL?**

* Makes **memory management simpler**.
* Prevents **race conditions** (when multiple threads modify data simultaneously).
* Python objects (like lists, dictionaries) become **thread-safe** without extra locks.

**Analogy:**

> If two students write in the same notebook at the same time, content may get mixed up.

> GIL ensures that **one student finishes writing before the next one starts**.

-






# ____________________________________________________________________________




### ✅ 4. **Workarounds / Solutions**

1. **Multiprocessing**

   * Each process has its **own Python interpreter**, so GIL is **not shared**.
   * CPU-heavy tasks run in **parallel**.

```python
from multiprocessing import Process

def count(n):
    for i in range(n):
        pass

processes = [Process(target=count, args=(10000000,)) for _ in range(4)]
for p in processes: p.start()
for p in processes: p.join()
```

2. **C extensions / NumPy**

   * Native code can **release the GIL**, allowing heavy computations to run faster.

---

### ✅ 5. **Summary Table**

| Topic        | Explanation                                                              |
| ------------ | ------------------------------------------------------------------------ |
| GIL          | A **lock** that allows only one thread to run Python bytecode at a time. |
| Advantage    | Safe memory management, avoids race conditions.                          |
| Disadvantage | CPU-bound multithreading is slow.                                        |
| I/O-bound    | Threads overlap during waiting → improves performance.                   |
| CPU-bound    | Threads run sequentially → multi-core CPU not fully utilized.            |
| Solution     | Use **multiprocessing** or **C extensions** for CPU-heavy tasks.         |

---

### 🔹 Key Takeaway

> GIL is like a **security guard** for Python memory. Threads are safe, but CPU-heavy tasks are slow.
> For **I/O-bound tasks**, multithreading works well. For **CPU-bound tasks**, use **multiprocessing** to fully utilize multiple cores.







### ✅ **Race Condition**

* A **race condition** occurs when **two or more threads try to modify the same data simultaneously**.
* The result becomes **unpredictable** — sometimes correct, sometimes wrong.
* In Python, using **GIL** and **locks** can help **avoid race conditions**.



### ✅ **Default Thread Safety in Python**

* Python’s **GIL** makes **simple operations thread-safe**.
* By default, **race conditions are rare** for small operations.
* **However**, for **complex operations or multiple-step processes**, race conditions **can still occur**, and using **locks is necessary**.


### ✅ **Threads vs Multiprocessing**

* **Threads** → Shared memory → Race condition **possible** → Need **locks**.
* **Multiprocessing** → Separate memory → **No race condition by default**.
* Only when using **shared objects in multiprocessing** (like `Value`, `Array`, or `Manager`) do you need **locks** to avoid race conditions.





# ____________________________________________________________________________________

Race condition apadina, **two or more threads simultaneously same data modify pannumbothu problem varuthu**.
Result unpredictable-a irukkum — sometimes correct, sometimes wrong.
Python la GIL & locks use pannina, race condition avoid panna mudiyum.

Python la **GIL simple operations-ku thread-safe**, default-a **race condition rare-a varum**.
> But **complex operations / multiple steps** la **race condition varum**, adhukku **Locks use panrathu necessary**.

Threads → shared memory → race condition possible → need **locks**.
> Multiprocessing → separate memory → **no race condition by default**.
> Only when using **shared objects in multiprocessing**, **Locks are needed**.

# __________________________________________________________________________________________

















# 🔹 **Race Condition – Tanglish Explanation**

---

### ✅ 1. **What is a Race Condition?**

* Race condition apadina, **two or more threads simultaneously same data modify pannumbothu problem varuthu**.
* Result unpredictable-a irukkum — sometimes correct, sometimes wrong.

---

### ✅ 2. **Tanglish Analogy**

> Imagine rendu students oru **single notebook la marks update panra**.
>
> * Student 1: +10 marks
> * Student 2: +20 marks
>
> If both write at the same time without waiting → final marks **wrong-a update aagum**.

**Race condition problem = threads “fight” panra situation to access same resource.**

---

### ✅ 3. **Python Example (Without Lock / Race Condition)**

```python
import threading

total = 0

def add_amount():
    global total
    for _ in range(100000):
        total += 1  # multiple threads access same variable

threads = [threading.Thread(target=add_amount) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()

print("Total =", total)
```

**Explanation:**

* Expected total = 200000
* Sometimes total < 200000 → because **threads access total at the same time**.
* This is **race condition**.

---

### ✅ 4. **How to Avoid Race Condition in Python**

* Use **Locks** (`threading.Lock()`) to **allow only one thread to access resource at a time**.

```python
import threading

total = 0
lock = threading.Lock()

def add_amount():
    global total
    for _ in range(100000):
        lock.acquire()
        total += 1
        lock.release()

threads = [threading.Thread(target=add_amount) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()

print("Total =", total)
```

**Explanation:**

* Lock ensures **one thread at a time** can modify `total`.
* Total will always = 200000 → no race condition.

---

### ✅ 5. **Tanglish Takeaway**

> Race condition = **threads or processes oru same resource me simultaneous access panra problem**.
> Python la GIL & locks use pannina, race condition avoid panna mudiyum.







### ✅ 1. **Race Condition Default-a Python la?**

* Python la **GIL (Global Interpreter Lock)** irukkum — **single thread Python code execute panrathu guarantee pannum**.
* Adhunaala, **simple Python objects like integers, lists, dicts default-a thread-safe** irukku **small operations** ku.

**Tanglish:**

> Simple-a, `x += 1` or list append panradhula race condition **rare-a varum** because **GIL one thread-ku lock pannuthu**.

---

### ✅ 2. **But Complex Operations / Multiple Steps**

* Race condition **still varum** if **one operation multiple steps involve pannuthu**.
* Eg: check-then-update, loops, multiple variables update, read-modify-write.

**Example:**

```python
import threading

counter = 0

def increment():
    global counter
    temp = counter      # Step 1: Read
    temp += 1           # Step 2: Modify
    counter = temp      # Step 3: Write

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()

print("Counter =", counter)
```

* Expected = 2
* Sometimes counter = 1 → **because two threads read & modify at same time**.

---

### ✅ 3. **Solution**

* Use **Locks** (`threading.Lock()`) for multiple-step operations.

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    lock.acquire()
    counter += 1
    lock.release()

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()

print("Counter =", counter)
```

* Now counter = 2 → **race condition avoid aaguthu**.

---

### ✅ 4. **Tanglish Takeaway**

> Python la **GIL simple operations-ku thread-safe**, default-a **race condition rare-a varum**.
> But **complex operations / multiple steps** la **race condition varum**, adhukku **Locks use panrathu necessary**.




Ah! Seri 😎, let me explain clearly. You’re asking:

*"If we use **multiprocessing**, tasks run truly in parallel, so why don’t we get race condition errors like threads?"*

---

### 1️⃣ **Threads vs Processes – Key Difference**

| Feature        | Thread                                                   | Process (Multiprocessing)                                  |
| -------------- | -------------------------------------------------------- | ---------------------------------------------------------- |
| Memory         | Shared memory (same variables, objects)                  | Separate memory space (each process has own copy)          |
| GIL            | Yes → only one thread executes Python bytecode at a time | GIL not shared → true parallel execution possible          |
| Race Condition | Can occur if multiple threads modify same object         | Rare for separate processes (memory not shared by default) |

---

### 2️⃣ **Why Multiprocessing Avoids Race Condition by Default**

* In **multiprocessing**, each process has its **own memory space**.
* They do **not share Python objects** automatically.
* So, **modifying a variable in one process does not affect another process** → no race condition happens by default.

**Example:**

```python
from multiprocessing import Process

counter = 0

def increment():
    global counter
    for _ in range(1000):
        counter += 1  # Each process modifies its own copy

processes = [Process(target=increment) for _ in range(2)]
for p in processes: p.start()
for p in processes: p.join()

print("Counter =", counter)
```

* Output = 0 (or 1000 in one process) → **processes did not share `counter`**.
* No race condition on shared memory because memory **is not shared**.

---

### 3️⃣ **When Race Condition Can Happen in Multiprocessing**

* If you **explicitly share memory** between processes using:

  * `multiprocessing.Value`
  * `multiprocessing.Array`
  * `Manager` objects

Then **race condition is possible**, and you need **Locks**.

**Example:**

```python
from multiprocessing import Process, Value, Lock

counter = Value('i', 0)
lock = Lock()

def increment():
    for _ in range(1000):
        lock.acquire()
        counter.value += 1
        lock.release()

processes = [Process(target=increment) for _ in range(2)]
for p in processes: p.start()
for p in processes: p.join()

print("Counter =", counter.value)
```

* Here, `Lock` ensures **safe increment** → race condition avoided even with true parallel processes.

---

### 4️⃣ **Tanglish Takeaway**

> Threads → shared memory → race condition possible → need **locks**.
> Multiprocessing → separate memory → **no race condition by default**.
> Only when using **shared objects in multiprocessing**, **Locks are needed**.

---





Ah bro, super question 🔥 Let’s break it down **Thunglish style** 😎

---

### 🟢 GIL = Global Interpreter Lock

* Python (CPython) ல் ஒரு **single lock** இருக்குது called **GIL**.
* GIL ஒரு நேரத்தில் **one thread மட்டும் Python bytecode execute பண்ணுறதுக்கு** allow பண்ணும்.
* அதனால multi-threading-ல் **CPU-bound tasks** (heavy calculations, loops, math operations) **parallel-ஆ run ஆகல**.

---

### 🟢 Example:

```python
import threading, time

def cpu_task(n):
    x = 0
    for i in range(10_000_000):
        x += i
    print(f"Done {n}")

threads = [threading.Thread(target=cpu_task, args=(i,)) for i in range(4)]
start = time.time()
for t in threads: t.start()
for t in threads: t.join()
print(time.time() - start)
```

* Even 4 threads, **execution time ≈ single thread**.
* GIL block பண்ணுது, because Python bytecode **only one thread at a time** execute பண்ணலாம்.

---

### 🟢 But I/O-bound tasks (file/network/sleep)

```python
import threading, time

def io_task(n):
    time.sleep(2)
    print(f"Done {n}")

threads = [threading.Thread(target=io_task, args=(i,)) for i in range(4)]
start = time.time()
for t in threads: t.start()
for t in threads: t.join()
print(time.time() - start)
```

* Here **threads mostly waiting** (`sleep` or network).
* GIL free ஆகுது **waiting time 동안** → next thread run ஆகுது.
* Total time much less than sequential.

---

### 🟢 Summary (Thunglish)

| Task Type | GIL Effect               | Result with Threading            |
| --------- | ------------------------ | -------------------------------- |
| CPU-bound | Threads block each other | No real speedup (parallel fails) |
| I/O-bound | GIL released during wait | Speedup ✅, tasks overlap         |

---

### 🔹 Simple analogy:

* CPU-bound → One person writing numbers on paper, even if 4 people available, GIL says **only one pen at a time** → slow.
* I/O-bound → People mostly waiting for paper/ink → others can write meanwhile → faster.

---

Bro, நீங்க வேண்டுமா நான் ஒரு **diagram** prepare பண்ணி **CPU-bound vs I/O-bound with GIL timing** காட்டுற மாதிரி குடுக்க? It will make things very clear visually.
