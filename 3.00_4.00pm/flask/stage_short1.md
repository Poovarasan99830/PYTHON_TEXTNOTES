





* **Customers** → Browser (Users)
* **Waiter** → Flask
* **Kitchen** → Python Logic
* **Menu Card** → HTML Templates
* **Tables, Chairs, Design** → CSS / Images (Static files)
* **Ledger Book** → Database






Route        → Entry point
Template     → UI
Static       → Assets
Redirect     → Flow control
url_for      → Safe linking
Jinja        → Dynamic HTML
Forms        → User input
API          → JSON backend
DB           → Persistence
ORM          → DB abstraction





## 🚪 1. ROUTES — *“Which Door Should the Customer Enter?”*
        ➡️ **Route = Direction board inside the restaurant**




## 🎭 2. RENDER TEMPLATE — *“Show the Menu Card”*




## 🔁 3. REDIRECT — *“Sorry, Please Go There Instead”*
         Redirect = Politely **send customer to another counter**




## 🗺️ 4. url_for — *“Use the Official Map”*

          url_for builds the URL, redirect sends the browser to it.
          
          Waiter uses **official restaurant map** 

          **Why important?**

             * If door name changes, map updates automatically
             * Avoid broken links

           ➡️ **url_for = Smart navigation system**


## 🎨 5. JINJA — *“Smart Menu Card Printer”*
        Menu card is **not fixed**.
        It changes based on **customer type**.

### 🔹 Inheritance — *“Same Hotel, Different Rooms”*
       **Story**

       * Same building structure
       * Different rooms inside

      ➡️ **Inheritance = Reuse common design**

## 🔢 6. URL PARAMETERS — *“Table Number on Entry”*
     URL parameter = **Information written on entry slip**


## 📝 7. FORM VALIDATION — *“Check Order Slip Before Cooking”*
      ➡️ **Form validation = Safety check**

## 🌐 8. REST API — *“Takeaway / Online Orders”*
       Some customers **don’t come inside**.
       They order via **Swiggy / Zomato** 📱

       * No HTML
       * Only JSON
       * Machine to machine talk

      ➡️ **REST API = Delivery counter**

## 🗄️ 9. DATABASE CONNECTION — *“Restaurant Ledger Book”*
            You must store:

           * Orders
           * Customers
           * Payments

### 🔹 SQLite — *“Small Notebook”* 📓
### 🔹 MySQL — *“Big Account Book”* 📚
### 🔹 ORM SQLAlchemy — *“Translator”* 🌐
         * You speak **Python**
         * Translator speaks **SQL**

        ➡️ **ORM = Language translator between you & DB**





Browser
   ↓
Routes
   ↓
Flask (Waiter)
   ↓
Jinja Templates
   ↓
HTML + Static
   ↓
Database (SQLite / MySQL)



Flask is a waiter who takes requests, talks to the kitchen, prints smart menus, stores orders, and serves customers





Route        → Entry point
Template     → UI


Static       → Assets
Redirect     → Flow control
url_for      → Safe linking
Jinja        → Dynamic HTML
Forms        → User input
API          → JSON backend
DB           → Persistence
ORM          → DB abstraction





---

## 🔹 FLASK
       **Flask** is a lightweight Python web framework used to build web applications and REST APIs.

🧠 **Why**
`Flask()` creates the WSGI app object. Everything (routes, config, extensions) attaches to this.


## 🔹 Routes
      **Routes** map a URL to a Python function that handles the request.

---

## 🔹 Render Template
      **Render template** sends an HTML file to the browser after processing dynamic data.

---

## 🔹 Templates
      **Templates** are HTML files with placeholders used to generate dynamic web pages.

---

## 🔹 Static
      **Static files** are assets like CSS, JavaScript, and images served directly to the browser.

---

## 🔹 Redirect
      **Redirect** tells the browser to go to a different URL after completing an action.

---

## 🔹 url_for
      **url_for** dynamically generates URLs for routes using function names.

---

## 🔹 Jinja
     **Jinja** is Flask’s templating engine used to create dynamic HTML pages.

---

## 🔹 Jinja Variables
      **Variables** insert dynamic data from Python into HTML templates.

---

## 🔹 Jinja Flow Control
      **Flow control** uses conditions and loops to control what HTML is rendered.

---

## 🔹 Jinja Inheritance
       **Inheritance** allows templates to reuse a common layout using a base template.

---

## 🔹 URL Parameters
      **URL parameters** pass dynamic values through the URL to the Flask route.

---

## 🔹 Form Validation
       **Form validation** checks user input on the server to ensure it is correct and safe.

---

## 🔹 REST API
       **REST API** is an interface that allows clients to communicate with the server using JSON and HTTP methods.

---

## 🔹 Database Connections
       **Database connections** allow Flask applications to store and retrieve persistent data.

---

## 🔹 SQLite
       **SQLite** is a lightweight, file-based database used for small applications and learning.

---

## 🔹 MySQL
       **MySQL** is a production-grade relational database used for scalable applications.

---

## 🔹 ORM (SQLAlchemy)
         **SQLAlchemy ORM** lets developers interact with databases using Python objects instead of SQL queries.

---



> **Flask routes requests, renders templates, handles forms and APIs, and stores data using databases.**







# 🔥 FLASK — DEV MODE

## 0️⃣ Project Structure

```txt
project/
│── app.py
│── templates/
│   │── base.html
│   │── index.html
│   │── user.html
│── static/
│   │── style.css
│── models.py
│── requirements.txt
```

---

## 1️⃣ Routes

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask"

@app.route("/about")
def about():
    return "About page"
```

---

## 2️⃣ Render Template

### app.py

```python
from flask import render_template

@app.route("/dashboard")
def dashboard():
    return render_template("index.html", title="Dashboard")
```

### templates/index.html

```html
<h1>{{ title }}</h1>
```

---

## 3️⃣ Templates & Static




## 🔹 Static
      **Static files** are assets like CSS, JavaScript, and images served directly to the browser.


      
### static/style.css

```css
body { background: #f5f5f5; }
```

### templates/base.html

```html


<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>




```

#_____________________________________________________________________________________
#_____________________________________________________________________________________



## 🔹 Redirect
      **Redirect** tells the browser to go to a different URL after completing an action.



## 🔹 url_for
     **url_for** dynamically generates URLs for routes using function names.

---



| Feature       | redirect                 | url_for      |
| ------------- | ------------------------ | ------------ |
| Purpose       | Navigate to another page | Generate URL |
| Changes page? | ✅ Yes                    | ❌ No         |
| Returns       | Response (302)           | String (URL) |
| Used alone?   | Yes                      | Yes          |


✅ Yes, url_for alone

<a href="{{ url_for('home') }}">Go Home</a>
url_for() always uses the function name, not the URL path.



✅ Yes, redirect alone
return redirect('/home')





# _______________________________________________________
## 4️⃣ Redirect
# _______________________________________________________


```python
from flask import redirect

@app.route("/old")
def old():
    return redirect("/new")

@app.route("/new")
def new():
    return "New page"
```

# _______________________________________________________
## 5️⃣ url_for
# _______________________________________________________


```python
from flask import url_for

@app.route("/login")
def login():
    return "Login"

@app.route("/go-login")
def go_login():
    return redirect(url_for("login"))
```





#_____________________________________________________________________________________
#_____________________________________________________________________________________





## 🔹 Jinja
     **Jinja** is Flask’s templating engine used to create dynamic HTML pages.

---

## 🔹 Jinja Variables
      **Variables** insert dynamic data from Python into HTML templates.

---

## 🔹 Jinja Flow Control
      **Flow control** uses conditions and loops to control what HTML is rendered.

---

## 🔹 Jinja Inheritance

**Inheritance** allows templates to reuse a common layout using a base template.

Template inheritance allows you to reuse a common HTML layout and define page-specific content in     child templates.

block content is not mandatory; block names are developer-defined and can be anything, as long as they match in both base and child templates.

super() is used inside a child template to keep the parent block content and add extra content.

Without super(), base content will be fully replaced.


extends → inherit layout

block → replace content

super() → keep parent 








## 6️⃣ Jinja

### 🔹 Variables

```html
<p>User: {{ username }}</p>
```

---

### 🔹 Flow Control

```html
{% if age >= 18 %}
<p>Adult</p>
{% else %}
<p>Minor</p>
{% endif %}
```

```html
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

---

### 🔹 Inheritance

```html
{% extends "base.html" %}
{% block content %}
<h2>Home</h2>
{% endblock %}
```




{% extends "base.html" %}

{% block content %}
{{ super() }}
<p>This is home page content</p>
{% endblock %}



#_____________________________________________________________________________________
#_____________________________________________________________________________________




## 🔹 URL Parameters
      **URL parameters** pass dynamic values through the URL to the Flask route.

      Flask provides URL converters like string, int, float, path, and uuid to validate and parse dynamic URL parameters


## 7️⃣ URL Parameters

```python
@app.route("/user/<int:id>")
def user(id):
    return f"User ID: {id}"
```

```python
@app.route("/post/<string:slug>")
def post(slug):
    return slug
```




## 1️⃣ Flask routes (backend)

```python
from flask import Flask, render_template
import uuid

app = Flask(__name__)

@app.route("/user/<string:name>")
def user(name):
    return f"User name: {name}"

@app.route("/user-id/<int:id>")
def user_id(id):
    return f"User ID: {id}"

@app.route("/price/<float:amount>")
def price(amount):
    return f"Price: {amount}"

@app.route("/files/<path:filepath>")
def files(filepath):
    return f"File path: {filepath}"

@app.route("/order/<uuid:order_id>")
def order(order_id):
    return f"Order ID: {order_id}"
```

---


## 2️⃣ HTML template using `<a>` tags (URL check)

```html
<!DOCTYPE html>
<html>
<body>

<h2>Check Flask URL Types</h2>

<a href="{{ url_for('user', name='ram') }}">String URL</a><br><br>

<a href="{{ url_for('user_id', id=5) }}">Int URL</a><br><br>

<a href="{{ url_for('price', amount=9.99) }}">Float URL</a><br><br>

<a href="{{ url_for('files', filepath='a/b/c.txt') }}">Path URL</a><br><br>

<a href="{{ url_for('order', order_id='550e8400-e29b-41d4-a716-446655440000') }}">
UUID URL
</a>

</body>
</html>
```

👉 Clicking each link will **open that URL** and **prove the type is working**.

---

## 3️⃣ Button style (using `<button>`)

### Method 1: Button inside `<a>` (recommended)

```html
<a href="{{ url_for('user', name='ram') }}">
    <button>String Button</button>
</a>
```

---

### Method 2: Button using `onclick`

```html
<button onclick="location.href='{{ url_for('user_id', id=10) }}'">
    Int Button
</button>
```


#__________________________________________________________________________
#__________________________________________________________________________


## 🔹 Form Validation
       **Form validation** checks user input on the server to ensure it is correct and safe.



## 8️⃣ Form Handling & Validation

### HTML

```html
<form method="POST">
    <input name="email">
    <button>Submit</button>
</form>
```

### Flask

```python
from flask import request

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        email = request.form.get("email")

        if not email:
            return "Email required", 400

        return "Success"
    return render_template("form.html")
```




**where data comes from**.
request.args
request.form
request.json


@app.route("/registers",methods = ["POST","GET"])
def registers():
    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('psw')
        con_password = request.form.get('con_psw')
        email = request.form.get('email')
    
        if not name or not password or not con_password or not email:
            return "❌ All Values are Required"
        if len(name)<=2:
            return "❌ Your Name Must Be 3 Characters"
        if len(password)<=3:
            return "❌ Your Password Must be 4 values"
        if password != con_password:
            return "❌ The Password is mismatch"
        if "@" not in email or "." not in email:
            return "❌ Enter Valid Email"
        
    return render_template("register_home.html")



#__________________________________________________________________________
#__________________________________________________________________________


## 1️⃣ Query Parameters (request.args)

### 🔹 What is it?

Data sent **in the URL** after `?`

```text
/search?q=python&page=1
```

### 🔹 How Flask reads it

```python
q = request.args.get("q")                  # "python"
page = request.args.get("page", type=int)  # 1
```



### 🔹 When to use (IMPORTANT)

Use **Query Params** when:

* Searching
* Filtering
* Pagination
* Sorting

### rule

> ❗ **If data does NOT change the server state → use query params**

### 🔹 Example

```python
@app.route("/search")
def search():
    q = request.args.get("q")
    page = request.args.get("page", 1, type=int)
    return f"Searching {q}, page {page}"







#__________________________________________________________________________
#__________________________________________________________________________



##2️⃣ JSON Body (request.get_json())

### 🔹 What is it?

Data sent **inside the request body** as JSON.


{
  "email": "test@gmail.com",
  "password": "1234"
}


### 🔹 How Flask reads it


data = request.get_json()
email = data["email"]
```



### 🔹 When to use

Use **JSON body** when:

* Sending structured data
* APIs
* Mobile / Frontend apps
* REST APIs




#__________________________________________________________________________
#__________________________________________________________________________


## 3️⃣ Form Data (`request.form`)

### 🔹 What is it?

Data sent from an **HTML form** using
`method="POST"` and **form fields** (`<input>`, `<select>`, etc.).

This data is sent as **form-encoded data**, **not JSON**.

---

### 🔹 Example HTML Form

```html
<form action="/login" method="post">
  <input type="email" name="email">
  <input type="password" name="password">
  <button type="submit">Login</button>
</form>
```

---

### 🔹 Data sent to server

```
email=test@gmail.com
password=1234
```

---

### 🔹 How Flask reads it

```python
from flask import request

email = request.form["email"]
password = request.form["password"]
```

✔ or (safe way):

```python
email = request.form.get("email")
password = request.form.get("password")
```

---

### 🔹 When to use

Use **Form Data (`request.form`)** when:

* Submitting **HTML forms**
* Traditional **web applications**
* Login / Register forms
* Data comes from **browser form submit**
* You are **NOT building APIs**

---

### 🔹 Important Notes ⚠️

* Works **only with POST / PUT**
* ❌ Cannot read JSON data
* Browser sends data as:

  ```
  application/x-www-form-urlencoded
  ```

---

### 🔹 Quick Comparison 🧠

| Type         | Used for   | Flask                |
| ------------ | ---------- | -------------------- |
| Query Params | URL data   | `request.args`       |
| Form Data    | HTML forms | `request.form`       |
| JSON Body    | APIs       | `request.get_json()` |



> **Search → Query Params**
> **API → JSON Body**
> **HTML Form → request.form**



Say this line 

> “URL is for asking, BODY is for giving data”

Then show:

* Browser URL → `request.args`
* Postman JSON → `request.get_json()`
* HTML form → `request.form`






Query Params → WHAT you want
Body → DATA you send
Headers → RULES & SECURITY
CORS → Browser permission system
Preflight → Permission check
Security Headers → Browser armor



#_____________________________________________________________________________________
#_____________________________________________________________________________________



# 📘 FLASK BACKEND – CORE LESSON NOTES

---
#_____________________________________________________________________________________
## 🟩 LESSON 1: HTTP METHODS

### 🔹 What is HTTP?

HTTP = **Hyper Text Transfer Protocol**
It defines **how client and server communicate**.

---

### 🔹 Why HTTP Methods?

They tell the server:

> **What action the client wants to perform**

---

### 🔹 Common HTTP Methods

| Method | Purpose     | Example      |
| ------ | ----------- | ------------ |
| GET    | Get data    | View page    |
| POST   | Send data   | Login form   |
| PUT    | Update data | Edit profile |
| DELETE | Delete data | Remove user  |

---

### 🔹 Flask Example

```python
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Login Submitted"
    return "Login Page"
```

---

### 🔹 Real-world Mapping 🧠

| Action              | Method |
| ------------------- | ------ |
| Open login page     | GET    |
| Submit login form   | POST   |
| Update user details | PUT    |
| Delete account      | DELETE |

---






















#_____________________________________________________________________________________
## 🟩 LESSON 2: COOKIES 🍪

---

### 🔹 What is a Cookie?

A **small data stored in the browser**.

* Stored on **client side**
* Automatically sent with every request

---

### 🔹 Why Cookies?

HTTP is **stateless**
➡ Server forgets user after request
➡ Cookie helps remember user

---

### 🔹 Flask Cookie Example

```python
from flask import make_response

@app.route("/set-cookie")
def set_cookie():
    resp = make_response("Cookie Set")
    resp.set_cookie("user", "admin")
    return resp
```

---

### 🔹 Read Cookie

```python
user = request.cookies.get("user")
```

---

### 🔹 Cookie Limitations ⚠️

* Not secure
* Can be modified by user
* Limited storage size

---
#_____________________________________________________________________________________
## 🟩 LESSON 3: SESSIONS 🗂️

---

### 🔹 What is a Session?

Session = **Server-side storage of user data**

* Safer than cookies
* Cookie stores only **session ID**

---

### 🔹 Why Sessions?

* Store login info
* Store user state
* Secure authentication

---

### 🔹 Flask Session Setup

```python
from flask import session

app.secret_key = "secret123"
```

---

### 🔹 Store Data in Session

```python
session["user"] = "admin"
```

---

### 🔹 Read Session

```python
if "user" in session:
    print("Logged in")
```

---

### 🔹 Remove Session (Logout)

```python
session.pop("user")
```

---

### 🔹 Cookie vs Session 🧠

| Cookie      | Session     |
| ----------- | ----------- |
| Client side | Server side |
| Less secure | More secure |
| Small data  | Larger data |

---
#_____________________________________________________________________________________
## 🟩 LESSON 4: AUTHENTICATION 🔐

---

### 🔹 What is Authentication?

Authentication = **Verify who the user is**

Example:

* Login
* Logout
* Protected pages

---
#_____________________________________________________________________________________
### 🔹 Authentication Flow

```text
User Login
   ↓
Check credentials
   ↓
Create session
   ↓
Allow access
```

---
#_____________________________________________________________________________________
### 🔹 Simple Login Example

```python
@app.route("/login", methods=["POST"])
def login():
    if request.form["username"] == "admin":
        session["user"] = "admin"
        return redirect("/dashboard")
```

---

### 🔹 Protect Routes

```python
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return "Welcome Dashboard"
    return redirect("/login")
```

---

### 🔹 Logout

```python
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
```

---
#_____________________________________________________________________________________
## 🟩 FINAL TEACHING FLOW (VERY IMPORTANT)

```text
Request Data
   ↓
HTTP Methods
   ↓
Cookies
   ↓
Sessions
   ↓
Authentication
```

---
#_____________________________________________________________________________________
## 🎯 AFTER THIS, STUDENTS CAN:

✅ Build login systems
✅ Understand backend flow
✅ Handle real projects
✅ Crack Flask interview questions


#_____________________________________________________________________________________
#_____________________________________________________________________________________

## 🔹 REST API
       **REST API** is an interface that allows clients to communicate with the server using JSON and HTTP methods.



## 9️⃣ REST API

### JSON API

```python
from flask import jsonify

@app.route("/api/users", methods=["GET"])
def users():
    return jsonify([
        {"id": 1, "name": "A"},
        {"id": 2, "name": "B"}
    ])
```

### POST API

```python
@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json
    return jsonify(data), 201
```

#_____________________________________________________________________________________
#_____________________________________________________________________________________


0005sqlite3
flask app1--app6

## 🔹 Database Connections
       **Database connections** allow Flask applications to store and retrieve persistent data.

---

## 🔹 SQLite
       **SQLite** is a lightweight, file-based database used for small applications and learning.

---

## 🔹 MySQL
       **MySQL** is a production-grade relational database used for scalable applications.

---

## 🔹 ORM (SQLAlchemy)
         **SQLAlchemy ORM** lets developers interact with databases using Python objects instead of SQL queries.


SQLite  ---> comes built-in with Python.

pip install mysqlclient -->Most common
pip install pymysql ---> Pure Python – easier on Windows

pip install sqlalchemy   -->ORM – Recommended







## 🔟 Database Connections

---

## 🔹 SQLite (Raw)

```python
import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT)")
cur.execute("INSERT INTO users VALUES(1, 'Poovarasan')")
conn.commit()
```

---

## 🔹 MySQL (Raw)

```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="testdb"
)

cur = db.cursor()
cur.execute("SELECT * FROM users")
```

---

## 🔹 ORM — SQLAlchemy

### Install

```bash
pip install flask-sqlalchemy
```

---

### app.py

```python
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)
```

---

### models.py

```python
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
```

---

### DB Operations

```python
db.create_all()

u = User(name="Poovarasan")
db.session.add(u)
db.session.commit()

users = User.query.all()
```

---

## 🚀 Minimal Run

```python
if __name__ == "__main__":
    app.run(debug=True)
```

---


## ⚡ DEV SUMMARY (Cheat Sheet)

```txt
Route        → @app.route
HTML         → render_template
CSS/JS       → static/
Redirect     → redirect(url_for())
Dynamic HTML → Jinja
URL data     → <int:id>
Forms        → request.form
API          → jsonify()

DB simple    → sqlite3
DB prod      → MySQL
ORM          → SQLAlchemy
```

#_____________________________________________________________________________________
#_____________________________________________________________________________________




## 1️⃣ What This Code Does

```python
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:1234@localhost/school_db'
```

### 🔹 Meaning (Breakdown)

| Part        | Meaning        |
| ----------- | -------------- |
| `mysql`     | Database type  |
| `pymysql`   | MySQL driver   |
| `root`      | MySQL username |
| `1234`      | MySQL password |
| `localhost` | Host           |
| `school_db` | Database name  |

👉 SQLAlchemy uses **ONE connection string** instead of many configs.

---

```python
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

### 🔹 Why this is needed?

* Prevents **warning messages**
* Saves memory
* Recommended setting

---

## 2️⃣ Required Installations (VERY IMPORTANT)

Run **all**:

```bash
pip install flask flask-sqlalchemy pymysql
```

---

## 3️⃣ Minimal Working Flask App ✅

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:1234@localhost/school_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Database Connected Successfully!"

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 4️⃣ Create a Table (Model)

```python
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def __repr__(self):
        return f"<Student {self.name}>"
```

### 🔹 Create table in MySQL

Open Python shell:

```bash
python
```

```python
from app import db
db.create_all()
```

✔ Table created in `school_db`

---

## 5️⃣ Common Errors & Fixes 🚨

### ❌ Error: `No module named 'pymysql'`

✔ Fix:

```bash
pip install pymysql
```

---

### ❌ Error: `Access denied for user 'root'`

✔ Fix:

* Check MySQL password
* Ensure MySQL server is running
* Try login manually:

```bash
mysql -u root -p
```

---

### ❌ Error: `Unknown database 'school_db'`

✔ Fix:

```sql
CREATE DATABASE school_db;
```

---

## 6️⃣ Interview Tip 🧠

> `SQLALCHEMY_DATABASE_URI` contains **database + driver + credentials**
> and replaces traditional MySQL config variables.

---






1️⃣ **FULL HTTP HEADERS LESSON NOTES**
2️⃣ **Authentication → Headers → JWT FLOW** (very important for modern backend)

This is **industry-aligned** and **student-safe (no confusion)**.

---

# 📘 LESSON 5: HTTP HEADERS (FULL NOTES)

---

## 🔹 What are HTTP Headers?

HTTP Headers are **key–value pairs** sent between **client and server**.

They carry **extra information** about:

* Request
* Response
* Authentication
* Content type

📌 Headers are **not visible in URL or body**.

---

## 🔹 Types of Headers

| Type                   | Description             |
| ---------------------- | ----------------------- |
| Request Headers        | Sent by client          |
| Response Headers       | Sent by server          |
| Authentication Headers | Used for login security |
| Content Headers        | Data format info        |

---

## 🟩 REQUEST HEADERS

### 🔹 What are Request Headers?

Headers sent **from client to server** with every request.

---

### 🔹 Common Request Headers

| Header        | Purpose      |
| ------------- | ------------ |
| Host          | Server name  |
| User-Agent    | Browser info |
| Content-Type  | Data format  |
| Authorization | Login token  |

---

### 🔹 Flask Example

```python
request.headers.get("User-Agent")
```

```python
request.headers.get("Content-Type")
```

---

## 🟩 RESPONSE HEADERS

### 🔹 What are Response Headers?

Headers sent **from server to client**.

---

### 🔹 Common Response Headers

| Header        | Purpose         |
| ------------- | --------------- |
| Content-Type  | Response format |
| Set-Cookie    | Store cookie    |
| Cache-Control | Cache rules     |

---

### 🔹 Flask Example

```python
resp = make_response("Hello")
resp.headers["Custom-Header"] = "Demo"
return resp
```

---

## 🟩 CONTENT-TYPE HEADER (VERY IMPORTANT)

### 🔹 What is Content-Type?

Tells server **what type of data is being sent**.

---

### 🔹 Common Content Types

| Type                              | Used for    |
| --------------------------------- | ----------- |
| application/json                  | APIs        |
| application/x-www-form-urlencoded | Forms       |
| multipart/form-data               | File upload |

---

### 🔹 Flask Usage

```python
request.content_type
```

---

## 🟩 AUTHORIZATION HEADER 🔐

### 🔹 What is Authorization Header?

Used to send **login credentials or token**.

Format:

```
Authorization: Bearer <token>
```

---

### 🔹 Why Authorization Header?

✔ Secure
✔ No URL exposure
✔ Used in APIs
✔ Works with mobile & frontend apps

---

### 🔹 Flask Read Example

```python
token = request.headers.get("Authorization")
```

---

## 🟩 HEADERS SUMMARY 🧠

| Concept          | Used for       |
| ---------------- | -------------- |
| Request Headers  | Client info    |
| Response Headers | Server info    |
| Content-Type     | Data format    |
| Authorization    | Authentication |

---

# 🔐 AUTH → HEADERS → JWT FLOW (MOST IMPORTANT)

This is how **REAL BACKEND SYSTEMS** work.

---

## 🟩 STEP 1: AUTHENTICATION (LOGIN)

### 🔹 User sends credentials

```json
{
  "email": "test@gmail.com",
  "password": "1234"
}
```

---

### 🔹 Server validates user

✔ Check database
✔ Password match

---

## 🟩 STEP 2: GENERATE JWT TOKEN

### 🔹 What is JWT?

JWT = **JSON Web Token**

* Encrypted string
* Represents logged-in user
* Time-limited

---

### 🔹 Token Creation (Concept)

```text
User Info → JWT Token
```

---

### 🔹 Server sends token in response

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

## 🟩 STEP 3: CLIENT STORES TOKEN

Client stores token in:

* LocalStorage (frontend)
* Memory (mobile app)

❌ Not in URL
❌ Not in cookies (for APIs)

---

## 🟩 STEP 4: CLIENT SENDS TOKEN IN HEADER

Every request:

```
Authorization: Bearer <JWT_TOKEN>
```

---

### 🔹 Example API Request

```http
GET /dashboard
Authorization: Bearer eyJhbGciOiJIUzI1...
```

---

## 🟩 STEP 5: SERVER VALIDATES TOKEN

Server:
✔ Reads Authorization header
✔ Verifies token
✔ Extracts user
✔ Allows access

---

### 🔹 Protected Route (Concept)

```python
token = request.headers.get("Authorization")
```

If valid → allow
Else → reject

---

## 🟩 AUTH FLOW VISUAL 🧠

```text
Login
  ↓
Generate Token
  ↓
Send Token
  ↓
Client Stores Token
  ↓
Authorization Header
  ↓
Protected API
```

---

## 🟩 SESSION vs JWT (INTERVIEW GOLD ⭐)

| Session       | JWT           |
| ------------- | ------------- |
| Server stored | Client stored |
| Cookie based  | Header based  |
| Web apps      | APIs          |
| Stateful      | Stateless     |

---

## 🏁 FINAL TEACHING SEQUENCE (PERFECT)

```text
Request Data
→ HTTP Methods
→ Cookies
→ Sessions
→ Authentication
→ Headers
→ JWT
```

---

## 🎯 AFTER THIS

✅ Build REST APIs
✅ Understand token auth
✅ Work with frontend & mobile apps
✅ Answer interview questions confidently



✔ Create **JWT mini project**
✔ Give **diagram slides**
✔ Provide **interview Q&A**
✔ Convert this into **PDF notes**






















Below is **DEV MODE + TEACH MODE**
👉 **Code-first**, but **every block explains *why* it exists**, like I’m mentoring you on a real project.

Assume: **Flask 2.x, Python 3.10+**

---

# 🔥 FLASK — DEV + TEACH MODE

---

## 0️⃣ Minimal App Setup (Always Start Here)

```python
from flask import Flask
app = Flask(__name__)
```



---

## 1️⃣ Routes (Request → Function Mapping)

```python
@app.route("/")
def home():
    return "Hello Flask"
```

🧠 **Teach**

* Route = URL endpoint
* Function = controller
* Browser hits `/` → Flask calls `home()`

Multiple methods:

```python
@app.route("/login", methods=["GET", "POST"])
def login():
    return "Login"
```

---

## 2️⃣ Render Template (Return HTML, not strings)

```python
from flask import render_template

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", user="admin")
```

🧠 **Teach**

* Use templates to separate **logic** from **UI**
* Never hardcode HTML in Python for real apps

---

## 3️⃣ Templates & Static (Frontend Separation)

### Folder rule (MANDATORY)

```txt
templates/   → HTML
static/      → CSS / JS / Images
```

### dashboard.html

```html
<h1>Welcome {{ user }}</h1>
```

### style.css

```css
body { font-family: Arial; }
```

```html
<link rel="stylesheet"
 href="{{ url_for('static', filename='style.css') }}">
```

🧠 **Teach**

* Flask auto-loads these folders
* `url_for()` prevents broken static links

---

## 4️⃣ Redirect (Change Flow)

```python
from flask import redirect, url_for

@app.route("/old")
def old():
    return redirect(url_for("home"))
```

🧠 **Teach**

* Redirect = new HTTP request
* Used after login, logout, form submit

---

## 5️⃣ url_for (Never Hardcode URLs)

```python
url_for("dashboard")
url_for("user", id=5)
```

🧠 **Teach**

* Refactors safely
* Flask resolves route → URL

---

## 6️⃣ Jinja Templating Engine

---

### 🔹 Variables

```html
<p>{{ username }}</p>
```

🧠 **Teach**

* Python → Template data binding

---

### 🔹 Flow Control

```html
{% if is_admin %}
Admin Panel
{% endif %}
```

```html
{% for u in users %}
<li>{{ u.name }}</li>
{% endfor %}
```

🧠 **Teach**

* Business logic stays in Python
* Display logic stays in Jinja

---

### 🔹 Inheritance (Layout Reuse)

#### base.html

```html
<body>
{% block content %}{% endblock %}
</body>
```

#### page.html

```html
{% extends "base.html" %}
{% block content %}
<h2>Page</h2>
{% endblock %}
```

🧠 **Teach**

* DRY principle
* All pages share layout

---

## 7️⃣ URL Parameters (Dynamic Routes)

```python
@app.route("/user/<int:id>")
def user(id):
    return f"User {id}"
```

🧠 **Teach**

* URL carries data
* Type safety built-in (`int`, `string`)

---

## 8️⃣ Form Handling + Validation

### HTML

```html
<form method="POST">
  <input name="email">
  <button>Save</button>
</form>
```

### Flask

```python
from flask import request

@app.route("/form", methods=["GET","POST"])
def form():
    if request.method == "POST":
        email = request.form.get("email")

        if not email:
            return "Email required", 400

        return redirect(url_for("home"))

    return render_template("form.html")
```

🧠 **Teach**

* `request.form` = POST data
* Always validate server-side

---

## 9️⃣ REST API (JSON, Not HTML)

```python
from flask import jsonify

@app.route("/api/users")
def api_users():
    return jsonify([
        {"id":1, "name":"A"},
        {"id":2, "name":"B"}
    ])
```

🧠 **Teach**

* Frontend/mobile consumes APIs
* JSON = language-agnostic

---

## 🔟 Database Connections

---

## 🔹 SQLite (Learning / Small Apps)

```python
import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT)")
conn.commit()
```

🧠 **Teach**

* File-based
* No concurrency handling

---

## 🔹 MySQL (Production)

```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="appdb"
)
```

🧠 **Teach**

* Multi-user
* Scales better
* Needs connection pooling

---

## 🔹 ORM — SQLAlchemy (RECOMMENDED)

### Setup

```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
```

### Model

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
```

### CRUD

```python
db.create_all()

u = User(name="Poovarasan")
db.session.add(u)
db.session.commit()

User.query.all()
```

🧠 **Teach**

* ORM abstracts SQL
* Portable across DBs
* Prevents SQL injection

---

## 🚀 Run App

```python
if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🧠 MENTOR SUMMARY

```txt
Route        → Entry point
Template     → UI
Static       → Assets
Redirect     → Flow control
url_for      → Safe linking
Jinja        → Dynamic HTML
Forms        → User input
API          → JSON backend
DB           → Persistence
ORM          → DB abstraction
```

---

## 🔜 NEXT (Recommended Path)

1️⃣ Blueprints (project structure)
2️⃣ JWT Authentication
3️⃣ CORS for frontend apps
4️⃣ Gunicorn + Nginx
5️⃣ Docker deployment

Tell me which one you want next and I’ll mentor you through it step-by-step.








