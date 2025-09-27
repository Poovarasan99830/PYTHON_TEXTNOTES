
# `multiprocessing`


2️⃣ `multiprocessing` (For CPU-bound tasks, fully utilizes multiple cores)**
     - Uses **multiple processes**, each with **its own memory space**.
     - **Bypasses the GIL**, allowing true **parallel execution** across CPU cores.
     - Best for **CPU-heavy computations** (ML, image processing, data processing).
     - More memory overhead since each process **has its own copy of Python objects**.




## 🔹 Real-time Example with Code

```python
from multiprocessing import Process
import time, os

def work(n):
    print(f"Process {os.getpid()} working on {n}")
    time.sleep(2)
    print(f"Done {n}")

if __name__ == "__main__":
    tasks = [Process(target=work, args=(i,)) for i in range(5)]
    for t in tasks: t.start()
    for t in tasks: t.join()
    print("All done!")

# ___________________________________________________

✅ Each task runs in **parallel** → reduces total time.


## 🔹 Tasks

1. Write a program to calculate factorials of 5 numbers in parallel.
2. Use `multiprocessing.Queue` to send results back to main process.
3. Use `Pool.map()` to apply a function on a list of 100 items.

---

## 🔹 Task Explanation

| Task      | Explanation                                |
| --------- | ------------------------------------------ |
| Factorial | Each process calculates independently.     |
| Queue     | Inter-process communication (IPC).         |
| Pool Map  | Easy distribution of workload across CPUs. |

---

## 🔹 Where Used

* Data science: matrix multiplications, simulations.
* AI/ML: parallel model training.
* Image/video/audio processing.
* Large file parsing.

---

## 🔹 Levels

* **Beginner** → Process, start(), join().
* **Intermediate** → Pool, Queue, Pipe.
* **Advanced** → Shared memory, synchronization (Locks, Semaphores).
* **General** → Heavy CPU tasks.

---

## 🔹 Best Practices

* Use `if __name__ == "__main__":` (Windows requirement).
* Avoid **too many processes** → overhead increases.
* Use `Pool` for many small tasks.
* Prefer `concurrent.futures.ProcessPoolExecutor` for cleaner syntax.

---

## 🔹 Pitfalls

* Higher memory usage (each process separate).
* Communication between processes is slower than threads.
* Debugging across processes is harder.

---

## 🔹 Interview Questions

1. Difference between multiprocessing and threading?
2. How does Python overcome GIL using multiprocessing?
3. When to use Pool vs Process?
4. Explain Queue vs Pipe.

---

---____________________________________________________________________________________________________

# 🔹 **Asynchronous Programming in Python (360° View)**

---

## ✅ Definition

* Async = **concurrent execution**, not parallel.
* Uses **event loop** to schedule tasks.
* Best for **I/O-bound tasks** (waiting for DB, API, network).

---

## 🔹 Real-time Example with Code

```python
import asyncio

async def task(n):
    print(f"Start {n}")
    await asyncio.sleep(2)
    print(f"End {n}")

async def main():
    await asyncio.gather(*(task(i) for i in range(3)))

asyncio.run(main())
```

✅ Tasks run **concurrently** → total time = ~2s instead of 6s.

---

## 🔹 Tasks

1. Write an async program to simulate 3 file downloads.
2. Use `asyncio.create_task()` to schedule tasks.
3. Fetch multiple URLs using `aiohttp`.

---

## 🔹 Task Explanation

| Task          | Explanation                     |
| ------------- | ------------------------------- |
| File download | No waiting → overlap execution. |
| create_task   | Fire-and-forget scheduling.     |
| aiohttp       | Real-world async networking.    |

---

## 🔹 Where Used

* Web servers (FastAPI, aiohttp).
* Chat applications.
* Stock market live updates.
* Gaming servers.
* Real-time notifications.

---

## 🔹 Levels

* **Beginner** → async def, await, coroutines.
* **Intermediate** → asyncio.gather, asyncio.create_task.
* **Advanced** → aiohttp, async DB drivers, producer-consumer patterns.
* **General** → I/O tasks.

---

## 🔹 Best Practices

* Always use `asyncio.gather` for parallel async tasks.
* Avoid blocking code (`time.sleep`) inside async → use `await asyncio.sleep()`.
* Use `async with` for resources like DB connections.
* Mix async + multiprocessing for combined I/O + CPU tasks.

---

## 🔹 Pitfalls

* Not true parallelism (still single thread).
* Mixing blocking code breaks async flow.
* Debugging async stack traces is tricky.

---

## 🔹 Interview Questions

1. Difference between async and threading?
2. How does event loop work?
3. Can async overcome GIL? (No, only multiprocessing can).
4. When to use `asyncio.create_task` vs `await`?

---

---

# 🔹 **Multiprocessing vs Asynchronous — Side by Side**

| Feature        | Multiprocessing                      | Asynchronous                |
| -------------- | ------------------------------------ | --------------------------- |
| Nature         | Parallel execution                   | Concurrent execution        |
| Best for       | CPU-bound tasks                      | I/O-bound tasks             |
| Memory         | Each process has separate memory     | Shared single memory/thread |
| Overcomes GIL? | ✅ Yes                                | ❌ No                        |
| Example        | Image processing, ML training        | API calls, DB queries       |
| Tool           | multiprocessing, ProcessPoolExecutor | asyncio, aiohttp, FastAPI   |
| Overhead       | Heavy (process creation)             | Light (event loop)          |

---

# 🔹 General Real-life Applications

✅ **Multiprocessing**

* Data crunching in AI/ML
* Video rendering
* Big simulations (climate models, physics)

✅ **Async**

* Web APIs (FastAPI)
* Messaging apps (WhatsApp, Slack)
* IoT sensors streaming
* Live dashboards

---

⚡ **360° Summary**

* **Multiprocessing** → heavy CPU work, true parallelism, more memory.
* **Async** → lightweight, single-thread concurrency, perfect for I/O waits.
* Often combined in **real-world projects**: e.g., Web API server (async) + background ML model processing (multiprocessing).





# ____________________________________________________________________
### 🟢 Case 1: Without Multiprocessing

```python
import os, time

def work(n):
    print(f"Process {os.getpid()} working on {n}", flush=True)
    time.sleep(2)
    print(f"Done {n}", flush=True)

for i in range(3):  # direct function call
    work(i)
```

✅ **Behavior:**

* All tasks run in the **main process**, so **PID is the same**.
* Execution is **sequential**: one task completes before the next starts.
* Output is predictable:

```
Process 12345 working on 0
Done 0
Process 12345 working on 1
Done 1
Process 12345 working on 2
Done 2
```

⏱ **Time:** ~6 seconds total (2 sec × 3 tasks)
# 👉 All tasks same PID (12345) → because everything runs in main process only. 
# 👉 Tasks run one by one (sequential).
---

### 🟢 Case 2: With Multiprocessing

```python
from multiprocessing import Process
import os, time

def work(n):
    print(f"Process {os.getpid()} working on {n}", flush=True)
    time.sleep(2)
    print(f"Done {n}", flush=True)

if __name__ == "__main__":
    tasks = [Process(target=work, args=(i,)) for i in range(5)]
    print("Starting processes...")
    for t in tasks:
        t.start()

    # Wait for all processes to finish
    for t in tasks:
        t.join()

     print("Main program finished!")
```

✅ **Behavior:**

* Each task runs in a **separate child process**, so **PIDs differ**.
* Execution is **parallel**: all tasks start simultaneously.
* Output order can be **mixed/interleaved**, depending on CPU scheduling:



---


```
Process 23456 working on 0
Process 23457 working on 1
Process 23458 working on 2
Process 23459 working on 3
Process 23460 working on 4
Done 0
Done 1
Done 2
Done 3
Done 4
```

⏱ **Time:** ~2 seconds total (all tasks overlap)



# 👉 Different PIDs → each task runs in a separate child process.
# 👉 Tasks run parallel (simultaneous) → all “working on …” print first, then after ~2 seconds all “Done …” appear.


### 🔹 Feature Comparison

| Feature          | Without Multiprocessing | With Multiprocessing    |
| ---------------- | ----------------------- | ----------------------- |
| **Process ID**   | Same for all (main PID) | Different for each task |
| **Execution**    | Sequential (one by one) | Parallel (simultaneous) |
| **Speed**        | Slower (waits for each) | Faster (tasks overlap)  |
| **Output order** | Predictable             | Mixed / interleaved     |

---

# ___________________________________________________________________



### What happens **without `join()`**

```python
from multiprocessing import Process
import os, time

def work(n):
    print(f"Process {os.getpid()} working on {n}", flush=True)
    time.sleep(2)
    print(f"Done {n}", flush=True)

if __name__ == "__main__":
    tasks = [Process(target=work, args=(i,)) for i in range(3)]

    print("Starting processes...")
    for t in tasks:
        t.start()

    # No join here
    print("Main program finished!")
```

**Possible Output:**

```
Starting processes...
Main program finished!
Process 12345 working on 0
Process 12346 working on 1
Process 12347 working on 2
Done 0
Done 1
Done 2
```

⚠️ Notice:

* `"Main program finished!"` prints immediately.
* The child processes are still running in the background.

---

### What happens **with `join()`**

```python
from multiprocessing import Process
import os, time

def work(n):
    print(f"Process {os.getpid()} working on {n}", flush=True)
    time.sleep(2)
    print(f"Done {n}", flush=True)

if __name__ == "__main__":
    tasks = [Process(target=work, args=(i,)) for i in range(3)]

    print("Starting processes...")
    for t in tasks:
        t.start()

    # Wait for all processes to finish
    for t in tasks:
        t.join()

    print("Main program finished!")
```

**Possible Output:**

```
Starting processes...
Process 12345 working on 0
Process 12346 working on 1
Process 12347 working on 2
Done 0
Done 1
Done 2
Main program finished!
```

✅ Here:

* The main program **waits** until all child processes are done.
* Only after all `"Done n"` messages appear, you see `"Main program finished!"`.

---

👉 **Summary:**

* `start()` → begins the process.
* `join()` → makes the main program wait until that process finishes.
* Without `join()`, the main process may end before child processes finish.


# ___________________________________________


## 🟢 Python Demo: Timing Comparison

```python
import threading, time, os

# ---------------------------
# Case 1: Without Multithreading
# ---------------------------
def work(n):
    print(f"Process {os.getpid()} working on {n}", flush=True)
    time.sleep(2)
    print(f"Done {n}", flush=True)

print("=== Without Multithreading ===")
start = time.time()

for i in range(3):
    work(i)

end = time.time()
print(f"Total time (no threading): {end - start:.2f} seconds\n")

# ---------------------------
# Case 2: With Multithreading
# ---------------------------
def work_thread(n):
    print(f"Thread {threading.get_ident()} in PID {os.getpid()} working on {n}", flush=True)
    time.sleep(2)
    print(f"Done {n}", flush=True)

print("=== With Multithreading ===")
start = time.time()

threads = [threading.Thread(target=work_thread, args=(i,)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()

end = time.time()
print(f"Total time (with threading): {end - start:.2f} seconds")
```

---

## 🔹 Expected Output

```
=== Without Multithreading ===
Process 12345 working on 0
Done 0
Process 12345 working on 1
Done 1
Process 12345 working on 2
Done 2
Total time (no threading): 6.00 seconds

=== With Multithreading ===
Thread 45678 in PID 12345 working on 0
Thread 45679 in PID 12345 working on 1
Thread 45680 in PID 12345 working on 2
Done 0
Done 2
Done 1
Total time (with threading): 2.01 seconds
```

---

### 🔹 Explanation (Thunglish)

1. **Without threading** → tasks run **one by one** → 3 tasks × 2 sec each = ~6 sec total.
2. **With threading** → tasks run **concurrently** → all sleep(2) happens at the same time → total ~2 sec.
3. **Output order** → With threading, `Done` lines **may shuffle** because threads finish at slightly different times.
4. **PID** → Same for all, **Thread ID** → different for each thread.

---

💡 **Conclusion:**

* **Threading** helps **I/O-bound tasks** finish much faster.
* CPU-bound tasks won’t see much speedup in Python because of **GIL**, but I/O tasks benefit big time.

---

# _______________________________________________________________


## 🟢 Case 3: With Multithreading

```python
import threading, os, time

def work(n):
    print(f"Thread {threading.get_ident()} working on {n}", flush=True)
    time.sleep(2)
    print(f"Done {n}", flush=True)

threads = [threading.Thread(target=work, args=(i,)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

### 👉 Behavior

* **Thread ID** is different for each thread (not PID).
* Runs **concurrently** (all “working on …” prints appear quickly).
* But in **CPython**, because of the **GIL (Global Interpreter Lock)**, only one thread executes Python bytecode at a time.
* Still useful for **I/O-bound tasks** (e.g., waiting, network requests).
* Output order = **not guaranteed** (like multiprocessing).

---

## 🟢 Case 4: With AsyncIO (Asynchronous Programming)

```python
import asyncio, os

async def work(n):
    print(f"Task {n} running in PID {os.getpid()}", flush=True)
    await asyncio.sleep(2)
    print(f"Done {n}", flush=True)

async def main():
    tasks = [asyncio.create_task(work(i)) for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())
```

### 👉 Behavior

* All tasks run in **the same process and same thread**.
* `asyncio` switches between tasks **during waiting (await)**.
* Very efficient for **I/O-bound tasks** (network calls, file ops, DB queries).
* Output order = **not guaranteed**, depends on scheduling, but usually all "working on" first, then all "Done".
* Fastest for many I/O operations since no process/thread overhead.

---

## 🟢 Final Comparison Table

| Feature            | Without Multiprocessing | With Multiprocessing          | With Multithreading             | With AsyncIO                |
| ------------------ | ----------------------- | ----------------------------- | ------------------------------- | --------------------------- |
| **Process/Thread** | Same PID (main process) | Different PID for each task   | Same PID, diff Thread IDs       | Same PID, same Thread       |
| **Execution**      | Sequential (blocking)   | Parallel (true multi-core)    | Concurrent (GIL limits CPU)     | Cooperative concurrency     |
| **Best For**       | Very small tasks        | CPU-bound (heavy compute)     | I/O-bound (network, disk, etc.) | Massive I/O-bound tasks     |
| **Speed**          | Slow (one by one)       | Fast (tasks overlap on cores) | Medium (context switches)       | Fastest for I/O-bound tasks |
| **Output order**   | Predictable             | Mixed / interleaved           | Mixed / interleaved             | Mixed / interleaved         |

---

✅ **Thunglish summary:**

* **Without Multiprocessing** → எல்லாமே main process-ல sequential.
* **Multiprocessing** → ஒவ்வொரு task-க்கும் தனி process, true parallelism (CPU-boundக்கு best).
* **Multithreading** → எல்லாம் same process-ல, different threads. GIL காரணமா CPU tasks slow, ஆனா I/O tasks super.
* **AsyncIO** → ஒரே thread-ல cooperative switching, thousands of I/O tasks handle பண்ண முடியும்.


# ____________________________________________________________----

### **🔹 Key Differences Between `threading`, `multiprocessing`, and `asyncio/await`**

| Feature              | **Threading** 🧵                                             | **Multiprocessing** 🔥                                    | **Asyncio/Await** ⚡ |
|--------------------  |----------------|--------------------|----------------|
| **Best For**         | I/O-bound tasks (waiting for network, file, DB)             | CPU-bound tasks (heavy computations, ML, image processing) | I/O-bound tasks (API calls, DB queries, WebSockets) |
| **Execution Type**   | Concurrent (switching between tasks)                        | Parallel (true multi-core execution)                       | Cooperative multitasking (single-threaded) |
| **Uses Multiple CPU Cores?** | ❌ No (Limited by GIL)                            | ✅ Yes (Each process has its own memory space)              | ❌ No (Single-threaded event loop) |
| **Overhead**         | Medium (Context switching slows down performance)           | High (Separate processes require memory & setup)           | Low (Efficient event loop, no thread switching) |
| **Scalability**      | Limited due to the GIL | Scales well across CPUs            | Scales well for I/O tasks |
| **Code Complexity**  | Simple | More complex (inter-process communication needed) | Requires `async` & `await` syntax |
| **When to Use?**     | ✅ Scraping, API requests, file operations, GUI apps        | ✅ Machine learning, image processing, number crunching   | ✅ WebSockets, API calls, DB queries, real-time apps |




🔹 Detailed Explanation of Each Concept**
1️⃣ `threading` (For I/O-bound tasks, NOT CPU-intensive)**
         - Uses **multiple threads** within **a single process**.
         - Only **one thread can run Python code at a time** due to the **Global Interpreter Lock (GIL)**.
         - Good for tasks where the CPU is mostly **waiting** (e.g., web scraping, file I/O).
         - **Inefficient for CPU-bound tasks** since threads can't run Python code in parallel.


________________________________________________________________________________________________________
✅ **Example: Using `threading` for API Calls**
python
import threading
import requests

def fetch_url(url):
    response = requests.get(url)
    print(f"Fetched {url} - {response.status_code}")

urls = ["https://httpbin.org/delay/2"] * 5
threads = []

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
```
🔴 **Problem:** If used for CPU-heavy tasks (e.g., image processing), the GIL will slow things down.



________________________________________________________________________________________________________
✅

2️⃣ `multiprocessing` (For CPU-bound tasks, fully utilizes multiple cores)**
     - Uses **multiple processes**, each with **its own memory space**.
     - **Bypasses the GIL**, allowing true **parallel execution** across CPU cores.
     - Best for **CPU-heavy computations** (ML, image processing, data processing).
     - More memory overhead since each process **has its own copy of Python objects**.



________________________________________________________________________________________________________
✅
✅ **Example: Using `multiprocessing` for CPU-heavy calculations**
```python
import multiprocessing

def calculate_squares(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    numbers = [10_000_000, 20_000_000, 30_000_000, 40_000_000]
    pool = multiprocessing.Pool(processes=4)  # Uses 4 CPU cores
    results = pool.map(calculate_squares, numbers)
    print(results)
```
✅ **Multiprocessing is ideal for ML, image processing, and simulations.**



________________________________________________________________________________________________________
✅ 

3️⃣ `asyncio` + `await` (For I/O-bound tasks, better than `threading`)**
    - **Uses an event loop** (single-threaded, non-blocking).
     - Great for **handling thousands of network requests** efficiently.
    - Works well for **real-time apps** like chat, live updates, and WebSockets.
    - **No thread switching overhead** like `threading`.



________________________________________________________________________________________________________
✅ **Example: Using `threading` for API Calls**
✅ **Example: Using `asyncio` for API Calls (Efficient!)**
```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} - {response.status}")
        return await response.text()

async def main():
    urls = ["https://httpbin.org/delay/2"] * 5
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())
```
✅ **Asyncio is best for fast, concurrent network operations**.



________________________________________________________________________________________________________
✅ 

## **🔹 When Should You Use Each?**
| **Scenario** | **Best Choice** |
|-------------|----------------|
| Making 100 API requests | ✅ `asyncio` (`aiohttp`) |
| Processing large images | ✅ `multiprocessing` |
| Running 10 web scraping tasks | ✅ `asyncio` or `threading` |
| Machine Learning training | ✅ `multiprocessing` |
| Real-time WebSocket chat app | ✅ `asyncio` |
| GUI apps (Tkinter, PyQt) | ✅ `threading` |



________________________________________________________________________________________________________
✅ 

## **🔹 Final Summary**
- **Use `asyncio` for I/O-heavy tasks** (networking, API calls, DB queries).
- **Use `threading` for tasks that wait but don't need CPU** (like downloading files).
- **Use `multiprocessing` for CPU-heavy tasks** (ML, image processing, calculations).