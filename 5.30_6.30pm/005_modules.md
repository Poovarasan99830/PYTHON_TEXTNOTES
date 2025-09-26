
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
   ```

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


