

**Concurrency** vs **Parallelism**


**Multithreading**   
**Multiprocessing**  
**Asynchronous Programming**  


# Overview:

Concurrency ──► Multithreading ──► Shares memory, GIL limits CPU-bound performance
             └─► Asyncio ──► Single thread, non-blocking I/O

Parallelism ──► Multiprocessing ──► Multiple processes, true parallel execution, bypasses GIL



# concurrency

Managing multiple tasks at the same time, but **not necessarily executing them at the exact same moment**.
It’s about switching between tasks efficiently. 


## **2. Multithreading in Python**

### What is Multithreading?

* Running multiple **threads** (lightweight units of a process) in the same memory space.
* Useful for **I/O-bound tasks** (waiting for files, network, database).
* **Not great for CPU-bound tasks** in Python because of the GIL.

---

### **Worker Process vs Thread**

* **Thread** → Lightweight, shares memory with other threads in the same process.
* **Worker Process** → Heavyweight, has its own memory space, runs independently (used in multiprocessing).




# example1 :


# -------------------------------------



# import time


# def download_file(file_name, download_time):
#     print(f"Started downloading: {file_name}")

#     time.sleep(download_time)

#     print(f"Completed downloading: {file_name}")


# # Start timer
# start_time = time.perf_counter()


# # Sequential execution
# download_file("file1.pdf", 3)
# download_file("file2.pdf", 2)
# download_file("file3.pdf", 4)


# # End timer
# end_time = time.perf_counter()


# print("\nAll downloads completed.")
# print(f"Total execution time: {end_time - start_time:.2f} seconds")





# ------------------------------------------------------

<!-- 
import threading
import time


def download_file(file_name, download_time):
    print(f"Started downloading: {file_name}")

    time.sleep(download_time)

    print(f"Completed downloading: {file_name}")


# Start timer
start_time = time.perf_counter()


# Create threads
t1 = threading.Thread(target=download_file,args=("file1.pdf", 3))

t2 = threading.Thread(target=download_file,args=("file2.pdf", 2))

t3 = threading.Thread(target=download_file,args=("file3.pdf", 4))


# Start threads
t1.start()
t2.start()
t3.start()


# Wait for all threads
t1.join()
t2.join()
t3.join()


# End timer
end_time = time.perf_counter()


print("\nAll downloads completed.")
print(f"Total execution time: {end_time - start_time:.2f} seconds") -->




# ```
#                  ┌───────────────┐
#                  │  Main Thread  │
#                  └───────┬───────┘
#                          │ creates
# ───────────────────────────────────────────────────
#         ┌────────────┬────────────┬────────────┬────────────┐
#         ▼            ▼            ▼            ▼
# ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐
# │ Thread-1   │ │ Thread-2   │ │ Thread-3   │ │ Thread-4   │
# │ file1.pdf  │ │ file2.jpg  │ │ file3.mp4  │ │ file4.zip  │
# └─────┬──────┘ └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
#       │ downloading   │ downloading   │ downloading   │ downloading
#       ▼               ▼               ▼               ▼
#   Completed        Completed        Completed        Completed
# ───────────────────────────────────────────────────
#                Main Thread Combines Output
#                      ↓
#         "All files downloaded."





# ------------------------------------------------------


| **Parallelism** | 

Executing multiple tasks at **exactly the same time** on multiple CPU cores or processors.                                                                 




# Example1:
 Two cashiers serving two customers at the same time in different checkout lines.     
 
#Example2:

1. Restaurant Kitchen (Best Analogy) 🍽️

Imagine a restaurant has 3 chefs.

👨‍🍳 Chef 1 → Makes Biryani
👨‍🍳 Chef 2 → Makes Noodles
👨‍🍳 Chef 3 → Makes Fried Rice



## ✅ **Definition**

**Multiprocessing** means running multiple **processes** at the same time.
Each process has:

✔ Its **own memory space**
✔ Its **own Python interpreter**
✔ Its **own GIL** (so GIL is bypassed)

That's why multiprocessing gives **TRUE parallel CPU execution**.



# Example:

from multiprocessing import Process

def task(name):
    print("Hello from child process",name)


if __name__ == "__main__":

   processes=[]


   for i in range(5):
         p=Process(target=task,args=(f"Process-{i+1}",))
         processes.append(p)
         p.start()

   for p in processes:
         p.join()

   print("All child processes have completed.")
       



# Main Process
#      |
#      ├── Process 1 → task(0)--->memory1
#      ├── Process 2 → task(1)--->memory2
#      ├── Process 3 → task(2)--->memory3
#      ├── Process 4 → task(3)--->memory4
#      └── Process 5 → task(4)--->memory5
# ------------------------------------------------------


# ______________________________________
**Asynchronous Programming**
# ______________________________________

* Programming method where **tasks don’t block each other**.
* While one task is waiting (API, DB, I/O), the program continues doing **other work**.
* Achieves **concurrency without multiple threads**.


* **asyncio** library → official async library in Python
* **Coroutines** → functions that can pause/resume (`async def`)
* **await** → pauses until the awaited coroutine completes

**Good for:** API calls, file downloads, DB queries, networking.




import asyncio


async def cook(work,seconds):
      print(f"Started cooking {work}")
      await asyncio.sleep(seconds)
      print(f"Completed cooking {work}")


async def main():

      t1=asyncio.create_task(cook("Pasta", 3))
      t2=asyncio.create_task(cook("Salad", 2))
      t3=asyncio.create_task(cook("Soup", 4))

      await asyncio.gather(t1, t2, t3)


asyncio.run(main())


