**create the tables (models)**, and then later use them to solve the **Django ORM Practice Tasks** 



# 📝 Django ORM Assignment

## 🔹 Part A: Table (Model) Creation

👉 Create the following models inside `models.py`:

### 1. Course

* `name` → `CharField(max_length=100)`

### 2. Student

* `name` → `CharField(max_length=100)`
* `age` → `IntegerField()`
* `marks` → `IntegerField()`
* `bio` → `TextField()` (optional)
* **Many-to-Many relationship** with `Course`

### 3. Author

* `name` → `CharField(max_length=100)`

### 4. Book

* `title` → `CharField(max_length=200)`
* **ForeignKey** to `Author` (`on_delete=models.CASCADE`)

✅ **Extra Instructions :**

* Implement `__str__` methods to return meaningful names.
* Run `python manage.py makemigrations` and `python manage.py migrate` to create the tables in the database.

---

## 🔹 Part B: ORM Query Practice

After creating tables and adding sample data, answer the following:

### 8. Aggregation (Sum, Avg, Min, Max)

1. Find the average age of all students.
2. Find the total marks scored by all students.
3. Find the minimum and maximum marks among students.
4. Count how many students are enrolled in each course.

### 9. Distinct (Unique values)

5. Get a list of all unique courses students are enrolled in.
6. Find the number of unique ages of students.

### 10. Values / Only Specific Fields

7. Fetch only the `name` and `age` of students (not full objects).
8. Fetch only the `name` of students using `.only()`.
9. Fetch all student details but skip the `bio` field using `.defer()`.

### 11. Relationships (FK / M2M)

10. Get all books written by a given author.
11. List all courses taken by a particular student.
12. Find all students enrolled in a particular course.

### 12. Q Objects (AND / OR queries)

13. Get all students whose name is either `"Rahul"` or `"Meena"`.
14. Get all students whose name is `"Rahul"` and age is greater than or equal to 18.
15. Get all students whose marks are greater than 80 or age is less than 20.

### 13. F Objects (Compare fields)

16. Find all students where `marks` are greater than `age`.
17. Find all students where `age` and `marks` are equal.
18. Increase all students’ marks by 5 using `F`.

### 14. Raw SQL (If needed)

19. Write a raw SQL query to fetch all students with age greater than 18.
20. Write a raw SQL query to get students who have marks more than 50.

---

👉 This way, **Part A (Models)** sets up the tables and **Part B (ORM Queries)** makes them practice ORM operations.