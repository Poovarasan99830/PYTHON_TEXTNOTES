-

## 🔹 What is an Exception?

An **exception** is an event that occurs during program execution that disrupts the normal flow of instructions.
Examples:

* Division by zero (`ZeroDivisionError`)
* Accessing an invalid index (`IndexError`)
* Opening a non-existent file (`FileNotFoundError`)

---

## 🔹 Why Use Exception Handling?

* To **prevent program crashes**.
* To **handle errors gracefully** and continue execution.
* To **give meaningful error messages** instead of Python’s default traceback.

---

## 🔹 Syntax of `try-except`

```python
try:
    # Code that may cause an exception
    risky_code = 10 / 0
except ZeroDivisionError:
    # Code to handle exception
    print("You cannot divide by zero!")
```

✅ Output:

```
You cannot divide by zero!
```

---

## 🔹 Multiple `except` Blocks

You can catch different exceptions separately:

```python
try:
    num = int("abc")  # ValueError
except ValueError:
    print("Invalid input, please enter a number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

---

## 🔹 Catching All Exceptions

```python
try:
    x = 10 / 0
except Exception as e:
    print("Error:", e)
```

✅ Output:

```
Error: division by zero
```

---

## 🔹 Using `else`

If no exception occurs, the `else` block runs:

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Division error")
else:
    print("Division successful:", x)
```

---

## 🔹 Using `finally`

The `finally` block **always runs** (useful for cleanup like closing files or database connections).

```python
try:
    f = open("data.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution finished.")
```

---

## 🔹 Raising Exceptions

You can raise exceptions manually using `raise`:

```python
age = -5
if age < 0:
    raise ValueError("Age cannot be negative")
```

---

## 🔹 Custom Exceptions

You can define your own exception classes:

```python
class NegativeAgeError(Exception):
    pass

age = -3
try:
    if age < 0:
        raise NegativeAgeError("Age cannot be negative")
except NegativeAgeError as e:
    print("Custom Exception:", e)
```

---

✅ **Summary**

* `try` → code that may cause error
* `except` → handles error
* `else` → runs if no error
* `finally` → runs no matter what
* `raise` → throw exception
* `Custom Exception` → create your own error types

---

Do you want me to also prepare **exercises with solutions** on Python exceptions (like I did for strings and sets), so your students can practice?
