

# Topic:Django Models & Migrations – Notes



#_________________________
## 1. What is a Model?
#_________________________


# A **Model** is a Python class that represents a **table in the database**.

Each **model = one table**
Each **field = one column**
Each **object = one row**

### Example

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
```

#_________________________
### What this means
#_________________________

| Model Part    | Database Part |
| ------------- | ------------- |
| Student class | student table |
| name          | column        |
| age           | column        |
| email         | column        |



#_________________________
## 2. What is Migration?
#_________________________



Migration is Django’s way of **tracking changes in models** and **applying them to the database**.

Think of it like:

> “Instructions for the database to match the model.”



#_________________________
## 3. Two Important Commands
#_________________________


python manage.py makemigrations
python manage.py migrate



What happens:

| Step           | Action                     |
| -------------- | -------------------------- |
| makemigrations | creates new migration file |
| migrate        | adds new column to table   |




| Command        | Purpose                   | Changes DB? |
| -------------- | ------------------------- | ----------- |
| makemigrations | Create migration file     | ❌ No        |
| migrate        | Apply changes to database | ✅ Yes       |





#_________________________
## 4. Real-world analogy
#_________________________


Imagine **Model = Building plan**

| Step           | Real life                        | Django                |
| -------------- | -------------------------------- | --------------------- |
| Create model   | Draw building plan               | Write model class     |
| makemigrations | Create construction instructions | Create migration file |
| migrate        | Build the building               | Create table in DB    |




`