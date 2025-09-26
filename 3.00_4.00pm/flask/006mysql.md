Perfect 👍 CRUD (Create, Read, Update, Delete) with Flask + MySQL is the best way to practice.
I’ll show you a **complete working structure** with `flask-mysqldb` covering all 4 operations.

---

# 🔹 Project Structure

```
flask_mysql_crud/
│── app.py
│── templates/
│   ├── index.html   (show all users)
│   ├── add.html     (create user)
│   ├── update.html  (update user)
```

---

# 🔹 app.py (CRUD Code)

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'country'

db = MySQL(app)

# Create table if not exists
def create_table():
    cursor = db.connection.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS collage(
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50),
            password VARCHAR(200))'''
    )
    cursor.close()

# -------------------- CREATE --------------------
@app.route("/add", methods=["GET", "POST"])
def add_user():
    create_table()
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        cur = db.connection.cursor()
        cur.execute("INSERT INTO collage(username, password) VALUES (%s, %s)", (username, password))
        db.connection.commit()
        cur.close()
        return redirect(url_for("index"))
    return render_template("add.html")

# -------------------- READ --------------------
@app.route("/")
def index():
    create_table()
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM collage")
    users = cur.fetchall()
    cur.close()
    return render_template("index.html", users=users)

# -------------------- UPDATE --------------------
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_user(id):
    cur = db.connection.cursor()
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        cur.execute("UPDATE collage SET username=%s, password=%s WHERE id=%s",
                    (username, password, id))
        db.connection.commit()
        cur.close()
        return redirect(url_for("index"))
    cur.execute("SELECT * FROM collage WHERE id=%s", (id,))
    user = cur.fetchone()
    cur.close()
    return render_template("update.html", user=user)

# -------------------- DELETE --------------------
@app.route("/delete/<int:id>")
def delete_user(id):
    cur = db.connection.cursor()
    cur.execute("DELETE FROM collage WHERE id=%s", (id,))
    db.connection.commit()
    cur.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
```

---

# 🔹 index.html (READ - Show all users)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Users</title>
</head>
<body>
    <h1>All Users</h1>
    <a href="{{ url_for('add_user') }}">➕ Add User</a>
    <table border="1" cellpadding="5" cellspacing="0">
        <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Password</th>
            <th>Actions</th>
        </tr>
        {% for user in users %}
        <tr>
            <td>{{ user[0] }}</td>
            <td>{{ user[1] }}</td>
            <td>{{ user[2] }}</td>
            <td>
                <a href="{{ url_for('update_user', id=user[0]) }}">✏️ Update</a> | 
                <a href="{{ url_for('delete_user', id=user[0]) }}">🗑️ Delete</a>
            </td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

---

# 🔹 add.html (CREATE)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Add User</title>
</head>
<body>
    <h1>Add New User</h1>
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username" required><br><br>
        
        <label>Password:</label>
        <input type="text" name="password" required><br><br>
        
        <button type="submit">Add</button>
    </form>
</body>
</html>
```

---

# 🔹 update.html (UPDATE)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Update User</title>
</head>
<body>
    <h1>Update User</h1>
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username" value="{{ user[1] }}" required><br><br>
        
        <label>Password:</label>
        <input type="text" name="password" value="{{ user[2] }}" required><br><br>
        
        <button type="submit">Update</button>
    </form>
</body>
</html>
```

---

✅ Now you have a **full CRUD app in Flask with MySQL**:

* `/` → Show all users (READ)
* `/add` → Add user (CREATE)
* `/update/<id>` → Update user (UPDATE)
* `/delete/<id>` → Delete user (DELETE)

---

👉 Do you want me to extend this into a **REST API (returning JSON instead of HTML pages)**, so you can use it for React/Angular frontend too?
















Perfect 🚀 Let’s extend the Flask + MySQL **CRUD app** into a **REST API** that returns **JSON responses** instead of rendering HTML pages.
This way you can easily connect React, Angular, or even a mobile app.

---

# 🔹 app.py (Flask REST API with MySQL)

```python
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'country'

db = MySQL(app)

# Create table if not exists
def create_table():
    cursor = db.connection.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS collage(
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50),
            password VARCHAR(200))'''
    )
    cursor.close()

# -------------------- CREATE --------------------
@app.route("/api/users", methods=["POST"])
def add_user():
    create_table()
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    cur = db.connection.cursor()
    cur.execute("INSERT INTO collage(username, password) VALUES (%s, %s)", (username, password))
    db.connection.commit()
    cur.close()

    return jsonify({"message": "User created successfully!"}), 201

# -------------------- READ ALL --------------------
@app.route("/api/users", methods=["GET"])
def get_users():
    create_table()
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM collage")
    rows = cur.fetchall()
    cur.close()

    users = [{"id": row[0], "username": row[1], "password": row[2]} for row in rows]
    return jsonify(users)

# -------------------- READ ONE --------------------
@app.route("/api/users/<int:id>", methods=["GET"])
def get_user(id):
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM collage WHERE id=%s", (id,))
    row = cur.fetchone()
    cur.close()

    if row:
        return jsonify({"id": row[0], "username": row[1], "password": row[2]})
    return jsonify({"error": "User not found"}), 404

# -------------------- UPDATE --------------------
@app.route("/api/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    cur = db.connection.cursor()
    cur.execute("UPDATE collage SET username=%s, password=%s WHERE id=%s", (username, password, id))
    db.connection.commit()
    cur.close()

    return jsonify({"message": "User updated successfully!"})

# -------------------- DELETE --------------------
@app.route("/api/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    cur = db.connection.cursor()
    cur.execute("DELETE FROM collage WHERE id=%s", (id,))
    db.connection.commit()
    cur.close()

    return jsonify({"message": "User deleted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
```

---

# 🔹 API Endpoints

| Method   | Endpoint          | Description       |
| -------- | ----------------- | ----------------- |
| `POST`   | `/api/users`      | Create a new user |
| `GET`    | `/api/users`      | Get all users     |
| `GET`    | `/api/users/<id>` | Get single user   |
| `PUT`    | `/api/users/<id>` | Update user       |
| `DELETE` | `/api/users/<id>` | Delete user       |

---

# 🔹 Example Requests (with `curl` or Postman)

### 1. Create User

```bash
curl -X POST http://127.0.0.1:5000/api/users \
     -H "Content-Type: application/json" \
     -d '{"username":"John","password":"1234"}'
```

### 2. Get All Users

```bash
curl http://127.0.0.1:5000/api/users
```

### 3. Get Single User

```bash
curl http://127.0.0.1:5000/api/users/1
```

### 4. Update User

```bash
curl -X PUT http://127.0.0.1:5000/api/users/1 \
     -H "Content-Type: application/json" \
     -d '{"username":"John Doe","password":"abcd"}'
```

### 5. Delete User

```bash
curl -X DELETE http://127.0.0.1:5000/api/users/1
```

---

✅ Now you have a **REST API CRUD** ready to connect with React, Angular, or even mobile apps.

👉 Do you also want me to show you how to **secure this API with JWT authentication** (so only logged-in users can perform CRUD)?














Great choice 🚀 — securing your Flask + MySQL CRUD API with **JWT authentication** is the professional way to go. Let’s build on top of the CRUD app I gave you.

We’ll use **Flask-JWT-Extended** for JWT handling.

---

# 🔹 Install Dependencies

```bash
pip install flask-mysqldb flask-jwt-extended
```

---

# 🔹 Updated `app.py` with JWT Security

```python
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# ---------------- Database Config ----------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'country'
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # change in production!

db = MySQL(app)
jwt = JWTManager(app)

# ---------------- Create Table ----------------
def create_table():
    cur = db.connection.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS collage(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    username VARCHAR(50) UNIQUE,
                    password VARCHAR(200))''')
    cur.close()

# ---------------- AUTH: Register ----------------
@app.route("/register", methods=["POST"])
def register():
    create_table()
    data = request.get_json()
    username = data.get("username")
    password = generate_password_hash(data.get("password"))

    cur = db.connection.cursor()
    try:
        cur.execute("INSERT INTO collage(username, password) VALUES (%s, %s)", (username, password))
        db.connection.commit()
    except Exception as e:
        return jsonify({"error": "User already exists"}), 400
    finally:
        cur.close()

    return jsonify({"message": "User registered successfully!"}), 201

# ---------------- AUTH: Login ----------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    cur = db.connection.cursor()
    cur.execute("SELECT * FROM collage WHERE username=%s", (username,))
    user = cur.fetchone()
    cur.close()

    if user and check_password_hash(user[2], password):
        access_token = create_access_token(identity=user[0])  # use ID as identity
        return jsonify({"access_token": access_token})
    return jsonify({"error": "Invalid username or password"}), 401

# ---------------- CRUD: Protected ----------------
@app.route("/api/users", methods=["GET"])
@jwt_required()
def get_users():
    cur = db.connection.cursor()
    cur.execute("SELECT id, username FROM collage")
    rows = cur.fetchall()
    cur.close()
    return jsonify([{"id": r[0], "username": r[1]} for r in rows])

@app.route("/api/users/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    current_user = get_jwt_identity()
    if current_user != id:
        return jsonify({"error": "Unauthorized action"}), 403

    cur = db.connection.cursor()
    cur.execute("DELETE FROM collage WHERE id=%s", (id,))
    db.connection.commit()
    cur.close()
    return jsonify({"message": "User deleted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
```

---

# 🔹 How It Works

1. **Register (`/register`)**

   * Creates a user (password stored as hash).

2. **Login (`/login`)**

   * Returns a **JWT access token**.

3. **Use JWT in Requests**
   Add header:

   ```
   Authorization: Bearer <your_token>
   ```

4. **Protected Endpoints**
   Example: `GET /api/users` only works if you send a valid JWT.

---

# 🔹 Example Flow (with `curl`)

### 1. Register

```bash
curl -X POST http://127.0.0.1:5000/register \
     -H "Content-Type: application/json" \
     -d '{"username":"john","password":"1234"}'
```

### 2. Login (Get Token)

```bash
curl -X POST http://127.0.0.1:5000/login \
     -H "Content-Type: application/json" \
     -d '{"username":"john","password":"1234"}'
```

Response:

```json
{"access_token": "eyJ0eXAiOiJKV1QiLCJh..."}
```

### 3. Access Protected API

```bash
curl http://127.0.0.1:5000/api/users \
     -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJh..."
```

---

✅ Now your CRUD API is **secured with JWT**.
👉 Do you want me to extend this with **role-based access (admin/user)** so only admins can delete/update users?















Perfect 🚀 — let’s extend your **Flask + MySQL + JWT** project with **Role-Based Access Control (RBAC)** so that:

* **Admin** can view, add, update, and delete users.
* **Normal users** can only view their own details.

---

## 🔹 Updated Table with Role Column

We add a `role` field (`admin` or `user`):

```sql
ALTER TABLE collage ADD role VARCHAR(20) DEFAULT 'user';
```

---

## 🔹 Updated `app.py`

```python
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# ---------------- Database Config ----------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'country'
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # change in production!

db = MySQL(app)
jwt = JWTManager(app)

# ---------------- Create Table ----------------
def create_table():
    cur = db.connection.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS collage(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    username VARCHAR(50) UNIQUE,
                    password VARCHAR(200),
                    role VARCHAR(20) DEFAULT 'user')''')
    cur.close()

# ---------------- AUTH: Register ----------------
@app.route("/register", methods=["POST"])
def register():
    create_table()
    data = request.get_json()
    username = data.get("username")
    password = generate_password_hash(data.get("password"))
    role = data.get("role", "user")  # default is "user"

    cur = db.connection.cursor()
    try:
        cur.execute("INSERT INTO collage(username, password, role) VALUES (%s, %s, %s)", 
                    (username, password, role))
        db.connection.commit()
    except Exception as e:
        return jsonify({"error": "User already exists"}), 400
    finally:
        cur.close()

    return jsonify({"message": "User registered successfully!"}), 201

# ---------------- AUTH: Login ----------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    cur = db.connection.cursor()
    cur.execute("SELECT * FROM collage WHERE username=%s", (username,))
    user = cur.fetchone()
    cur.close()

    if user and check_password_hash(user[2], password):
        access_token = create_access_token(identity={"id": user[0], "role": user[3]})
        return jsonify({"access_token": access_token})
    return jsonify({"error": "Invalid username or password"}), 401

# ---------------- Helper: Admin Required ----------------
def admin_required(identity):
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

# ---------------- CRUD: View All Users (Admin only) ----------------
@app.route("/api/users", methods=["GET"])
@jwt_required()
def get_users():
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    cur = db.connection.cursor()
    cur.execute("SELECT id, username, role FROM collage")
    rows = cur.fetchall()
    cur.close()
    return jsonify([{"id": r[0], "username": r[1], "role": r[2]} for r in rows])

# ---------------- CRUD: View Own Profile (Any user) ----------------
@app.route("/api/profile", methods=["GET"])
@jwt_required()
def get_profile():
    identity = get_jwt_identity()
    cur = db.connection.cursor()
    cur.execute("SELECT id, username, role FROM collage WHERE id=%s", (identity["id"],))
    user = cur.fetchone()
    cur.close()
    return jsonify({"id": user[0], "username": user[1], "role": user[2]})

# ---------------- CRUD: Delete User (Admin only) ----------------
@app.route("/api/users/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    cur = db.connection.cursor()
    cur.execute("DELETE FROM collage WHERE id=%s", (id,))
    db.connection.commit()
    cur.close()
    return jsonify({"message": "User deleted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🔹 How It Works

### Register User

```bash
curl -X POST http://127.0.0.1:5000/register \
     -H "Content-Type: application/json" \
     -d '{"username":"alice","password":"1234","role":"admin"}'
```

### Login (Get Token)

```bash
curl -X POST http://127.0.0.1:5000/login \
     -H "Content-Type: application/json" \
     -d '{"username":"alice","password":"1234"}'
```

Response:

```json
{"access_token": "eyJhbGciOiJIUzI1NiIsInR..."}
```

### Access as Admin

```bash
curl http://127.0.0.1:5000/api/users \
     -H "Authorization: Bearer <token>"
```

### Access as Normal User

```bash
curl http://127.0.0.1:5000/api/profile \
     -H "Authorization: Bearer <token>"
```

---

✅ Now you have **Role-Based Access Control** in your CRUD app.

👉 Do you want me to also add **Update (PUT) operation with RBAC** so that:

* Users can update **their own profile**
* Admins can update **any user**?








Great 👍 Let’s add **Update (PUT)** with RBAC:

* **Users** → Can update only their own `username/password`.
* **Admins** → Can update any user’s `username/password/role`.

---

## 🔹 Updated `app.py` (only new part added at bottom)

```python
# ---------------- CRUD: Update User ----------------
@app.route("/api/users/<int:id>", methods=["PUT"])
@jwt_required()
def update_user(id):
    identity = get_jwt_identity()
    data = request.get_json()

    cur = db.connection.cursor()

    # If normal user → can update only themselves
    if identity["role"] == "user":
        if identity["id"] != id:
            return jsonify({"error": "You can only update your own profile"}), 403

        username = data.get("username")
        password = data.get("password")

        if username:
            cur.execute("UPDATE collage SET username=%s WHERE id=%s", (username, id))
        if password:
            from werkzeug.security import generate_password_hash
            hashed_pw = generate_password_hash(password)
            cur.execute("UPDATE collage SET password=%s WHERE id=%s", (hashed_pw, id))

        db.connection.commit()
        cur.close()
        return jsonify({"message": "Profile updated successfully!"})

    # If admin → can update anyone (username, password, role)
    elif identity["role"] == "admin":
        username = data.get("username")
        password = data.get("password")
        role = data.get("role")

        if username:
            cur.execute("UPDATE collage SET username=%s WHERE id=%s", (username, id))
        if password:
            from werkzeug.security import generate_password_hash
            hashed_pw = generate_password_hash(password)
            cur.execute("UPDATE collage SET password=%s WHERE id=%s", (hashed_pw, id))
        if role:
            cur.execute("UPDATE collage SET role=%s WHERE id=%s", (role, id))

        db.connection.commit()
        cur.close()
        return jsonify({"message": "User updated successfully by Admin!"})

    cur.close()
    return jsonify({"error": "Invalid role"}), 403
```

---

## 🔹 Usage Examples

### ✅ User updating their own profile

```bash
curl -X PUT http://127.0.0.1:5000/api/users/2 \
     -H "Authorization: Bearer <user_token>" \
     -H "Content-Type: application/json" \
     -d '{"username":"new_user","password":"newpass"}'
```

### ✅ Admin updating another user’s role

```bash
curl -X PUT http://127.0.0.1:5000/api/users/3 \
     -H "Authorization: Bearer <admin_token>" \
     -H "Content-Type: application/json" \
     -d '{"role":"admin"}'
```

---

⚡ Now your CRUD API has **full RBAC**:

* Register ✅
* Login ✅
* View All Users (Admin) ✅
* View Own Profile (User) ✅
* Delete User (Admin) ✅
* Update User/Profile (Admin/User) ✅

---

Would you like me to also add a **refresh token system** (so users don’t need to log in again and again when the access token expires)?










Ah! This is a common question when using **MySQL (or any SQL database) with Python**. Let me explain clearly.

---

### **1️⃣ Purpose of `%s`**

In your line:

```python
cur.execute("INSERT INTO collage23(username, password) VALUES (%s, %s)", (username, password))
```

* `%s` **acts as a placeholder** for the values you want to insert.
* The actual values are passed **separately** as a tuple `(username, password)`.
* This is called **parameterized queries**.

---

### **2️⃣ Why Not Direct String Formatting**

You might think of doing this:

```python
cur.execute(f"INSERT INTO collage23(username, password) VALUES ('{username}', '{password}')")
```

❌ **This is unsafe** because:

* It can lead to **SQL injection attacks** if `username` or `password` contains malicious SQL code.
* Parameterized queries (`%s`) **safely escape values** for you.

---

### **3️⃣ How it Works**

1. `%s` is replaced internally by the **escaped value** from the tuple `(username, password)`.
2. Database receives a safe, properly formatted SQL query.
3. You don’t have to worry about quotes, special characters, or SQL injection.

---

### **4️⃣ Example**

```python
username = "alice"
password = "mypassword123"
cur.execute("INSERT INTO collage23(username, password) VALUES (%s, %s)", (username, password))
```

* The database sees:

```sql
INSERT INTO collage23(username, password) VALUES ('alice', 'mypassword123');
```

* Safe and secure.

---

If you want, I can **show a diagram of how `%s` placeholders work internally** in Python MySQL, which makes it super clear why we don’t use normal string formatting.

Do you want me to do that?










Great! Let’s visualize **how `%s` placeholders work internally** when you execute a query in Python MySQL.

---

### **Diagram: How `%s` Works**

```
Python Code:
-------------------------
username = "alice"
password = "mypassword123"
cur.execute(
    "INSERT INTO collage23(username, password) VALUES (%s, %s)",
    (username, password)
)

Step 1: SQL with placeholders
-------------------------
INSERT INTO collage23(username, password) VALUES (%s, %s)

Step 2: Python/MySQL Driver Escapes Values
-------------------------
- "alice"  -> safely escaped as 'alice'
- "mypassword123" -> safely escaped as 'mypassword123'

Step 3: Final SQL Sent to Database
-------------------------
INSERT INTO collage23(username, password)
VALUES ('alice', 'mypassword123');

Step 4: Database executes the query
-------------------------
New row is inserted into `collage23` table
```

---

### **Key Points**

1. `%s` is **not Python string formatting**. It’s a **placeholder recognized by the MySQL driver**.
2. Actual values are **passed separately** as a tuple `(username, password)`.
3. The driver **handles escaping automatically**, protecting against SQL injection.
4. Always use `%s` **instead of f-strings or `+` concatenation** for database queries.

---

If you want, I can also **show an example of what happens if you don’t use `%s` and try direct string formatting**, so you can see why it’s risky.

Do you want me to show that?
