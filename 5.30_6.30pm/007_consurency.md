**Concurrency** vs **Parallelism**


**Multithreading**   
**Multiprocessing**  
**Asynchronous Programming**  


# Overview:

Concurrency ──► Multithreading ──► Shares memory, GIL limits CPU-bound performance
             └─► Asyncio ──► Single thread, non-blocking I/O

Parallelism ──► Multiprocessing ──► Multiple processes, true parallel execution, bypasses GIL




## **1. Concurrency vs Parallelism**

                                                                                                  
| **Concurrency** | 

Managing multiple tasks at the same time, but **not necessarily executing them at the exact same moment**.
It’s about switching between tasks efficiently. 

#Example:
A single cashier at a grocery store handles multiple customers by switching between scanning, bagging, and answering questions. 




| **Parallelism** | 

Executing multiple tasks at **exactly the same time** on multiple CPU cores or processors.                                                                 

#Example:
 Two cashiers serving two customers at the same time in different checkout lines.                                                |



**Key Difference**:

* Concurrency → *Dealing with* multiple things at once (can be single-core).
* Parallelism → *Doing* multiple things at once (requires multi-core).

---___________________________________________________________________________________

## **2. Multithreading in Python**

### What is Multithreading?

* Running multiple **threads** (lightweight units of a process) in the same memory space.
* Useful for **I/O-bound tasks** (waiting for files, network, database).
* **Not great for CPU-bound tasks** in Python because of the GIL.

---

### **Worker Process vs Thread**

* **Thread** → Lightweight, shares memory with other threads in the same process.
* **Worker Process** → Heavyweight, has its own memory space, runs independently (used in multiprocessing).

---

### **GIL (Global Interpreter Lock)**

* Python (CPython) has a **mutex** called the GIL that ensures only **one thread executes Python bytecode at a time**.
* Even on a multi-core CPU, threads cannot run Python code truly in parallel.
* Good for avoiding race conditions, but bad for CPU-heavy computations.




**Example**:

```python
import threading

def task():
    for i in range(5):
        print(f"Task running: {i}")

thread1 = threading.Thread(target=task)
thread2 = threading.Thread(target=task)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
```

➡ Threads will interleave execution, but **not run CPU-heavy code in parallel** due to the GIL.

---___________________________________________________________________________________

### **Threading Module**

* Python's `threading` library allows:

  * Creating and managing threads
  * Synchronization (`Lock`, `Semaphore`)
  * Thread-safe communication (`queue.Queue`)

Example with Lock:

```python
import threading

lock = threading.Lock()
count = 0

def increment():
    global count
    for _ in range(1000):
        with lock:
            count += 1

threads = [threading.Thread(target=increment) for _ in range(5)]

for t in threads: t.start()
for t in threads: t.join()

print(count)  # Always 5000 due to lock
```






---___________________________________________________________________________________

## **3. Multiprocessing in Python**

* Uses **separate processes** instead of threads.
* **Bypasses the GIL** because each process has its own Python interpreter and memory.
* Ideal for **CPU-bound tasks** (math-heavy computations, image processing).

Example:

```python
from multiprocessing import Process, Value

def increment(counter):
    for _ in range(1000):
        with counter.get_lock():
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)
    processes = [Process(target=increment, args=(counter,)) for _ in range(5)]

    for p in processes: p.start()
    for p in processes: p.join()

    print(counter.value)  # 5000
```

---___________________________________________________________________________________

## **4. Asynchronous Programming**

### Key Idea

* Runs **tasks concurrently** in a single thread using an **event loop**.
* **Non-blocking I/O** — the program doesn’t wait for slow operations; it continues running other tasks.
* Uses **coroutines**.

---

### **Asyncio Library**

* Python's built-in library for asynchronous programming.
* Manages an event loop that schedules and runs coroutines.

---

### **Coroutine**

* Special function that can pause and resume execution.
* Defined with `async def`.
* You use `await` to pause until an async operation finishes.

Example:

```python
import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main():
    await asyncio.gather(greet(), greet(), greet())

asyncio.run(main())
```

➡ Outputs "Hello" three times immediately, then "World" three times after 1 second — running concurrently in one thread.

---

### **async / await**

* `async def` → defines a coroutine.
* `await` → pauses coroutine until the awaited task completes.
* `asyncio.gather()` → runs multiple coroutines concurrently.

---

## **5. When to Use What**

| Task Type                                            | Best Approach                     | Why                                                       |
| ---------------------------------------------------- | --------------------------------- | --------------------------------------------------------- |
| **I/O-bound** (network, file read/write, DB queries) | Multithreading or Asyncio         | I/O waits a lot → Threads or event loop keep CPU busy.    |
| **CPU-bound** (math, data processing, compression)   | Multiprocessing                   | Bypasses GIL and uses multiple cores.                     |
| **Mixed workload**                                   | Combine multiprocessing + asyncio | Processes for CPU-heavy work, asyncio for I/O-heavy work. |

---

## **6. Quick Summary Diagram**

```
Concurrency ──► Multithreading ──► Shares memory, GIL limits CPU-bound performance
             └─► Asyncio ──► Single thread, non-blocking I/O

Parallelism ──► Multiprocessing ──► Multiple processes, true parallel execution, bypasses GIL
```

---

If you want, I can make you a **full visual diagram of Concurrency, Parallelism, Multithreading, Multiprocessing, and Asyncio in Python** so you can use it for teaching or revision.



