
#       30-08-2025 TO 01-09-2025
#       TOPIC: FUNCTIONS


#  PART1- Python Functions – Detailed Notes
#  part2-->Scope (LEGB Rule) and **Namespace and Scope**
#  PART3- **universal template** for Python function parameter order.
#  PART3- step-by-step exercise track for Python function parameter order.
#  PART4- *task-based exercises** for the topics (Function definition, return, arguments, rules, namespace &    
#  PART5-  Mini Project: Student Grade Management System
#  PART6- Mini Project: Employee Management System 
#  Part7-task beginner level



_____________________________________________________________________________________________
                                      PART-1
#_____________________________________________________________________________________________


Got it 👍
You’re asking about a structured explanation of **functions in Python** — specifically *definition, return, arguments & parameters (with all variations), rules, namespace, and scope*.

Here’s a clean breakdown:

---

# 🔹 Python Functions – Detailed Notes

## 1. **Defined**

A **function** is a block of reusable code that performs a specific task.
In Python, functions are defined using the `def` keyword.

```python
def greet(name):
    return f"Hello, {name}!"
```

---

## 2. **Return**

* The `return` statement sends a result from a function back to the caller.
* If no `return` is used, the function returns `None` by default.

```python
def add(a, b):
    return a + b

print(add(5, 3))   # 8
```

---

## 3. **Arguments and Parameters**

* **Parameters** → variables listed in the function definition.
* **Arguments** → values passed to a function when it is called.

### 🔹 a) Default and Non-default Parameters

* **Default**: Assigns a value in definition, used if no argument is provided.
* **Non-default**: Requires an argument when calling.

```python
def greet(name="Guest"):  # Default parameter
    print(f"Hello, {name}!")

greet("Alice")   # Hello, Alice!
greet()          # Hello, Guest
```

⚠️ Rule: Non-default parameters must appear **before** default parameters.

✅ Correct:

```python
def func(a, b=10): pass
```

❌ Wrong:

```python
def func(a=10, b): pass  # SyntaxError
```

---

### 🔹 b) Positional and Keyword Arguments

* **Positional**: Values assigned based on position.
* **Keyword**: Values assigned using parameter names.

```python
def info(name, age):
    print(name, age)

info("Ravi", 25)               # Positional
info(age=25, name="Ravi")      # Keyword
```

---

### 🔹 c) Arbitrary Arguments (`*args`)

* Used when the number of arguments is unknown.
* Collected into a **tuple**.

```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))   # 10
```

---

### 🔹 d) Keyword Arbitrary Arguments (`**kwargs`)

* Accepts multiple **keyword arguments**.
* Collected into a **dictionary**.

```python
def profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

profile(name="Ravi", age=25, city="Chennai")
```

---

### 🔹 e) Argument Syntax Rules

1. **Order of parameters** must follow:

   ```
   def func(positional, /, positional_or_keyword, *, keyword_only):
   ```

   Or in practice:

   ```
   def func(a, b, c=10, *args, d, **kwargs):
   ```

   General Rule:

   ```
   Positional → Default → *args → Keyword-only → **kwargs
   ```

2. **Positional must come before keyword**.

   ```python
   def func(a, b):
       pass

   func(1, 2)          # OK
   func(a=1, b=2)      # OK
   func(1, b=2)        # OK
   func(a=1, 2)        # ❌ SyntaxError
   ```

______________________________________________________________________________________________________
_____________________________________________________________________________________________
                   PART-2
#_____________________________________________________________________________________________

## 4. **Namespace and Scope**

### 🔹 Namespace

* A **namespace** is a mapping between names and objects.
* Types:

  1. **Local** – Inside a function.
  2. **Enclosing** – In nested functions.
  3. **Global** – At the module level.
  4. **Built-in** – Provided by Python (like `len`, `print`).

---

### 🔹 Scope (LEGB Rule)

When you reference a variable, Python searches in order:

1. **L (Local)** – Inside current function.
2. **E (Enclosing)** – Inside outer functions.
3. **G (Global)** – Defined in the module.
4. **B (Built-in)** – Predefined by Python.

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()

outer()   # local
```

---

✅ That covers everything you listed with structured notes and examples.

Do you want me to **convert this into a student-friendly lesson plan with exercises + solutions** (like small coding tasks for each concept), or just keep it as **reference notes**?




💯 correct observation 👌 You’re asking:

> “Inga enakku outer x iruku, but still `global x` use panna outer x ignore panniduchu. Why?”

---

### 🔍 Let’s check carefully

```python
x = "global"   # Global variable

def outer():
    x = "enclosing"   # Outer variable
    def inner():
        global x      # Force inner() to connect only to GLOBAL
        print(x)      # → "global"
        x = "modified global"
        print(x)      # → "modified global"
    inner()
    print(x)          # → "enclosing" (not changed!)

outer()
print(x)              # → "modified global"
```

---

### ⚡ Thunglish Explanation

* `outer()` la irukkara `x = "enclosing"` → **enclosing scope variable**.
* But inside `inner()`, we wrote `global x`.

`global x` nu sonna, Python oda meaning:
👉 “I don’t care about enclosing scope, I will **directly connect to global x only**.”

So:

* Inner function `x` → global ah link aagiduchu.
* Outer la irukkara `x` totally ignored.
* So outer print pannumbodhu → `"enclosing"` dhaan varum (unchanged).
* Global x update aagiduchu → `"modified global"`.

---

### 🖼️ Diagram

```
Global Scope:      x = "global"
Outer Scope:       x = "enclosing"
Inner Scope:
    global x → connects to GLOBAL, not outer
    print(x) → "global"
    x = "modified global"
```

Result:

```
inner() print: "global"
inner() print: "modified global"
outer() print: "enclosing"
global print: "modified global"
```

---

### 🎯 Thunglish One-liner

**`global x` → direct ah global variable kitta connect pannidum, middle la irukkara outer x ah ignore pannidum.**
That’s why outer-x untouched, but global-x modified.

---



Perfect 👍 let’s take the **same example** and replace `global` with `nonlocal`.

---

### 🖼️ Example with `nonlocal`

```python
x = "global"   # Global variable

def outer():
    x = "enclosing"   # Outer variable
    def inner():
        nonlocal x    # Force inner() to connect to OUTER's x
        print(x)      # → "enclosing"
        x = "modified enclosing"
        print(x)      # → "modified enclosing"
    inner()
    print(x)          # → "modified enclosing"

outer()
print(x)              # → "global" (unchanged)
```

---

### ⚡ Thunglish Explanation

* `outer()` la irukkara `x = "enclosing"` → enclosing scope variable.
* `inner()` la `nonlocal x` nu sonna:
  👉 “I will connect to **nearest enclosing function’s variable** (outer-x), not global.”

So:

* Inner function `x` → directly outer x ah use panniduchu.
* Outer-x value update aagiduchu.
* Global-x untouched.

---

### 🖼️ Diagram

```
Global Scope:      x = "global"
Outer Scope:       x = "enclosing"
Inner Scope:
    nonlocal x → connects to OUTER
    print(x) → "enclosing"
    x = "modified enclosing"
```

Result:

```
inner() print: "enclosing"
inner() print: "modified enclosing"
outer() print: "modified enclosing"
global print: "global"
```

---

### 🎯 Side-by-Side Thunglish Summary

| Keyword      | Connects to                           | What happens in our example                |
| ------------ | ------------------------------------- | ------------------------------------------ |
| **global**   | Top-level variable (`x = "global"`)   | Inner modifies global-x, outer-x ignored   |
| **nonlocal** | Nearest enclosing (`x = "enclosing"`) | Inner modifies outer-x, global-x untouched |

---

⚡ One-Liner Thunglish:

* **`global`** → “Skip outer, go straight to global.”
* **`nonlocal`** → “Skip local, go to nearest outer function variable.”

---



Superb 🚀 let’s do a **3-layer nested example** with `global`, `nonlocal`, and plain local so you can compare everything in one shot.

---

### 🖼️ Code: Local vs Nonlocal vs Global

```python
x = "global"   # Global variable

def outer():
    x = "enclosing"   # Outer variable

    def inner_local():
        x = "local"
        print("inner_local:", x)

    def inner_nonlocal():
        nonlocal x
        print("inner_nonlocal before:", x)
        x = "modified enclosing"
        print("inner_nonlocal after:", x)

    def inner_global():
        global x
        print("inner_global before:", x)
        x = "modified global"
        print("inner_global after:", x)

    # Call all three
    inner_local()
    inner_nonlocal()
    inner_global()
    print("outer after all:", x)

outer()
print("global after all:", x)
```

---

### 🔍 Expected Output

```
inner_local: local
inner_nonlocal before: enclosing
inner_nonlocal after: modified enclosing
inner_global before: global
inner_global after: modified global
outer after all: modified enclosing
global after all: modified global
```

---

### 🖼️ Thunglish Explanation

1. **inner\_local**

   * `x = "local"` → totally new local variable inside `inner_local()`.
   * No effect on outer or global.
     👉 Output: `"local"`

2. **inner\_nonlocal**

   * `nonlocal x` → connect to `outer()`’s `x`.
   * Before change: `"enclosing"`
   * After change: `"modified enclosing"`
     👉 Outer’s `x` modified.

3. **inner\_global**

   * `global x` → connect to top-level global `x`.
   * Before change: `"global"`
   * After change: `"modified global"`
     👉 Global `x` modified, outer untouched.

---

### 🎯 Side-by-Side Result Table

| Function         | Connects to which `x`? | Effect               |
| ---------------- | ---------------------- | -------------------- |
| `inner_local`    | Creates new local-x    | Only inside function |
| `inner_nonlocal` | Nearest enclosing-x    | Changes outer-x      |
| `inner_global`   | Top-level global-x     | Changes global-x     |

---

⚡ One-line Thunglish summary:

* **Local** → “Naan enakku thaniya oru x create panren.”
* **Nonlocal** → “Naan outer la irukkara x ah use & modify panren.”
* **Global** → “Enakku outer vendam, direct ah global x ah modify panren.”

---

👉 Do you want me to also make a **diagram (3 concentric circles)** showing Local → Enclosing → Global scopes with arrows for `local`, `nonlocal`, and `global`?

_____________________________________________________________________________________________
                   PART-3
#_____________________________________________________________________________________________






Perfect 👍 Let’s build a **universal template** for Python function parameter order.

---



👉 / = everything before must be positional only.

👉* = everything after must be keyword only.

👉Together they give very fine control over how your function is called.

👉  You cannot have more than one **kwargs in a signature.
👉  You cannot put keyword-only parameters after **kwargs.

👉  arguments must always come before keyword arguments in a function call.




# 🔹 Universal Function Parameter Order

Python enforces a **strict sequence** in function definitions:

```
def func(
    positional_only,       # before /
    /,
    positional_or_keyword, # normal ones
    default_values,        # normal with defaults
    *args,                 # collects extra positional
    keyword_only,          # after *, must be named
    keyword_only_defaults, # keyword-only with defaults
    **kwargs               # collects extra keywords
):
    ...
```

---

## 🔹 Rules of Order (must be followed)

1. **Positional-only**: Before `/`

   * Must be passed without keywords.

   ```python
   def f(a, /): ...
   ```

2. **Positional-or-keyword**: Before `*`

   * Can be passed either way.

   ```python
   def f(a, b): ...
   ```

3. **Default values**: Allowed for both positional-or-keyword and keyword-only.

   ```python
   def f(a, b=10): ...
   ```

4. **`*args`**: Captures extra **positional arguments**.

   ```python
   def f(*args): ...
   ```

5. **Keyword-only**: After `*` or `*args`, must be named explicitly.

   ```python
   def f(*, c, d=20): ...
   ```

6. **`**kwargs`**: Captures extra **keyword arguments**.

   ```python
   def f(**kwargs): ...
   ```

---

## 🔹 LEGAL Patterns

✔ Correct:

```python
def func(a, /, b, c=10, *args, d, e=20, **kwargs): ...
```

✔ Correct:

```python
def func(a, b, /, c, *args, **kwargs): ...
```

---

## 🔴 ILLEGAL Patterns

❌ Two `**kwargs`:

```python
def func(a, **x, **y): ...
```

❌ Keyword-only param after `**kwargs`:

```python
def func(a, **kwargs, c): ...
```

❌ Default before non-default (positional):

```python
def func(a=1, b): ...
```

---

# 🔹 Visual Template (for teaching)

```
|---- positional-only ----|   |---- pos/keyword ----|   |-- *args --|   |---- keyword-only ----|   |-- **kwargs --|
      a, b, /                      c, d=10               *args           e, f=20                   **kwargs
```

---

✅ This template works for **any function signature**.
Do you want me to create a **diagram/flowchart (boxes + arrows)** that visually shows how arguments get bound during a function call (like mapping `call → parameters → args/kwargs`)?






_____________________________________________________________________________________________
                                           PART-3
_________________________________________________________________________________________


Great 👍 Let’s design a **step-by-step exercise track** just for `/` and `*` so students move from **easy → medium → tricky**.

---

# 📝 Lesson Exercises: `/` and `*` in Python Functions

---

## 🔹 Part A: Positional-only (`/`)

### **Exercise A1: Simple positional-only**

```python
def add(a, b, /):
    return a + b

print(add(3, 4))        # ?
print(add(a=3, b=4))    # ?
```

👉 **Task:** Predict both outputs.

---

### ✅ Solution A1

```
7
❌ TypeError (a and b are positional-only)
```

---

### **Exercise A2: Mixed with normal parameters**

```python
def greet(first, /, last):
    return f"Hello {first} {last}"

print(greet("John", "Doe"))           # ?
print(greet("John", last="Doe"))      # ?
print(greet(first="John", last="Doe")) # ?
```

👉 **Task:** Which calls work, which fail?

---

### ✅ Solution A2

* `"Hello John Doe"` ✅
* `"Hello John Doe"` ✅
* ❌ Error (`first` is positional-only)

---

---

## 🔹 Part B: Keyword-only (`*`)

### **Exercise B1: Force keywords**

```python
def connect(*, host, port):
    return f"Connecting to {host}:{port}"

print(connect(host="127.0.0.1", port=3306))  # ?
print(connect("127.0.0.1", 3306))            # ?
```

👉 **Task:** What happens?

---

### ✅ Solution B1

* ✅ `"Connecting to 127.0.0.1:3306"`
* ❌ TypeError (must pass by keyword)

---

### **Exercise B2: Mixing positional + keyword-only**

```python
def power(base, *, exp=2):
    return base ** exp

print(power(5))            # ?
print(power(5, exp=3))     # ?
print(power(base=5))       # ?
```

👉 **Task:** Predict results.

---

### ✅ Solution B2

* `25` (default exp=2)
* `125`
* ✅ `25` (base can be named too)

---

---

## 🔹 Part C: Combining `/` and `*`

### **Exercise C1: Full separation**

```python
def demo(a, /, b, *, c):
    return a + b + c

print(demo(1, 2, c=3))       # ?
print(demo(1, b=2, c=3))     # ?
print(demo(a=1, b=2, c=3))   # ?
```

👉 **Task:** Which succeed, which fail?

---

### ✅ Solution C1

* `6` ✅
* `6` ✅
* ❌ Error (a is positional-only)

---

### **Exercise C2: With defaults**

```python
def multiply(x, /, y=2, *, z=3):
    return x * y * z

print(multiply(4))               # ?
print(multiply(4, 5))            # ?
print(multiply(4, z=10))         # ?
print(multiply(x=4, y=5, z=6))   # ?
```

👉 **Task:** Predict outputs.

---

### ✅ Solution C2

* `4 * 2 * 3 = 24`
* `4 * 5 * 3 = 60`
* `4 * 2 * 10 = 80`
* ❌ Error (`x` is positional-only)

---

---

## 🔹 Part D: Tricky / Advanced

### **Exercise D1: Order confusion**

```python
def f(a, b=2, /, *, c, d=4):
    return a + b + c + d

print(f(1, c=3))         
print(f(1, 10, c=5))     
print(f(1, b=10, c=5))   
```

👉 **Task:** Explain which works and why.

---

### ✅ Solution D1

* `1 + 2 + 3 + 4 = 10` ✅
* `1 + 10 + 5 + 4 = 20` ✅
* ❌ Error (`b` is positional-only, can’t be passed as keyword)

---

### **Exercise D2: Combine everything**

```python
def func(a, /, b, *args, c, d=10, **kwargs):
    return a, b, args, c, d, kwargs

print(func(1, 2, 3, 4, c=5, d=20, x=100, y=200))
```

👉 **Task:** Predict the tuple result.

---

### ✅ Solution D2

```
a = 1
b = 2
args = (3, 4)
c = 5
d = 20
kwargs = {'x': 100, 'y': 200}

Output: (1, 2, (3, 4), 5, 20, {'x': 100, 'y': 200})
```

---

# 🎯 Teaching Tip

* Start students with **A1 → A2 → B1 → B2** (easy wins).
* Then move to **C1, C2** (combining).
* End with **D1, D2** as “challenge problems.”

---

Do you want me to also create a **visual diagram worksheet (like a chart with boxes for positional-only, normal, keyword-only, etc.)** so students can fill in arguments step by step during class?


_____________________________________________________________________________________________
                                    PART-4
#_____________________________________________________________________________________________






Perfect ✅ You want **task-based exercises** for the topics (Function definition, return, arguments, rules, namespace & scope).
I’ll create **progressive tasks** — starting simple, then moving deeper.

---

# 📝 Python Function Practice Tasks

## 1. **Function Definition & Return**

* **Task 1:** Write a function `square(n)` that returns the square of a number.
* **Task 2:** Write a function `is_even(n)` that returns `True` if the number is even, otherwise `False`.
* **Task 3:** Write a function `sum_and_diff(a, b)` that returns both sum and difference as a tuple.

---

## 2. **Default & Non-default Parameters**

* **Task 4:** Create a function `greet(name="Guest")` that prints `"Hello, <name>"`. Try calling with and without a name.
* **Task 5:** Write a function `power(base, exponent=2)` that calculates base^exponent. Test with `power(5)` and `power(2, 3)`.

---

## 3. **Positional & Keyword Arguments**

* **Task 6:** Define a function `student_info(name, age, city)` and call it:

  * Using positional arguments.
  * Using keyword arguments.
  * Mixing positional and keyword arguments.

* **Task 7:** Write a function `order(item, price, quantity)` and call it in different ways using positional and keyword arguments.

---

## 4. **Arbitrary Arguments (`*args`)**

* **Task 8:** Create a function `add_all(*args)` that returns the sum of all numbers passed.
* **Task 9:** Write a function `max_value(*args)` that returns the largest number among given arguments.

---

## 5. **Keyword Arbitrary Arguments (`**kwargs`)**

* **Task 10:** Create a function `profile(**kwargs)` that prints all details in the format:


  key : value


  Example call:

 
  profile(name="Ravi", age=25, city="Chennai")
 

* **Task 11:** Create a function `employee(**kwargs)` that must accept at least `name` and `id`. Print "Invalid" if they are missing.

---

## 6. **Argument Syntax Rules**

* **Task 12:** Create a function with the following signature:


  def func(a, b=10, *args, c=20, **kwargs):
      pass
 

  * Call it with different combinations of arguments and observe outputs.



* **Task 13:** Try calling a function with keyword before positional argument (e.g. `func(a=5, 10)`) and note the error.




## 7. **Namespace & Scope**

* **Task 14:** Write a program with a global variable `x = 10`. Inside a function, print `x`. Then change `x` inside the function using `global` keyword.
* **Task 15:** Create nested functions (`outer`, `inner`) where `inner()` accesses a variable from `outer()` using `nonlocal`.
* **Task 16:** Write a program with variables named `len = 100`. Then call `print(len("abc"))`. Observe the error and explain why.

---

👉 These tasks cover everything you listed — from basics to advanced (namespace, scope, args rules).

Would you like me to also **provide sample solutions** for these tasks (so students can self-check), or do you want them only as **practice assignments**?








_____________________________________________________________________________________________
                               PART-5
#_____________________________________________________________________________________________






Great 👍 I’ll give you **solutions** for each task so that students can check after attempting.

---

# ✅ Python Functions – Tasks with Solutions

---

## 1. **Function Definition & Return**

**Task 1:**

```python
def square(n):
    return n * n

print(square(5))   # 25
```

**Task 2:**

```python
def is_even(n):
    return n % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False
```

**Task 3:**

```python
def sum_and_diff(a, b):
    return a + b, a - b

print(sum_and_diff(10, 4))   # (14, 6)
```

---

## 2. **Default & Non-default Parameters**

**Task 4:**

```python
def greet(name="Guest"):
    print(f"Hello, {name}")

greet("Alice")   # Hello, Alice
greet()          # Hello, Guest
```

**Task 5:**

```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25
print(power(2, 3))   # 8
```

---

## 3. **Positional & Keyword Arguments**

**Task 6:**

```python
def student_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Positional
student_info("Ravi", 25, "Chennai")

# Keyword
student_info(age=22, city="Delhi", name="Priya")

# Mixed
student_info("Arun", city="Mumbai", age=30)
```

**Task 7:**

```python
def order(item, price, quantity):
    print(f"Item: {item}, Price: {price}, Quantity: {quantity}")

# Positional
order("Book", 200, 3)

# Keyword
order(item="Pen", price=10, quantity=5)

# Mixed
order("Laptop", quantity=2, price=50000)
```

---

## 4. **Arbitrary Arguments (`*args`)**

**Task 8:**

```python
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))   # 10
```

**Task 9:**

```python
def max_value(*args):
    return max(args)

print(max_value(10, 25, 3, 40, 7))   # 40
```

---

## 5. **Keyword Arbitrary Arguments (`**kwargs`)**

**Task 10:**

```python
def profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

profile(name="Ravi", age=25, city="Chennai")
```

**Task 11:**

```python
def employee(**kwargs):
    if "name" in kwargs and "id" in kwargs:
        for key, value in kwargs.items():
            print(key, ":", value)
    else:
        print("Invalid")

employee(name="John", id=101, dept="HR")   # Valid
employee(dept="Finance")                   # Invalid
```

---

## 6. **Argument Syntax Rules**

**Task 12:**

```python
def func(a, b=10, *args, c=20, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("c:", c)
    print("kwargs:", kwargs)

func(1)                                # a=1, b=10
func(1, 2, 3, 4, c=50, x=100, y=200)   # args=(3,4)
```

**Task 13:**

```python
def example(a, b):
    print(a, b)

# example(a=1, 2)  ❌ SyntaxError
example(1, b=2)     # ✅ Correct
```

---

## 7. **Namespace & Scope**

**Task 14:**

```python
x = 10   # Global variable

def change_global():
    global x
    x = 20
    print("Inside function:", x)

change_global()
print("Outside function:", x)
```

**Task 15:**

```python
def outer():
    x = "outer value"
    def inner():
        nonlocal x
        x = "changed by inner"
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
```

**Task 16:**

```python
len = 100   # Shadows built-in function

try:
    print(len("abc"))   # ❌ Error: 'int' object is not callable
except Exception as e:
    print("Error:", e)

# Fix: del len  → restores built-in
del len
print(len("abc"))   # ✅ 3
```

---

✨ Now you have a **task + solution bank** that covers:
✔ Function definition
✔ Return values
✔ All argument types
✔ Syntax rules
✔ Namespace & scope

Would you like me to also **add a few challenge-style tasks** (slightly tricky, real-world style) so students can apply these concepts in mini problems?


_____________________________________________________________________________________________
#________________________________________PART-6_____________________________________________________
____________________________________________________________________________________________________





Perfect 🎯 A **mini-project** will help students apply all these function concepts together.
Here’s a compact but **real-world style project** that uses *default parameters, positional/keyword arguments, `*args`, `**kwargs`, return values, namespace & scope*.

---

# 🏫 Mini Project: Student Grade Management System

## 📌 Problem Statement

Create a system to manage students’ marks, calculate results, and display reports using **functions**.

---

## 🔑 Features & Function Requirements

### **1. Add Student**

* Function: `add_student(name, roll, marks, grade="Not Assigned")`
* Stores student info in a global `students` list.
* Uses **default argument** for grade.

---

### **2. Calculate Average Marks**

* Function: `average_marks(*marks)`
* Accepts variable marks and returns average.
* Uses **`*args`**.

---

### **3. Display Student Details**

* Function: `student_report(**kwargs)`
* Prints student details in `key : value` format.
* Uses **`**kwargs`**.

---

### **4. Update Grade**

* Function: `update_grade(roll, grade)`
* Searches student by roll number and updates grade.
* Demonstrates **positional + keyword arguments**.

---

### **5. Scope Example**

* Have a global counter `total_students`.
* Inside `add_student()`, use **global** keyword to update it.
* Inside nested function, use **nonlocal** to update a temporary value.

---

## 🖥️ Sample Implementation

```python
# Global storage
students = []
total_students = 0   # Global variable

# 1. Add Student
def add_student(name, roll, *marks, grade="Not Assigned"):
    global total_students
    avg = average_marks(*marks)   # calling another function
    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "average": avg,
        "grade": grade
    }
    students.append(student)
    total_students += 1

# 2. Calculate Average (using *args)
def average_marks(*marks):
    return sum(marks) / len(marks) if marks else 0

# 3. Display Student Details (using **kwargs)
def student_report(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    print("-" * 30)

# 4. Update Grade
def update_grade(roll, grade):
    for student in students:
        if student["roll"] == roll:
            student["grade"] = grade
            return f"Grade updated for {student['name']}"
    return "Student not found"

# 5. Namespace & Scope (LEGB Rule)
def namespace_demo():
    x = "local"
    def inner():
        nonlocal x
        x = "changed by inner"
        print("Inside inner:", x)
    inner()
    print("Inside outer:", x)

# -------------------------------
# Demo Run
# -------------------------------
add_student("Ravi", 101, 85, 90, 80)
add_student("Priya", 102, 70, 75, 80)
add_student("Arun", 103, 95, 88, 92)

print("Total Students:", total_students)

# Show reports
for stu in students:
    student_report(**stu)

# Update grade
print(update_grade(102, "B+"))
print(update_grade(105, "A"))  # Student not found

# Show updated report
for stu in students:
    student_report(**stu)

# Namespace demo
namespace_demo()
```

---

## 📊 Sample Output

```
Total Students: 3
name : Ravi
roll : 101
marks : (85, 90, 80)
average : 85.0
grade : Not Assigned
------------------------------
name : Priya
roll : 102
marks : (70, 75, 80)
average : 75.0
grade : Not Assigned
------------------------------
name : Arun
roll : 103
marks : (95, 88, 92)
average : 91.67
grade : Not Assigned
------------------------------
Grade updated for Priya
Student not found
name : Ravi
roll : 101
marks : (85, 90, 80)
average : 85.0
grade : Not Assigned
------------------------------
name : Priya
roll : 102
marks : (70, 75, 80)
average : 75.0
grade : B+
------------------------------
name : Arun
roll : 103
marks : (95, 88, 92)
average : 91.67
grade : Not Assigned
------------------------------
Inside inner: changed by inner
Inside outer: changed by inner
```

---

✅ This project makes students use:

* **Return values** (`average_marks`)
* **Default params** (`grade="Not Assigned"`)
* **Positional + Keyword args** (`update_grade`)
* **`*args` & `**kwargs`** (`marks`, `student_report`)
* **Namespace & Scope (global, nonlocal)**

---

Would you like me to create a **second mini-project** (like **Employee Management System**) so students can practice the same concepts in another context?


___________________________________________________________________________________________________
#________________________________________PART-7____________________________________________________
___________________________________________________________________________________________________







Awesome 🚀 Let’s design a **second mini-project**:

---

# 🏢 Mini Project: Employee Management System

## 📌 Problem Statement

Build a system to manage employees’ details, calculate salaries, and update departments using **Python functions**.

---

## 🔑 Features & Function Requirements

### **1. Add Employee**

* Function: `add_employee(name, emp_id, salary, dept="General")`
* Adds employee details into a global list `employees`.
* Uses **default argument** for `dept`.

---

### **2. Calculate Total Salary**

* Function: `total_salary(*salaries)`
* Accepts multiple salaries and returns the total.
* Uses **`*args`**.

---

### **3. Display Employee Details**

* Function: `employee_report(**kwargs)`
* Prints employee details in the format:

  ```
  key : value
  ```
* Uses **`**kwargs`**.

---

### **4. Update Department**

* Function: `update_department(emp_id, dept)`
* Updates employee department by `emp_id`.
* Demonstrates **positional + keyword arguments**.

---

### **5. Scope Example**

* Use a global variable `total_employees`.
* Update it inside `add_employee()` using **global**.
* Inside a nested function, modify a local variable using **nonlocal**.

---

## 🖥️ Sample Implementation

```python
# Global storage
employees = []
total_employees = 0   # Global variable

# 1. Add Employee
def add_employee(name, emp_id, salary, dept="General"):
    global total_employees
    employee = {
        "name": name,
        "id": emp_id,
        "salary": salary,
        "dept": dept
    }
    employees.append(employee)
    total_employees += 1

# 2. Calculate Total Salary (using *args)
def total_salary(*salaries):
    return sum(salaries)

# 3. Display Employee Details (using **kwargs)
def employee_report(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    print("-" * 30)

# 4. Update Department
def update_department(emp_id, dept):
    for emp in employees:
        if emp["id"] == emp_id:
            emp["dept"] = dept
            return f"Department updated for {emp['name']}"
    return "Employee not found"

# 5. Namespace & Scope (LEGB Rule)
def scope_demo():
    x = "local variable"
    def inner():
        nonlocal x
        x = "modified by inner"
        print("Inner:", x)
    inner()
    print("Outer:", x)

# -------------------------------
# Demo Run
# -------------------------------
add_employee("Ravi", 201, 50000)
add_employee("Priya", 202, 60000, dept="HR")
add_employee("Arun", 203, 45000, dept="IT")

print("Total Employees:", total_employees)

# Show reports
for emp in employees:
    employee_report(**emp)

# Update department
print(update_department(202, "Finance"))
print(update_department(210, "Admin"))  # Employee not found

# Calculate total salary
print("Total Salary:", total_salary(50000, 60000, 45000))

# Namespace demo
scope_demo()
```

---

## 📊 Sample Output

```
Total Employees: 3
name : Ravi
id : 201
salary : 50000
dept : General
------------------------------
name : Priya
id : 202
salary : 60000
dept : HR
------------------------------
name : Arun
id : 203
salary : 45000
dept : IT
------------------------------
Department updated for Priya
Employee not found
Total Salary: 155000
Inner: modified by inner
Outer: modified by inner
```

---

✅ This project ensures students practice:

* **Return values** (`total_salary`)
* **Default params** (`dept="General"`)
* **Positional + Keyword args** (`update_department`)
* **`*args` & `**kwargs`** (`salaries`, `employee_report`)
* **Namespace & Scope (global, nonlocal)**

---

👉 Now you have **two mini-projects**:

1. **Student Grade Management System** 🏫
2. **Employee Management System** 🏢

Would you like me to also create a **combined challenge project** (e.g., *School Management System* with both students + employees\*) that uses *all these concepts together*?



#_____________________________________________________________________________________________
                    ____________PART8________________
_____________________________________________________________________________________________




Got it 👍 You want **practice exercises for creating functions in Python**.
I’ll give you a mix of beginner → intermediate → advanced problems so you can practice step by step.

---

## 🔹 Beginner Level

These will help you get comfortable with **defining functions, parameters, and return values**.

1. **Simple Greeting**
   Write a function `greet()` that prints `"Hello, welcome to Python!"`.

2. **Square of a Number**
   Write a function `square(num)` that returns the square of a number.

3. **Even or Odd**
   Write a function `check_even_odd(n)` that prints whether a number is even or odd.

4. **Sum of Two Numbers**
   Write a function `add(a, b)` that returns the sum of two numbers.

5. **Factorial**
   Write a function `factorial(n)` that returns the factorial of `n`.



   def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example
print(factorial(5))  # Output: 120


---

## 🔹 Intermediate Level

Here you’ll practice with **default arguments, multiple return values, and recursion**.

6. **Find Maximum**
   Write a function `find_max(a, b, c)` that returns the largest of three numbers.

7. **Default Arguments**
   Write a function `power(base, exp=2)` that returns base raised to the exponent.
   (Default exponent is 2 → square).

8. **Prime Number Check**
   Write a function `is_prime(n)` that returns `True` if the number is prime, otherwise `False`.

9. **Reverse a String**
   Write a function `reverse_string(s)` that returns the reversed string.

10. **Fibonacci (Recursive)**
    Write a recursive function `fibonacci(n)` that returns the `n`th Fibonacci number.

---

## 🔹 Advanced Level

These will push you towards **lambda functions, higher-order functions, and problem-solving**.

11. **Palindrome Check**
    Write a function `is_palindrome(s)` that returns `True` if the string is a palindrome.

12. **Calculator Function**
    Write a function `calculator(a, b, op)` where `op` can be `"add"`, `"sub"`, `"mul"`, `"div"`.
    The function should return the result.

13. **Lambda + Map/Filter**

* Use `map` with a lambda to square all numbers in a list.
* Use `filter` with a lambda to get even numbers from a list.

14. **Recursive Sum of Digits**
    Write a recursive function `sum_of_digits(n)` that returns the sum of digits of `n`.
    (Example: `sum_of_digits(1234) → 10`)

15. **Anagram Check**
    Write a function `is_anagram(str1, str2)` that returns `True` if both strings are anagrams.

---

👉 Do you want me to **give you solutions with explanations** for these exercises,
or do you prefer to **try them yourself first** and then I’ll check your answers?






Got it 👍 Let’s go one by one with clear Python implementations for each:

---

### **11. Palindrome Check**

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # normalize: ignore case & spaces
    return s == s[::-1]

# Example
print(is_palindrome("madam"))    # True
print(is_palindrome("hello"))    # False
```

---

### **12. Calculator Function**

```python
def calculator(a, b, op):
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"

# Example
print(calculator(10, 5, "add"))  # 15
print(calculator(10, 5, "div"))  # 2.0
```

---

### **13. Lambda + Map/Filter**

```python
# Square numbers using map + lambda
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# Even numbers using filter + lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
```

---

### **14. Recursive Sum of Digits**

```python
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

# Example
print(sum_of_digits(1234))  # 10
print(sum_of_digits(987))   # 24
```

---

### **15. Anagram Check**

```python
def is_anagram(str1, str2):
    return sorted(str1.lower().replace(" ", "")) == sorted(str2.lower().replace(" ", ""))

# Example
print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello", "world"))     # False
```

---

✅ These are clean, ready-to-use solutions.

Do you also want me to **combine all into one Python script** with test cases for each, so you can run it directly?


What is Anagram?

Anagram-nu sollumbothu, oru word oda letters-a rearrange pannitu innooru valid word create pannurathu.
Adhuvum same letters use pannikanum, count kooda same-a irukanum.




Okay 🙂 let me explain in **Tunglish (Tamil + English mix)** style:

---

### **What is Anagram?**

Anagram-nu sollumbothu, oru word oda letters-a **rearrange** pannitu innooru valid word create pannurathu.
Adhuvum **same letters use pannikanum, count kooda same-a irukanum**.

---

### **Example**

* `"listen"` → rearrange panna `"silent"` aagum ✅
* `"evil"` → rearrange panna `"vile"` aagum ✅
* `"hello"` → `"world"` panna mudiyadhu ❌ (letters match aagala)

---

### **How your function works?**

```python
def is_anagram(str1, str2):
    return sorted(str1.lower().replace(" ", "")) == sorted(str2.lower().replace(" ", ""))
```

1. `str1.lower().replace(" ", "")`
   → ellaa letters-um lowercase-la convert pannidurom, space remove pannidurom.

   Example: `"Listen"` → `"listen"`

2. `sorted(str1...)`
   → letters-a sort panna:
   `"listen"` → `['e','i','l','n','s','t']`
   `"silent"` → `['e','i','l','n','s','t']`

3. Compare both sorted lists.
   Same-a irundhaa `True`, illa `False`.

---

### **Output**

```python
print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello", "world"))     # False
```

---

💡 So in short:
**Anagram na oru word oda letters use pannitu vera word form pannurathu.**

---

Do you want naan **5 real-life anagram examples** (fun words) kudukkanumaa for students?





Super 👍 inga **5 real-life anagram examples** kudukiren (students ku easy-ah puriyum mathiri):

---

### 🔹 Example 1

**Word:** `listen`
**Anagram:** `silent`

➡️ Rendu perum same letters use panniduchu, just order maari irukku.

---

### 🔹 Example 2

**Word:** `earth`
**Anagram:** `heart`

➡️ Same letters rearrange panna new word form aagum.

---

### 🔹 Example 3

**Word:** `save`
**Anagram:** `vase`

➡️ Simple, letters order mattum change.

---

### 🔹 Example 4

**Word:** `night`
**Anagram:** `thing`

➡️ Both words different meaning but same letters.

---

### 🔹 Example 5

**Word:** `race`
**Anagram:** `care`

➡️ Nice and easy one.

---

👉 Ithula oru fun activity pannalaam: students kitte words kuduthu **"anagram find pannunga"** nu challenge kudutha, avanga ku romba interest varum.

Naan unga students ku oru **mini exercise sheet** prepare panniduvenaa (fill in the blanks type with anagrams)?
