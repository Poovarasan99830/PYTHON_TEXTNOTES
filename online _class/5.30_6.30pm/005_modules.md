
Python Important Modules & Tools – One-Liner Summary

# PART1 ->  OS → Files, folders, environment variables handle panna.

# PART2 -> Random → Random numbers & data generate panna.

# PART3 -> Datetime → Date & time create, format, calculate panna.

# PART4  -> Requests → Internet communication (API calls, web data fetch).

# PART5 -> pip → Library manager (install, update, remove external packages).

# PART6 -->TASK


___________________________________________________________________________________

_______________________________PART1____________________________________________________


## 🔹 `os` Module in Python – 360° View

### 1. **Definition**

* `os` module → Python oda **interface to Operating System**.
* Files, directories, processes, environment variables ellam control panna use aagum.

---

### 2. **Key Features (with one-liner use)**

1. **Working Directory**

   ```python
   import os
   print(os.getcwd())   # Current directory path
   os.chdir("C:/Users") # Change working directory
   ```

   👉 *Analogy*: “Ippo naan enga irukken?” → `os.getcwd()` sollum.

2. **File & Directory Handling**

   ```python
   os.mkdir("test")       # Create folder
   os.makedirs("a/b/c")   # Create nested folders
   os.listdir(".")        # List all files/folders
   os.remove("file.txt")  # Delete a file
   os.rmdir("test")       # Delete empty folder
   import shutil
   shutil.rmtree("folder_name")  #delete a non-empty directory

   ```

   👉 *Analogy*: Files & cupboards manage panra servant maadhiri.

3. **Path Handling (`os.path`)**

   ```python
   from os import path
   print(path.exists("file.txt"))   # File iruka?
   print(path.join("folder", "a.txt")) # Safe path combine
   print(path.abspath("file.txt"))  # Absolute path
   ``
   
   
   
 import os
from os import path

print("Current Directory:", os.getcwd())
print("Absolute Path:", path.abspath("file.txt"))

| Term           | Meaning                                                |
| -------------- | ------------------------------------------------------ |
| `path`         | Submodule from `os` for path operations                |
| `abspath()`    | Converts relative path → absolute path                 |
| Example Output | Full path like `C:\Users\Poovarasan\Projects\file.txt` |
  `

# ___________________________________________________________________________________
from os import path


folder = "reports"
year = "2025"
filename = "john.txt"

file_path = path.join(folder, year, filename)
print(file_path)

 👉 *Analogy*: Google Maps la “full address vs short route” nu paatha maadhiri.


 
# ___________________________________________________________________________________

path.join() = path string build pannum (OS safe ah).

File create panna vendumna → open() or makedirs() use panna vendum.

Automatically file/folder add pannaathu.




# ___________________________________________________________________________________

Real-time Use Cases

File Uploads in Flask/Django → User upload panna file correct folder la save panna.

Log Files → logs/2025/error.log path safe ah build pannum.

Cross-Platform Projects → Windows/Linux both la run panna vendum nu irundha.

Dynamic Folders → Year-wise, user-wise, category-wise folders generate panna.



# ___________________________________________________________________________________



4. **Environment Variables**

   ```python
   print(os.environ.get("PATH"))     # PATH env variable
   os.environ["MYAPP"] = "TestApp"   # New env var set
   ```

   👉 *Analogy*: Passport la stored personal info maadhiri system details.


   Super 👍 neenga **environment variables** ku analogy passport la personal info maadhiri nu sonninga — athu correct ah irukku 👏.
Naan ippo Tunglish la **clear ah** explain panren:

---

## 🔎 What are Environment Variables?

* System level la store pannirukkira **key–value pairs**.
* OS la programs ku **settings / system info** kudukkum.
* Example: PATH, USER, HOME, TEMP, etc.

👉 Passport la personal details store pannirukkara maadhiri,
environment variables system details store pannum.

---

## 📝 Example Code

```python
import os

# Get existing environment variable
print(os.environ.get("PATH"))  # System PATH variable

# Set new environment variable (runtime only)
os.environ["MYAPP"] = "TestApp"
print(os.environ.get("MYAPP"))
```

### Output (sample):

```
C:\Windows\System32;C:\Python39;...
TestApp
```

---

## 🎯 Why is it used?

### 1. **PATH Variable**

* PATH la programs / executables path store pannirukkum.
* Example: `python` nu type panna terminal la → PATH la irukkira python.exe location open aagum.

---

### 2. **Sensitive Data Store**

* Database password, API keys direct code la potta risk.
* Safe ah environment variable la store pannalaam.

```python
os.environ["DB_PASSWORD"] = "secret123"
print(os.environ.get("DB_PASSWORD"))
```

---

### 3. **Cross-Platform Config**

* Windows la oru value, Linux la inoru value set pannalaam.
* Program path difference handle panna easy.

---

### 4. **Temporary Settings (Runtime)**

* Script run pannumbothu temporary values kudukkalaam.
* Example: Testing ku `DEBUG=1` set panna.

---

## 🔑 Simple Analogy

* **Passport** → Personal details (Name, DOB, Address) store.
* **Environment variables** → System details (PATH, USER, DB\_PASSWORD) store.
* Program run aagumbothu → system indha info kudukkum.

---

👉 So usage:

* **PATH → executables locate panna**
* **Config → DB, API keys store panna**
* **Portable apps → OS la settings read panna**


# ___________________________________________________________________________________



5. **Process Management**

   ```python
   print(os.getpid())      # Current process ID
   os.system("dir")        # Run system command (Windows)
   os.system("ls -l")      # Run command (Linux/Mac)
   ```

   👉 *Analogy*: Boss → servant ku “poo poi pannu” nu command kudukkara maadhiri.

---

### 3. **Thunglish Analogy**

`os` module-na oru **bridge** maadhiri irukkum → Python oda code → OS kitta sollum:

* “File open pannu”
* “Folder create pannu”
* “Enna directory la irukken nu sollu”
* “Environment la enna details irukku?”

---

### 4. **When to Use**

* Files/folders manage panna.
* System info fetch panna.
* Path resolve panna (cross-platform safe).
* Automation scripts (cleaning folders, log handling).

---



___________________________________________________________________________________

_______________________________PART2____________________________________________________





## 🔹 `random` Module in Python – 360° View

### 1. **Definition**

* `random` module → **Random number & data generate panna** Python library.
* Mainly **simulations, testing, games, cryptography (basic level)** la use aagum.

---

### 2. **Key Functions**

#### ✅ Basic Random Numbers

```python
import random

print(random.random())   # 0.0 ≤ x < 1.0 (float)
print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.uniform(1, 5))   # Random float between 1 and 5
```

👉 *Analogy*: Dice throw pannina maadhiri unpredictable number.

---

#### ✅ Random Choices from Sequence

```python
items = ["apple", "banana", "cherry"]
print(random.choice(items))        # One random item
print(random.choices(items, k=2))  # Multiple with replacement
print(random.sample(items, 2))     # Multiple without replacement
```

👉 *Analogy*: Basket la fruits irundha oru random fruit pick panra maadhiri.

---

#### ✅ Shuffle Data

```python
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)   # Shuffle order
print(cards)
```

👉 *Analogy*: Cards shuffle pannura dealer maadhiri.

---

#### ✅ Reproducibility with `seed()`

```python
random.seed(10)
print(random.randint(1, 100))  # Same output every time with same seed
```

👉 *Analogy*: Same seed kudutha same crop varum maadhiri. Seed fix panna, randomness repeatable aagum.

---

### 3. **Use Cases**

* **Games** → Dice roll, card shuffle.
* **Simulations** → Probability, experiments.
* **Data Science/ML** → Random sampling & train/test split.
* **Testing** → Random test data generate.

---

### 4. **Thunglish Analogy**

`random` module-na oru **lottery machine** maadhiri.

* Ticket numbers maadhiri random numbers generate pannum.
* Basket la irundhu random fruits choose pannum.
* Cards shuffle maadhiri list shuffle pannum.

---




___________________________________________________________________________________

_______________________________PART3____________________________________________________





## 🔹 `datetime` Module – 360° View

👉 *"Date & time create, format, calculate panna use aagum."*

### 1. **Create & Get Current Date/Time**

```python
import datetime

now = datetime.datetime.now()
today = datetime.date.today()
print(now)    # 2025-08-31 10:30:15
print(today)  # 2025-08-31
```

### 2. **Formatting Dates**

```python
print(now.strftime("%d-%m-%Y %H:%M:%S"))  # 31-08-2025 10:30:15
```

### 3. **Parsing Strings to Date**

```python
dt = datetime.datetime.strptime("31-08-2025", "%d-%m-%Y")
print(dt)  # 2025-08-31 00:00:00
```

### 4. **Date Calculations**

```python
from datetime import timedelta

tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print(tomorrow, yesterday)
```

👉 *Analogy*: Calendar + Clock app maadhiri work pannum.




___________________________________________________________________________________

_______________________________PART4____________________________________________________

---

## 🔹 `requests` Module – 360° View

👉 *"Internet communication (API calls, web data fetch)."*

### 1. **Basic GET Request**

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json())
```

### 2. **POST Request**

```python
data = {"name": "Poovarasan", "job": "Developer"}
res = requests.post("https://reqres.in/api/users", data=data)
print(res.json())
```

### 3. **Handling Status Codes**

```python
if response.status_code == 200:
    print("Success!")
else:
    print("Error:", response.status_code)
```

👉 *Analogy*: Browser maadhiri website/API kitta poi data fetch pannum.

-



___________________________________________________________________________________

_______________________________PART5____________________________________________________


## 🔹 `pip` – 360° View

👉 *"Python library manager – install, update, remove external packages."*

### 1. **Install a Package**

```bash
pip install requests
```

### 2. **Upgrade a Package**

```bash
pip install --upgrade requests
```

### 3. **Uninstall a Package**

```bash
pip uninstall requests
```

### 4. **Freeze Installed Packages**

```bash
pip freeze > requirements.txt
```

👉 *Analogy*: App Store / Play Store maadhiri – Python ku apps (libraries) download & update pannura tool.

---

✨ Ippo unga note full 360° aachu:

* **datetime →** Calendar + Clock
* **requests →** Browser / Postman maadhiri communication
* **pip →** App Store maadhiri library manager





___________________________________________________________________________________

_______________________________PART6 ____________________________________________________
Super 👍 neenga already **360° notes** prepare panniteenga!
Ippa naan unga **students ku hands-on tasks** ready panren.
Each module ku **concept-based tasks** kudukuren (easy → medium → real-world type).

---

# 🔹 **Tasks for Students (Module-wise)**

---

## 🟢 PART1 – `os` Module Tasks

1. **Working Directory**

   * Task: Write a program to print the current working directory and then change it to another folder in your system.

2. **File & Folder Handling**

   * Task: Create a folder called `"School"`, inside it create `"Students"` folder, then delete `"Students"` folder.

3. **Path Handling**

   * Task: Ask user for a filename, check if the file exists, and if yes → print its absolute path.

4. **Environment Variables**

   * Task: Print the `PATH` environment variable. Then, set a new environment variable called `"MY_PROJECT"`.

5. **Process Management**

   * Task: Run a system command (`dir` in Windows or `ls` in Linux) using Python and display the output.

👉 *Mini Project*: Create a script that automatically creates a `"Logs"` folder and saves today’s date as a filename (`31-08-2025.txt`) inside it.

---

## 🟢 PART2 – `random` Module Tasks

1. **Basic Random Numbers**

   * Task: Generate 10 random integers between 1 and 50.

2. **Random Choices**

   * Task: Create a fruit basket list and pick 3 random fruits.

3. **Shuffle**

   * Task: Create a list of numbers 1–10, shuffle it, and print the new order.

4. **Seed**

   * Task: Use a fixed seed (e.g., 100) and generate random numbers. Run multiple times and confirm same output.

👉 *Mini Project*: Create a simple **lottery system** where user enters their name → program randomly selects a winner from a list.

---

## 🟢 PART3 – `datetime` Module Tasks

1. **Current Date & Time**

   * Task: Print today’s date and time in `DD-MM-YYYY HH:MM:SS` format.

2. **Formatting**

   * Task: Display current month name (e.g., `"August"`) and weekday name (e.g., `"Sunday"`).

3. **Parsing**

   * Task: Convert `"01-01-2026"` string into a datetime object and print it.

4. **Date Calculation**

   * Task: Calculate how many days are left until New Year from today.

👉 *Mini Project*: Ask user’s **date of birth** → print how many days they have lived till today.

---

## 🟢 PART4 – `requests` Module Tasks

1. **Basic GET**

   * Task: Fetch data from `https://jsonplaceholder.typicode.com/posts/1` and print only `"title"`.

2. **POST**

   * Task: Send a fake user record (name + job) to `https://reqres.in/api/users` and print the response.

3. **Status Code**

   * Task: Write a function that checks if a website is up or down (200 → “Website is live”, else “Website is down”).

👉 *Mini Project*: Create a small program that fetches **current weather data** for a city using OpenWeather API (or any free API).

---

## 🟢 PART5 – `pip` Tasks

1. **Install**

   * Task: Install `requests` library using pip.

2. **Upgrade**

   * Task: Upgrade an existing library (e.g., `pip install --upgrade requests`).

3. **Uninstall**

   * Task: Uninstall `requests` library (then reinstall).

4. **Freeze**

   * Task: Generate a `requirements.txt` file for your environment.

👉 *Mini Project*: Create a **requirements.txt** for your mini projects above, and share it with classmates to reproduce your environment.

---

✅ **Summary of Student Practice Flow**

* **os → File automation project**
* **random → Lottery / Game project**
* **datetime → Birthday calculator project**
* **requests → Weather API project**
* **pip → Requirements management**

---

Do you want me to prepare this in a **day-wise lab plan (like 5 days = 5 modules with mini-projects at end)** so students can follow step by step?













_______________________________PART 6____________________________________________________



Super sir 👍 Naan ippo unga **ART1 – `os` Module Tasks** ku full working Python answers ready ah kodukaren.
Neenga Windows/Linux both la try panna mudiyum (some commands system dependent).

---

## 🔹 1. **Working Directory**

```python
import os

# Print current working directory
print("Current Directory:", os.getcwd())

# Change directory (update path according to your system)
new_path = "C:\\Users"   # Windows Example
# new_path = "/home/user"  # Linux Example
os.chdir(new_path)

print("Changed Directory:", os.getcwd())
```

---

## 🔹 2. **File & Folder Handling**

```python
import os

# Create folder "School"
os.mkdir("School")

# Create subfolder "Students"
os.mkdir("School/Students")

print("Folders created successfully.")

# Remove "Students" folder
os.rmdir("School/Students")

print("Students folder deleted.")
```

---

## 🔹 3. **Path Handling**

```python
import os

filename = input("Enter a filename: ")

if os.path.exists(filename):
    print("File exists.")
    print("Absolute Path:", os.path.abspath(filename))
else:
    print("File does not exist.")
```

---________________________________________________________________________________

## 🔹 4. **Environment Variables**

```python
import os

# Print PATH variable
print("PATH Variable:", os.environ.get("PATH"))

# Set new environment variable
os.environ["MY_PROJECT"] = "Python_OS_Module"

print("MY_PROJECT Variable:", os.environ.get("MY_PROJECT"))
```

⚠️ Note: Setting environment variables with `os.environ` is **temporary** (only for the current Python process). If you restart Python, variable will reset.





### 🎓 **School Analogy for Environment Variables**

1. **School Notice Board = Environment Variable Store**

   * In a school, notice board la **important information** paste pannuvanga (exam dates, holidays, events).
   * System la, **environment variables** ah use pannitu, OS and programs ku **important path/info** store pannuvom (like PATH, JAVA\_HOME, PYTHONPATH).

---

2. **PATH Variable = Route Map**

   * Suppose neenga “Library ku po” nu sonna, but **exact route** board la mention pannirukkuna → student easy-ah poi mudichiduvan.
   * Same maadhiri, PATH variable system ku sollum → “Program run panna enna enna locations la search panna vendum”.

---

3. **New Notice (MY\_PROJECT) = Temporary Information**

   * Teacher notice board la temporary note potta: *“Tomorrow bring graph paper”*.
   * Adhu next day remove panniduvanga → permanent ah irukkadhu.
   * Same maadhiri, neenga `os.environ["MY_PROJECT"] = "Python_OS_Module"` nu set panna, adhu **temporary variable**, program run aagirukkum time la mattum irukkum.

---

4. **Permanent Notice = Permanent Environment Variable**

   * Annual function date paste panna → adhu long time ku irukkum.
   * System la permanent environment variables set panna neenga settings la (Windows/Linux) save panna vendum.

---

👉 **Simple Summary in Tunglish:**

* **Notice Board = Environment Variables**
* **PATH = Shortcut/Route Map**
* **Temporary Notice = `os.environ` variable (only current program ku valid)**
* **Permanent Notice = System la set pannina permanent variables**

---

Sir, unga students ku naan oru **mini activity** create pannalaamaa?
Eg: “School Notice Board” analogy use pannitu, avanga ku **draw and label environment variable chart** task kuduthaa, romba fun-ahum puriyum-ahum irukkum.

---_____________________________________________________________________________________

## 🔹 5. **Process Management**

```python
import os

# Windows
os.system("dir")

# Linux/Mac
# os.system("ls")
```
"dir" command enna pannum? → Current folder la irukkura files and folders list show pannum.
---










_______________________________PART6 (Task-explalaination)  ____________________________________________________



Super 👍 Naan unga ku **PART2 – `random` Module Tasks** full answers ready ah kodukaren.

---

## 🔹 1. **Basic Random Numbers**

```python
import random

# Generate 10 random integers between 1 and 50
for _ in range(10):
    print(random.randint(1, 50))
```

---

## 🔹 2. **Random Choices**

```python
import random

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple"]

# Pick 3 random fruits
selected = random.sample(fruits, 3)
print("Random Fruits:", selected)
```

---

## 🔹 3. **Shuffle**

```python
import random

numbers = list(range(1, 11))  # 1 to 10
print("Original:", numbers)

random.shuffle(numbers)
print("Shuffled:", numbers)
```

---

## 🔹 4. **Seed**

```python
import random

random.seed(100)  # Fix seed
for _ in range(5):
    print(random.randint(1, 100))
```

➡️ If you run this program **multiple times**, output will be **same** because of fixed seed.

---________________________________________________________________________________________








Perfect 👍
Let’s create **complete, structured notes** for **important Python modules**, following exactly your requested format:

---

# 🐍 **Important Python Modules – Full Notes**

---

## 🧩 1. `os` Module

### ➤ **Definition:**

The `os` module provides functions to interact with the operating system — like creating, deleting, navigating, and managing files and directories.

### ➤ **Real-Time Example with Code:**

```python
import os

# Create a new directory
os.mkdir("test_folder")

# List files and directories
print(os.listdir())

# Get current working directory
print(os.getcwd())

# Remove directory
os.rmdir("test_folder")
```

### ➤ **Tasks:**

1. Create a folder if not exists.
2. Rename or delete files.
3. Navigate directories dynamically.

### ➤ **Task Explanation:**

Used when your program needs to handle system-level file operations (like a file manager or data automation script).

### ➤ **Where Used:**

* File management apps
* Automation scripts
* Server file maintenance tasks

### ➤ **Levels:**

* **Beginner:** `os.getcwd()`, `os.listdir()`
* **Intermediate:** `os.rename()`, `os.remove()`
* **Advanced:** `os.walk()`, environment variable manipulation

---

## 📂 2. `sys` Module

### ➤ **Definition:**

The `sys` module gives access to system-specific parameters and functions such as command-line arguments and the Python interpreter.

### ➤ **Real-Time Example with Code:**

```python
import sys

print("Python version:", sys.version)
print("Arguments passed:", sys.argv)

# Exit the program
sys.exit("Stopping program manually")
```

### ➤ **Tasks:**

1. Handle command-line arguments.
2. Exit scripts manually.
3. Get Python runtime info.

### ➤ **Task Explanation:**

Used for controlling the interpreter, especially in CLI tools or automation scripts.

### ➤ **Where Used:**

* Command-line utilities
* Automation scripts
* Debugging and runtime monitoring

### ➤ **Levels:**

* **Beginner:** `sys.version`
* **Intermediate:** `sys.argv`
* **Advanced:** `sys.path` manipulation for imports

---


## 📅 3. `datetime` Module

### ➤ **Definition:**

Used to handle dates and times — formatting, arithmetic, and scheduling tasks.

### ➤ **Real-Time Example with Code:**

```python
from datetime import datetime, timedelta

# Current time
now = datetime.now()
print("Now:", now)

# Add 5 days
future = now + timedelta(days=5)
print("Future Date:", future)

# Format date
print(now.strftime("%d-%m-%Y %H:%M:%S"))
```

### ➤ **Tasks:**

1. Calculate difference between two dates.
2. Format timestamps for logs.
3. Schedule or delay tasks.

### ➤ **Task Explanation:**

Helpful in projects involving reports, timestamps, or scheduling.

### ➤ **Where Used:**

* Attendance tracking
* Report generation
* Time-based automation

### ➤ **Levels:**

* **Beginner:** `datetime.now()`
* **Intermediate:** `timedelta`
* **Advanced:** Timezone and localization

---


## 🔢 4. `math` Module

### ➤ **Definition:**

Provides mathematical functions like trigonometry, logarithms, and constants.

### ➤ **Real-Time Example with Code:**

```python
import math

print("Square root:", math.sqrt(16))
print("Power:", math.pow(2, 3))
print("Pi value:", math.pi)
print("Sin(90°):", math.sin(math.radians(90)))
```

### ➤ **Tasks:**

1. Perform scientific calculations.
2. Work with angles and logarithms.
3. Round or truncate numeric data.

### ➤ **Task Explanation:**

Used where precise mathematical or geometrical computations are required.

### ➤ **Where Used:**

* Engineering software
* Data science and AI
* Game development (physics)

### ➤ **Levels:**

* **Beginner:** `math.sqrt()`, `math.pi`
* **Intermediate:** `math.log()`, `math.factorial()`
* **Advanced:** `math.radians()`, `math.trunc()`

---

## 📊 5. `random` Module

### ➤ **Definition:**

Used to generate random numbers, choices, and shuffling for simulations or games.

### ➤ **Real-Time Example with Code:**

```python
import random

print("Random number:", random.randint(1, 10))
print("Random choice:", random.choice(["apple", "banana", "cherry"]))
print("Random float:", random.random())

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled:", numbers)
```

### ➤ **Tasks:**

1. Generate random test data.
2. Shuffle elements randomly.
3. Select random samples.

### ➤ **Task Explanation:**

Used in scenarios requiring unpredictability (like password generation or gaming).

### ➤ **Where Used:**

* Games
* Simulations
* Testing and AI model data augmentation

### ➤ **Levels:**

* **Beginner:** `random.randint()`
* **Intermediate:** `random.choice()`
* **Advanced:** `random.sample()`, `random.shuffle()`

---

## 🌐 6. `requests` Module *(3rd party)*

### ➤ **Definition:**

Simplifies sending HTTP requests (GET, POST, PUT, DELETE) to web APIs.

### ➤ **Real-Time Example with Code:**

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()
print(data)
```

### ➤ **Tasks:**

1. Connect to web APIs.
2. Send and receive JSON data.
3. Automate website interactions.

### ➤ **Task Explanation:**

Essential for backend communication with external APIs or services.

### ➤ **Where Used:**

* Web scraping
* API integration
* Chatbots and automation

### ➤ **Levels:**

* **Beginner:** `requests.get()`
* **Intermediate:** `requests.post()`
* **Advanced:** Authentication, headers, and sessions

---

## 🧮 7. `pandas` Module

### ➤ **Definition:**

Powerful library for data manipulation and analysis using DataFrames.

### ➤ **Real-Time Example with Code:**

```python
import pandas as pd

data = {"Name": ["A", "B", "C"], "Score": [90, 80, 85]}
df = pd.DataFrame(data)
print(df)

# Filter
print(df[df["Score"] > 80])
```

### ➤ **Tasks:**

1. Load, clean, and analyze data.
2. Perform operations like group, merge, sort.
3. Export results to CSV or Excel.

### ➤ **Task Explanation:**

Used widely in data science, ML pipelines, and reporting dashboards.

### ➤ **Where Used:**

* Data analysis
* Machine Learning preprocessing
* Business intelligence tools

### ➤ **Levels:**

* **Beginner:** Create DataFrames
* **Intermediate:** Filter, sort, groupby
* **Advanced:** Merge, join, pivot tables

---

## 💾 8. `json` Module

### ➤ **Definition:**

Used for encoding and decoding JSON (JavaScript Object Notation) data.

### ➤ **Real-Time Example with Code:**

```python
import json

person = {"name": "Poovarasan", "age": 25}
# Convert to JSON string
json_data = json.dumps(person)

# Convert back to Python object
decoded = json.loads(json_data)

print(json_data)
print(decoded)
```

### ➤ **Tasks:**

1. Save data in JSON format.
2. Parse API responses.
3. Serialize or deserialize Python objects.

### ➤ **Task Explanation:**

Bridges the gap between Python and web communication (API or frontend).

### ➤ **Where Used:**

* APIs
* Config files
* Data serialization

### ➤ **Levels:**

* **Beginner:** `json.dumps()`, `json.loads()`
* **Intermediate:** Read/write JSON files
* **Advanced:** Custom encoders/decoders

---

Would you like me to continue with **more advanced modules** (like `re`, `subprocess`, `logging`, `threading`, `sqlite3`, etc.) in the same format for a **complete “Python Module Notes Book”** (PDF-ready version)?


Perfect 💯

Let’s continue and **complete your “Python Important Modules – Full Notes”** in the same structured and exam-ready format.
This section covers **advanced and high-utility modules** every developer must know.

---

# 🧠 **Important Python Modules – Part 2 (Advanced & Common Use)**

---

## 🔍 9. `re` Module (Regular Expressions)

### ➤ **Definition:**

The `re` module handles text pattern matching using **regular expressions** (powerful for searching, validating, or replacing strings).

### ➤ **Real-Time Example with Code:**

```python
import re

text = "My email is example123@gmail.com"
pattern = r"[a-zA-Z0-9._]+@[a-z]+\.[a-z]+"

match = re.search(pattern, text)
if match:
    print("Email found:", match.group())
```

### ➤ **Tasks:**

1. Validate emails, phone numbers, or passwords.
2. Extract data from messy text.
3. Replace unwanted patterns.

### ➤ **Task Explanation:**

Used in form validation, text cleaning, and NLP preprocessing.

### ➤ **Where Used:**

* Data extraction (web scraping)
* Validation in backend forms
* Log file analysis

### ➤ **Levels:**

* **Beginner:** `re.search()`, `re.match()`
* **Intermediate:** `re.findall()`, `re.sub()`
* **Advanced:** Compiling regex patterns for performance

---

## ⚙️ 10. `subprocess` Module

### ➤ **Definition:**

Allows you to **run external system commands** (like shell or terminal commands) directly from Python.

### ➤ **Real-Time Example with Code:**

```python
import subprocess

# Run system command
result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
print(result.stdout)
```

### ➤ **Tasks:**

1. Automate shell commands.
2. Create system-level scripts.
3. Integrate Python with other software.

### ➤ **Task Explanation:**

Helps in DevOps automation, file backups, or deployment scripting.

### ➤ **Where Used:**

* DevOps automation
* Script orchestration
* System admin tasks

### ➤ **Levels:**

* **Beginner:** `subprocess.run()`
* **Intermediate:** `capture_output=True`
* **Advanced:** Piping and error handling

---

## 🧾 11. `logging` Module

### ➤ **Definition:**

Used to record program execution details — helps in debugging, monitoring, and auditing.

### ➤ **Real-Time Example with Code:**

```python
import logging

logging.basicConfig(level=logging.INFO, filename="app.log", filemode="w")
logging.info("Application started")
logging.warning("Low memory warning")
logging.error("An error occurred!")
```

### ➤ **Tasks:**

1. Record runtime events or errors.
2. Create system logs for debugging.
3. Maintain logs in production apps.

### ➤ **Task Explanation:**

Essential for production environments to track system behavior and diagnose issues.

### ➤ **Where Used:**

* Web servers
* APIs and backend apps
* Machine learning pipelines

### ➤ **Levels:**

* **Beginner:** `logging.info()`, `logging.error()`
* **Intermediate:** Log file creation
* **Advanced:** Custom log formatters and handlers

---

## 🧵 12. `threading` Module

### ➤ **Definition:**

Enables **multithreading** — running multiple tasks (threads) concurrently in a single process.

### ➤ **Real-Time Example with Code:**

```python
import threading
import time

def greet(name):
    print(f"Hello {name}")
    time.sleep(2)
    print(f"Goodbye {name}")

t1 = threading.Thread(target=greet, args=("Poovarasan",))
t2 = threading.Thread(target=greet, args=("AI System",))

t1.start()
t2.start()
t1.join()
t2.join()
```

### ➤ **Tasks:**

1. Run background tasks.
2. Handle multiple requests at once.
3. Improve performance in I/O-bound programs.

### ➤ **Task Explanation:**

Used to speed up programs where tasks can run in parallel.

### ➤ **Where Used:**

* Web servers
* Chatbots
* Background data processing

### ➤ **Levels:**

* **Beginner:** Create threads
* **Intermediate:** `join()`, `start()`
* **Advanced:** Thread synchronization (Locks)

---

## 🗄️ 13. `sqlite3` Module

### ➤ **Definition:**

Provides an inbuilt **lightweight SQL database** engine — no external server required.

### ➤ **Real-Time Example with Code:**

```python
import sqlite3

# Connect and create table
conn = sqlite3.connect("students.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER, name TEXT)")
cur.execute("INSERT INTO student VALUES (1, 'Poovarasan')")
conn.commit()

# Fetch data
cur.execute("SELECT * FROM student")
print(cur.fetchall())

conn.close()
```

### ➤ **Tasks:**

1. Store structured data locally.
2. Query and filter records using SQL.
3. Build simple database-backed apps.

### ➤ **Task Explanation:**

Used as the default database in small-scale apps or prototypes.

### ➤ **Where Used:**

* Django default database
* Mobile & IoT apps
* Local data caching

### ➤ **Levels:**

* **Beginner:** Create DB, tables
* **Intermediate:** CRUD operations
* **Advanced:** Transactions & indexing

---

## 🕸️ 14. `BeautifulSoup` (from `bs4`)

### ➤ **Definition:**

Used for **web scraping** — extracting data from HTML and XML documents.

### ➤ **Real-Time Example with Code:**

```python
from bs4 import BeautifulSoup
import requests

url = "https://example.com"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")
print(soup.title.text)
```

### ➤ **Tasks:**

1. Extract data (titles, links) from web pages.
2. Parse HTML/XML files.
3. Build data scraping pipelines.

### ➤ **Task Explanation:**

Transforms raw HTML into structured data for analysis or storage.

### ➤ **Where Used:**

* Web data extraction
* Research automation
* Data analytics

### ➤ **Levels:**

* **Beginner:** Parse HTML
* **Intermediate:** Extract tags
* **Advanced:** Combine with APIs and `pandas`

---

## ☁️ 15. `smtplib` Module

### ➤ **Definition:**

Used to send emails directly through SMTP (Simple Mail Transfer Protocol).

### ➤ **Real-Time Example with Code:**

```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("This is a test email from Python!")
msg["Subject"] = "Python Email"
msg["From"] = "sender@example.com"
msg["To"] = "receiver@example.com"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("sender@example.com", "password")
    server.send_message(msg)
```

### ➤ **Tasks:**

1. Send automated emails.
2. Notify admins/users via email.
3. Create custom mail alerts.

### ➤ **Task Explanation:**

Used in applications that require notifications or reports.

### ➤ **Where Used:**

* CRM systems
* Automated alerting
* User verification systems

### ➤ **Levels:**

* **Beginner:** Connect & send email
* **Intermediate:** Email templates
* **Advanced:** Attachments, HTML mails

---

## 🧰 16. `itertools` Module

### ➤ **Definition:**

Provides fast, memory-efficient **iterator tools** for looping and combination tasks.

### ➤ **Real-Time Example with Code:**

```python
import itertools

nums = [1, 2, 3]
perms = itertools.permutations(nums)
for p in perms:
    print(p)
```

### ➤ **Tasks:**

1. Generate combinations and permutations.
2. Chain multiple iterables.
3. Efficient looping.

### ➤ **Task Explanation:**

Useful in combinatorial tasks and optimization problems.

### ➤ **Where Used:**

* Data analysis
* Algorithmic problems
* AI search spaces

### ➤ **Levels:**

* **Beginner:** `count()`, `cycle()`
* **Intermediate:** `combinations()`
* **Advanced:** Custom iterator pipelines

---

## ⚡ 17. `time` Module

### ➤ **Definition:**

Handles time-related functions like delays, timestamps, and measurements.

### ➤ **Real-Time Example with Code:**

```python
import time

print("Start")
time.sleep(2)
print("After 2 seconds:", time.ctime())
```

### ➤ **Tasks:**

1. Delay code execution.
2. Get current timestamp.
3. Measure performance.

### ➤ **Task Explanation:**

Used in automation, scheduling, and performance monitoring.

### ➤ **Where Used:**

* Task scheduling
* Logging and monitoring
* Benchmarks

### ➤ **Levels:**

* **Beginner:** `sleep()`, `ctime()`
* **Intermediate:** `time.time()`
* **Advanced:** Profiling with `perf_counter()`

---

✅ **Summary Table – Python Modules & Skill Levels**

| Module          | Purpose          | Level        | Common Use       |
| --------------- | ---------------- | ------------ | ---------------- |
| `os`            | OS operations    | Beginner–Adv | File handling    |
| `sys`           | System control   | Beginner–Adv | CLI tools        |
| `datetime`      | Date/time mgmt   | Beginner–Adv | Logging, reports |
| `math`          | Math ops         | Beginner–Adv | Games, data      |
| `random`        | Random data      | Beginner–Adv | Games, testing   |
| `requests`      | Web APIs         | Beginner–Adv | Backend          |
| `pandas`        | Data analysis    | Beginner–Adv | Data science     |
| `json`          | Data exchange    | Beginner–Adv | APIs             |
| `re`            | Pattern matching | Beginner–Adv | Text processing  |
| `logging`       | Debugging logs   | Beginner–Adv | Apps             |
| `sqlite3`       | Local DB         | Beginner–Adv | Django           |
| `threading`     | Multitasking     | Beginner–Adv | Concurrency      |
| `BeautifulSoup` | Web scraping     | Beginner–Adv | Data extraction  |
| `subprocess`    | System commands  | Beginner–Adv | DevOps           |
| `smtplib`       | Email            | Beginner–Adv | Alerts           |
| `itertools`     | Loops & combos   | Beginner–Adv | Algorithms       |
| `time`          | Time control     | Beginner–Adv | Scheduling       |

---

Would you like me to now **convert all of these notes into a professional, formatted PDF (with headings, colors, and table of contents)** — titled
📘 *“Python Important Modules – Complete Notes (With Examples & Levels)”*?
I can generate it instantly for download.
