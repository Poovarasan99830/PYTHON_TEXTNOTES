

# _______________________________________________
# **DQL (Data Query Language) — Notes**
# _______________________________________________



# _______________________________________________
### **Definition**
# _______________________________________________



* Used to **fetch/read** data from the database.
* Only one command → **SELECT**.

---

# _______________________________________________
# 📌 **Purpose**
# _______________________________________________


* Retrieve specific data from tables.
* Apply filters, sorting, grouping, limits, joins.



# _______________________________________________
# *DQL (Data Query Language) — Topic-wise Teaching Notes**
# _______________________________________________
---



5. DQL (Data Query Language)

(Teach in very clear clause-wise order)

🔹 Step-by-step topics:

1️⃣ SELECT
2️⃣ FROM
3️⃣ WHERE
4️⃣ GROUP BY
5️⃣ HAVING
6️⃣ ORDER BY
7️⃣ LIMIT
8️⃣ DISTINCT
9️⃣ ALIAS



# _______________________________________________
# 1️⃣ **SELECT — (Choose Columns)**
# _______________________________________________


### **Definition:**

Used to select *which columns* you want to display.

### **Syntax:**

```sql
SELECT column1, column2
FROM table_name;
```



### **Examples:**

```sql
SELECT name, salary FROM employees;
SELECT * FROM employees;   -- all columns
```

---
# _______________________________________________
# 2️⃣ **FROM — (Choose Table)**
# _______________________________________________



### **Definition:**

Tells SQL which *table* to fetch data from.

### **Syntax:**

```sql
SELECT * 
FROM employees;
```

### **Key Point:**

`SELECT` asks **what**,
`FROM` tells **from where**.

---



# _______________________________________________
# 3️⃣ **WHERE — (Filter Rows)**
# _______________________________________________




### **Definition:**

Used to filter rows based on conditions.

### **Syntax:**

```sql
SELECT * FROM employees
WHERE salary > 50000;
```






# _______________________________________________
### **Operators Used:**
# _______________________________________________




`=`, `!=`, `>`, `<`, `>=`, `<=`, `BETWEEN`, `IN`, `LIKE`, `AND`, `OR`

### **Examples:**

```sql
SELECT * FROM employees WHERE department = 'IT';
SELECT * FROM employees WHERE age BETWEEN 25 AND 35;
```







---
# _______________________________________________
What Are Aggregate Functions?
# _______________________________________________




Aggregate functions perform a calculation on a group of values and return a single result.

They are used with:

SELECT

GROUP BY

HAVING




Usually used with aggregate functions:

* `COUNT()`
* `SUM()`
* `AVG()`
* `MAX()`
* `MIN()`

### **Syntax:**

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

---


# _______________________________________________
# 4️⃣ **GROUP BY — (Group Rows)**
# _______________________________________________




### **Definition:**

Groups multiple rows into one row based on a column.



# 5️⃣ **HAVING — (Filter Groups)**

### **Definition:**

Filters groups **after** GROUP BY.

### **Syntax:**

```sql
SELECT department, COUNT(*) AS total
FROM employees
GROUP BY department
HAVING total > 3;
```

### **Key Difference:**

| WHERE                 | HAVING             |
| --------------------- | ------------------ |
| Filters rows          | Filters groups     |
| Before GROUP BY       | After GROUP BY     |
| Cannot use aggregates | Can use aggregates |








# _______________________________________________
# 6️⃣ **ORDER BY — (Sort Rows)**
# _______________________________________________



### **Definition:**

Sorts the result.

### **Syntax:**

```sql
SELECT name, salary
FROM employees
ORDER BY salary DESC;
```

### **Options:**

* `ASC` (default)
* `DESC`









# _______________________________________________
# 7️⃣ **LIMIT — (Restrict Row Count)**
# _______________________________________________



### **Definition:**

Limits number of rows returned.

### **Syntax:**

```sql
SELECT * FROM employees LIMIT 5;
```

### **Pagination:**

```sql
SELECT * FROM employees LIMIT 10 OFFSET 20;
```










# _______________________________________________
# 8️⃣ **DISTINCT — (Remove Duplicates)**
# _______________________________________________


### **Definition:**

Used to select unique values.

### **Syntax:**

```sql
SELECT DISTINCT department
FROM employees;
```






# _______________________________________________
# 9️⃣ **ALIAS (AS) — (Rename Column/Table)**
# _______________________________________________




### **Definition:**

Creates a temporary name for column/table.

### **Syntax:**

```sql
SELECT name AS emp_name
FROM employees;
```

### **Table Alias Example:**

```sql
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d
ON e.dept_id = d.id;
```

---










# _______________________________________________
# 🔟 **JOIN — (Fetch Data from Multiple Tables)**
# _______________________________________________





### **Definition:**

Used to combine rows from 2 tables based on a related column.

### **Types:**

* INNER JOIN
* LEFT JOIN
* RIGHT JOIN
* CROSS JOIN

### **Example:**

```sql
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.id;
```

