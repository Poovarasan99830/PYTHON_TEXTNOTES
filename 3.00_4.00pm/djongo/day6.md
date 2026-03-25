

# ------------------------------------------------------
# TOPICS: ✅ Django Admin  ✅ Relational Models   ✅ Optimization
# ------------------------------------------------------

# ------------------------------------------------------
# ✅TOPIC: 1️⃣ Django Admin 
# ------------------------------------------------------



## 🔹 What is Django Admin?

Django Admin is a built-in interface that allows administrators to manage database data easily without writing frontend code.

It provides:

* Add
* Update
* Delete
* View records

---

## 🔹 Enabling Admin

1. Add app in `INSTALLED_APPS`
2. Create superuser:

   ```id="a1"
   python manage.py createsuperuser
   ```
3. Register model in `admin.py`

---

## 🔹 Model Registration

```python
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

Purpose:

* Makes model visible in admin panel.

---

## 🔹 Custom Admin Class

```python
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'course']
    search_fields = ['name']
    list_filter = ['course']

admin.site.register(Student, StudentAdmin)
```

---

## 🔹 Important Admin Options

| Option            | Purpose                    |
| ----------------- | -------------------------- |
| `list_display`    | Columns shown in list page |
| `search_fields`   | Search bar fields          |
| `list_filter`     | Right-side filters         |
| `ordering`        | Default sorting            |
| `readonly_fields` | Prevent editing            |
| `fieldsets`       | Group fields visually      |

---

## 🔹 Admin Benefits

* Quick data management
* No frontend needed
* Auto CRUD
* Secure (staff-only access)




# ------------------------------------------------------
# ✅ TOPIC: 2️⃣ Relational Models
# ------------------------------------------------------

## 🔹 What are Relational Models?

Relational models define relationships between database tables.

Django ORM supports:

1. One-to-One
2. One-to-Many
3. Many-to-Many

---
# ------------------------------------------------------
# 🔹 1️⃣ One-to-One Relationship
# ------------------------------------------------------

```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
```

### 📌 Concept:

* One record linked to exactly one record.
* Example: One user → One profile.


# ------------------------------------------------------
# 🔹 2️⃣ One-to-Many (ForeignKey)
# ------------------------------------------------------

```python
class Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
```

### 📌 Concept:

* One course → Many students.
* ForeignKey creates relationship.



# ------------------------------------------------------
# 🔹 3️⃣ Many-to-Many
# ------------------------------------------------------

```python
class Student(models.Model):
    courses = models.ManyToManyField(Course)
```

### 📌 Concept:

* Many students → Many courses.
* Django creates intermediate table automatically.

---

## 🔹 on_delete Options

| Option      | Meaning                |
| ----------- | ---------------------- |
| CASCADE     | Delete related records |
| PROTECT     | Prevent deletion       |
| SET_NULL    | Set field to NULL      |
| SET_DEFAULT | Set default value      |

---

## 🔹 Related Name

```python
course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students")
```

Allows:

```python
course.students.all()
```

# ------------------------------------------------------
# ✅ TOPIC: 3️⃣ Django Optimization

# ------------------------------------------------------

## 🔹 What is Optimization?

Optimization improves performance and reduces database queries.

Main goal:

> Reduce query count + Improve speed

---

# 🔹 1️⃣ select_related()

Used for:

* ForeignKey
* OneToOne

```python
Student.objects.select_related("course")
```

### 📌 Purpose:

* Performs SQL JOIN
* Reduces extra queries


# ------------------------------------------------------
# 🔹 2️⃣ prefetch_related()
# ------------------------------------------------------

Used for:

* ManyToMany
* Reverse ForeignKey

```python
Course.objects.prefetch_related("student_set")
```

### 📌 Purpose:

* Fetch related objects efficiently
* Prevents N+1 query problem


# ------------------------------------------------------
# 🔹 3️⃣ N+1 Query Problem
# ------------------------------------------------------

Bad:

```python
for student in students:
    print(student.course.name)
```

Causes:
1 query for students

* N queries for courses

Solution:

```python
students = Student.objects.select_related("course")
```

# ------------------------------------------------------
# 🔹 4️⃣ Indexing
# ------------------------------------------------------

```python
name = models.CharField(max_length=100, db_index=True)
```

Purpose:

* Faster searching
* Faster filtering

# ------------------------------------------------------
# 🔹 5️⃣ Query Optimization
# ------------------------------------------------------

Use:

* `.only()`
* `.values()`
* `.values_list()`
* `.exists()`
* `.count()`

Example:

```python
Student.objects.filter(course="Python").only("name")
```

# ------------------------------------------------------
# 🔹 6️⃣ Caching
# ------------------------------------------------------

Used to:

* Store frequently accessed data
* Reduce DB hits


# ------------------------------------------------------
# 🔹 7️⃣ Pagination
# ------------------------------------------------------

Limits records returned per request.

Improves:

* Performance
* Memory usage



# ------------------------------------------------------
# 🔹 Quick Comparison
# ------------------------------------------------------

| Feature          | Purpose              |
| ---------------- | -------------------- |
| select_related   | Optimize FK queries  |
| prefetch_related | Optimize M2M queries |
| Index            | Faster lookup        |
| Pagination       | Limit large data     |
| Caching          | Reduce DB load       |

# ------------------------------------------------------
# 🔹 5-Line Viva Summary
# ------------------------------------------------------

Django Admin provides an automatic interface for managing database records securely.
Relational models define relationships like One-to-One, ForeignKey, and Many-to-Many.
Optimization improves performance by reducing database queries.
select_related and prefetch_related prevent N+1 query issues.
Indexing and pagination further enhance application performance.

# ------------------------------------------------------