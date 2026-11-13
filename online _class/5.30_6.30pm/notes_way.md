
961 ---calender
1009 ---math
1094 ---request
117 --jeson
1237 -re
1320 --logging







1. Definition
2. Example Code
3. Tasks / Questions
4. Real-World Inspired Example
5. Industry Use Cases
6. Important Methods + Real-World Usage

---



# ________________________________________________________________________


# **Python Important Modules — Complete Notes with Methods & Project Use**



-> Definition 
→  Example Code 
→  Tasks/Questions 
→  Real-World Inspired Example 
→  Industry Use Cases 
→  Important Methods & Project Usage**

---

## 1️⃣ `calendar` Module

**Definition:** Handles dates, months, weekdays, leap years, and generates/manipulates calendar data.

**Example Code:**

```python
import calendar
print(calendar.month(2025, 10))  # Prints October 2025 calendar
```

**Tasks / Questions:**

1. Print full year calendar.
2. Check leap years 2000–2030.
3. Find weekday of a specific date.
4. Generate a meeting schedule for Mondays.

**Real-World Inspired Example:**

```python
import calendar
year = 2025
month = 10
c = calendar.Calendar(firstweekday=0)
mondays = [day for day, weekday in c.itermonthdays2(year, month) if day != 0 and weekday == 0]
print(f"Mondays in {month}/{year}:")
for day in mondays:
    print(f"- {year}-{month:02d}-{day:02d}")
```

**Industry Use Cases:**

* Delivery date estimation in e-commerce
* Ticket/event calendars in booking apps
* Predictive scheduling in AI apps
* Attendance & payroll in HR systems

**Important Methods & Real-World Usage:**

| Method                           | Description                             | Real-World Usage                                     |
| -------------------------------- | --------------------------------------- | ---------------------------------------------------- |
| `month(year, month)`             | Returns month as string                 | Display monthly calendar in apps / booking platforms |
| `monthcalendar(year, month)`     | Returns weeks as lists of day numbers   | Generate weekly schedules or attendance sheets       |
| `prcal(year)`                    | Prints the full year calendar           | Yearly planning tools in HR/project management       |
| `yeardays2calendar(year, width)` | List weeks with day numbers and weekday | Predictive scheduling in AI tools                    |
| `weekday(year, month, day)`      | Returns day of week index               | Determine day for delivery, booking, payroll         |
| `isleap(year)`                   | Check leap year                         | Validate scheduling for leap years                   |

---


#  ________________________________________________________________________


## 🗓️ **1️⃣ Print Full Year Calendar**

**Goal:** Display the complete calendar for a given year.

```python
import calendar

year = 2025
print(calendar.calendar(year))
```

✅ **Output:**
Shows all months of 2025 in a formatted calendar.

---

## 🕓 **2️⃣ Check Leap Years (2000–2030)**

**Goal:** Find which years between 2000–2030 are leap years.

```python
import calendar

for year in range(2000, 2031):
    if calendar.isleap(year):
        print(f"{year} is a Leap Year ✅")
    else:
        print(f"{year} is not a Leap Year ❌")
```

✅ **Output Example:**

```
2000 is a Leap Year ✅
2001 is not a Leap Year ❌
...
2028 is a Leap Year ✅
2030 is not a Leap Year ❌
```

---

## 📅 **3️⃣ Find Weekday of a Specific Date**

**Goal:** Display the weekday name (e.g., Monday, Tuesday, etc.) of a given date.

```python
import calendar

year = 2025
month = 10
day = 27

weekday_number = calendar.weekday(year, month, day)
weekday_name = calendar.day_name[weekday_number]

print(f"{day}-{month}-{year} falls on a {weekday_name}.")
```

✅ **Output Example:**

```
27-10-2025 falls on a Monday.
```

---

## 📆 **4️⃣ Generate a Meeting Schedule for Mondays**

**Goal:** Generate all Mondays in a specific month to plan weekly meetings.

```python
import calendar

year = 2025
month = 11  # Example: November 2025

month_calendar = calendar.monthcalendar(year, month)
mondays = [week[calendar.MONDAY] for week in month_calendar if week[calendar.MONDAY] != 0]

print(f"📅 Meeting Schedule for {calendar.month_name[month]} {year}:")
for m in mondays:
    print(f"- {m}-{month}-{year} (Monday)")
```

✅ **Output Example:**

```
📅 Meeting Schedule for November 2025:
- 3-11-2025 (Monday)
- 10-11-2025 (Monday)
- 17-11-2025 (Monday)
- 24-11-2025 (Monday)
```


# ________________________________________________________________________


















## 2️⃣ `math` Module

**Definition:** Performs operations: trigonometry, factorials, rounding, powers, constants (`pi`, `e`).

**Example Code:**

```python
import math
radius = 5
area = math.pi * radius ** 2
print("Circle area:", area)
```

**Tasks / Questions:**

1. Calculate area/perimeter of shapes.
2. Check perfect squares with `sqrt()`.
3. Compute compound interest.
4. Trigonometric calculations for sensor/AI data.

**Real-World Inspired Example:**

```python
import math
products = {"Tray A": 5, "Tray B": 7, "Tray C": 10}
for name, radius in products.items():
    area = math.pi * radius ** 2
    discount_price = round(area * 0.5, 2)
    print(f"{name}: Area = {area:.2f} cm², Discounted Price = ${discount_price}")
```

**Industry Use Cases:**

* Price rounding and discount calculations in e-commerce
* Physics/angles in gaming apps
* Distance calculations in AI/ML
* Portfolio metrics and compound interest in finance apps

**Important Methods & Real-World Usage:**

| Method                   | Description             | Real-World Usage                       |
| ------------------------ | ----------------------- | -------------------------------------- |
| `pow(x, y)`              | x^y                     | Interest calculations, AI computations |
| `sqrt(x)`                | Square root             | Distance calculations, normalization   |
| `factorial(n)`           | n!                      | Probability/combinatorics in AI        |
| `ceil(x)`                | Round up                | Price rounding, inventory estimation   |
| `floor(x)`               | Round down              | Price/logistics planning               |
| `gcd(a, b)`              | Greatest common divisor | Scheduling intervals, cryptography     |
| `log(x, base)`           | Logarithm               | ML feature scaling, finance            |
| `sin(x), cos(x), tan(x)` | Trigonometry            | Gaming, AI sensor data                 |
| `pi, e`                  | Constants               | Geometry, physics simulation, AI math  |

---

## 3️⃣ `requests` Module

**Definition:** Send HTTP requests (GET, POST, PUT, DELETE) to access or send data.

**Example Code:**

```python
import requests
res = requests.get("https://api.github.com")
print(res.status_code)
print(res.json())
```

**Tasks / Questions:**

1. Fetch public data (weather, crypto, news).
2. Send POST form data.
3. Handle error codes.
4. Download and save HTML from websites.

**Real-World Inspired Example:**

```python
import requests
city = "Bangalore"
api_url = f"https://wttr.in/{city}?format=%t+%C"
try:
    response = requests.get(api_url)
    if response.status_code == 200:
        print(f"Current weather in {city}: {response.text}")
    else:
        print("Failed to fetch weather data")
except Exception as e:
    print("Error:", e)
```

**Industry Use Cases:**

* Product/order API calls in e-commerce
* AI Apps (ChatGPT) communication
* Payment gateway API integration
* IoT sensor data transmission

**Important Methods & Real-World Usage:**

| Method                       | Description           | Real-World Usage                          |
| ---------------------------- | --------------------- | ----------------------------------------- |
| `get(url, params)`           | Send GET request      | Fetch API data: weather, products, crypto |
| `post(url, data/json)`       | Send POST request     | Submit forms, payment gateways, AI APIs   |
| `put(url, data/json)`        | Update resource       | Update user/product info via API          |
| `delete(url)`                | Delete resource       | Remove obsolete entries                   |
| `head(url)`                  | Fetch headers         | Check URL/resource availability           |
| `options(url)`               | Discover HTTP methods | API debugging/discovery                   |
| `timeout`, `auth`, `headers` | Request customization | Secure API calls, token-based auth        |

---

*(And the same for `json`, `re`, and `logging` modules following the exact same structure.)*

---


Perfect! Here’s the **full six-module notes** in the complete format you requested:

---

# **Python Important Modules — Complete Notes with Methods & Project Use**

Each module includes:
**Definition → Example Code → Tasks/Questions → Real-World Inspired Example → Industry Use Cases → Important Methods & Project Usage**

---

## 1️⃣ `calendar` Module

**Definition:** Handles dates, months, weekdays, leap years, and generates/manipulates calendar data.

**Example Code:**

```python
import calendar
print(calendar.month(2025, 10))  # Prints October 2025 calendar
```

**Tasks / Questions:**

1. Print full year calendar.
2. Check leap years 2000–2030.
3. Find weekday of a specific date.
4. Generate a meeting schedule for Mondays.

**Real-World Inspired Example:**

```python
import calendar
year = 2025
month = 10
c = calendar.Calendar(firstweekday=0)
mondays = [day for day, weekday in c.itermonthdays2(year, month) if day != 0 and weekday == 0]
print(f"Mondays in {month}/{year}:")
for day in mondays:
    print(f"- {year}-{month:02d}-{day:02d}")
```

**Industry Use Cases:**

* Delivery date estimation in e-commerce
* Ticket/event calendars in booking apps
* Predictive scheduling in AI apps
* Attendance & payroll in HR systems

**Important Methods & Real-World Usage:**

| Method                           | Description                             | Real-World Usage                                     |
| -------------------------------- | --------------------------------------- | ---------------------------------------------------- |
| `month(year, month)`             | Returns month as string                 | Display monthly calendar in apps / booking platforms |
| `monthcalendar(year, month)`     | Returns weeks as lists of day numbers   | Generate weekly schedules or attendance sheets       |
| `prcal(year)`                    | Prints the full year calendar           | Yearly planning tools in HR/project management       |
| `yeardays2calendar(year, width)` | List weeks with day numbers and weekday | Predictive scheduling in AI tools                    |
| `weekday(year, month, day)`      | Returns day of week index               | Determine day for delivery, booking, payroll         |
| `isleap(year)`                   | Check leap year                         | Validate scheduling for leap years                   |

---

## 2️⃣ `math` Module

**Definition:** Performs operations: trigonometry, factorials, rounding, powers, constants (`pi`, `e`).

**Example Code:**

```python
import math
radius = 5
area = math.pi * radius ** 2
print("Circle area:", area)
```

**Tasks / Questions:**

1. Calculate area/perimeter of shapes.
2. Check perfect squares with `sqrt()`.
3. Compute compound interest.
4. Trigonometric calculations for sensor/AI data.

**Real-World Inspired Example:**

```python
import math
products = {"Tray A": 5, "Tray B": 7, "Tray C": 10}
for name, radius in products.items():
    area = math.pi * radius ** 2
    discount_price = round(area * 0.5, 2)
    print(f"{name}: Area = {area:.2f} cm², Discounted Price = ${discount_price}")
```

**Industry Use Cases:**

* Price rounding and discount calculations in e-commerce
* Physics/angles in gaming apps
* Distance calculations in AI/ML
* Portfolio metrics and compound interest in finance apps

**Important Methods & Real-World Usage:**

| Method                   | Description             | Real-World Usage                       |
| ------------------------ | ----------------------- | -------------------------------------- |
| `pow(x, y)`              | x^y                     | Interest calculations, AI computations |
| `sqrt(x)`                | Square root             | Distance calculations, normalization   |
| `factorial(n)`           | n!                      | Probability/combinatorics in AI        |
| `ceil(x)`                | Round up                | Price rounding, inventory estimation   |
| `floor(x)`               | Round down              | Price/logistics planning               |
| `gcd(a, b)`              | Greatest common divisor | Scheduling intervals, cryptography     |
| `log(x, base)`           | Logarithm               | ML feature scaling, finance            |
| `sin(x), cos(x), tan(x)` | Trigonometry            | Gaming, AI sensor data                 |
| `pi, e`                  | Constants               | Geometry, physics simulation, AI math  |

---

## 3️⃣ `requests` Module

**Definition:** Send HTTP requests (GET, POST, PUT, DELETE) to access or send data.

**Example Code:**

```python
import requests
res = requests.get("https://api.github.com")
print(res.status_code)
print(res.json())
```

**Tasks / Questions:**

1. Fetch public data (weather, crypto, news).
2. Send POST form data.
3. Handle error codes.
4. Download and save HTML from websites.

**Real-World Inspired Example:**

```python
import requests
city = "Bangalore"
api_url = f"https://wttr.in/{city}?format=%t+%C"
try:
    response = requests.get(api_url)
    if response.status_code == 200:
        print(f"Current weather in {city}: {response.text}")
    else:
        print("Failed to fetch weather data")
except Exception as e:
    print("Error:", e)
```

**Industry Use Cases:**

* Product/order API calls in e-commerce
* AI Apps (ChatGPT) communication
* Payment gateway API integration
* IoT sensor data transmission

**Important Methods & Real-World Usage:**

| Method                       | Description           | Real-World Usage                          |
| ---------------------------- | --------------------- | ----------------------------------------- |
| `get(url, params)`           | Send GET request      | Fetch API data: weather, products, crypto |
| `post(url, data/json)`       | Send POST request     | Submit forms, payment gateways, AI APIs   |
| `put(url, data/json)`        | Update resource       | Update user/product info via API          |
| `delete(url)`                | Delete resource       | Remove obsolete entries                   |
| `head(url)`                  | Fetch headers         | Check URL/resource availability           |
| `options(url)`               | Discover HTTP methods | API debugging/discovery                   |
| `timeout`, `auth`, `headers` | Request customization | Secure API calls, token-based auth        |

---

## 4️⃣ `json` Module

**Definition:** Encode/decode JSON data for storage and communication between systems.

**Example Code:**

```python
import json
data = {"name": "Poovarasan", "age": 22}
json_str = json.dumps(data)
print(json_str)
```

**Tasks / Questions:**

1. Convert Python dict → JSON string
2. Save JSON to a file
3. Read JSON file & modify values
4. Parse API responses in JSON format

**Real-World Inspired Example:**

```python
import json
products = [
    {"name": "Laptop", "price": 1500},
    {"name": "Headphones", "price": 100},
    {"name": "Keyboard", "price": 50}
]
with open("products.json", "w") as f:
    json.dump(products, f, indent=4)
with open("products.json", "r") as f:
    loaded_products = json.load(f)
print("Loaded Products:", loaded_products)
```

**Industry Use Cases:**

* Product data exchange in e-commerce
* Model input/output in AI/ML apps
* Frontend-backend communication in web apps
* Conversation log storage in chatbots

**Important Methods & Real-World Usage:**

| Method                       | Description                      | Real-World Usage                          |
| ---------------------------- | -------------------------------- | ----------------------------------------- |
| `dump(obj, file)`            | Write JSON to file               | Save product data, logs, AI model outputs |
| `dumps(obj)`                 | Convert Python obj → JSON string | API responses, web communication          |
| `load(file)`                 | Read JSON file                   | Load product catalogs, preferences        |
| `loads(string)`              | Convert JSON string → Python obj | Parse API responses, config data          |
| `JSONEncoder`, `JSONDecoder` | Custom serialization             | AI model input/output, custom data types  |

---

## 5️⃣ `re` Module

**Definition:** Use regular expressions for pattern matching in text (emails, phone numbers, hashtags).

**Example Code:**

```python
import re
text = "My email is user123@gmail.com"
result = re.findall(r'\S+@\S+', text)
print(result)
```

**Tasks / Questions:**

1. Validate emails & phone numbers
2. Replace unwanted words
3. Extract hashtags
4. Analyze log files for errors

**Real-World Inspired Example:**

```python
import re
text = """
Contact us at support@shop.com or sales@shop.com.
Follow our newsletter at news@shop.com
"""
emails = re.findall(r'\S+@\S+', text)
print("Extracted Emails:", emails)
```

**Industry Use Cases:**

* Validate user input in e-commerce
* Text cleaning in AI/NLP apps
* Extract IPs/URLs in cybersecurity tools
* Hashtag/mention extraction in social media apps

**Important Methods & Real-World Usage:**

| Method                       | Description             | Real-World Usage                 |
| ---------------------------- | ----------------------- | -------------------------------- |
| `match(pattern, string)`     | Check pattern at start  | Validate inputs (email, PIN)     |
| `search(pattern, string)`    | Find pattern anywhere   | Find keywords, extract info      |
| `findall(pattern, string)`   | List all matches        | Extract emails, hashtags, phones |
| `finditer(pattern, string)`  | Iterator over matches   | Efficient log parsing            |
| `sub(pattern, repl, string)` | Replace matched text    | Clean text, mask sensitive data  |
| `split(pattern, string)`     | Split string by pattern | Tokenize text, extract data      |
| `compile(pattern)`           | Precompile regex        | Optimize repeated searches       |

---

## 6️⃣ `logging` Module

**Definition:** Record INFO, WARNING, ERROR messages for debugging and analytics.

**Example Code:**

```python
import logging
logging.basicConfig(level=logging.INFO, filename="app.log")
logging.info("Application started")
logging.warning("Low disk space")
logging.error("Failed to open file")
```

**Tasks / Questions:**

1. Log INFO/WARNING/ERROR
2. Save logs to file
3. Create custom log formats
4. Rotate log files by date/time

**Real-World Inspired Example:**

```python
import logging
logging.basicConfig(filename="price_changes.log", level=logging.INFO, format="%(asctime)s - %(message)s")
products = {"Laptop": 1500, "Headphones": 100, "Keyboard": 50}
for name, price in products.items():
    new_price = price * 0.9
    logging.info(f"{name}: Original ${price} → New ${new_price}")
```

**Industry Use Cases:**

* Monitor user activity & payment failures in e-commerce
* Track AI/ML model training steps
* Log banking transactions & intrusion attempts
* Debug & monitor web servers

**Important Methods & Real-World Usage:**

| Method                                            | Description                 | Real-World Usage                      |
| ------------------------------------------------- | --------------------------- | ------------------------------------- |
| `basicConfig()`                                   | Setup default logging       | Simple logging in scripts/apps        |
| `getLogger(name)`                                 | Create/return logger object | Multiple module logging independently |
| `addHandler(handler)`                             | Add file/stream handler     | Rotate logs, multiple outputs         |
| `setLevel(level)`                                 | Set logging threshold       | Control verbosity in production/debug |
| `info(msg), warning(msg), error(msg), debug(msg)` | Log messages                | Track activity, errors, server events |

---

✅ **General AI + Industry Relevance Summary**

| Module     | Real-World Use Case       | Common in Apps        |
| ---------- | ------------------------- | --------------------- |
| `calendar` | Scheduling, reminders     | Booking, HR, delivery |
| `math`     | AI math, pricing logic    | Gaming, finance       |
| `requests` | Connect APIs              | ChatGPT, Swiggy       |
| `json`     | API data format           | Web + AI integration  |
| `re`       | Text cleaning, validation | NLP, user input       |
| `logging`  | Debug + analytics         | E-commerce, servers   |

---
\