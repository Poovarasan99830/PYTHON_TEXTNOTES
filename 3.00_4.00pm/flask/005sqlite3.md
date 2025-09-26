Perfect ✅ You want a **360° view of SQLite3 in Python** — from basics to advanced, including best practices, projects, and even interview-level concepts. Let’s structure this like a **complete roadmap**:

---

# 🔹 360° SQLite3 in Python

## 1. Fundamentals

* **What is SQLite?**

  * File-based database (no server needed).
  * Stores data in a single `.db` file.
  * Built into Python via `sqlite3` module.

* **Why use it?**

  * Lightweight, portable, fast.
  * Perfect for local apps, testing, small-scale projects.

---

## 2. Core Concepts

### 📌 Connecting to a Database

```python
import sqlite3
conn = sqlite3.connect("mydb.db")   # creates if not exists
cur = conn.cursor()
```

### 📌 Creating Tables

```python
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
""")
```

### 📌 Inserting Data

```python
cur.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", ("Alice", 25, "alice@example.com"))
conn.commit()
```

### 📌 Fetching Data

```python
cur.execute("SELECT * FROM users")
print(cur.fetchall())   # list of tuples
```

### 📌 Updating & Deleting

```python
cur.execute("UPDATE users SET age = ? WHERE id = ?", (26, 1))
cur.execute("DELETE FROM users WHERE id = ?", (2,))
conn.commit()
```

---

## 3. Intermediate Concepts

### 📌 Parameterized Queries (prevent SQL Injection)

```python
user_input = "Alice"
cur.execute("SELECT * FROM users WHERE name = ?", (user_input,))
```

### 📌 Fetching Options

```python
cur.fetchone()   # single row
cur.fetchmany(5) # next 5 rows
cur.fetchall()   # all rows
```

### 📌 Using `with` (auto-commit and close)

```python
with sqlite3.connect("mydb.db") as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())
```

### 📌 Row Factory (fetch as dictionary)

```python
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("SELECT * FROM users")
for row in cur.fetchall():
    print(dict(row))
```

---

## 4. Advanced Features

### 📌 Transactions

```python
try:
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Eve", 28))
    conn.commit()
except:
    conn.rollback()
```

### 📌 Indexes (speed up queries)

```python
cur.execute("CREATE INDEX IF NOT EXISTS idx_name ON users(name)")
```

### 📌 Joins

```python
cur.execute("""
SELECT orders.id, users.name, orders.amount
FROM orders
JOIN users ON users.id = orders.user_id
""")
```

### 📌 Foreign Keys

```python
cur.execute("PRAGMA foreign_keys = ON;")
cur.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")
```

### 📌 Views

```python
cur.execute("CREATE VIEW IF NOT EXISTS user_orders AS SELECT users.name, orders.amount FROM users JOIN orders ON users.id=orders.user_id")
```

---

## 5. Best Practices

* Always use **parameterized queries** (`?`) → prevent SQL Injection.
* Use **indexes** for faster search on frequently queried columns.
* Use **`with sqlite3.connect()`** to auto-close connections.
* Normalize data (use foreign keys).
* For frequent reads → use **row\_factory** for dict-style access.
* For scaling → migrate to **PostgreSQL/MySQL** when needed.

---

## 6. Debugging & Utilities

* **Check tables**

```python
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())
```

* **Check schema**

```python
cur.execute("PRAGMA table_info(users)")
print(cur.fetchall())
```

* **Export/Import**

  * Copy `.db` file directly (it’s just a file).
  * Use `sqlite3` CLI tool for dump:

    ```
    sqlite3 mydb.db .dump > backup.sql
    ```

---

## 7. Real-World Mini Projects

1. **To-Do List App**

   * Tables: `tasks(id, title, status)`
   * CRUD operations.

2. **Student Management System**

   * Tables: `students`, `courses`, `enrollments`
   * Practice joins.

3. **Inventory & Billing System**

   * Products, customers, orders.
   * Use transactions.

4. **Flask/Django App with SQLite**

   * Use SQLite as backend for quick prototypes.

---

## 8. Interview / Advanced Knowledge

* **Difference b/w SQLite & other DBs**

  * Serverless, file-based, lightweight.
  * Not ideal for high concurrency.

* **Data types in SQLite**

  * `NULL`, `INTEGER`, `REAL`, `TEXT`, `BLOB` (flexible typing).

* **Limitations**

  * Limited write concurrency (single writer at a time).
  * File-size limit \~ 140TB.
  * No stored procedures or advanced user management.

* **Optimization**

  * Use **transactions** to speed up bulk inserts.
  * Use **indexes** on search-heavy columns.
  * VACUUM command to optimize DB file.

---

✅ That’s the **360° SQLite3 roadmap in Python**: basics → intermediate → advanced → best practices → projects → interview prep.

Do you want me to design a **structured 30-day learning plan with exercises & projects** so you can fully master SQLite3 hands-on?

Sure! Let’s break down this snippet **line by line** and explain what it does in a Flask + MySQL context:

---

```python
create_table()
```

* This is calling a function named `create_table()`.
* Presumably, this function **creates a table** in your MySQL database if it doesn’t exist already (like `collage` table).
* This ensures that the table is ready before you try to fetch data from it.

---

```python
cur = db.connection.cursor()
```

* `db` is probably your **Flask-MySQLdb instance**.
* `.connection.cursor()` creates a **cursor object**.
* **Cursor** is used to execute SQL queries and fetch data from the database.

---

```python
cur.execute("SELECT * FROM collage")
```

* Executes a SQL query to **fetch all rows** from the `collage` table.
* `*` means all columns.

---

```python
users = cur.fetchall()
```

* `.fetchall()` retrieves **all the results** of the query.
* The results are stored in the variable `users` as a **list of tuples**, where each tuple represents a row in the table.

---

```python
cur.close()
```

* Closes the cursor to **free up resources**.
* It’s a good practice to close cursors after use.

---

```python
return render_template("index.html", users=users)
```

* This sends the fetched data (`users`) to the HTML template `index.html`.
* In the template, you can use `users` to display the data, e.g., in a table.

---

### ✅ **Summary**

1. Ensure the table exists.
2. Connect to the database and execute a query to get all data.
3. Store the data in a variable.
4. Close the cursor.
5. Pass the data to an HTML template to display it on a webpage.

---

If you want, I can **also show an example of how `index.html` would display these users** in a table. That will make it very clear.

Do you want me to do that?
