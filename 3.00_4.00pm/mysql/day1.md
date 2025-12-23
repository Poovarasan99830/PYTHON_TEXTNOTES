




# _____________________________________________________
#  **SQL Data Types with Table Creation Example**
# _____________________________________________________




SQL data types are used to define **what type of data** a column can store.

Below are the most common data types (MySQL):

---

# 🔹 **1. Numeric Data Types**

| Data Type     | Description              | Example Value |
| ------------- | ------------------------ | ------------- |
| INT           | Whole numbers            | 10, 200       |
| BIGINT        | Larger whole numbers     | 999999        |
| FLOAT         | Decimal (less precision) | 45.67         |
| DOUBLE        | Decimal (more precision) | 78.12345      |
| DECIMAL(10,2) | Exact decimal values     | 999.99        |

---

# 🔹 **2. String / Character Data Types**

| Data Type  | Description            | Example                |
| ---------- | ---------------------- | ---------------------- |
| CHAR(n)    | Fixed-length string    | ’ABC’                  |
| VARCHAR(n) | Variable-length string | “John”                 |
| TEXT       | Large text data        | Comments, descriptions |

---

# 🔹 **3. Date & Time Data Types**

| Data Type | Description                   |
| --------- | ----------------------------- |
| DATE      | Stores year-month-day         |
| TIME      | Stores time only              |
| DATETIME  | Stores both date & time       |
| TIMESTAMP | Auto time for record creation |

---

# 🔹 **4. Boolean**

| Data Type            | Description         |
| -------------------- | ------------------- |
| BOOLEAN / TINYINT(1) | True / False values |

---

# 🔹 **5. Binary / Files**

| Data Type | Description                    |
| --------- | ------------------------------ |
| BLOB      | Store images, files, PDFs etc. |

---

---
# _____________________________________________________
# 🟢 **REAL TABLE CREATION EXAMPLE WITH ALL DATA TYPES**
# _____________________________________________________




```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age INT,
    marks DECIMAL(5,2),
    email VARCHAR(100),
    phone CHAR(10),
    is_active BOOLEAN DEFAULT 1,
    join_date DATE,
    last_login DATETIME,
    profile_photo BLOB,
    description TEXT
);
```


# _____________________________________________________
# 🟡 **Insert Sample Data**
# _____________________________________________________




```sql
INSERT INTO students 
(name, age, marks, email, phone, is_active, join_date, last_login, description)
VALUES
("Arun", 21, 89.50, "arun@gmail.com", "9876543210", 1, "2025-12-01", "2025-12-01 10:30:00", "Good student");
```

---

# 🟣 **Select Data**

```sql
SELECT * FROM students;
```






# _____________________________________________________
## **1️⃣ Definition**
# _____________________________________________________




**DDL (Data Definition Language)** commands define, modify, or remove **database structure** — including my, databases, indexes, and views.

It doesn’t handle *data values* — it handles *the design* (like the “blueprint” of the database).

Every DDL command is **auto-committed** → meaning once executed, changes **cannot be rolled back** (unlike DML commands).










---
# _____________________________________________________
## **2️⃣ Example Code (N+ Examples for Each DDL Command)**
# _____________________________________________________





# _____________________________________________________
### 🧱 **A. CREATE — Build new database objects**
# _____________________________________________________




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
# _____________________________________________________
### 🛠️ **B. ALTER — Modify existing database objects**
# _____________________________________________________




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
# _____________________________________________________
### 🧨 **C. DROP — Permanently delete database objects**
# _____________________________________________________





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
# _____________________________________________________
### 🧹 **D. TRUNCATE — Remove all rows but keep structure**
# _____________________________________________________





```sql
-- 1. Remove all student records, keep table
TRUNCATE TABLE students;

-- 2. Reset data for monthly logs
TRUNCATE TABLE sales_logs;

-- 3. Clear staging table before importing new data
TRUNCATE TABLE staging_orders;
```





---
# _____________________________________________________
### 🪶 **E. RENAME — Change table or database names**
# _____________________________________________________





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
# _____________________________________________________
### 🧾 **F. COMMENT — Add notes/documentation**
# _____________________________________________________





```sql
-- 1. Add comment to a table
ALTER TABLE employees COMMENT = 'Stores company employee details';

-- 2. Add comment to a column
ALTER TABLE employees MODIFY emp_name VARCHAR(100) COMMENT 'Full name of the employee';

-- 3. View table comments
SHOW TABLE STATUS LIKE 'employees';
```


# _____________________________________________________
## **6️⃣ Important Methods + Real-World Usage**
# _____________________________________________________





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



# _____________________________________________________
