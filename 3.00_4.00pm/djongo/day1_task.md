


## 🧩 **Project Structure**

```
django_learning_portal/
│
├── manage.py
├── django_learning_portal/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── learning/
    ├── __init__.py
    ├── urls.py
    ├── views.py
    ├── models.py
    ├── static/
    │   ├── css/style.css
    │   └── images/logo.png
    └── templates/learning/
        ├── base.html
        ├── home.html
        ├── about.html
        ├── contact.html
        ├── hello.html
        ├── student.html
        ├── courses.html
        ├── marks.html
        ├── products.html
        ├── product_detail.html
        ├── report.html
        └── portfolio/
            ├── home.html
            ├── about.html
            ├── skills.html
            ├── projects.html
            └── contact.html
```

---

## ⚙️ **Step-by-Step Implementation**

### 🧠 **Task 2 – Multi-Page Navigation**

**Concepts:** Multiple templates, routing

* Add routes in `learning/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```

* Add views:

```python
def home(request):
    return render(request, 'learning/home.html')

def about(request):
    return render(request, 'learning/about.html')

def contact(request):
    return render(request, 'learning/contact.html')



* Add navigation links (`<a href="{% url 'about' %}">About</a>`).

 ____________________________________________________________________________________




### ⚙️ **Task 3 – Dynamic URLs**

**Concepts:** URL parameters

* Add in `urls.py`:

```python
path('hello/<str:name>/', views.hello_user, name='hello_user'),
```

* In `views.py`:

```python
def hello_user(request, name):
    return render(request, 'learning/hello.html', {'name': name})
```

* In `hello.html`:

```html
<h2>Hello, {{ name }}! Welcome to Django.</h2>
```

------____________________________________________________________________________________

### ⚙️ **Task 4 – Passing Data to Templates**

**Concepts:** Context dictionary

```python
def student_info(request):
    student = {'name': 'Ravi', 'roll': 101, 'course': 'Python Full Stack'}
    return render(request, 'learning/student.html', {'student': student})

def course_list(request):
    courses = ['Python', 'Django', 'Flask', 'HTML', 'CSS']
    return render(request, 'learning/courses.html', {'courses': courses})
```

------____________________________________________________________________________________

### ⚙️ **Task 5 – Conditional Rendering**

**Concepts:** `{% if %}`, `{% else %}`

```python
def marks_view(request):
    marks = 55
    return render(request, 'learning/marks.html', {'marks': marks})
```

In template:

```html
{% if marks >= 40 %}
<p style="color:green;">Pass</p>
{% else %}
<p style="color:red;">Fail</p>
{% endif %}
```

------____________________________________________________________________________________

### ⚙️ **Task 6 – Template Inheritance**

**Concepts:** `base.html`, `{% block %}`, `{% extends %}`

* Create `base.html`:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Django Learning Portal</title>
  {% load static %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
  <header>
    <img src="{% static 'images/logo.png' %}" width="80">
    <nav>
      <a href="{% url 'home' %}">Home</a> |
      <a href="{% url 'about' %}">About</a> |
      <a href="{% url 'contact' %}">Contact</a>
    </nav>
  </header>

  <hr>
  {% block content %}{% endblock %}
  <hr>

  <footer><p>© 2025 Django Learning Portal</p></footer>
</body>
</html>
```

Each child page (e.g. `home.html`):

```html
{% extends 'learning/base.html' %}
{% block content %}
<h2>Welcome to Django Learning Portal!</h2>
{% endblock %}
```

------____________________________________________________________________________________

### ⚙️ **Task 7 – Static Files**

**Concepts:** CSS, images

* In `settings.py`:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'learning/static']
```

* Example `style.css`:

```css
body { font-family: Arial; background-color: #f9f9f9; }
nav a { margin: 5px; text-decoration: none; }
```

------____________________________________________________________________________________

### ⚙️ **Task 8 – Dynamic Pages & Loops**

```python
def product_list(request):
    products = [
        {'id': 1, 'name': 'Laptop', 'price': 55000},
        {'id': 2, 'name': 'Mouse', 'price': 800},
        {'id': 3, 'name': 'Keyboard', 'price': 1500},
    ]
    return render(request, 'learning/products.html', {'products': products})

def product_detail(request, id):
    products = [
        {'id': 1, 'name': 'Laptop', 'price': 55000},
        {'id': 2, 'name': 'Mouse', 'price': 800},
        {'id': 3, 'name': 'Keyboard', 'price': 1500},
    ]
    product = next((p for p in products if p['id'] == id), None)
    return render(request, 'learning/product_detail.html', {'product': product})
```



# ___________________________________________________________________________________

## 1️⃣ `views.py` (DRY, no repeated lists)

```python
from django.shortcuts import render
from django.http import Http404

# Central products list
products = [
    {'id': 1, 'name': 'Laptop', 'price': 55000},
    {'id': 2, 'name': 'Mouse', 'price': 800},
    {'id': 3, 'name': 'Keyboard', 'price': 1500},
]

# Product List View
def product_list(request):
    # Send all products to template
    return render(request, 'learning/products.html', {'products': products})

# Product Detail View
def product_detail(request, id):
    # Find the product by id
    product = next((p for p in products if p['id'] == id), None)
    
    # If product not found, return 404
    if not product:
        raise Http404("Product does not exist")
    
    return render(request, 'learning/product_detail.html', {'product': product})
```

**Tanglish ELI5:**

* `products` → oru central basket, ellam views use pannalam.
* `product_list` → ellā products pathuthu template la display pannum.
* `product_detail` → user click panna ID receive pannitu, single product fetch pannum.

---

## 2️⃣ `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
]
```

**Tanglish ELI5:**

* `/products/` → list page
* `/products/<id>/` → detail page, id pass aagum

---

## 3️⃣ `products.html` (List Page)

```html
<h1>Products</h1>
<ul>
  {% for product in products %}
    <li>
      {{ product.name }} - ₹{{ product.price }}
      <!-- Link to detail page, pass id -->
      <a href="{% url 'product_detail' product.id %}">View Details</a>
    </li>
  {% endfor %}
</ul>
```

**Tanglish ELI5:**

* Loop panna ellā products display aagum
* Click panna `{% url 'product_detail' product.id %}` → detail page la ponum

---

## 4️⃣ `product_detail.html` (Detail Page)

```html
<h1>{{ product.name }}</h1>
<p>Price: ₹{{ product.price }}</p>
<p>ID: {{ product.id }}</p>

<a href="{% url 'product_list' %}">Back to Products</a>
```

**Tanglish ELI5:**

* `{{ product.name }}` → product name display
* `{{ product.price }}` → product price display
* `{{ product.id }}` → internal id display (optional)
* Back link → list page ku ponum

---

### ✅ Flow Summary

1. User visits `/products/` → sees all products.
2. Click **View Details** → goes to `/products/<id>/`.
3. `product_detail` view fetches the product using the ID.
4. Template shows product details and a **Back link**.




------____________________________________________________________________________________

### ⚙️ **Task 9 – Mini Project 1: Student Report Card**

```python
def report_card(request):
    students = [
        {'name': 'Ravi', 'roll': 101, 'marks': 88},
        {'name': 'Kumar', 'roll': 102, 'marks': 39},
        {'name': 'Priya', 'roll': 103, 'marks': 95},
    ]
    topper = max(students, key=lambda s: s['marks'])
    return render(request, 'learning/report.html', {'students': students, 'topper': topper})
```

Template uses:

```html
{% for s in students %}
<tr {% if s.name == topper.name %}style="background-color:gold;"{% endif %}>
  <td>{{ s.name }}</td><td>{{ s.roll }}</td><td>{{ s.marks }}</td>
  <td>{% if s.marks >= 40 %}Pass{% else %}Fail{% endif %}</td>
</tr>
{% endfor %}
```

------____________________________________________________________________________________

### ⚙️ **Task 10 – Mini Project 2: Personal Portfolio**

Each page (Home, About, Skills, Projects, Contact) extends `base.html`.
No backend logic needed; use templates only.

---

### ✅ **Outcome**

By the end, students will:

* Create reusable templates and navigation.
* Use URL parameters and dynamic rendering.
* Pass and loop through data in templates.
* Apply conditionals and inheritance.
* Manage static files (CSS, images).
* Build multi-page and mini-projects — all in one Django app.


---____________________________________________________________________________________