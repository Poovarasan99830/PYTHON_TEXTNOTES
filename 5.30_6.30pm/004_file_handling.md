Super! 👍 You gave me a **list of File Handling + Error Handling tasks**.
Na unga ku **Python solution** code + **Thunglish (Tamil + English) explanation** kudukaren.

---

# 🔹 **File Handling Tasks**

### 1. Basic File Operations

```python
# Create file and write name
with open("mydata.txt", "w") as f:
    f.write("My name is Poovarasan\n")

# Read file
with open("mydata.txt", "r") as f:
    print("File content:\n", f.read())

# Append age
with open("mydata.txt", "a") as f:
    f.write("Age: 25\n")
```

👉 **Thunglish explain**:

* `"w"` → write mode (old content erase pannidum).
* `"r"` → read mode.
* `"a"` → append mode (old content ku new add pannum).

---

### 2. Line Processing

```python
# Print each line with line number
with open("sample.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"Line {i}: {line.strip()}")

# Count words, chars, lines
with open("sample.txt", "r") as f:
    text = f.read()
    words = text.split()
    print("Lines:", text.count("\n") + 1)
    print("Words:", len(words))
    print("Characters:", len(text))
```

👉 **Thunglish**:

* `enumerate` → line number auto count pannum.
* `split()` → words separate aagum.
* `len(text)` → character count.

---

### 3. Search in File

```python
# Count word occurrence
word = "python"
count = 0
with open("sample.txt", "r") as f:
    for line in f:
        count += line.lower().count(word.lower())
print(f"'{word}' appears {count} times")

# Replace word
with open("sample.txt", "r") as f:
    text = f.read()

text = text.replace("python", "java")

with open("sample.txt", "w") as f:
    f.write(text)
```

👉 **Thunglish**:

* `.count(word)` → epdi oru word occur aaguthu nu count pannum.
* `.replace("old", "new")` → word replace aagum.

---

### 4. Copying & Merging

```python
# Copy file
with open("file1.txt", "r") as f1, open("file2.txt", "w") as f2:
    f2.write(f1.read())

# Merge files
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as f3:
    f3.write(f1.read() + "\n" + f2.read())
```

👉 **Thunglish**:

* Read file1 content → write file2 la copy panna.
* Two file content join → third file la merge panna.

---

### 5. CSV Handling

```python
import csv

# Read CSV and average
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    total, count = 0, 0
    for row in reader:
        total += int(row[1])
        count += 1
    print("Average Marks:", total/count)

# Add new student
with open("students.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Arun", 88])
```

👉 **Thunglish**:

* `csv.reader` → file read pannum.
* `csv.writer` → new data write/add pannum.

---

# 🔹 **Error Handling Tasks**

### 1. Basic Try-Except

```python
# Division by zero
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero not allowed")

# Invalid input
try:
    n = int(input("Enter a number: "))
    print("Square:", n*n)
except ValueError:
    print("Error: Invalid number")
```

👉 **Thunglish**:

* `try-except` use panna runtime error crash aagala.

---

### 2. Multiple Exceptions

```python
try:
    a = int(input("Enter num1: "))
    b = int(input("Enter num2: "))
    print("Result:", a / b)
except ValueError:
    print("Error: Invalid input")
except ZeroDivisionError:
    print("Error: Division by zero not allowed")
```

---

### 3. File Error Handling

```python
# File not found
try:
    with open("nofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")

# Permission error
try:
    with open("/system/protected.txt", "w") as f:
        f.write("test")
except PermissionError:
    print("Permission denied.")
```

---

### 4. Custom Exceptions

```python
class NegativeValueError(Exception):
    pass

def check_number(n):
    if n < 0:
        raise NegativeValueError("Negative number not allowed")
    return n

try:
    print(check_number(-5))
except NegativeValueError as e:
    print("Error:", e)


class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError("Invalid age entered")
    return age

try:
    print(check_age(200))
except InvalidAgeError as e:
    print("Error:", e)
```

---

### 5. Finally Block

```python
try:
    f = open("sample.txt", "r")
    print(f.read())
finally:
    f.close()
    print("File closed safely")
```

---

# 🔹 **Combined Tasks**

### 1. Read File + Count Words + Error Handling

```python
try:
    with open("sample.txt", "r") as f:
        text = f.read()
        if not text.strip():
            raise ValueError("File is empty")
        print("Word count:", len(text.split()))
except FileNotFoundError:
    print("Error: File not found")
except ValueError as e:
    print("Error:", e)
```

---

### 2. Student Data with Grades

```python
try:
    with open("students.txt", "r") as f:
        for line in f:
            name, marks = line.strip().split(",")
            try:
                marks = int(marks)
            except ValueError:
                print(f"Invalid marks for {name}")
                continue

            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 50:
                grade = "C"
            else:
                grade = "F"

            print(f"{name} -> {grade}")
except FileNotFoundError:
    print("Error: Student file not found")
```

---

✅ With this you can **practice file handling + error handling** tasks easily.
👉 Do you want me to create a **single Python practice file** with all these tasks together (so you can run one by one)?
