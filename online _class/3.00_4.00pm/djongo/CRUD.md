
---

## 📁 Project Folder Structure

```
product_project/
│
├── manage.py
├── product_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
└── products/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── products/
            ├── base.html
            ├── product_list.html
            ├── product_form.html
            └── product_confirm_delete.html
```

---

## 🧩 `models.py`

```python
from django.db import models
from django.utils.text import slugify
import itertools

class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    sku = models.CharField(max_length=50, unique=True, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Auto-generate unique slug from name"""
        if not self.slug:
            base = slugify(self.name)[:150] or "product"
            slug_candidate = base
            for i in itertools.count(1):
                if not Product.objects.filter(slug=slug_candidate).exists():
                    break
                slug_candidate = f"{base}-{i}"
            self.slug = slug_candidate
        super().save(*args, **kwargs)
```

---

## 🧾 `forms.py`

```python
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'price', 'description', 'image', 'stock', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional SKU'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
```

---

## ⚙️ `views.py`

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import ProductForm

# 🟢 List all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# 🟢 Create a new product
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Product added successfully!")
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Add Product'})

# 🟡 Edit product
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Product updated successfully!")
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Edit Product'})

# 🔴 Delete product
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "🗑️ Product deleted successfully!")
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})
```

---

## 🌐 `urls.py` (inside `products` app)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.product_create, name='product_create'),
    path('edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
]
```

---

## 🧱 Project-level `urls.py` (in `product_project/urls.py`)

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## ⚙️ Add to `settings.py`

```python
INSTALLED_APPS = [
    # default apps...
    'django.contrib.staticfiles',
    'products',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## 🎨 Templates

### 📄 `base.html`

```html
<!DOCTYPE html>
<html>
<head>
  <title>Django Product App</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <nav class="navbar navbar-dark bg-dark">
    <div class="container">
      <a href="{% url 'product_list' %}" class="navbar-brand">🛒 Product Dashboard</a>
    </div>
  </nav>
  <div class="container mt-3">
    {% block content %}{% endblock %}
  </div>
</body>
</html>
```

---

### 📄 `product_list.html`

```html
{% extends "products/base.html" %}
{% block content %}
<div class="container mt-4">
  <h2>🛍️ Product List</h2>
  <a href="{% url 'product_create' %}" class="btn btn-primary mb-3">➕ Add Product</a>

  {% for message in messages %}
    <div class="alert alert-success">{{ message }}</div>
  {% endfor %}

  <table class="table table-bordered table-striped">
    <thead class="table-dark">
      <tr>
        <th>Image</th>
        <th>Name</th>
        <th>Price</th>
        <th>Stock</th>
        <th>Active</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      {% for p in products %}
      <tr>
        <td>
          {% if p.image %}
            <img src="{{ p.image.url }}" width="60" height="60" style="object-fit: cover;">
          {% else %}
            —
          {% endif %}
        </td>
        <td>{{ p.name }}</td>
        <td>₹{{ p.price }}</td>
        <td>{{ p.stock }}</td>
        <td>{{ p.is_active|yesno:"✅,❌" }}</td>
        <td>
          <a href="{% url 'product_edit' p.pk %}" class="btn btn-sm btn-warning">Edit</a>
          <a href="{% url 'product_delete' p.pk %}" class="btn btn-sm btn-danger">Delete</a>
        </td>
      </tr>
      {% empty %}
      <tr><td colspan="6">No products found.</td></tr>
      {% endfor %}
    </tbody>
  </table>
</div>
{% endblock %}
```

---

### 📄 `product_form.html`

```html
{% extends "products/base.html" %}
{% block content %}
<div class="container mt-4">
  <h2>{{ title }}</h2>
  <form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-success">💾 Save</button>
    <a href="{% url 'product_list' %}" class="btn btn-secondary">🔙 Back</a>
  </form>
</div>
{% endblock %}
```

---

### 📄 `product_confirm_delete.html`

```html
{% extends "products/base.html" %}
{% block content %}
<div class="container mt-5 text-center">
  <h3>⚠️ Are you sure you want to delete <b>{{ product.name }}</b>?</h3>
  <form method="POST">
    {% csrf_token %}
    <button type="submit" class="btn btn-danger">Yes, Delete</button>
    <a href="{% url 'product_list' %}" class="btn btn-secondary">Cancel</a>
  </form>
</div>
{% endblock %}
```

---

## ✅ Final Setup Commands

```bash
# Create DB
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver
```

Now visit:
👉 [http://127.0.0.1:8000/products/](http://127.0.0.1:8000/products/)

---

Would you like me to add **search + price/stock filter + pagination** next?
That will make this app look like a real mini e-commerce admin dashboard 🚀
