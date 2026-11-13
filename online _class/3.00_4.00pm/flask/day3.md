

# 1. Flask Route (`@app.route()`)

## Definition

A **Route** tells Flask **which function should run when a particular URL is requested.**

**Syntax**

```python
@app.route("/hello")
def display():
    return "Hello World"
```

---

## Why?

Without routes, Flask doesn't know

> "User `/hello` request pannanga...
> Which function execute pannanum?"

Route solves this problem.

---

## How it works?

```
Browser
   |
GET /hello
   |
Flask
   |
Looks for @app.route("/hello")
   |
display()
   |
Returns "Hello World"
```

---

## Real World Analogy 🏢

Imagine a hospital.

Receptionist asks

> "Which doctor?"

```
Heart → Heart Doctor

Eye → Eye Doctor

Skin → Skin Doctor
```

Similarly,

```
/hello → display()

/login → login()

/register → register()
```

Route acts like the receptionist.

---

# 2. Rendering HTML Templates (`render_template()`)

## Definition

`render_template()` is used to **display an HTML page** from the `templates` folder.

```python
return render_template("register.html")
```

---

## Why?

Instead of returning plain text,

```
Hello World
```

we usually want a proper webpage with

* Buttons
* Forms
* Images
* CSS
* Tables

HTML is needed for that.

---

## How?

```
Browser
      |
GET /register
      |
Flask
      |
render_template("register.html")
      |
templates/register.html
      |
HTML page shown
```

---

## Real World Analogy

Restaurant example.

Customer:

"I need Menu Card."

Waiter goes inside

Brings Menu Card.

```
Customer
     ↓
Waiter
     ↓
Kitchen
     ↓
Menu Card
```

Similarly

```
Browser
      ↓
Flask
      ↓
Templates Folder
      ↓
HTML Page
```

---

# 3. URL Parameters

URL parameters send data through the URL.

There are **2 types**

* Path Parameters
* Query Parameters

---

# 4. Path Parameters

## Definition

Path parameters are values written **inside the URL path**.

Example

```python
@app.route("/greet/<name>")
def greet_user(name):
    return f"Hello {name}"
```

URL

```
/greet/Poovarasan
```

Output

```
Hello Poovarasan
```

---

## Why?

To identify **one specific resource**.

Example

```
User 1

User 2

User 3
```

Each user has different URL.

---

## How?

```
Browser

/greet/Ram

      ↓

Flask

name="Ram"

      ↓

Function executes
```

---

## Real World Example

House Address

```
House No 10

House No 20

House No 30
```

Address directly identifies one house.

Similarly,

```
/product/25

/order/101

/student/45
```

---

# 5. Query Parameters

## Definition

Query parameters send data using **key=value** after `?`

Example

```
/user?name=John
```

Python

```python
name = request.args.get("name")
```

---

## Why?

Used for

* Search
* Filter
* Sort
* Pagination

---

## How?

```
Browser

/user?name=John

        ↓

Flask

request.args.get("name")

        ↓

John
```

---

## Real World Example

Amazon Search

```
Shoes

Brand=Nike

Price=1000
```

URL

```
/products?brand=nike&price=1000
```

---

# Difference

| Path Parameter      | Query Parameter  |
| ------------------- | ---------------- |
| Inside URL          | After `?`        |
| Identifies resource | Filters data     |
| Mandatory           | Usually optional |
| `/user/10`          | `/user?id=10`    |

---

# 6. Form Data

## Definition

Form data is information entered by the user in an HTML form.

Example

```
Name

Email

Password
```

---

## Why?

To collect user information.

Examples

* Login
* Registration
* Contact Form

---

## How?

```
User

↓

HTML Form

↓

POST Request

↓

Flask

↓

request.form.get()

↓

Database
```

---

# 7. `request.form.get()`

## Definition

Used to read form values submitted by the user.

```python
name = request.form.get("name")
```

---

## Why?

Without this, Flask cannot read the values entered in the form.

---

## Real World Analogy

Application Form

Student fills

```
Name

Email

Phone
```

Office staff reads the form.

Similarly,

```
HTML Form

↓

request.form.get()

↓

Python Variable
```

---

# 8. HTTP Methods

HTTP methods tell the server **what action the client wants to perform**.

---

## GET

### Definition

Used to **retrieve data**.

```python
@app.route("/users")
```

Example

```
Open Google

Search Products

View Profile
```

Analogy

Library → Read a book.

---

## POST

### Definition

Used to **send new data**.

Example

```
Register

Login

Submit Form
```

Analogy

Fill a college admission form.

---

## PUT

### Definition

Used to **update existing data**.

Example

```
Update Profile

Change Password
```

Analogy

Changing your Aadhaar address.

---

## DELETE

### Definition

Used to **remove data**.

Example

```
Delete Account

Delete Product
```

Analogy

Throwing a document into the dustbin.

---

# 9. SQLite Database

## Definition

SQLite is a lightweight database stored as a **single file**.

```
mydatabase.db
```

---

## Why?

To store data permanently.

Without a database,

```
Restart server

↓

All data lost
```

With a database,

```
Restart server

↓

Data remains
```

---

## Real World Analogy

Notebook

You write today's attendance.

Tomorrow it's still there.

Database works the same way.

---

# 10. Database Connection

## Definition

A database connection links your Flask application to the database.

```python
conn = sqlite3.connect(database)
```

---

## Why?

Without a connection, Flask cannot

* Insert
* Update
* Delete
* Read data

---

## Real World Analogy

Phone Call

You cannot talk to your friend until the call is connected.

Similarly,

```
Flask

↓

Connection

↓

Database
```

---

# 11. Table Creation

## Definition

A table stores data in rows and columns.

```sql
CREATE TABLE users(...)
```

---

## Why?

To organize information.

Example

| id | name | email                                   |
| -- | ---- | --------------------------------------- |
| 1  | John | [john@gmail.com](mailto:john@gmail.com) |

---

## Real World Analogy

An Excel sheet.

---

# 12. INSERT Data

## Definition

Used to store new records in the database.

```sql
INSERT INTO users(...)
```

---

## Why?

When a new user registers, their details must be saved permanently.

---

## Flow

```
User

↓

Register Form

↓

POST Request

↓

request.form.get()

↓

Database Connection

↓

INSERT Query

↓

Data Saved
```

---

# 13. `create_table()`

## Definition

Creates the `users` table if it does not already exist.

---

## Why?

Without a table, there is nowhere to store user data.

---

# 14. `if __name__ == "__main__":`

## Definition

Runs the Flask application only when this file is executed directly.

```python
if __name__ == "__main__":
    create_table()
    app.run(debug=True)
```

---

## Why?

It prevents the application from starting automatically when the file is imported into another Python file.

---

## Real World Analogy

A TV remote.

Press the **Power** button to start the TV. Until then, the TV stays off.

Similarly,

```
Python File

↓

if __name__ == "__main__"

↓

Start Flask Server
```

---

# 🎯 Complete Flow (Easy to Teach)

```text
Browser
   │
   ▼
User opens /register
   │
   ▼
Flask Route (@app.route)
   │
   ▼
render_template("register.html")
   │
   ▼
Registration Form Displayed
   │
User enters Name, Email, Password
   │
Clicks Submit
   │
   ▼
POST Request → /insert
   │
   ▼
request.form.get()
   │
   ▼
Database Connection
   │
   ▼
INSERT INTO users
   │
   ▼
SQLite Database (mydatabase.db)
   │
   ▼
"Data inserted successfully"
```

This sequence helps students understand the **entire Flask application flow**, from opening a webpage to saving data in the database.
