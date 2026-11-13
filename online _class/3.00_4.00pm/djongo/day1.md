
# ----------------------------
Flask vs Django  Difference
# ----------------------------


| Feature           | Flask                                                    | Django                                                         |
| ----------------- | -------------------------------------------------------- | -------------------------------------------------------------- |
| Framework Type    | Micro-framework (lightweight, minimal)                   | Full-stack framework (batteries included)                      |
| Flexibility       | Highly flexible, developer chooses everything            | Strict structure, follows predefined rules                     |
| Built-in Features | Limited (no built-in ORM, admin, auth)                   | Comes with ORM, admin panel, authentication, security          |
| Development Speed | Slower for large apps (manual setup needed)              | Faster for large apps (ready-to-use components)                |
| Use Case          | Best for APIs, microservices, AI/ML apps, small projects | Best for large applications like e-commerce, ERP, social media |


# --------------------------------------------
MVC vs MVT Architecture Difference
# --------------------------------------------


| Feature           | MVC (Model–View–Controller)                      | MVT (Model–View–Template)                                |
| ----------------- | ------------------------------------------------ | -------------------------------------------------------- |
| Full Form         | Model – View – Controller                        | Model – View – Template                                  |
| Used In           | Flask, Spring, ASP.NET, Laravel                  | Django                                                   |
| Control Flow      | Controller handles user requests                 | Django framework handles control internally              |
| View Role         | UI + presentation logic                          | Only presentation (HTML rendering)                       |
| Controller Role   | Acts as middle layer between Model and View      | No explicit controller (Django handles it automatically) |
| Developer Control | More manual control over flow                    | Framework manages flow internally                        |
| Complexity        | Slightly more complex due to explicit controller | Simpler for web apps using Django                        |


# ----------------------------

# _____________________________________________________
    # Django installation AND project setup
# _____________________________________________________



#Django installation and setup

py -m venv myenv
myenv/Scripys/activate
pip install django


django-admin startproject myproject .
python manage.py startapp myapp
python manage.py runserver



# ____________________________________________________
### **2 Project Folder (`myproject/`)**
# _____________________________________________________


django-admin startproject myproject → creates a new folder myproject.

This folder contains the **project configuration files**.

🔹 `__init__.py`---->* Empty file but **makes Python treat this folder as a package**.

🔹 `settings.py`---->* The **heart of the project**.
                     * Configure database, installed apps, middleware, templates, static files, etc.

🔹 `urls.py`    ---->* The **URL roadmap**.* Maps URLs to views.



🔹 `wsgi.py` and `asgi.py`---->* **Server integration files**.

                          ---->* WSGI → traditional web servers.
                          ----->* ASGI → asynchronous servers (websockets, async views).


                          WSGI is synchronous and suitable for traditional Django apps, while ASGI supports asynchronous communication and is required for real-time features like WebSockets.


                          WSGI:

                            WSGI (Web Server Gateway Interface) is a standard interface that defines how a web server communicates with a Python web application in a synchronous (blocking) manner.

                            WSGI handles one request at a time per worker → simple & stable

                          
                          ASGI:
                            ASGI (Asynchronous Server Gateway Interface) is a modern Python interface standard that defines how a web server communicates with Python applications using both synchronous and asynchronous (non-blocking) communication.


                           


# _____________________________________________________
## 🧩 **3️⃣ Django App Structure**
# _____________________________________________________


Create an app inside the project:


python manage.py startapp myapp


myapp/
│
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── migrations/
```

### 🔹 File Roles:

* `models.py` → defines database tables (ORM).
* `views.py` → contains business logic and request handling.
* `urls.py` (optional) → app-level URL routing.
* `admin.py` → register models for Django admin panel.
* `apps.py` → app configuration (auto-generated).
* `migrations/` → stores database migration files.




| Section                      | Purpose                         |
| ---------------------------- | ------------------------------- |
| `BASE_DIR`                   | Root folder path                |
| `SECRET_KEY`                 | Used for encryption             |
| `DEBUG`                      | Development mode toggle         |
| `ALLOWED_HOSTS`              | Allowed domains                 |
| `INSTALLED_APPS`             | Registered Django & custom apps |
| `MIDDLEWARE`                 | Request/response filters        |
| `ROOT_URLCONF`               | Main URLs file                  |
| `TEMPLATES`                  | Template engine settings        |
| `DATABASES`                  | Database connection             |
| `AUTH_PASSWORD_VALIDATORS`   | Password strength rules         |
| `LANGUAGE_CODE`, `TIME_ZONE` | Localization                    |
| `STATIC_URL`                 | Static file handling            |
| `REST_FRAMEWORK`             | DRF pagination setup            |




---_______________________________________________________________________

## **Summary**

> “In Django, the project folder contains `manage.py` to run commands.
> The inner project folder has all configuration files like `settings.py`, `urls.py`, `wsgi/asgi.py`.
> Each app has its own 
    `models.py`, 
    `views.py`,
    `templates` folder, and 
    `admin.py` for modularity.
> This structure is clear, organized, and scalable for both small and large projects.”



_______________________________________________________________________
# Django Intro
_______________________________________________________________________



render--->used to return template files

What is a URL parameter-->

| URL                  | Meaning                 |
| -------------------- | ----------------------- |
| `/product/10/`       | Show product with ID 10 |
| `/user/5/`           | Show user with ID 5     |
| `/post/hello-world/` | Show blog post          |


| Type    | Syntax        | Example URL          | Value       |
| ------- | ------------- | -------------------- | ----------- |
| Integer | `<int:id>`    | `/user/10/`          | 10          |Only numbers (integers) are allowed.
| String  | `<str:name>`  | `/user/john/`        | john        |Accepts text (letters) — no slashes /.
| Slug    | `<slug:post>` | `/post/hello-world/` | hello-world |Clean URL format → letters + numbers + hyphen (-)
| UUID    | `<uuid:id>`   | `/user/uuid/`        | uuid value  |Unique long ID (random string) — used for security & uniqueness
                                                                 UUID = Universally Unique Identifier
                                                                 
| Path    | `<path:file>` | `/file/a/b/c/`       | a/b/c       |Accepts full path including slashes



Why do we use URL Parameters in Django?
   URL parameters are used to pass data through the URL to a view function.


Query Parameters
   these come after the question mark (?) in the URL.
   /user/?id=5
    user_id = request.GET.get('id')


# _______________________________________________________________________
