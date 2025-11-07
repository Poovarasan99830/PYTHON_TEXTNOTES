

```
flask_sqlite_app/
│
├── app.py
├── requirements.txt
├── render.yaml
├── Procfile
└── database.db  (created automatically when you run the app)











---

## **1️⃣ `app.py`**

```python
from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Persistent storage path (Render will mount /data)
DB_PATH = "/data/database.db"

# Create table if not exists
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return "Flask + SQLite app running on Render!"

@app.route("/add", methods=["POST"])
def add_user():
    name = request.json.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    return jsonify({"message": f"User '{name}' added successfully!"})

@app.route("/users", methods=["GET"])
def get_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    os.makedirs("/data", exist_ok=True)
    init_db()
    app.run(host="0.0.0.0", port=5000)
```

---

## **2️⃣ `requirements.txt`**

```txt
Flask==3.0.3
gunicorn==22.0.0

```







---

## **3️⃣ `Procfile`**

*(Optional for Render, but useful for portability to Heroku)*

```txt
web: gunicorn app:app
```

---

## **4️⃣ `render.yaml`**

```yaml
services:
  - type: web
    name: flask-sqlite-app
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    disk:
      name: sqlite-data
      mountPath: /data
      sizeGB: 1
```

---

## **5️⃣ How to Deploy on Render**

1. Put these files in a folder `flask_sqlite_app/`.
2. Initialize Git:

```bash
cd flask_sqlite_app
git init
git add .
git commit -m "Initial commit"
```

3. Push to GitHub:

```bash
git branch -M main
git remote add origin https://github.com/yourusername/flask_sqlite_app.git
git push -u origin main
```

4. On Render:

   * Click **New → Web Service**.
   * Select your GitHub repo.
   * Render will read `render.yaml` and deploy automatically.

.

| File            | Purpose                                           | Example                                       |
| --------------- | ------------------------------------------------- | --------------------------------------------- |
| **Procfile**    | Tells Render how to start your app                | `web: gunicorn todo_project.wsgi:application` |


| **render.yaml** | Defines deployment settings, build/start commands | auto-deploy setup      


                       |
| **.gitignore**  | Excludes unnecessary files from GitHub            | avoids `.venv`, cache, db files               |
