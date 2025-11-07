Perfect 👍 — since you already have a **`Register`** model linked **OneToOne** with Django’s built-in `User` model, let’s build a **complete Registration + Login system** (step-by-step) using **Django Auth** and your **Register (Profile)** model.

---

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

---

Would you like me to make this version **with class-based views (CBV)** instead of function-based (FBV)?
