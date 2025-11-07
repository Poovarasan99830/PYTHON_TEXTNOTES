

## **1️⃣ You write a Django model**

Example:


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    


This is **Python code**, not SQL yet. Django doesn’t touch the database yet.

---

## **2️⃣ Django creates migrations**

When you run:

```bash
python manage.py makemigrations
```

Django generates a **migration file** (Python) that says: “Hey, create a table called `Product` with these columns and types.”

It looks like:

```python
migrations.CreateModel(
    name='Product',
    fields=[
        ('id', models.AutoField(primary_key=True)),
        ('name', models.CharField(max_length=100)),
        ('price', models.DecimalField(max_digits=10, decimal_places=2)),
        ('description', models.TextField()),
    ],
)
```

This is still **Python instructions**, not actual SQL.

---

## **3️⃣ Django runs migrations → SQL**
```bash
python manage.py migrate
```
When you run:



Django **translates your migration Python code into SQL commands** and sends them to your database.

Example SQL that gets executed:

```sql
CREATE TABLE "shop_product" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(100) NOT NULL,
    "price" decimal(10, 2) NOT NULL,
    "description" text NOT NULL
);
```

✅ Now your table exists in the database.

---

## **4️⃣ Django ORM queries → SQL**

When you write:

```python
Product.objects.filter(price__gte=1000)
```

Django **translates it to SQL** like:

```sql
SELECT * FROM "shop_product" WHERE price >= 1000;
```

The database executes the SQL, and Django gives you back Python objects.

---

### **Summary**

1. You write models in Python.
2. Django creates migrations (Python instructions).
3. Migrations are converted to SQL and applied to the database.
4. Queries you write in Django ORM are also converted to SQL automatically.

Basically, **Django ORM is a translator** between your Python code and SQL database.


________________________________________________________________________________
_________________⚙️ 2️⃣ Models.py________________________________________________
_________________________________________________________________________________



from django.db import models


# 1️⃣ STUDENT REGISTRATION MODEL
class StudentRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 2️⃣ JOB APPLICATION MODEL
class JobApplication(models.Model):
    POSITION_CHOICES = [
        ("DEV", "Developer"),
        ("TST", "Tester"),
        ("DSN", "Designer"),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Email must be unique
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    resume = models.FileField(upload_to="resumes/")  # Stored inside MEDIA folder

    def __str__(self):
        return f"{self.full_name} - {self.get_position_display()}"


# 3️⃣ APPOINTMENT MODEL
class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    # Prevent booking same doctor at same date/time
    class Meta:
        unique_together = ("doctor_name", "date", "time")

    def __str__(self):
        return f"{self.patient_name} with Dr. {self.doctor_name} on {self.date} at {self.time}"






________________________________________________________________________________
_________________⚙️ 2️⃣ forms.py_________________________________________________
_________________________________________________________________________________





from django import forms
from .models import StudentRegistration, JobApplication, Appointment


# ---------- Student Registration Form ----------
class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ['name', 'email', 'age', 'course']


# ---------- Job Application Form ----------
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['full_name', 'email', 'position', 'resume']


# ---------- Appointment Form ----------
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'doctor_name', 'date', 'time']



__________________________________________________________________________________
_________________⚙️ 2️⃣ views.py_________________________________________________
_____________________________________________________________________________


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentRegistrationForm, JobApplicationForm, AppointmentForm


# ---------- Student Registration View ----------
def student_register(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Student registered successfully!")
            return redirect('student_register')  # reload same page after success
    else:
        form = StudentRegistrationForm()
    return render(request, "student_register.html", {"form": form})


# ---------- Job Application View ----------
def job_apply(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Job application submitted successfully!")
            return redirect('job_apply')
    else:
        form = JobApplicationForm()
    return render(request, "job_apply.html", {"form": form})


# ---------- Appointment View ----------
def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Appointment booked successfully!")
            return redirect('book_appointment')
    else:
        form = AppointmentForm()
    return render(request, "book_appointment.html", {"form": form})




________________________________________________________________________________
_________________⚙️ 2️⃣ views.py_________________________________________________
_________________________________________________________________________________
<!DOCTYPE html>
<html>
<head>
    <title>Student Registration</title>
</head>
<body>
    <h2>🧑‍🎓 Student Registration Form</h2>

    {% if messages %}
        {% for message in messages %}
            <p style="color:green;">{{ message }}</p>
        {% endfor %}
    {% endif %}

    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
</body>
</html>





________________________________________________________________________________
_________________⚙️ 2️⃣ views.py_________________________________________________
_________________________________________________________________________________


<!DOCTYPE html>
<html>
<head>
    <title>Job Application</title>
</head>
<body>
    <h2>💼 Job Application Form</h2>

    {% if messages %}
        {% for message in messages %}
            <p style="color:green;">{{ message }}</p>
        {% endfor %}
    {% endif %}

    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>


________________________________________________________________________________
_________________⚙️ 2️⃣ views.py_________________________________________________
_________________________________________________________________________________


<!DOCTYPE html>
<html>
<head>
    <title>Appointment Booking</title>
</head>
<body>
    <h2>🩺 Book Appointment</h2>

    {% if messages %}
        {% for message in messages %}
            <p style="color:green;">{{ message }}</p>
        {% endfor %}
    {% endif %}

    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Book</button>
    </form>
</body>
</html>




________________________________________________________________________________
_________________⚙️ 2️⃣ views.py_________________________________________________
_________________________________________________________________________________

from django.urls import path
from . import views

urlpatterns = [
    path('student/register/', views.student_register, name='student_register'),
    path('job/apply/', views.job_apply, name='job_apply'),
    path('appointment/book/', views.book_appointment, name='book_appointment'),
]



________________________________________________________________________________
_________________⚙️ 2️⃣ views.py_________________________________________________
_________________________________________________________________________________


python manage.py makemigrations
python manage.py migrate



________________________________________________________________________________
_________________⚙️ 2️⃣ views.py_________________________________________________
_________________________________________________________________________________

python manage.py runserver


http://127.0.0.1:8000/student/register/
http://127.0.0.1:8000/job/apply/
http://127.0.0.1:8000/appointment/book/


________________________________________________________________________________
_________________⚙️ 2️⃣ views.py_________________________________________________
_________________________________________________________________________________

# students = StudentRegistration.objects.all()

<!-- {% for student in students %}
        <p>{{ student.name }} - {{ student.age }}</p>
    {% endfor %} -->



# students=StudentRegistration.objects.get(id=1)

<!-- {{ students.name }} - {{ students.age }} -->





# filter()
# students = StudentRegistration.objects.filter(name="Varun")
<!-- 
for s in students:
    print(s.name) -->






# ------------------------------------------------------
# 🔹 FILTER (price >= 500)
# ------------------------------------------------------
products = Product.objects.filter(price__gte=500)
for p in products:
    print(p.name, p.price)


# ------------------------------------------------------
# 🔹 EXCLUDE (name != 'monitor')
# ------------------------------------------------------
products = Product.objects.exclude(name="monitor")
for p in products:
    print(p.name)


# ------------------------------------------------------
# 🔹 GET (Fetch one object by ID)
# ------------------------------------------------------
p = Product.objects.get(id=4)
print(p.name)


# ------------------------------------------------------
# 🔹 UPDATE (Single object)
# ------------------------------------------------------
p = Product.objects.get(id=4)
p.name = "ZOO"
p.save()
print("Updated:", p.name)


# ------------------------------------------------------
# 🔹 UPDATE (Bulk update)
# ------------------------------------------------------
Product.objects.filter(name="tv").update(name="Television movie")
print("Updated all TVs to Television movie")


# ------------------------------------------------------
# 🔹 DELETE (Single object)
# ------------------------------------------------------
p = Product.objects.get(id=7)
p.delete()
print("Deleted one product with ID 7")


# ------------------------------------------------------
# 🔹 DELETE (Bulk delete)
# ------------------------------------------------------
Product.objects.filter(name="mobilephone").delete()
print("Deleted all products named mobilephone")


# ------------------------------------------------------
# 🔹 ORDER BY (Ascending)
# ------------------------------------------------------
products = Product.objects.all().order_by('name')
for p in products:
    print(p.name)


# ------------------------------------------------------
# 🔹 ORDER BY (Case-insensitive)
# ------------------------------------------------------
from django.db.models.functions import Lower
products = Product.objects.all().order_by(Lower('name'))
for p in products:
    print(p.name)


# ------------------------------------------------------
# 🔹 CASE-INSENSITIVE FILTER
# ------------------------------------------------------
products = Product.objects.filter(name__iexact="laptops")
for p in products:
    print(p.name)


# ------------------------------------------------------
# 🔹 LIMIT (First 3)
# ------------------------------------------------------
products = Product.objects.all()[:3]
for p in products:
    print(p.name)


# ------------------------------------------------------
# 🔹 COUNT
# ------------------------------------------------------
count = Product.objects.count()
print("Total products:", count)


# ------------------------------------------------------
# 🔹 EXISTS
# ------------------------------------------------------
exists = Product.objects.filter(name="laptop").exists()
print("Laptop exists?", exists)


# ------------------------------------------------------
# 🔹 AGGREGATE — AVG, SUM
# ------------------------------------------------------
from django.db.models import Avg, Sum

avg_price = Product.objects.aggregate(Avg('price'))
print("Average Price:", avg_price)

sum_price = Product.objects.aggregate(Sum('price'))
print("Total Price:", sum_price)


# ------------------------------------------------------
# 🔹 DISTINCT (Unique Prices)
# ------------------------------------------------------
unique_prices = Product.objects.values('price').distinct()
for u in unique_prices:
    print(u['price'])


# ------------------------------------------------------
# 🔹 VALUES (Select specific columns)
# ------------------------------------------------------
products = Product.objects.values('name', 'price')
for p in products:
    print(p['name'], p['price'])


# ------------------------------------------------------
# 🔹 ONLY (Fetch only one field)
# ------------------------------------------------------
products = Product.objects.only('name')
for p in products:
    print(p.name)







# ------------------------------------------------------

# 🔹 1. VALUES (Select specific columns)

# ------------------------------------------------------

```python
products = Product.objects.values('name', 'price')
for p in products:
    print(p['name'], p['price'])
```

**Notes:**

* `values()` fetches **only specified columns** from the database.
* Returns a **list of dictionaries**.
* Useful for **optimized queries** when you don’t need full model objects.

---

# ------------------------------------------------------

# 🔹 2. ONLY (Fetch only one field)

# ------------------------------------------------------

```python
products = Product.objects.only('name')
for p in products:
    print(p.name)
```

**Notes:**

* `only()` fetches the **full objects**, but **only loads specified fields initially**.
* Other fields are loaded **lazily** if accessed.

---

# ------------------------------------------------------

# 🔹 3. Q Objects (AND / OR queries)

# ------------------------------------------------------

```python
from django.db.models import Q

# OR condition
students = Student.objects.filter(Q(name="Arun") | Q(name="Kumar"))

# AND condition
students = Student.objects.filter(Q(name="Arun") & Q(age__gte=18))

for s in students:
    print(s.name, s.age)
```

**Notes:**

* `Q` objects allow **complex queries** using **AND (&) / OR (|)**.
* OR: fetches students with name "Arun" **or** "Kumar".
* AND: fetches students with name "Arun" **and** age ≥ 18.

---

# ------------------------------------------------------

# 🔹 4. F Objects (Compare fields)

# ------------------------------------------------------

```python
from django.db.models import F

# Fetch students where marks > age
students = Student.objects.filter(marks__gt=F('age'))

for s in students:
    print(s.name, s.marks, s.age)
```

**Notes:**

* `F` objects allow **comparing one field with another field** in the same model.
* Example: marks > age, price < discount, etc.

---

# ------------------------------------------------------

# 🔹 5. Raw SQL (If needed)

# ------------------------------------------------------

```python
# Using raw SQL query
students = Student.objects.raw("SELECT * FROM app_student WHERE age > 18")

for s in students:
    print(s.name, s.age)
```

**Notes:**

* `raw()` allows running **custom SQL queries** directly.
* Use only if Django ORM **cannot perform the query efficiently**.
* Returns **model objects**, so you can iterate like normal QuerySets.

---
