
# 🔎 What is a ViewSet?

Normally in DRF you write multiple views for CRUD:

* `ListAPIView` → List all
* `RetrieveAPIView` → Get one
* `CreateAPIView` → Add new
* `UpdateAPIView` → Update
* `DestroyAPIView` → Delete

👉 With **ViewSet**, you can combine all of them in **one class**.
👉 With a **Router**, URLs are created automatically.

---

## ✅ Step 1: Serializer

```python
# myapp/serializers.py
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
```

---

## ✅ Step 2: ViewSet

```python
# myapp/views.py
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

* `ModelViewSet` = gives **list, create, retrieve, update, delete** automatically.
* You only need to define `queryset` + `serializer_class`.

---

## ✅ Step 3: URLs with Router

```python
# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

---

## ✅ Step 4: Test in Browser/Postman

Now DRF gives you all CRUD automatically 🚀

| Method | URL            | Action                |
| ------ | -------------- | --------------------- |
| GET    | `/students/`   | List all students     |
| GET    | `/students/1/` | Get student with ID=1 |
| POST   | `/students/`   | Create new student    |
| PUT    | `/students/1/` | Update student        |
| PATCH  | `/students/1/` | Partial update        |
| DELETE | `/students/1/` | Delete student        |

---

## ✅ Example POST (Create Student)

```json
{
  "name": "Alice",
  "age": 22,
  "email": "alice@example.com"
}
```

---

# 📌 Summary for Students

* **ViewSet** = One class for all CRUD operations.
* **Router** = Generates URLs automatically.
* **ModelViewSet** = Quickest way to create full CRUD API.





# myapp/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name



# myproject/settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,  # show 5 students per page
}


pip install django-filter
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
}





Ok! 😄 Let me explain this **Django REST Framework URL setup** in **Thunglish** like I’m explaining to a 5-year-old.

---

### Code you have:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drfapp import views

router = DefaultRouter()
router.register(r'students', views.StudentViewSet)

urlpatterns = [
 path('', include(router.urls)),
]
```

---

### Step by step Thunglish:

1️⃣ **`from django.urls import path, include`**

* Django ku solra **roads / paths** (URLs) eppo varum-nu manage panna.
* `path` → oru road / URL define panna.
* `include` → vere file-la irukkura roads-a kooda connect panna.

2️⃣ **`from rest_framework.routers import DefaultRouter`**

* DRF-la, **DefaultRouter** use pannina **automatic roads** ready-a varum.
* Manual-a `path('students/', ...)` type panna venda.
* Router-a use pannina **list, create, update, delete** roads ellam ready-a irukkum.

3️⃣ **`router = DefaultRouter()`**

* Ippo oru **router box** ready pannrom.
* Intha box-ku `views` attach pannina, **URLs auto-generate aagum**.

4️⃣ **`router.register(r'students', views.StudentViewSet)`**

* `r'students'` → road name.
* `views.StudentViewSet` → logic eppo nadakum-nu solra box.
* Router automatically:







```
GET /students/        → ellarum students list pannu
POST /students/       → pudhu student add pannu
GET /students/1/      → student 1 details paathu varu
PUT /students/1/      → student 1 update pannu
DELETE /students/1/   → student 1 delete pannu
```















5️⃣ **`urlpatterns = [ path('', include(router.urls)) ]`**

* Main URL file-la (usually `urls.py`) oru road path-a declare pannom.
* `''` → main road.
* `include(router.urls)` → router-la irukkura ellam roads add aagum.

---

✅ **In short in Thunglish:**

* Router = magic box, automatically REST roads ready pannum.
* `StudentViewSet` = box inside logic, **students ku actions** pannum.
* `urlpatterns` = main road-la router attach pannom, so browser / Postman-la easy-a access pannalaam.

---

If you want, I can **draw a small fun picture showing students REST roads like a playground map** 😄.

Do you want me to do that?
