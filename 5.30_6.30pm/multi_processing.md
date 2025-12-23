

# ____________________________________________

# **MULTIPROCESSING — PYTHON**

# ____________________________________________

* Multiprocessing → **True Parallelism** (multiple CPUs working at same time)
* Bypasses GIL → Each process has **its own Python interpreter**
* Best for **CPU-heavy tasks** (math, ML, image processing, video encoding)

---

# ____________________________________________

# **Multiprocessing vs Multithreading (Quick Recap)**

# ____________________________________________

| Concept             | Meaning                                                         |
| ------------------- | --------------------------------------------------------------- |
| **Multithreading**  | Many threads inside **same memory**, GIL blocks CPU parallelism |

| **Multiprocessing** | Many **processes**, separate memory, true multi-core execution  |

| **Async**           | Single-thread, event-loop, for non-blocking I/O                 |
| **GIL**             | Allows only one thread to run Python bytecode                   |

---

### **Real Example in Tanglish**

* Multithreading → *Oru staff 5 subjects handle panna try pannra* (fast-aa handles but one body)
* Multiprocessing → *5 staff 5 subjects teach pannra* (real parallel)

---

# ____________________________________________

# **MULTIPROCESSING**

# ____________________________________________

→ Definition
→ Real-time example
→ N number Examples
→ Tasks
→ Task Explanation
→ Advanced Concepts
→ Where Used
→ Levels (Beginner, Intermediate, Advanced, General)

---

# ____________________________________________

# **→ Definition**

# ____________________________________________

### ✅ **Definition**

**Multiprocessing** means running multiple **processes** at the same time.
Each process has:

✔ Its **own memory space**
✔ Its **own Python interpreter**
✔ Its **own GIL** (so GIL is bypassed)

That's why multiprocessing gives **TRUE parallel CPU execution**.

---

### ✔ Best for:

* CPU-heavy tasks
* Image processing
* Video rendering
* Machine learning
* Numerical computation
* Large loops, heavy math
* Data science workloads

---

### ✔ Key Functions

| Function      | Meaning                      |
| ------------- | ---------------------------- |
| `Process()`   | Creates a new process        |
| `.start()`    | Starts process execution     |
| `.join()`     | Wait until process finishes  |
| `Pool()`      | Creates worker process pool  |
| `cpu_count()` | How many CPU cores available |

---

# ____________________________________________

# **→ Real-time examples**

# ____________________________________________

### 1. **Instagram Filters Processing**

One filter = one CPU-core
Multiple filters processed **in parallel**.



### 2. **TikTok Video Compression**

Each video compressed by different process.

### 3. **Flipkart Price Engine**

Multiple sellers price calculation = parallel compute.

### 4. **Face Recognition / Image Classification**

Each image assigned to a process.

---

# ____________________________________________

# **N NUMBER OF EXAMPLES**

# ____________________________________________



# ____________________________________________
# ✅ **Example 1 — Thread vs Multiprocessing (TIME–BASED DIFFERENCE)**

# ____________________________________________






*(Super clear benchmark example)*

## 🎯 **Task:**

CPU heavy calculation – sum of squares from 1 to 50 million.

## ⚡ Normal Threading Version

👉 Threads share the same CPU core
👉 **GIL blocks true parallel execution**
👉 So threads run **one-by-one** → **slow**

### **Thread Code**

```python



import threading
import time

def cpu_work():
    total = 0
    for i in range(50_000_00):
        total += i*i

start = time.time()

t1 = threading.Thread(target=cpu_work)
t2 = threading.Thread(target=cpu_work)

t1.start()
t2.start()

t1.join()
t2.join()

print("Thread time:", time.time() - start)
```

### ⏱ **Typical Output**

```
Thread time: 8.5 seconds
```

**WHY SLOW?**
✔ GIL → only one thread can execute Python bytecode at a time
✔ Two threads = still one core usage
✔ CPU 50% wasted

---

## ⚡ Multiprocessing Version

👉 Each process has **its own Python interpreter**
👉 **No GIL between processes**
👉 OS gives **each process a CPU core**
👉 Runs **true parallel** → **much faster**
# ✅ **WITH MULTIPROCESSING — FAST**

```python

import multiprocessing
import time



def cpu_work():
    total = 0
    for i in range(50_000_00):
        total += i*i
    print(total)



if __name__ == "__main__":

    start = time.time()

    p1 = multiprocessing.Process(target=cpu_work)
    p2 = multiprocessing.Process(target=cpu_work)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Process time:", time.time() - start)





# ____________________________________________

# EXAMPLE 2 → Class-based Multiprocessing

# ____________________________________________

```python
from multiprocessing import Process
import time, random

class PriceEngine:
    def calculate(self, seller):
        print(f"{seller} → calculating price...")
        time.sleep(2)
        print(f"{seller} → Price: {random.randint(200, 500)}")

    def start_task(self, seller):
        p = Process(target=self.calculate, args=(seller,))
        p.start()
        return p

engine = PriceEngine()

tasks = [
    engine.start_task("Seller A"),
    engine.start_task("Seller B"),
    engine.start_task("Seller C"),
]

for t in tasks:
    t.join()
```

✔ All sellers processed in **parallel**
✔ Total time = **2 sec**, not 6 sec
✔ Multithreading la GIL block pannum
✔ Multiprocessing la GIL problem **illai**

---

# ____________________________________________

# EXAMPLE 3 → CPU Core Utilization

# ____________________________________________

```python
from multiprocessing import cpu_count

print("Total CPU Cores =", cpu_count())
```

8 core CPU = 8 processes parallel
16 core CPU = 16 processes parallel

---

# ____________________________________________

# EXAMPLE 4 → Multiprocessing Pool

# ____________________________________________

Pool = Fixed set of worker processes
Faster, cleaner, scalable.

```python
from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == "__main__":
    with Pool(processes=4) as p:
        result = p.map(square, [1,2,3,4,5,6,7,8])
        print(result)
```

✔ 4 workers execute jobs
✔ Efficient scheduling
✔ Automatically manages processes

---

# ____________________________________________

# EXAMPLE 5 → Real CPU-heavy program

# ____________________________________________

```python
from multiprocessing import Pool
import math

def compute_factorial(n):
    return math.factorial(n)

numbers = [50000, 60000, 70000, 80000]

if __name__ == "__main__":
    with Pool() as pool:
        result = pool.map(compute_factorial, numbers)
        print("Done")
```

✔ Each factorial calculation → different CPU core
✔ HUGE performance boost

---

# ____________________________________________

# → ADVANCED CONCEPTS

# ____________________________________________



### ✔ GIL Bypass

Each process has its own interpreter → GIL does NOT block.

### ✔ Process vs Thread

| Concept      | Thread    | Process  |
| ------------ | --------- | -------- |
| Memory       | Shared    | Separate |
| Safety       | Less      | High     |
| Overhead     | Low       | High     |
| CPU Parallel | ❌ Limited | ✔ True   |
| GIL          | Blocks    | No block |

---

### ✔ Inter-process Communication (IPC)

1. `Queue`
2. `Pipe`
3. `Manager`

Avoids shared memory issues.

---

### ✔ Daemon Processes

```python
p.daemon = True
```

Used for background tasks.

---

# ____________________________________________

# WHERE USED?

# ____________________________________________

✔ Video processing
✔ AI / ML training
✔ Scientific computing
✔ Cryptography
✔ Image resizing
✔ Billing engines
✔ Price calculation
✔ Data science pipelines
✔ CPU simulation
✔ Automated testing




# ____________________________________________

# TASKS

# ____________________________________________

1️⃣ Create 4 processes to compute squares
2️⃣ Use Pool to process 1–20 numbers
3️⃣ Use multiprocessing to compress 5 images


# ____________________________________________

# TASK EXPLANATIONS

# ____________________________________________

---

# ____________________________________________
# Task 1 → Process to compute squares
# ____________________________________________




```python
from multiprocessing import Process
import time

def square(n):
    print(f"Process {n} → Square = {n*n}")

processes = []
for i in range(1, 6):
    p = Process(target=square, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

print("Main Process completed.")
```



# CODE Explanation

**Purpose:** Run multiple square calculations in parallel across different CPU cores.
**Concept:** Each process has its own memory and its own GIL, allowing true parallel execution without interference.
**Code:** The program creates five Process objects, starts each one, and then waits for all of them using join().
**Flow:** Process 1 runs → Process 2 runs → Process 3, 4, 5 run (all simultaneously on different cores).
**Output:** Five separate square results printed, possibly in different orders because processes execute independently.
**Benefit:** Provides real parallelism for CPU-heavy tasks and avoids GIL limitations completely.


# ____________________________________________
# Task 2 → Pool to compute squares
# ____________________________________________




```python
from multiprocessing import Pool

def square(n):
    return n*n

if __name__ == "__main__":
    with Pool(4) as p:
        print(p.map(square, range(1, 11)))
```




# CODE Explanation

**Purpose:** Run multiple square computations in parallel using a worker pool.
**Concept:** A Pool creates a fixed number of processes, and each process executes tasks independently in true parallelism.
**Code:** Pool(4) creates 4 worker processes, and map() distributes the numbers 1–10 across these workers.
**Flow:** Worker 1, 2, 3, 4 compute squares → tasks finish → results are collected in order.
**Output:** A final list printed as `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`, always in order even though execution was parallel.
**Benefit:** Simplifies parallel processing by automatically managing workers, task distribution, and result collection.



# ____________________________________________
# Task 3 → Use Multiprocessing to Compress 5 Images
# ___________________________________________


```python

from multiprocessing import Pool
from PIL import Image
import os

# Image compression function
def compress_image(image_path):
    img = Image.open(image_path)
    filename = os.path.basename(image_path)
    output_path = f"compressed_{filename}"

    img.save(output_path, optimize=True, quality=40)   # Compress
    return f"{filename} → compressed!"

if __name__ == "__main__":
    images = [
        "img1.jpg",
        "img2.jpg",
        "img3.jpg",
        "img4.jpg",
        "img5.jpg"
    ]

    with Pool(processes=4) as pool:
        results = pool.map(compress_image, images)

    print("\n".join(results))




```
### CODE Explanation **

**Purpose:** Compress multiple images faster using parallel processing.
**Concept:** Each image is processed by a different process, achieving true parallelism.
**Code:** Pool(4) creates 4 workers, and map() distributes the 5 image compression tasks.
**Flow:** Worker 1 compresses img1 → Worker 2 compresses img2 → Worker 3 and 4 run simultaneously → last image waits for a free worker.
**Output:** Five compressed image files saved with names like `compressed_img1.jpg`.
**Benefit:** Greatly speeds up image processing by using all CPU cores efficiently.

---



# ____________________________________________
# Task 4 → Inter-process communication via Queue
# ____________________________________________





```python
from multiprocessing import Process, Queue

def worker(q, value):
    q.put(value * 2)

if __name__ == "__main__":
    q = Queue()
    p = Process(target=worker, args=(q, 10))
    p.start()
    p.join()
    print("Result:", q.get())
```

---


# CODE Explanation


**Purpose:** Send data from a child process back to the main process safely.
**Concept:** A Queue enables inter-process communication (IPC) because processes do not share memory.
**Code:** The main process creates a Queue, starts a worker process, and the worker uses q.put() to send back a computed value.
**Flow:** Worker receives value → doubles it → puts result into Queue → main process waits (join) → retrieves result with q.get().
**Output:** The main process prints: `Result: 20`.
**Benefit:** Allows clean, safe, and structured data transfer between processes without shared-memory issues.


# ____________________________________________

# FINAL SUMMARY TABLE

# ____________________________________________

| Topic           | Meaning                         |
| --------------- | ------------------------------- |
| Multiprocessing | True parallel execution         |
| Threading       | Concurrency only                |
| Async           | Non-blocking, single-thread     |
| CPU tasks       | Best with multiprocessing       |
| GIL             | Does NOT affect multiprocessing |
| Pool            | Reuses worker processes         |
| IPC             | Safe data sharing               |
| Process         | Separate memory                 |






# ____________________________________________

# Memory Architecture — Text (ASCII) Diagrams

# ____________________________________________

---

# ____________________________________________

## 1) Single Process — Multiple Threads (Shared Memory)
# ____________________________________________


```
                ┌───────────────────────────────────────────────┐
                │             Operating System (OS)            │
                │  (Scheduler, Kernel, assigns CPU time quanta)│
                └───────────────────────────────────────────────┘
                              ▲
                              │
                ┌───────────────────────────────────────────────┐
                │             Python Process (PID 1234)        │
                │                                               │
                │  ┌────────────┐   ┌──────────────┐           │
                │  │ Code/Text  │   │   Globals    │  <-- Shared │
                │  │ (immutable) │  │ (module vars)│   by all    │
                │  └────────────┘   └──────────────┘   threads   │
                │                                               │
                │  ┌────────────────────────────────────────┐   │
                │  │                HEAP                     │   │
                │  │   (objects, lists, dicts — all threads  │   │
                │  │    can access same objects via refs)   │   │
                │  └────────────────────────────────────────┘   │
                │                                               │
                │  ┌───────┐    ┌───────┐    ┌───────┐         │
                │  │Stack  │    │Stack  │    │Stack  │         │
                │  │Thread1│    │Thread2│    │Thread3│  <--   │
                │  │(locals)│   │(locals)│   │(locals)│   private│
                │  └───────┘    └───────┘    └───────┘    each  │
                │                                               │
                │  ┌──────────────┐   ┌───────────────┐        │
                │  │ File Descs   │   │ Network sockets│       │
                │  └──────────────┘   └───────────────┘        │
                └───────────────────────────────────────────────┘
```


### **Key Points **

✅ A **process** has its own **heap, global variables, and code section** — and **all threads inside that process share these**.

✅ **Local variables** live in the **stack**, and each thread has **its own separate stack**, so each thread gets its own local variables.

✅  The **GIL (Global Interpreter Lock)** exists inside the **Python interpreter**, and it affects **threads** — it ensures that **only one thread runs Python bytecode at a time**.

✅  Use **threads for I/O-bound tasks**, because threads **share memory**, making communication between them **fast and efficient**.




# ____________________________________________

## 2) Multiple Processes (Separate Address Spaces)
# ____________________________________________




```
                ┌───────────────────────────────────────────────┐
                │             Operating System (OS)            │
                └───────────────────────────────────────────────┘
                 ▲                    ▲                   ▲
                 │                    │                   │
    ┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐
    │ Python Process (P1)  │ │ Python Process (P2)  │ │ Python Process (P3)  │
    │  (PID 2001)          │ │  (PID 2002)          │ │  (PID 2003)          │
    │  ┌───────────────┐   │ │  ┌───────────────┐   │ │  ┌───────────────┐   │
    │  │ Code / Globals│   │ │  │ Code / Globals│   │ │  │ Code / Globals│   │
    │  └───────────────┘   │ │  └───────────────┘   │ │  └───────────────┘   │
    │  ┌───────────────┐   │ │  ┌───────────────┐   │ │  ┌───────────────┐   │
    │  │   HEAP        │   │ │  │   HEAP        │   │ │  │   HEAP        │   │
    │  │ (objects owned)│  │ │  │ (objects owned)│  │ │  │ (objects owned)│  │
    │  └───────────────┘   │ │  └───────────────┘   │ │  └───────────────┘   │
    │  ┌───────┐           │ │  ┌───────┐           │ │  ┌───────┐           │
    │  │Stack  │           │ │  │Stack  │           │ │  │Stack  │           │
    │  └───────┘           │ │  └───────┘           │ │  └───────┘           │
    └──────────────────────┘ └──────────────────────┘ └──────────────────────┘


### **Key Points**

✅ **Processes have completely separate memory spaces** — their heaps and global variables are **not shared**.

✅ To communicate between processes, you must use **IPC mechanisms** such as **Queue, Pipe, SharedMemory, or Manager**.

✅ The **GIL exists inside each process**, but because each process has its **own interpreter**, the GIL does **not stop true parallel CPU execution** — the OS can run different processes on different CPU cores.

✅* Processes are **heavier** and have more **startup overhead**, but they provide **real parallelism** for CPU-bound work.


# ____________________________End________________________________