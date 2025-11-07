
---

## **1️⃣ Project Structure**

```
django_orm_dashboard/
├── manage.py
├── django_orm_dashboard/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── dashboard_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── dashboard.html
└── db.sqlite3
```

---

## **2️⃣ `models.py`** (inside `dashboard_app`)

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
```

---

## **3️⃣ `views.py`** (inside `dashboard_app`)

```python
from django.shortcuts import render
from django.db.models import Q, F, Sum, Avg, Count, Max, Min, Value
from django.db.models.functions import Lower, Concat
from django.db.models import ExpressionWrapper, DecimalField
from .models import Product

def display(request):
    # Handle POST to add product
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        if name and price and description:
            Product.objects.create(
                name=name,
                price=price,
                description=description
            )

    # 1️⃣ Basic Queries
    all_products = Product.objects.all()
    filtered = Product.objects.filter(price__gte=500)
    excluded = Product.objects.exclude(name="Monitor")
    Product.objects.filter(name="TV").update(name="Television")
    Product.objects.update(price=F('price') + 50)

    # 2️⃣ Advanced Field Lookups
    contains_lookup = Product.objects.filter(name__contains="phone")
    icontains_lookup = Product.objects.filter(name__icontains="Phone")
    startswith_lookup = Product.objects.filter(name__startswith="S")
    endswith_lookup = Product.objects.filter(name__endswith="pro")
    in_lookup = Product.objects.filter(price__in=[100, 200, 500])
    range_lookup = Product.objects.filter(price__range=(100, 500))
    null_lookup = Product.objects.filter(description__isnull=True)

    # 3️⃣ Chaining Queries
    chain_filter = Product.objects.filter(price__gte=200).exclude(name__icontains="TV").order_by(Lower('name'))

    # 4️⃣ Aggregation & Annotation
    aggregate_data = Product.objects.aggregate(
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )

    price_after_tax = Product.objects.annotate(
        price_with_tax=ExpressionWrapper(F('price') * 1.1, output_field=DecimalField())
    )

    # 5️⃣ Exists / Count
    laptop_exists = Product.objects.filter(name="Laptop").exists()
    product_count = Product.objects.count()

    # 6️⃣ Distinct + Values / Values_list
    distinct_names = Product.objects.values('name').distinct()
    name_price_values = Product.objects.values('name', 'price')
    name_price_list = Product.objects.values_list('name', 'price')

    # 7️⃣ Raw SQL
    raw_query = Product.objects.raw('SELECT * FROM dashboard_app_product')

    # 8️⃣ Q Objects (complex conditions)
    q_filter = Product.objects.filter(Q(name__icontains="Laptop") & Q(price__gte=400))
    q_exclude = Product.objects.filter(~Q(name__icontains="Monitor"))

    # 9️⃣ Annotate with Concat
    concat_field = Product.objects.annotate(
        name_desc=Concat('name', Value(' - '), 'description')
    )

    context = {
        "all_products": all_products,
        "filtered": filtered,
        "excluded": excluded,
        "aggregate_data": aggregate_data,
        "price_after_tax": price_after_tax,
        "laptop_exists": laptop_exists,
        "product_count": product_count,
        "distinct_names": distinct_names,
        "name_price_values": name_price_values,
        "name_price_list": name_price_list,
        "raw_query": raw_query,
        "q_filter": q_filter,
        "q_exclude": q_exclude,
        "contains_lookup": contains_lookup,
        "icontains_lookup": icontains_lookup,
        "startswith_lookup": startswith_lookup,
        "endswith_lookup": endswith_lookup,
        "in_lookup": in_lookup,
        "range_lookup": range_lookup,
        "null_lookup": null_lookup,
        "chain_filter": chain_filter,
        "concat_field": concat_field,
    }

    return render(request, "dashboard.html", context)
```

---

## **4️⃣ `urls.py`** (inside `dashboard_app`)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.display, name='dashboard'),
]
```

---

## **5️⃣ Project-level `urls.py`** (`django_orm_dashboard/urls.py`)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard_app.urls')),
]
```

---

## **6️⃣ `dashboard.html`** (inside `dashboard_app/templates/`)

> Use the **full template** I created in the previous message. It contains **all tables** for all ORM operations.

---

## **7️⃣ Setup Steps**

1. Create Django project and app:

```bash
django-admin startproject django_orm_dashboard
cd django_orm_dashboard
python manage.py startapp dashboard_app
```

2. Add `dashboard_app` to `INSTALLED_APPS` in `settings.py`.

3. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Run server:

```bash
python manage.py runserver
```

5. Open: `http://127.0.0.1:8000/dashboard/`

* You’ll see **all ORM operations rendered in tables**.
* Add products via the form to test **POST + ORM operations**.
* Developers can see **CRUD, filter, aggregate, annotate, Q, F, raw queries** in real-time.

---

If you want, I can **also extend this project to include**:

* **Pagination** for large tables
* **Search & filter inputs** dynamically
* **AJAX updates**

…so your ORM dashboard becomes **fully production-ready and scalable**.

Do you want me to add these next?
