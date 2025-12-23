



# _______________________________________________
# **WHAT IS A JOIN?**
# ________________________________________________




A **JOIN** is used to combine rows from two or more tables **based on a related column**.

✔ JOIN always works using a **common column**
✔ Usually a **primary key ↔ foreign key**

Example pattern:

```sql
FROM tableA
JOIN tableB
ON tableA.id = tableB.fk_id;
```


# ________________________________________________
# ALL TYPES OF JOINS (Simple Notes)
# ________________________________________________




### ✔ 1. **INNER JOIN**
     Returns only **matching records** in both tables.



### ✔ 2. **LEFT JOIN**
      Returns **all records from left table**,

     * matching records from right table
     * NULL where no match.



### ✔ 3. **RIGHT JOIN**
     Returns **all records from right table**,

    * matching records from left table
     * NULL where no match.


### ✔ 4. **FULL JOIN** (not in MySQL normally)
      Returns **all rows** from both sides.



### ✔ 5. **CROSS JOIN**
       Returns **all possible combinations** (cartesian product).




# ________________________________________________
# **1. ONE-TO-ONE QUERIES**
# ________________________________________________





(persons ↔ passports)

### ✔ 1. Get all persons with their passport details (INNER JOIN)






```sql
SELECT p.person_id, p.name, pp.passport_number
FROM persons p
INNER JOIN passports pp
ON p.person_id = pp.reference_id;
```

---

### ✔ 2. Show all persons even if they don’t have a passport (LEFT JOIN)

```sql
SELECT p.person_id, p.name, pp.passport_number
FROM persons p
LEFT JOIN passports pp
ON p.person_id = pp.reference_id;
```

---

### ✔ 3. Show all passports even if person record is missing (RIGHT JOIN)

```sql
SELECT p.person_id, p.name, pp.passport_number
FROM persons p
RIGHT JOIN passports pp
ON p.person_id = pp.reference_id;
```

---

### ✔ 4. Get passport details of person with ID = 1

```sql
SELECT *
FROM passports
WHERE reference_id = 1;
```

---

### ✔ 5. Subquery: find the person whose passport reference_id = 7

```sql
SELECT *
FROM persons
WHERE person_id = (
    SELECT reference_id 
    FROM passports 
    WHERE reference_id = 7
);
```

---

---

# ________________________________________________
# **2. ONE-TO-MANY QUERIES**
# ________________________________________________




(departments ↔ employees)

### ✔ 1. Show employees with their department name




```sql
SELECT e.emp_id, e.name, d.dept_name
FROM employees e
JOIN departments d
ON e.emp_refer_id = d.dept_id;
```

---

### ✔ 2. Show all departments even if they have no employees (LEFT JOIN)

```sql
SELECT d.dept_id, d.dept_name, e.name AS employee_name
FROM departments d
LEFT JOIN employees e
ON d.dept_id = e.emp_refer_id;
```

---

### ✔ 3. Get all employees under “Human Resources” department




```sql
SELECT e.*
FROM employees e
JOIN departments d
ON e.emp_refer_id = d.dept_id
WHERE d.dept_name = 'Human Resources';
```

---

### ✔ 4. Count how many employees are in each department





```sql
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees
FROM departments d
LEFT JOIN employees e
ON d.dept_id = e.emp_refer_id
GROUP BY d.dept_name;
```

---

### ✔ 5. Find departments with no employees


```sql
SELECT d.*
FROM departments d
LEFT JOIN employees e
ON d.dept_id = e.emp_refer_id
WHERE e.emp_id IS NULL;
```

---

---

# ________________________________________________
#  **3. MANY-TO-MANY QUERIES**
# ________________________________________________




(students ↔ courses via student_courses)

### ✔ 1. Show which student is taking which course

```sql
SELECT s.name AS student, c.course_name AS course
FROM students s
JOIN student_courses sc ON s.student_id = sc.student_id
JOIN courses c ON sc.course_id = c.course_id;
```

---

### ✔ 2. Show all courses taken by student with ID = 1

```sql
SELECT c.course_name
FROM courses c
JOIN student_courses sc ON c.course_id = sc.course_id
WHERE sc.student_id = 1;
```

---

### ✔ 3. Show all students enrolled in “Database Management” course

```sql
SELECT s.name
FROM students s
JOIN student_courses sc ON s.student_id = sc.student_id
JOIN courses c ON sc.course_id = c.course_id
WHERE c.course_name = 'Database Management';
```

---

### ✔ 4. Count students per course

```sql
SELECT c.course_name, COUNT(sc.student_id) AS total_students
FROM courses c
LEFT JOIN student_courses sc ON c.course_id = sc.course_id
GROUP BY c.course_name;
```

---

### ✔ 5. Find students who are not enrolled in any course

```sql
SELECT s.*
FROM students s
LEFT JOIN student_courses sc
ON s.student_id = sc.student_id
WHERE sc.course_id IS NULL;
```

---



# ________________________________________________
# 4.  MIXED JOIN + AGGREGATES + SUBQUERY **
# ________________________________________________




### **Q1. Find the department with the highest number of employees.**

**A16:**

```sql
SELECT d.dept_name, COUNT(e.emp_id) AS total
FROM departments d
JOIN employees e ON d.dept_id = e.emp_refer_id
GROUP BY d.dept_name
ORDER BY total DESC
LIMIT 1;
```

---

### **Q2. Find the student who is enrolled in the maximum number of courses.**

**A17:**

```sql
SELECT s.name, COUNT(sc.course_id) AS total_courses
FROM students s
JOIN student_courses sc
ON s.student_id = sc.student_id
GROUP BY s.name
ORDER BY total_courses DESC
LIMIT 1;
```

---

### **Q3. Get courses that have more than 2 students enrolled.**

**A18:**

```sql
SELECT c.course_name, COUNT(sc.student_id) AS total
FROM courses c
JOIN student_courses sc ON c.course_id = sc.course_id
GROUP BY c.course_name
HAVING COUNT(sc.student_id) > 2;
```

---

### **Q4. Show employees who work in departments where employee count > 3.**

**A19:**

```sql
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d ON e.emp_refer_id = d.dept_id
WHERE d.dept_id IN (
    SELECT emp_refer_id
    FROM employees
    GROUP BY emp_refer_id
    HAVING COUNT(emp_id) > 3
);
```

---

### **Q5. Find persons who have passports ending with ‘IN’.**

**A20:**

```sql
SELECT p.name, pp.passport_number
FROM persons p
JOIN passports pp
ON p.person_id = pp.reference_id
WHERE pp.passport_number LIKE '%IN';
```


✔ WHERE → filter rows
✔ ORDER BY → sorting
✔ LIMIT → restrict number of rows
✔ DISTINCT → unique values
✔ BETWEEN → range
✔ LIKE → pattern
✔ IN → list of values


# ________________________________________________



