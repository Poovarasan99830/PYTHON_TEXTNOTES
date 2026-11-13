
#________________________________________________
#  *What is a RELATION?**
#________________________________________________

    A relation is how **two tables connect**.
    To connect, both tables must have **one common value**.



Example:

   students.dept_id = departments.dept_id

So a student belongs to a department.

   ✔ Relation = Mapping between tables
  ✔ Relation only works if values match

---


#________________________________________________
#  **What is a FOREIGN KEY?**
#________________________________________________

    A **foreign key (FK)** is the *bridge* between tables.



Definition:

🔹 A Primary Key in one table
🔹 Appears as a normal column in another table
🔹 And is used to connect them



Example:

### departments table

```sql

   dept_id INT PRIMARY KEY


```

### students table

```sql
     dept_id INT  -- becomes foreign key here
```

Add relation using FOREIGN KEY:

```sql
ALTER TABLE students
ADD FOREIGN KEY (dept_id)
REFERENCES departments(dept_id);
```

Meaning:

✔ students.dept_id must exist in departments.dept_id
✔ No invalid data allowed
✔ Keeps database correct (integrity)





Below is the **continuation of your notes**, written in the **same professional, beginner-friendly style** as your RELATION and FOREIGN KEY notes.

We now explain **TYPES OF RELATIONSHIPS** using **your own tables**:

✔ persons–passports
✔ departments–employees
✔ students–courses

---

#________________________________________________
#  **WHAT IS A DATABASE RELATIONSHIP?**
#________________________________________________



A relationship describes **how many records in one table** are connected to
**how many records in another table**.

Every database relationship is based on:

✔ Primary Key (unique in main table)
✔ Foreign Key (reference in another table)

There are **3 real types**:

1️⃣ One-to-One (1 : 1)
2️⃣ One-to-Many (1 : M)
3️⃣ Many-to-Many (M : M)

Now let’s explain each one using your tables.

---

#________________________________________________
# **1. ONE-TO-ONE RELATIONSHIP (1 : 1)**
#________________________________________________


# _____________________________
### ✔ Definition
# ______________________________


One record in table A
↔ one record in table B.

No duplicates allowed on both sides.

---
# _____________________________
# ✔ Your Example – persons ↔ passports
# _____________________________

```
persons.person_id  =  passports.reference_id
```

Each person has **at most one passport**.

Each passport belongs to **only one person**.

---
# _____________________________
### Table Structure Showing Relationship
# _____________________________


```sql
CREATE TABLE persons (
    person_id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE passports (
    passport_id INT PRIMARY KEY,
    passport_number VARCHAR(20),
    reference_id INT UNIQUE,
    FOREIGN KEY(reference_id) REFERENCES persons(person_id)
);
```

Notice:

✔ `reference_id` is UNIQUE → so only **one passport per person**
✔ Perfect one-to-one mapping

---

### Real Meaning

✔ Person 8 → passport assigned
✔ Person 7 → passport assigned
✔ Person 3 → no passport (but allowed)

---

#________________________________________________
# **2. ONE-TO-MANY RELATIONSHIP (1 : M)**
#________________________________________________


# _____________________________
### ✔ Definition
# _____________________________


One record in Table A
↔ Many records in Table B.

Table A = “parent”
Table B = “child”

Parent’s PK → appears many times as FK in child.

---
# _____________________________
# ✔ Your Example – departments ↔ employees
# _____________________________


```
departments.dept_id = employees.emp_refer_id
```

One department
→ can have many employees.

But an employee
→ belongs to only one department.

---
# _____________________________
### Table Structure Showing Relationship
# _____________________________



#### departments

```sql
dept_id INT PRIMARY KEY
```

#### employees

```sql
emp_refer_id INT  -- foreign key
```

### Real Meaning Using Your Data

| dept_id | dept_name       | employee count |
| ------- | --------------- | -------------- |
| 1       | Human Resources | 4 employees    |
| 4       | IT              | 2 employees    |
| 3       | Sales           | 1 employee     |
| 5       | Marketing       | 1 employee     |

Examples:

✔ Department 1 has Arun, Priya, Karthik, Deepa
✔ Department 4 has Meena, Rahul

This is exactly one-to-many.

---

#________________________________________________
# **3. MANY-TO-MANY RELATIONSHIP (M : M)**
#________________________________________________



# _____________________________
### ✔ Definition
# _____________________________




Many records in Table A
↔ Many records in Table B.

This requires a **third (bridge) table**.

---


# _____________________________
# ✔ Your Example – students ↔ courses
# _____________________________




A student can take many courses.
A course can have many students.

**Bridge table used: student_courses**

---
# _____________________________
### Table Structure Showing Relationship
# _____________________________



#### students

```sql
student_id INT PRIMARY KEY
```

#### courses

```sql
course_id INT PRIMARY KEY
```

#### student_courses (bridge)

```sql
student_id INT  -- FK
course_id INT   -- FK
```

---

### Real Meaning Using Your Data

| student | courses enrolled |
| ------- | ---------------- |
| 1       | 101, 102, 103    |
| 2       | 101, 104         |
| 3       | 103, 105         |
| 4       | 102, 104         |
| 5       | 101, 103, 105    |

And the reverse:

| course | students enrolled |
| ------ | ----------------- |
| 101    | 1,2,5             |
| 102    | 1,4               |
| 103    | 1,3,5             |
| 104    | 2,4               |
| 105    | 3,5               |

This is a perfect many-to-many relationship.

---

# ________________________________________________
# SUMMARY TABLE
# ________________________________________________



| Relationship Type | Meaning                   | Your Example                             |
| ----------------- | ------------------------- | ---------------------------------------- |
| **1 : 1**         | One record ↔ one record   | persons ↔ passports                      |
| **1 : M**         | One record ↔ many records | departments ↔ employees                  |
| **M : M**         | Many ↔ many records       | students ↔ courses (via student_courses) |

---







