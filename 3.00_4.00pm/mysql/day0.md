


# 🎓 **TEACH MODE — Why these commands? How they work?**

When we edit a table in MySQL, we actually do two things:

---

# 🧩 **PART 1: Changing Column Properties**

(Example: NOT NULL, DEFAULT, datatype)

Columns belong to the **structure** of the table.
To change a column structure → we use:

```
ALTER TABLE … MODIFY COLUMN
```

### Why?

Because MODIFY means:

> “I want to change how this column is defined.”

### Example (NOT NULL):

```sql
ALTER TABLE employees 
MODIFY id INT NOT NULL;
```

### Example (DEFAULT):

```sql
ALTER TABLE employees 
ALTER COLUMN age SET DEFAULT 18;
```

These do not affect other columns, only *column design*.

---





# 🧩 **PART 2: Changing Table-Level Rules**

(Example: PRIMARY KEY, UNIQUE, FOREIGN KEY, CHECK)

These are **constraints** applied at table level, so we use:

```
ALTER TABLE … ADD
ALTER TABLE … DROP
```

Why?

Because these are like *rules* for the entire table, not just one column.

---












# 📦 **Understanding Each Constraint With Logic**

---

## 1️⃣ **NOT NULL**

* Prevents NULL value.
* This is a **column rule**, so we MODIFY the column.

### Add NOT NULL

```sql
ALTER TABLE employees 
MODIFY age INT NOT NULL;
```

### Remove NOT NULL

```sql
ALTER TABLE employees 
MODIFY age INT NULL;
```

🧠 **Teaching tip:**
MySQL must know the datatype again → because MODIFY rewrites the column definition.

---

## 2️⃣ **DEFAULT**

* Auto-fills value when you don’t provide one.
* This is **not a strict constraint**, only a *property*.
* So we use SET DEFAULT / DROP DEFAULT.

### Add DEFAULT

```sql
ALTER TABLE employees 
ALTER COLUMN age SET DEFAULT 18;
```

### Remove DEFAULT

```sql
ALTER TABLE employees 
ALTER COLUMN age DROP DEFAULT;
```

🧠 **Teaching tip:**
DEFAULT never stops invalid values → therefore it is not a constraint.

---




Why MySQL Uses Two Keywords?
✔ MODIFY → For complete column definition rewrite
✔ ALTER COLUMN → For minor column attribute changes

(Mainly DEFAULT)


Super Simple Understanding
MODIFY = Big changes (datatype, null, auto_increment)
ALTER COLUMN = Small change (default only)








## 3️⃣ **UNIQUE**

* Ensures no duplicate values.
* This is a **table-level constraint** because MySQL creates a **unique index** behind the scenes.

### Add UNIQUE

```sql
ALTER TABLE employees
ADD CONSTRAINT uq_email UNIQUE(email);
```

### Remove UNIQUE

```sql
ALTER TABLE employees
DROP INDEX uq_email;
```

🧠 **Teaching tip:**
UNIQUE = index with uniqueness
So dropping UNIQUE means dropping index.


WHY NOT "DROP CONSTRAINT"?

Because in MySQL:

PRIMARY KEY → dropped using DROP PRIMARY KEY

FOREIGN KEY → dropped using DROP FOREIGN KEY

CHECK → dropped using DROP CHECK

UNIQUE → actually stored as an INDEX → so dropped using DROP INDEX

This is specific to MySQL (not PostgreSQL/Oracle).
















## 4️⃣ **PRIMARY KEY**

* Identifies each record uniquely.
* Combines: NOT NULL + UNIQUE
* Only one primary key allowed.

### Add PRIMARY KEY

```sql
ALTER TABLE employees
ADD PRIMARY KEY (id);
```

### Remove PRIMARY KEY

```sql
ALTER TABLE employees
DROP PRIMARY KEY;
```

🧠 **Teaching tip:**
Primary key also creates an index.
Removing it makes the table lose its main identifier.

---

## 5️⃣ **FOREIGN KEY**

* Connects two tables.
* Ensures child must match parent.

### Add FK

```sql
ALTER TABLE orders
ADD CONSTRAINT fk_orders_emp
FOREIGN KEY (emp_id)
REFERENCES employees(id)
ON DELETE CASCADE;
```

### Remove FK

```sql
ALTER TABLE orders
DROP FOREIGN KEY fk_orders_emp;
```

🧠 **Teaching tip:**
Foreign key must always have a **name**.
MySQL will not drop it without the name.

---

## 6️⃣ **CHECK** (MySQL 8+)

### Add CHECK

```sql
ALTER TABLE employees
ADD CONSTRAINT chk_age CHECK (age >= 18);
```

### Remove CHECK

```sql
ALTER TABLE employees
DROP CHECK chk_age;
```

🧠 **Teaching tip:**
Check must return TRUE, otherwise insert/update fails.

---

# 🧠 **VERY IMPORTANT SUMMARY FOR EXAMS**

| Constraint  | Why ADD / DROP? | Why MODIFY?    |
| ----------- | --------------- | -------------- |
| NOT NULL    | ❌               | ✔ column-level |
| DEFAULT     | ❌               | ✔ column-level |
| UNIQUE      | ✔ table-level   | ❌              |
| PRIMARY KEY | ✔ table-level   | ❌              |
| FOREIGN KEY | ✔ table-level   | ❌              |
| CHECK       | ✔ table-level   | ❌              |

---

# 🎯 **FINAL TEACHING MESSAGE**

* **NOT NULL** and **DEFAULT** belong to **column definition** → use MODIFY.
* **PRIMARY, UNIQUE, FOREIGN, CHECK** belong to **table rules** → use ADD/DROP.
* All changes start with `ALTER TABLE` because we are altering structure.















# _________________________________________
# ✅ **1. NOT NULL**
# _________________________________________



### **Syntax**

```sql
ALTER TABLE table_name
MODIFY column_name datatype NOT NULL;

ALTER TABLE table_name
MODIFY column_name datatype NULL;
```





### **Example**

```sql
ALTER TABLE employees
MODIFY age INT NOT NULL;

ALTER TABLE employees
MODIFY age INT NULL;
```

---




# _________________________________________
# ✅ **2. DEFAULT**
# _________________________________________




### **Syntax**

```sql
ALTER TABLE table_name
ALTER COLUMN column_name SET DEFAULT value;

ALTER TABLE table_name
ALTER COLUMN column_name DROP DEFAULT;
```

### **Example**

```sql
ALTER TABLE employees
ALTER COLUMN age SET DEFAULT 18;

ALTER TABLE employees
ALTER COLUMN age DROP DEFAULT;
```

---



“Only update the default value. No change to datatype or constraints.”
This is very lightweight and fast.
# _________________________________________
# ✅ **3. UNIQUE**
# _________________________________________




### **Syntax**

```sql
ALTER TABLE table_name
ADD CONSTRAINT constraint_name UNIQUE(column_name);

ALTER TABLE table_name
DROP INDEX constraint_name;
```

### **Example**

```sql
ALTER TABLE employees
ADD CONSTRAINT uq_email UNIQUE(email);

ALTER TABLE employees
DROP INDEX uq_email;
```

---


# _________________________________________
# ✅ **4. PRIMARY KEY**
# _________________________________________





### **Syntax**

```sql
ALTER TABLE table_name
ADD PRIMARY KEY (column_name);

ALTER TABLE table_name
DROP PRIMARY KEY;
```

### **Example**

```sql
ALTER TABLE employees
ADD PRIMARY KEY(id);

ALTER TABLE employees
DROP PRIMARY KEY;
```

---

# _________________________________________
# ✅ **5. FOREIGN KEY**
# _________________________________________




### **Syntax**

```sql
ALTER TABLE child_table
ADD CONSTRAINT fk_name 
FOREIGN KEY (child_column)
REFERENCES parent_table(parent_column);

ALTER TABLE child_table
DROP FOREIGN KEY fk_name;
```

### **Example**

```sql
ALTER TABLE orders
ADD CONSTRAINT fk_orders_emp
FOREIGN KEY (emp_id)
REFERENCES employees(id);

ALTER TABLE orders
DROP FOREIGN KEY fk_orders_emp;
```

---


# _________________________________________
# ✅ **6. CHECK** (MySQL 8+)
# _________________________________________




### **Syntax**

```sql
ALTER TABLE table_name
ADD CONSTRAINT chk_name CHECK (condition);

ALTER TABLE table_name
DROP CHECK chk_name;
```

### **Example**

```sql
ALTER TABLE employees
ADD CONSTRAINT chk_age CHECK (age >= 18);

ALTER TABLE employees
DROP CHECK chk_age;
```

---

# _________________________________________

# ⭐ SUPER SIMPLE SUMMARY
# _________________________________________




| Constraint | Add                   | Remove           |
| ---------- | --------------------- | ---------------- |
| NOT NULL   | MODIFY col NOT NULL   | MODIFY col NULL  |
| DEFAULT    | SET DEFAULT           | DROP DEFAULT     |
| UNIQUE     | ADD CONSTRAINT UNIQUE | DROP INDEX       |
| PRIMARY    | ADD PRIMARY KEY       | DROP PRIMARY KEY |
| FOREIGN    | ADD FOREIGN KEY       | DROP FOREIGN KEY |
| CHECK      | ADD CHECK             | DROP CHECK       |

---

# ⚡ **COLUMN-LEVEL VS TABLE-LEVEL**

### Column-level

```sql
age INT CHECK (age > 18)
```

### Table-level

```sql
CHECK (age > 18)
```

---

# 🛠️ **ADDING, UPDATING & DELETING CONSTRAINTS**

---

# ✅ **1️⃣ ADD CONSTRAINT (ALTER TABLE)**

### Add PRIMARY KEY

```sql
ALTER TABLE students ADD PRIMARY KEY (id);
```

### Add UNIQUE

```sql
ALTER TABLE users ADD CONSTRAINT unique_email UNIQUE (email);
```

### Add NOT NULL

```sql
ALTER TABLE employees MODIFY name VARCHAR(50) NOT NULL;
```

### Add CHECK

```sql
ALTER TABLE employees ADD CONSTRAINT check_age CHECK (age >= 18);
```

### Add DEFAULT

```sql
ALTER TABLE employees ALTER COLUMN status SET DEFAULT 'ACTIVE';
```

### Add FOREIGN KEY

```sql
ALTER TABLE orders
ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id);
```

### Add AUTO_INCREMENT

```sql
ALTER TABLE students MODIFY id INT AUTO_INCREMENT;
```

---

# ✅ **2️⃣ UPDATE / MODIFY CONSTRAINT**

> MySQL rule: **You must DROP → then ADD the updated version**

### Example: Update CHECK

```sql
ALTER TABLE employees DROP CONSTRAINT check_age;
ALTER TABLE employees ADD CONSTRAINT check_age CHECK (age >= 21);
```

### Update DEFAULT

```sql
ALTER TABLE employees ALTER COLUMN status SET DEFAULT 'INACTIVE';
```

### Change NULL → NOT NULL

```sql
ALTER TABLE employees MODIFY name VARCHAR(50) NOT NULL;
```

### Change NOT NULL → NULL

```sql
ALTER TABLE employees MODIFY name VARCHAR(50) NULL;
```

---

# ✅ **3️⃣ DELETE (DROP) CONSTRAINT**

### Drop PRIMARY KEY

```sql
ALTER TABLE students DROP PRIMARY KEY;
```

### Drop UNIQUE

```sql
ALTER TABLE users DROP INDEX unique_email;
```

### Drop NOT NULL

```sql
ALTER TABLE employees MODIFY name VARCHAR(50) NULL;
```

### Drop CHECK

```sql
ALTER TABLE employees DROP CONSTRAINT check_age;
```

### Drop DEFAULT

```sql
ALTER TABLE employees ALTER COLUMN status DROP DEFAULT;
```

### Drop FOREIGN KEY

Find FK name:

```sql
SHOW CREATE TABLE orders;
```

Drop FK:

```sql
ALTER TABLE orders DROP FOREIGN KEY fk_user;
```

### Drop AUTO_INCREMENT

```sql
ALTER TABLE students MODIFY id INT;
```

---

# 📌 **FINAL INTERVIEW NOTES (Summary Table)**

| Operation | Constraint     | Command                      |
| --------- | -------------- | ---------------------------- |
| Add       | PRIMARY KEY    | ADD PRIMARY KEY              |
| Add       | UNIQUE         | ADD CONSTRAINT … UNIQUE      |
| Add       | FOREIGN KEY    | ADD CONSTRAINT … FOREIGN KEY |
| Add       | CHECK          | ADD CONSTRAINT … CHECK       |
| Add       | NOT NULL       | MODIFY column NOT NULL       |
| Add       | DEFAULT        | ALTER COLUMN SET DEFAULT     |
| Add       | AUTO_INCREMENT | MODIFY column AUTO_INCREMENT |
| Update    | Any            | DROP → ADD again             |
| Delete    | UNIQUE         | DROP INDEX                   |
| Delete    | FOREIGN KEY    | DROP FOREIGN KEY             |
| Delete    | CHECK          | DROP CONSTRAINT              |
| Delete    | DEFAULT        | DROP DEFAULT                 |
| Delete    | NOT NULL       | MODIFY column NULL           |

---




Here is the **clear explanation** of **why you cannot DROP these constraints directly** in MySQL and **what actually happens internally** 👇

---

# ✅ **Why You CANNOT Directly DROP These Constraints in MySQL**

MySQL does **not allow dropping constraints** using simple commands like:

```sql
ALTER TABLE table_name DROP PRIMARY KEY;
ALTER TABLE table_name DROP UNIQUE;
ALTER TABLE table_name DROP CHECK;
ALTER TABLE table_name DROP NOT NULL;
```

Because of **two reasons**:

---

# 🟥 1️⃣ MySQL Treats Each Constraint Differently Internally

Each constraint type has special rules:

| Constraint      | Why you cannot drop simply                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **PRIMARY KEY** | Table MUST have a unique row identifier. Removing requires knowing which column becomes primary, or table may become unusable. |
| **UNIQUE**      | Internally stored as an INDEX. You must drop the index, not the constraint name.                                               |
| **CHECK**       | Treated as a `constraint_name`. You must drop the constraint by name.                                                          |
| **NOT NULL**    | Not a constraint — it’s a **column property**. You must modify the column, not drop a constraint.                              |

---

# 🟥 2️⃣ MySQL Syntax Does Not Support `DROP CONSTRAINT` for All Types

MySQL only allows:

* `DROP PRIMARY KEY`
* `DROP INDEX index_name`
* `DROP CHECK check_name`

But **NOT**:

* ❌ `DROP NOT NULL`
* ❌ `DROP UNIQUE`
* ❌ `DROP COLUMN constraint`

Because these are not stored as “constraints” internally.

---

# ✅ **Correct Way to Remove Each Constraint**

### 🔵 1. PRIMARY KEY → Drop like this:

```sql
ALTER TABLE employees DROP PRIMARY KEY;
```

---

### 🔵 2. UNIQUE → Drop the INDEX (because UNIQUE = index)

First find index name:

```sql
SHOW INDEXES FROM employees;
```

Then drop:

```sql
ALTER TABLE employees DROP INDEX index_name;
```

---

### 🔵 3. CHECK → Drop by constraint name

```sql
ALTER TABLE employees DROP CHECK salary_chk;
```

---

### 🔵 4. NOT NULL → Modify column

Because NOT NULL is a **column attribute**, not a constraint.

Example:

```sql
ALTER TABLE employees 
MODIFY COLUMN email VARCHAR(100) NULL;
```

---

# 🟩 **Summary Table (Very Important)**

| Constraint  | Why cannot drop directly?         | Correct way           |
| ----------- | --------------------------------- | --------------------- |
| PRIMARY KEY | Table needs unique identity       | DROP PRIMARY KEY      |
| UNIQUE      | Stored as INDEX                   | DROP INDEX index_name |
| CHECK       | Stored as constraint              | DROP CHECK check_name |
| NOT NULL    | Not a constraint, column property | MODIFY COLUMN to NULL |

---




# 🧩 **MySQL DDL Commands 
---





Great question!
Many students think **normalization = constraints**, but that is **NOT true**.

Normalization is achieved by **designing tables correctly**, not by using constraints.

Let me explain very simply:

---

# ⭐ **Normalization is a DESIGN technique — NOT a constraint**

### ✔ Normalization = How you design tables

### ✔ Constraints = Rules applied to columns

You **use constraints**, but constraints alone **cannot achieve normalization**.

---

# ⭐ **How to Achieve Normalization (Step-by-Step)**

Normalization is done by:

1. **Splitting large tables**
2. **Removing duplicate (repeating) data**
3. **Separating unrelated attributes into different tables**
4. **Creating relationships using keys**
5. **Applying constraints to keep data clean**

---

# ⭐ **STEP 1 → Apply 1NF (First Normal Form)**

**Goal: Remove repeating columns + ensure atomic values**

❌ Wrong table (Not 1NF):

| student | course1 | course2 |

✔ Fixed table (1NF):

| student | course |

👉 Achieved by TABLE DESIGN, not by constraints.

---

# ⭐ **STEP 2 → Apply 2NF (Second Normal Form)**

**Goal: No partial dependency on composite key**

Example:

**Before (Not 2NF):**

| student_id | course_id | course_name |

Here **course_name** depends only on `course_id`, not on the full composite key.

✔ Fix (2NF):

Split into:

**Courses Table**

```
course_id | course_name
```

**StudentCourse Table**

```
student_id | course_id
```

👉 Achieved by SPLITTING TABLES.

---

# ⭐ **STEP 3 → Apply 3NF (Third Normal Form)**

**Goal: No transitive dependency**

❌ Before (Not 3NF):

| emp_id | emp_name | city | pincode | state |

Here:

* city → pincode → state
  (Non-key column depends on another non-key column)

✔ Fix (3NF):

Split into:

**Employees Table**

```
emp_id | emp_name | city
```

**City Table**

```
city | pincode | state
```

👉 Achieved by TABLE RESTRUCTURING.

---

# ⭐ **So do we use constraints? YES, but not for normalization**

Constraints help after normalization:

### ✔ PRIMARY KEY

– Uniquely identifies rows
– Creates relationships

### ✔ FOREIGN KEY

– Connects normalized tables
– Enforces relationships

### ✔ UNIQUE

– Prevents duplicates

### ✔ NOT NULL

– Ensures important data is not empty

### ✔ CHECK

– Enforces valid data rules

### ✔ DEFAULT

– Sets default values

---

# ⭐ **Normalization = Table Design**

Normalization is achieved by:

* Breaking big tables into smaller ones
* Removing duplicate data
* Creating meaningful relations

**Constraints = Rules** to protect data after normalization.

---

# ⭐👉 Simple Example (Full Normalization Process)**

## ❌ Unnormalized Table:

| OrderID | CustomerName | Product1 | Product2 | City | Pincode |

---

## ✔ Apply 1NF:

Remove repeating product columns:

| OrderID | CustomerName | Product | City | Pincode |

---

## ✔ Apply 2NF:

Split customer details:

**Customers**

```
CustomerID | CustomerName | City | Pincode
```

**Orders**

```
OrderID | CustomerID
```

**OrderProducts**

```
OrderID | Product
```

---

## ✔ Apply 3NF:

Separate city details:

**City**

```
City | Pincode
```

---

# ⭐ Final Answer (Clear):

### 🔥 **Normalization is achieved through table RESTRUCTURING, not by constraints.**

### 🔥 **Constraints support normalization but do not create it.**

---

If you want, I can explain with a LIVE example using a single big table → convert to 1NF → 2NF → 3NF with diagrams.




Below is a **TEACHING-STYLE EXPLANATION** with **clear examples and tables** for every Normal Form (1NF, 2NF, 3NF, BCNF).
Very easy to understand.

---

# 🌟 **Normalization — Full Teaching Mode with Examples**

Normalization helps to:
✔ Remove duplicate data
✔ Avoid update/delete anomalies
✔ Make the database clean and efficient

We will take **one raw (bad) table** and fix it step-by-step for each normal form.

---

# 🟥 **RAW UNNORMALIZED TABLE (UNF)**

**Problem Table: `orders_raw`**

| OrderID | CustomerName | Items Purchased     | Item Prices |
| ------- | ------------ | ------------------- | ----------- |
| 101     | Arjun        | Pen, Pencil, Eraser | 10, 5, 3    |
| 102     | Divya        | Notebook, Pen       | 50, 10      |

❌ Issues:

* Multiple values in the same column
* Repeating groups
* Hard to calculate totals
* Cannot search price of a single item

---

# 🟦 **1NF (First Normal Form) — Remove multi-valued columns**

**Rule:**
✔ All values must be **atomic** (single value)
✔ No repeating groups

---

## ✅ **1NF Converted Table: `orders_1nf`**

| OrderID | CustomerName | Item     | ItemPrice |
| ------- | ------------ | -------- | --------- |
| 101     | Arjun        | Pen      | 10        |
| 101     | Arjun        | Pencil   | 5         |
| 101     | Arjun        | Eraser   | 3         |
| 102     | Divya        | Notebook | 50        |
| 102     | Divya        | Pen      | 10        |

✔ Now every row is atomic
❌ Still has redundancy (customer repeats)

---

# 🟩 **2NF (Second Normal Form) — Remove Partial Dependency**

**Rule:**
✔ Must be in 1NF
✔ No dependency on **part of a composite key**

Here **composite key = (OrderID, Item)**
But **CustomerName** depends only on **OrderID**, not on Item.
👉 That's partial dependency.

### 🔧 Fix: Split into two tables

---

## ✅ **Table 1: `orders`** (Order-level data)

| OrderID | CustomerName |
| ------- | ------------ |
| 101     | Arjun        |
| 102     | Divya        |

---

## ✅ **Table 2: `order_items`** (Item-level data)

| OrderID | Item     | ItemPrice |
| ------- | -------- | --------- |
| 101     | Pen      | 10        |
| 101     | Pencil   | 5         |
| 101     | Eraser   | 3         |
| 102     | Notebook | 50        |
| 102     | Pen      | 10        |

✔ No partial dependencies
❌ Still item price depends on Item (repeated)

---

# 🟨 **3NF (Third Normal Form) — Remove Transitive Dependency**

**Rule:**
✔ Must be in 2NF
✔ No **non-key column** depends on another **non-key column**

In `order_items` table:

* ItemPrice depends on Item
* Item is not a key
  👉 This is **transitive dependency**

### 🔧 Fix: Separate items into another table

---

## ✅ **Table 1: `orders`**

| OrderID | CustomerName |
| ------- | ------------ |
| 101     | Arjun        |
| 102     | Divya        |

---

## ✅ **Table 2: `order_items`**

| OrderID | ItemID |
| ------- | ------ |
| 101     | 1      |
| 101     | 2      |
| 101     | 3      |
| 102     | 4      |
| 102     | 1      |

---

## ✅ **Table 3: `items`**

| ItemID | ItemName | Price |
| ------ | -------- | ----- |
| 1      | Pen      | 10    |
| 2      | Pencil   | 5     |
| 3      | Eraser   | 3     |
| 4      | Notebook | 50    |

✔ No transitive dependencies
✔ Perfect relational design

---

# 🟧 **BCNF (Boyce-Codd Normal Form)**

**Rule:**
✔ For every functional dependency,
**LHS MUST be a candidate key**

### Example Problem

| Teacher | Subject |
| ------- | ------- |
| Ram     | Maths   |
| Ram     | Physics |
| Lakshmi | Science |

Dependency:

* One teacher teaches many subjects
* One subject is taught by only one teacher
  👉 FD: **Subject → Teacher**
  But **Subject** is not a key → violates BCNF

### 🔧 Fix BCNF: Split tables

## Table 1: `teachers`

| TeacherID | TeacherName |
| --------- | ----------- |
| 1         | Ram         |
| 2         | Lakshmi     |

## Table 2: `subjects`

| SubjectID | SubjectName | TeacherID |
| --------- | ----------- | --------- |
| 1         | Maths       | 1         |
| 2         | Physics     | 1         |
| 3         | Science     | 2         |

✔ Now every determinant is a key
✔ Fully normalized

---

# 🎉 **Summary Table**

| Normal Form | What It Fixes           | Example Fix                  |
| ----------- | ----------------------- | ---------------------------- |
| **1NF**     | Multi-values            | Multiple items → Single rows |
| **2NF**     | Partial dependencies    | CustomerName separated       |
| **3NF**     | Transitive dependencies | Item price separated         |
| **BCNF**    | More strict key rules   | Teacher–Subject split        |

---

If you want, I can also provide:

📌 ER Diagram for all Normal Forms
📌 SQL commands to create these tables
📌 Real-time company example (billing, e-commerce, HR)

Just tell me!
