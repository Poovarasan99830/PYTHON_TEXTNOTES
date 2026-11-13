

# 🧩 **1️⃣ Install MySQL and Required Packages**

First, make sure MySQL Server is installed and running on your system.
Then install the Python MySQL connector:

```bash
pip install mysqlclient
```

✅ Alternative (if `mysqlclient` fails):

```bash
pip install PyMySQL
```

(We’ll show both options below 👇)

---

# ⚙️ **2️⃣ Update Your `settings.py`**

Find this section in your Django project’s main `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Replace it with the MySQL configuration:

---

## ✅ **Option 1: Using `mysqlclient` (Recommended)**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'studentdb',          # Database name
        'USER': 'root',               # MySQL username
        'PASSWORD': 'yourpassword',   # MySQL password
        'HOST': 'localhost',          # Or your DB host
        'PORT': '3306',               # Default MySQL port
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
```

---

## ✅ **Option 2: Using `PyMySQL`**

If you installed `PyMySQL` instead of `mysqlclient`,
add this **line at the top** of your `__init__.py` (in your main project folder):

```python
import pymysql
pymysql.install_as_MySQLdb()
```

Then use the **same DATABASES** settings as above.

---

# 🗃️ **3️⃣ Create the Database in MySQL**

Open MySQL terminal or use a tool like phpMyAdmin / MySQL Workbench.

Run:

```sql
CREATE DATABASE studentdb;
```

*(Make sure the name matches `NAME` in your Django settings.)*

---

# 🧱 **4️⃣ Apply Migrations**

Now apply Django’s migrations to create tables in your MySQL database:

```bash
python manage.py makemigrations
python manage.py migrate
```

✅ This will automatically create all Django system tables + your models inside MySQL.

---

# 🧑‍💻 **5️⃣ Create Superuser (for admin panel)**

```bash
python manage.py createsuperuser
```

Then login at:
👉 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

# 🧠 **6️⃣ Verify Connection**

You can confirm it’s connected by checking in MySQL:

```sql
USE studentdb;
SHOW TABLES;
```

You should see tables like:

```
auth_user
student_app_studentregistration
django_session
django_admin_log
```

---

# ⚡ **7️⃣ (Optional) Troubleshooting Tips**

| Error                                                          | Fix                                                                   |
| -------------------------------------------------------------- | --------------------------------------------------------------------- |
| `django.db.utils.OperationalError: (1045, "Access denied...")` | Check username/password                                               |
| `ModuleNotFoundError: No module named 'MySQLdb'`               | Install `mysqlclient` or use `PyMySQL`                                |
| `Can't connect to MySQL server`                                | Ensure MySQL service is running (`sudo service mysql start`)          |
| Charset error                                                  | Add `'OPTIONS': {'charset': 'utf8mb4'}` inside `DATABASES['default']` |

---

# ✅ **8️⃣ Final Check**

Run your Django server again:

```bash
python manage.py runserver
```

Then test:

* Create a student using your form
* Check MySQL → `SELECT * FROM student_app_studentregistration;`
  (you’ll see your saved record 🎉)

---

# 🧾 **Summary**

| Step | Action                                 |
| ---- | -------------------------------------- |
| 1️⃣  | Install `mysqlclient` or `PyMySQL`     |
| 2️⃣  | Update `settings.py` DATABASES section |
| 3️⃣  | Create the database manually in MySQL  |
| 4️⃣  | Run `makemigrations` + `migrate`       |
| 5️⃣  | Create superuser and runserver         |
| ✅  | Django now uses MySQL as backend       |

---___________________________________________________________________
