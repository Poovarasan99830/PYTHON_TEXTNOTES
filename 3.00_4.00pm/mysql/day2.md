
# 🧩 **MySQL DML Commands**

---
# ______________________________________________________________________
## **1️⃣ Definition**
# ______________________________________________________________________




**DML (Data Manipulation Language)** commands are used to **manipulate or manage the data stored** inside database tables — not the structure itself.

They allow you to:

* **Insert** new records,
* **Update** existing data,
* **Delete** unwanted data,
* **Retrieve** (Select) information from tables.

Unlike DDL, **DML commands can be rolled back** if not committed — meaning you can undo changes before saving permanently.

---


# ______________________________________________________________________
## **2️⃣ Example Code (N+ Examples for Each DML Command)**
# ______________________________________________________________________





# ______________________________________________________________________
### 🟢 **A. INSERT — Add new records to a table**
# ______________________________________________________________________





```sql
-- 1. Insert single record
INSERT INTO students (student_id, name, age, grade)
VALUES (1, 'Arjun', 16, 'A');

-- 2. Insert multiple records
INSERT INTO students (student_id, name, age, grade)
VALUES 
(2, 'Kavya', 15, 'B'),
(3, 'Ravi', 17, 'A'),
(4, 'Meena', 14, 'C');

-- 3. Insert data only into selected columns
INSERT INTO students (student_id, name)
VALUES (5, 'Suresh');

-- 4. Insert data using another table
INSERT INTO alumni_students
SELECT * FROM students WHERE grade = 'A';

-- 5. Insert with default values
INSERT INTO students VALUES (6, DEFAULT, DEFAULT, DEFAULT);
```

---
# ______________________________________________________________________
### 🟠 **B. UPDATE — Modify existing records**
# ______________________________________________________________________





```sql
-- 1. Update single column
UPDATE students
SET grade = 'A'
WHERE student_id = 4;

-- 2. Update multiple columns
UPDATE students
SET name = 'Kavya R', age = 16
WHERE student_id = 2;

-- 3. Update all rows (use carefully)
UPDATE students
SET grade = 'B';

-- 4. Update using condition
UPDATE employees
SET salary = salary * 1.10
WHERE dept_id = 101;

-- 5. Update from another table (join update)
UPDATE orders AS o
JOIN customers AS c ON o.customer_id = c.id
SET o.customer_name = c.name;
```

---

### 🔴 **C. DELETE — Remove data from tables**

```sql
-- 1. Delete specific record
DELETE FROM students
WHERE student_id = 3;

-- 2. Delete based on condition
DELETE FROM employees
WHERE salary < 30000;

-- 3. Delete all records (table stays)
DELETE FROM products;

-- 4. Delete with subquery
DELETE FROM employees
WHERE dept_id IN (
    SELECT dept_id FROM departments WHERE location = 'Chennai'
);

-- 5. Delete from joined tables (advanced)
DELETE s
FROM sales AS s
JOIN returns AS r ON s.id = r.sale_id
WHERE r.status = 'Refunded';
```

---

### 🔵 **D. SELECT — Retrieve data from tables**

```sql
-- 1. Select all columns
SELECT * FROM students;

-- 2. Select specific columns
SELECT name, grade FROM students;

-- 3. Select with condition
SELECT * FROM employees WHERE salary > 50000;

-- 4. Select with sorting
SELECT name, age FROM students ORDER BY age DESC;

-- 5. Select with aggregation
SELECT dept_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept_id;

-- 6. Select with alias
SELECT name AS EmployeeName, salary AS Pay FROM employees;

-- 7. Select using joins
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;

-- 8. Select with subquery
SELECT name FROM students
WHERE grade = (SELECT MAX(grade) FROM students);
```

---

## **3️⃣ Tasks / Practice Questions**

Try the following hands-on:

1. Insert 5 new records into `employee` table.
2. Update salary of employees in `Sales` department by 10%.
3. Delete all employees who haven’t logged in for 1 year.
4. Retrieve employee names and their department names using JOIN.
5. List all students with grade ‘A’.
6. Insert records from one table to another using subquery.
7. Delete records of products with zero stock.
8. Display all orders sorted by date (latest first).
9. Show total number of employees in each department.
10. Update marks of students who scored below average by +5%.

---

## **4️⃣ Real-World Inspired Examples**

### 🏦 **Banking System**

```sql
-- Insert new customer
INSERT INTO customers (cust_id, name, account_type, balance)
VALUES (101, 'Ramesh Kumar', 'Savings', 15000);

-- Update balance after transaction
UPDATE customers SET balance = balance - 500 WHERE cust_id = 101;

-- Delete inactive customers
DELETE FROM customers WHERE last_login < '2024-01-01';

-- Retrieve high-balance customers
SELECT name, balance FROM customers WHERE balance > 100000;
```

---

### 🛒 **E-Commerce Platform**

```sql
-- Add new product
INSERT INTO products (product_name, price, stock)
VALUES ('Wireless Mouse', 750, 100);

-- Update stock after sale
UPDATE products SET stock = stock - 1 WHERE product_id = 3;

-- Delete discontinued products
DELETE FROM products WHERE status = 'discontinued';

-- Fetch top 5 selling products
SELECT product_name, SUM(quantity) AS total_sold
FROM sales
GROUP BY product_name
ORDER BY total_sold DESC
LIMIT 5;
```

---

### 🏥 **Hospital Management**

```sql
-- Insert new patient record
INSERT INTO patients (patient_id, name, disease, doctor)
VALUES (201, 'Priya', 'Fever', 'Dr. Arun');

-- Update doctor name for certain cases
UPDATE patients SET doctor = 'Dr. Karthik' WHERE disease = 'Cold';

-- Delete old records
DELETE FROM patients WHERE admission_date < '2024-01-01';

-- Retrieve all admitted patients
SELECT name, disease, doctor FROM patients WHERE status = 'Admitted';
```

---

## **5️⃣ Industry Use Cases**

| Industry       | DML Use Case               | Description                                        |
| -------------- | -------------------------- | -------------------------------------------------- |
| **FinTech**    | Transaction Handling       | Insert, update, and retrieve customer transactions |
| **E-Commerce** | Product & Order Management | Manage product stock and customer orders           |
| **Healthcare** | Patient Record Updates     | Insert, modify, or delete patient visit records    |
| **Banking**    | Account Balances           | Update after deposits or withdrawals               |
| **Education**  | Student Result Management  | Update scores, retrieve top performers             |
| **Analytics**  | Data Aggregation           | Query summaries and reports                        |

---

## **6️⃣ Important Methods + Real-World Usage**

| Command  | Key Role                    | Real-World Example                              |
| -------- | --------------------------- | ----------------------------------------------- |
| `INSERT` | Add new data                | Add new user or order record                    |
| `UPDATE` | Modify existing data        | Adjust product price or employee salary         |
| `DELETE` | Remove unwanted data        | Delete old logs or inactive accounts            |
| `SELECT` | Retrieve data (most common) | Generate reports, dashboards, or search results |

---

## ⚙️ **Pro Tip: DML vs DDL Quick Summary**

| Feature     | DDL (Structure)          | DML (Data)                     |
| ----------- | ------------------------ | ------------------------------ |
| Full Form   | Data Definition Language | Data Manipulation Language     |
| Purpose     | Defines structure/schema | Manages table data             |
| Rollback    | ❌ Not possible           | ✅ Possible before COMMIT       |
| Examples    | CREATE, ALTER, DROP      | SELECT, INSERT, UPDATE, DELETE |
| Auto-Commit | ✅ Yes                    | ❌ No (needs COMMIT manually)   |


