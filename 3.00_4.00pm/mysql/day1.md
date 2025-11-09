

# 🧩 **MySQL DDL Commands 
---

## **1️⃣ Definition**

**DDL (Data Definition Language)** commands define, modify, or remove **database structure** — including my, databases, indexes, and views.

It doesn’t handle *data values* — it handles *the design* (like the “blueprint” of the database).

Every DDL command is **auto-committed** → meaning once executed, changes **cannot be rolled back** (unlike DML commands).

---

## **2️⃣ Example Code (N+ Examples for Each DDL Command)**

### 🧱 **A. CREATE — Build new database objects**

```sql
-- 1. Create a new database
CREATE DATABASE school_db;

-- 2. Create a new table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade CHAR(2)
);

-- 3. Create a table with constraints
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(100) NOT NULL,
    dept_id INT,
    salary DECIMAL(10,2) CHECK (salary > 0)
);

-- 4. Create a table based on another table
CREATE TABLE senior_employees AS
SELECT * FROM employees WHERE salary > 80000;

-- 5. Create an index
CREATE INDEX idx_dept_id ON employees(dept_id);

-- 6. Create a view
CREATE VIEW high_paid AS
SELECT emp_name, salary FROM employees WHERE salary > 100000;
```

---

### 🛠️ **B. ALTER — Modify existing database objects**

```sql
-- 1. Add a new column
ALTER TABLE students ADD COLUMN email VARCHAR(100);

-- 2. Modify column data type
ALTER TABLE students MODIFY COLUMN age SMALLINT;

-- 3. Rename a column
ALTER TABLE students RENAME COLUMN grade TO class_grade;

-- 4. Drop a column
ALTER TABLE students DROP COLUMN email;

-- 5. Add a constraint (unique key)
ALTER TABLE employees ADD CONSTRAINT unique_email UNIQUE (emp_name);

-- 6. Rename a table
ALTER TABLE employees RENAME TO staff;

-- 7. Add multiple columns at once
ALTER TABLE staff
ADD COLUMN doj DATE,
ADD COLUMN location VARCHAR(50);
```

---

### 🧨 **C. DROP — Permanently delete database objects**

```sql
-- 1. Drop a table
DROP TABLE staff;

-- 2. Drop a view
DROP VIEW high_paid;

-- 3. Drop an index
DROP INDEX idx_dept_id ON employees;

-- 4. Drop an entire database
DROP DATABASE school_db;

-- 5. Drop a column constraint
ALTER TABLE employees DROP CONSTRAINT unique_email;
```

---

### 🧹 **D. TRUNCATE — Remove all rows but keep structure**

```sql
-- 1. Remove all student records, keep table
TRUNCATE TABLE students;

-- 2. Reset data for monthly logs
TRUNCATE TABLE sales_logs;

-- 3. Clear staging table before importing new data
TRUNCATE TABLE staging_orders;
```

---

### 🪶 **E. RENAME — Change table or database names**

```sql
-- 1. Rename a single table
RENAME TABLE students TO student_info;

-- 2. Rename multiple tables
RENAME TABLE orders TO order_history,
             customers TO client_data;

-- 3. Rename a database
RENAME DATABASE old_db TO new_db;  -- (Note: Some MySQL versions don’t support this directly)
```

---

### 🧾 **F. COMMENT — Add notes/documentation**

```sql
-- 1. Add comment to a table
ALTER TABLE employees COMMENT = 'Stores company employee details';

-- 2. Add comment to a column
ALTER TABLE employees MODIFY emp_name VARCHAR(100) COMMENT 'Full name of the employee';

-- 3. View table comments
SHOW TABLE STATUS LIKE 'employees';
```

---

## **3️⃣ Tasks / Practice Questions**

Try solving these hands-on:

1. Create a database `company_db`.
2. Create tables: `department`, `employee`, `project`.
3. Add `JOINING_DATE` to `employee`.
4. Rename `employee` to `emp_master`.
5. Drop `project` table.
6. Truncate `department`.
7. Add a column `project_id` in `emp_master`.
8. Create an index on `emp_name`.
9. Create a view for employees with salary > 1,00,000.
10. Add comments to describe each column.

---

## **4️⃣ Real-World Inspired Examples**

### 🏦 **Banking System**

* Create accounts table:

  ```sql
  CREATE TABLE accounts (
      account_no BIGINT PRIMARY KEY,
      holder_name VARCHAR(100),
      balance DECIMAL(15,2),
      branch_code CHAR(5)
  );
  ```
* Modify structure when adding online banking:

  ```sql
  ALTER TABLE accounts ADD COLUMN email VARCHAR(100);
  ```
* Drop inactive test tables:

  ```sql
  DROP TABLE test_transactions;
  ```

### 🛒 **E-commerce**

* Create table for products:

  ```sql
  CREATE TABLE products (
      product_id INT AUTO_INCREMENT PRIMARY KEY,
      product_name VARCHAR(100),
      price DECIMAL(10,2),
      stock INT
  );
  ```
* Add discount column:

  ```sql
  ALTER TABLE products ADD COLUMN discount DECIMAL(5,2) DEFAULT 0;
  ```
* Reset monthly temporary cart data:

  ```sql
  TRUNCATE TABLE temp_cart;
  ```

### 🏥 **Hospital Management**

* Add new column for doctor specialization:

  ```sql
  ALTER TABLE doctors ADD COLUMN specialization VARCHAR(50);
  ```
* Rename table for clarity:

  ```sql
  RENAME TABLE patient_data TO patients;
  ```
* Drop deprecated tables after system migration:

  ```sql
  DROP TABLE old_appointments;
  ```

---

## **5️⃣ Industry Use Cases**

| Industry             | DDL Use Case                 | Description                                    |
| -------------------- | ---------------------------- | ---------------------------------------------- |
| **FinTech**          | Schema Migration             | Add/remove columns for compliance data         |
| **E-Commerce**       | Product Catalog Setup        | Create tables for products, orders, reviews    |
| **Healthcare**       | Patient DB Design            | Define structure for hospital modules          |
| **Banking**          | Security Audits              | Drop obsolete or test tables                   |
| **SaaS Platforms**   | Multi-tenant Schema Creation | Automatically create databases for each client |
| **Data Warehousing** | Truncate for ETL cycles      | Clean staging tables nightly                   |
| **DevOps**           | Database Automation          | DDL inside deployment scripts                  |

---

## **6️⃣ Important Methods + Real-World Usage**

| Command        | Key Role                   | Real-World Example                    |
| -------------- | -------------------------- | ------------------------------------- |
| `CREATE`       | Define structure           | Create tables for customer & billing  |
| `ALTER`        | Modify schema              | Add new analytics columns             |
| `DROP`         | Delete structure           | Remove test or deprecated tables      |
| `TRUNCATE`     | Clear data, keep structure | Monthly reset of temporary tables     |
| `RENAME`       | Change names               | Rename after feature update           |
| `COMMENT`      | Document design            | Add notes for developer handoff       |
| `CREATE INDEX` | Performance tuning         | Speed up queries in reporting tools   |
| `CREATE VIEW`  | Logical abstraction        | Simplify complex joins for dashboards |

---

## ⚙️ **Pro Tip: DDL vs DML Quick Summary**

| Feature   | DDL                      | DML                            |
| --------- | ------------------------ | ------------------------------ |
| Full Form | Data Definition Language | Data Manipulation Language     |
| Purpose   | Defines structure        | Manipulates data               |
| Rollback  | ❌ Not possible           | ✅ Possible                     |
| Examples  | CREATE, ALTER, DROP      | SELECT, INSERT, UPDATE, DELETE |

