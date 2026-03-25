

✅ **Django Model Fields**
✅ **Constraints**
✅ **Choices (for dropdown-like fields)**




# **Django Models — Fields, Constraints, and Choices**



#________________________________________
## 1. What is a Model Field?
#________________________________________


A **model field** defines a **column in the database table**.
Each field represents one piece of data for every row (object).

### Example:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    joined_date = models.DateField(auto_now_add=True)
```

**Here:**

* `name` → Text (varchar)
* `age` → Number
* `email` → Email, must be unique
* `joined_date` → Date added automatically


#________________________________________
## 🧰 2. Commonly Used Django Model Fields
#________________________________________




| Field Name                                 | Description           | Example                                                             |
| ------------------------------------------ | --------------------- | ------------------------------------------------------------------- |
| `CharField(max_length=n)`                  | Short text            | `name = models.CharField(max_length=50)`                            |
| `TextField()`                              | Long text             | `bio = models.TextField()`                                          |
| `IntegerField()`                           | Integer number        | `age = models.IntegerField()`                                       |
| `DecimalField(max_digits, decimal_places)` | Decimal value         | `price = models.DecimalField(max_digits=6, decimal_places=2)`       |
| `FloatField()`                             | Floating-point number | `height = models.FloatField()`                                      |
| `BooleanField()`                           | True / False          | `is_active = models.BooleanField(default=True)`                     |
| `DateField()`                              | Date only             | `dob = models.DateField()`                                          |
| `DateTimeField()`                          | Date + Time           | `created_at = models.DateTimeField(auto_now_add=True)`              |
| `EmailField()`                             | Email address         | `email = models.EmailField()`                                       |
| `FileField()` / `ImageField()`             | File / Image upload   | `photo = models.ImageField(upload_to='photos/')`                    |
| `ForeignKey()`                             | One-to-Many relation  | `course = models.ForeignKey(Course, on_delete=models.CASCADE)`      |
| `ManyToManyField()`                        | Many-to-Many relation | `skills = models.ManyToManyField(Skill)`                            |
| `OneToOneField()`                          | One-to-One relation   | `profile = models.OneToOneField(Profile, on_delete=models.CASCADE)` |




#________________________________________
## 🧩 3. Model **Constraints**
#________________________________________



Constraints control **rules or restrictions** on data stored in the table.

### ✳️ Built-in Constraints

| Constraint              | Description                 | Example                                                         |
| ----------------------- | --------------------------- | --------------------------------------------------------------- |
| `unique=True`           | No duplicate values allowed | `email = models.EmailField(unique=True)`                        |
| `null=True`             | Field can be `NULL` in DB   | `middle_name = models.CharField(max_length=20, null=True)`      |
| `blank=True`            | Field can be empty in forms | `nickname = models.CharField(max_length=20, blank=True)`        |
| `default=value`         | Set a default value         | `country = models.CharField(default='India', max_length=30)`    |
| `choices=[()]`          | Restrict to certain options | (see below 👇)                                                  |
| `validators=[function]` | Custom validation           | `age = models.IntegerField(validators=[MinValueValidator(18)])` |




#________________________________________
### ⚙️ Database-Level Constraints (inside `Meta` class)
#________________________________________



```python
class Product(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'code'], name='unique_product')
        ]
```

✅ **This creates a unique pair** → (`name`, `code`)
You cannot insert two rows with the same name and code combination.



#________________________________________
## 🎯 4. Field **Choices** (Dropdown-like options)
#________________________________________



Use `choices` when you want to **limit valid values**.

```python
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
```

#________________________________________
**In admin panel or form:**
#________________________________________


You’ll see a **dropdown menu** with *Male, Female, Other*.

✅ **In database:**
It stores `'M'`, `'F'`, or `'O'`.

---
#________________________________________
# ## Pro tip — Better readability
#________________________________________


You can access choice labels easily:

```python
s = Student.objects.get(id=1)
print(s.get_gender_display())   # Output: Male
```

---

## 🧾 Summary Table

| Feature        | Purpose             | Example                                                       |
| -------------- | ------------------- | ------------------------------------------------------------- |
| **Field**      | Define table column | `name = models.CharField(max_length=50)`                      |
| **Constraint** | Control data rules  | `unique=True`, `null=False`, `validators`, `UniqueConstraint` |
| **Choices**    | Restrict options    | `choices=[('A', 'Active'), ('I', 'Inactive')]`                |

#________________________________________#________________________________________#______________________
