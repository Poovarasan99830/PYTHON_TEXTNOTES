
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
