
# ____________________________________________________________________________________________________

## 🧱 Project Setup Overview

### ✅ Models

* `User` → from `django.contrib.auth.models`
* `Register` → custom profile model (you already have it)

### ✅ Views

* Register (sign-up)
* Login
* Logout
* Profile (optional)

### ✅ Templates

* `register.html`
* `login.html`
* `profile.html`

---

## ⚙️ 1️⃣ models.py

You already have this (just keep as-is):

```python
from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
```

---

## ⚙️ 2️⃣ forms.py

We’ll create **two forms**:

1. `UserRegisterForm` → for username, email, password
2. `RegisterForm` → for profile (bio, avatar)

```python
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Register

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['bio', 'avatar']
```

---

## ⚙️ 3️⃣ views.py

Handles registration, login, logout, and profile.

```python
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, RegisterForm
from .models import Register

# ------------------------------
# 🔹 Register View
# ------------------------------
def register_view(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = RegisterForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = RegisterForm()

    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


# ------------------------------
# 🔹 Login View
# ------------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


# ------------------------------
# 🔹 Logout View
# ------------------------------
def logout_view(request):
    logout(request)
    return redirect('login')


# ------------------------------
# 🔹 Profile View
# ------------------------------
@login_required
def profile_view(request):
    profile, created = Register.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'profile': profile})
```

---

## ⚙️ 4️⃣ urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
```

---

## 🧩 5️⃣ Templates (basic examples)

### 📄 register.html

```html
<h2>Register</h2>
<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ user_form.as_p }}
    {{ profile_form.as_p }}
    <button type="submit">Register</button>
</form>

<p>Already have an account? <a href="{% url 'login' %}">Login</a></p>
```

---

### 📄 login.html

```html
<h2>Login</h2>
<form method="POST">
    {% csrf_token %}
    <p>Username: <input type="text" name="username"></p>
    <p>Password: <input type="password" name="password"></p>
    <button type="submit">Login</button>
</form>

<p>Don’t have an account? <a href="{% url 'register' %}">Register</a></p>
```

---

### 📄 profile.html

```html
<h2>Welcome, {{ user.username }}</h2>
{% if profile.avatar %}
    <img src="{{ profile.avatar.url }}" width="100">
{% endif %}
<p>{{ profile.bio }}</p>

<a href="{% url 'logout' %}">Logout</a>
```

---

## ⚙️ 6️⃣ settings.py (important)

```python
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'login'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

and in your **main urls.py**:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('yourapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## ✅ Done!

You now have:

* **Registration page** with user + profile data
* **Login & Logout** using Django auth
* **Profile view** showing `bio` and `avatar`







# ______________________________________________________________________________________

## 🔹 Code:

```python
profile = profile_form.save(commit=False)
profile.user = user
profile.save()
```






<!-- `profile_form.save(commit=False)`


profile = Register(bio="hello", avatar="img.jpg")


`Register` model-la `user = OneToOneField(User)


profile.save() -->





| Line                  | Purpose                       |
| --------------------- | ----------------------------- |
| `commit=False`        | prepare object but don’t save |
| `profile.user = user` | connect user object           |
| `profile.save()`      | finally save to DB            







---

## 🧠 Step-by-Step Meaning

### 🧩 1️⃣ `profile_form.save(commit=False)`

➡️ Normally `form.save()` nu panna, Django **direct-a database-la** save pannum.
But `commit=False` nu kudutha, adhu **temporary object** create pannum —
**save pannaama**, just Python memory-la object ready aagum.

📘 Example:

```python
profile = Register(bio="hello", avatar="img.jpg")
```

Ippo idhu **DB-la illa**, just ready irukura Python object.
So namma idhula innum extra data set panna mudiyum (like user field).

---

### 🧩 2️⃣ `profile.user = user`

`Register` model-la `user = OneToOneField(User)` irukku.
Adhu required field — so `user` assign pannama save panna, error varum.

Ippo `user_form.save()` kudukura line-la oru `user` object already create aagiduchu.
So we assign that new `user` to our profile manually 👇

```python
profile.user = user
```

💬 Meaning:
"Indha profile vandhu indha user-oda profile da."

---

### 🧩 3️⃣ `profile.save()`

Ippo object fully ready — all fields fill panniduchu (`bio`, `avatar`, and now `user`).
So `save()` kudukumbodhu Django finally DB-la insert pannum ✅

---

## 🔍 Full Flow Example

1️⃣ User submits register form:

```
username = poova
email = poova@gmail.com
password = ****
bio = “I love Django”
avatar = “photo.jpg”
```

2️⃣ `user_form.save()` → creates:

```
User(id=1, username='poova', email='poova@gmail.com')
```

3️⃣ `profile_form.save(commit=False)` → prepares:

```
Register(bio='I love Django', avatar='photo.jpg')
```

(but not saved yet)

4️⃣ `profile.user = user` → attach the link:

```
Register(user=User(id=1), bio='I love Django', avatar='photo.jpg')
```

5️⃣ `profile.save()` → now DB-la save aagum.

✅ Final DB:

```
User → id=1, username='poova'
Register → id=1, user_id=1, bio='I love Django', avatar='photo.jpg'
```

---

## 🧩 Why We Need `commit=False`

If you don’t use `commit=False`,
and try directly `profile_form.save()`,
Django will throw error like:

> "IntegrityError: NOT NULL constraint failed: Register.user_id"

Because `user` field mandatory but not yet linked —
so save panna mudiyadhu until we attach the user manually.

---

💡 **Summary in One Line:**

| Line                  | Purpose                       |
| --------------------- | ----------------------------- |
| `commit=False`        | prepare object but don’t save |
| `profile.user = user` | connect user object           |
| `profile.save()`      | finally save to DB            |

# _________________________________________________________________________________



profile, created = Register.objects.get_or_create(user=request.user)



try:
    profile = Register.objects.get(user=request.user)
except Register.DoesNotExist:
    profile = Register.objects.create(user=request.user)

# __________________________________________________________________________________________


So the reason we use two variables is:

One (profile) to get the actual object.

One (created) to know whether it was newly created or already existed.



| Situation             | `profile`                | `created` |
| --------------------- | ------------------------ | --------- |
| First time user visit | New Register object      | `True`    |
| Already has profile   | Existing Register object | `False`   |


# _____________________________________________________________________________________________


| Setting               | Purpose                                              |
| --------------------- | ---------------------------------------------------- |
| `DEFAULT_AUTO_FIELD`  | Sets default ID type (`BigAutoField`) for all models |
| `LOGIN_URL`           | Redirects unauthenticated users to login page        |
| `LOGIN_REDIRECT_URL`  | Redirects after successful login                     |
| `LOGOUT_REDIRECT_URL` | Redirects after logout                               |
| `MEDIA_URL`           | URL path for serving uploaded files                  |
| `MEDIA_ROOT`          | Local folder to store uploaded files                 |





                🔐 DJANGO AUTH FLOW

        ┌───────────────────────────────┐
        │   User tries to open a page   │
        │   (e.g., /profile/)           │
        └──────────────┬────────────────┘
                       │
                       ▼
        ┌───────────────────────────────┐
        │  @login_required decorator    │
        │  checks authentication        │
        └──────────────┬────────────────┘
                       │
        ┌──────────────┴──────────────┐
        │  ✅ Logged In?               │
        └──────────────┬──────────────┘
         YES           │ NO
          │            ▼
          │   Redirect to LOGIN_URL
          │   (example: /login/)
          │
          ▼
 ┌───────────────────────────────┐
 │  User enters credentials      │
 │  (username & password)        │
 └──────────────┬────────────────┘
                │
                ▼
     ┌─────────────────────────────┐
     │  Authentication successful? │
     └──────────────┬──────────────┘
         YES        │        NO
          │         ▼
          │   Show login error
          │
          ▼
 ┌───────────────────────────────┐
 │ Redirect to LOGIN_REDIRECT_URL│fail...
 │  (example: /profile/)         │
 └──────────────┬────────────────┘
                │
                ▼
      ┌───────────────────────────────┐
      │  User views protected page    │
      │  (like profile, dashboard)    │
      └──────────────┬────────────────┘
                     │
                     ▼
     ┌───────────────────────────────┐
     │ User clicks "Logout"          │
     └──────────────┬────────────────┘
                    │
                    ▼
     ┌───────────────────────────────┐
     │ Redirect to LOGOUT_REDIRECT_URL│
     │  (example: /login/)           │
     └───────────────────────────────┘



| Setting               | Example URL | Purpose                                    |
| --------------------- | ----------- | ------------------------------------------ |
| `LOGIN_URL`           | `/login/`   | Page to show when user not logged in       |
| `LOGIN_REDIRECT_URL`  | `/profile/` | Where user goes **after successful login** |
| `LOGOUT_REDIRECT_URL` | `/login/`   | Where user goes **after logging out**      |




# ______________________________________________________________________________________


             🖼️ DJANGO MEDIA FILE FLOW

           (Example: Profile Picture Upload)


┌──────────────────────────────────────────────┐
│  User uploads file in a form (e.g., image)   │
│  <input type="file" name="profile_pic">      │
└───────────────────────────┬──────────────────┘
                            │
                            ▼
               Django saves the file to:

         MEDIA_ROOT = BASE_DIR / 'media'
         (Example: C:/project/media/)

                            │
                            ▼
 ┌────────────────────────────────────────────┐
 │   Actual File Path (in your system):       │
 │   C:/project/media/profile_pic.jpg         │
 └────────────────────────────────────────────┘
                            │
                            ▼
        Django assigns a URL to access it via:

           MEDIA_URL = '/media/'

                            │
                            ▼
 ┌────────────────────────────────────────────┐
 │  Public URL (used in templates):           │
 │  http://127.0.0.1:8000/media/profile_pic.jpg │
 └────────────────────────────────────────────┘
                            │
                            ▼
         Template displays it using:
         <img src="{{ user.profile_pic.url }}" />



| Setting           | Example Value                             | Purpose                                           |
| ----------------- | ----------------------------------------- | ------------------------------------------------- |
| `MEDIA_ROOT`      | `BASE_DIR / 'media'`                      | Folder where uploaded files are physically stored |
| `MEDIA_URL`       | `/media/`                                 | URL path used to access uploaded files in browser |
| Example File Path | `C:/project/media/profile.jpg`            | Real file location                                |
| Example File URL  | `http://127.0.0.1:8000/media/profile.jpg` | How you view it on the site                       |
























| Relationship | Meaning     |
| ------------ | ----------- |
| One-to-One   | 1 ↔ 1       |
| One-to-Many  | 1 ↔ many    |
| Many-to-Many | many ↔ many |




A One-to-One relationship is a relationship where each record in one table is associated with exactly one record in another table.


USER (1)  --------  (1) PROFILE




+------------+          1 : 1          +---------------+
|   USER     |------------------------|   REGISTER    |
+------------+                        +---------------+
| PK id      |                        | PK id         |
| username   |                        | FK user_id    |
| email      |                        | bio           |
| password   |                        | avatar        |
+------------+                        +---------------+




Key Explanation 

PK → Primary Key

FK → Foreign Key

Register.user_id → references User.id

user_id is UNIQUE → ensures One-to-One



The User entity is connected to the Register entity using a One-to-One relationship, where each user has exactly one profile and each profile belongs to exactly one user.




# 🔹 2. OneToOne (1:1)

  

from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
    


we did NOT write user_id in the model.
Then how are both tables connected?
Where is the foreign key?”



user = OneToOneField(User)

↓ Django creates ↓

user_id  → Foreign Key → User.id
(unique)




user = models.OneToOneField(User, on_delete=models.CASCADE)

user_id   INTEGER   UNIQUE   FOREIGN KEY → User(id) 







Django automatically creates a user_id column in the database when we use OneToOneField. This column acts as a foreign key referencing the User table and enforces a one-to-one relationship using a unique constraint.




TABLE 1: User (Already in Django)

| id | username | email                                   |
| -- | -------- | --------------------------------------- |
| 1  | arun     | [arun@gmail.com](mailto:arun@gmail.com) |
| 2  | bala     | [bala@gmail.com](mailto:bala@gmail.com) |




TABLE 2: Register (Profile Table)

| id | user_id | bio            | avatar   |
| -- | ------- | -------------- | -------- |
| 1  | 1       | I love coding  | arun.jpg |
| 2  | 5      | Django student | bala.png |





Visual Diagram

User Table                 Register Table
-----------               ----------------
id  username               id  user_id  bio
1   arun      --------->   1   1        I love coding
2   bala      --------->   2   2        Django student





The Register table has a foreign key (user_id) that uniquely connects to the User table, ensuring one profile per user.

In OneToOneField, Django creates a foreign key with a UNIQUE constraint, ensuring one record per related object.














---

## 1️⃣ What is One-to-Many (1:M)?

**Definition (simple):**

> **One Author can write MANY Books**
> **But each Book belongs to ONLY ONE Author**

📌 Real-world meaning:

* One author → multiple books ✅
* One book → multiple authors ❌ (not here)





author = models.ForeignKey(Author, on_delete=models.CASCADE)

* `Book` table **depends on** `Author` table
* Each book stores **author_id**
* One author_id can appear **many times** in Book table








### 🗄️ Author Table

| id | name | bio      |
| -- | ---- | -------- |
| 1  | Ram  | Writer   |
| 2  | Ravi | Novelist |

---

### 🗄️ Book Table

| id | title  | publication_date | author_id |
| -- | ------ | ---------------- | --------- |
| 1  | Book A | 2022-01-01       | 1         |
| 2  | Book B | 2023-05-10       | 1         |
| 3  | Book C | 2021-03-15       | 2         |


### Key Insight

* Author **1** → Book A, Book B
* Author **2** → Book C






## 4️⃣ What Django Automatically Does

When you write:

```python
author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

Django does **ALL** this automatically:

✅ Creates `author_id` column
✅ Adds **foreign key constraint**
✅ Links Book → Author
✅ Enables reverse access (`author.book_set`)
✅ Handles delete behavior










### Other options (FYI):

* `SET_NULL`
* `PROTECT`
* `RESTRICT`
* `DO_NOTHING`

But `CASCADE` is **most common for 1:M**.

---

## 6️⃣ How Data Is Inserted (Step by Step)

### Step 1: Create Author

```python
author = Author.objects.create(
    name="Chetan Bhagat",
    bio="Indian author"
)
```

### Step 2: Create Books for that Author

```python
Book.objects.create(
    title="2 States",
    publication_date="2009-10-08",
    author=author
)

Book.objects.create(
    title="Half Girlfriend",
    publication_date="2014-10-01",
    author=author
)
```

👉 Django internally stores:

```
author_id = author.id
```

---

## 7️⃣ How to FETCH Data (Very Important Concept)

---

### 🔹 Book → Author (Forward Relation)

```python
book = Book.objects.get(title="2 States")
print(book.author.name)
```

🧠 Django does:

```sql
SELECT * FROM author WHERE id = book.author_id;
```

---

### 🔹 Author → Books (Reverse Relation)

This is **magic created by Django** 🔮

```python
author = Author.objects.get(name="Chetan Bhagat")
books = author.book_set.all()
```

👉 Output:

* 2 States
* Half Girlfriend

### Why `book_set`?

* Django automatically names it:

```
<modelname>_set
```

You can customize it 👇

```python
author = models.ForeignKey(
    Author,
    on_delete=models.CASCADE,
    related_name="books"
)
```

Now:

```python
author.books.all()
```

---

## 8️⃣ Django ORM Query Examples

### All books of one author

```python
Book.objects.filter(author__name="Chetan Bhagat")
```

### Count books of author

```python
author.books.count()
```

### Get author from book

```python
book.author
```

---

## 9️⃣ Django Admin (Behind the Scenes)

When registered in admin:

* Author page shows authors
* Book form shows **dropdown of Authors**
* Dropdown comes from ForeignKey relation

📌 Admin UI knows relationship automatically.

---





## 🔟 Why UNIQUE is NOT on ForeignKey

```python
author = models.ForeignKey(...)
```

If you add `unique=True`:

* One author can have only ONE book
* That becomes **One-to-One**

So:

* `unique=True` → OneToOne
* No unique → OneToMany














🔹 courses = models.ManyToManyField(Course)
Django does ALL this automatically:

✅ Creates a third table (junction / intermediate table)
✅ Stores student_id and course_id
✅ Adds foreign key constraints to both tables
✅ Links Student ↔ Course
✅ Enables reverse access (course.student_set)
✅ Prevents duplicate connections
✅ Handles add / remove relations without deleting data

| id | name |    
| -- | ---- |
| 1  | Arun |
| 2  | Bala |


| id | name   |
| -- | ------ |
| 1  | Python |
| 2  | Django |


| id | student_id | course_id |
| -- | ---------- | --------- |
| 1  | 1          | 1         |
| 2  | 1          | 2         |
| 3  | 2          | 1         |





One student → many courses

One course → many students


student = Student.objects.create(name="Arun")
course1 = Course.objects.create(name="Python")
course2 = Course.objects.create(name="Django")

student.courses.add(course1, course2)



🔹 Full Concept Summary

✔ Many-to-Many = ManyToManyField
✔ Uses a third (intermediate) table
✔ Both tables connect via IDs
✔ No direct ForeignKey in main tables
✔ Django auto-creates relation table
✔ Reverse relation created automatically
✔ related_name improves readability
✔ ORM hides SQL but SQL still runs


Simple Sentence (Very Important ⭐)

ManyToMany means:

“One Student can learn MANY Courses,
and ONE Course can have MANY Students.”



| Relationship | Key                         |
| ------------ | --------------------------- |
| One-to-Many  | ForeignKey                  |
| Many-to-Many | ManyToManyField + 3rd Table |
