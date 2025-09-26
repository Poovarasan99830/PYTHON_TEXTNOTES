
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

