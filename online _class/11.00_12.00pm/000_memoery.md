

# 🔥 **Types of Operators in Python**

Python has **7 major types** of operators:

1. **Arithmetic Operators**
2. **Assignment Operators**
3. **Comparison (Relational) Operators**
4. **Logical Operators**
5. **Bitwise Operators**
6. **Membership Operators**
7. **Identity Operators**

Let’s go one by one with examples.

---

# 1️⃣ **Arithmetic Operators**

Used for mathematical calculations.

| Operator | Meaning             | Example   | Output |
| -------- | ------------------- | --------- | ------ |
| `+`      | Addition            | `10 + 5`  | 15     |
| `-`      | Subtraction         | `10 - 5`  | 5      |
| `*`      | Multiplication      | `10 * 5`  | 50     |
| `/`      | Division (float)    | `10 / 4`  | 2.5    |
| `//`     | Floor Division      | `10 // 4` | 2      |
| `%`      | Modulus (remainder) | `10 % 4`  | 2      |
| `**`     | Exponent            | `2 ** 3`  | 8      |

---

# 2️⃣ **Assignment Operators**

Used to assign values, update values.

| Operator | Meaning                 | Example              |
| -------- | ----------------------- | -------------------- |
| `=`      | Assign                  | `x = 5`              |
| `+=`     | Add and assign          | `x += 3` (x = x + 3) |
| `-=`     | Subtract and assign     | `x -= 3`             |
| `*=`     | Multiply and assign     | `x *= 3`             |
| `/=`     | Divide and assign       | `x /= 3`             |
| `//=`    | Floor divide and assign | `x //= 3`            |
| `%=`     | Modulo and assign       | `x %= 3`             |
| `**=`    | Power and assign        | `x **= 3`            |

---

# 3️⃣ **Comparison (Relational) Operators**

Returns **True/False**.

| Operator | Meaning          | Example         |
| -------- | ---------------- | --------------- |
| `==`     | Equal            | `5 == 5` → True |
| `!=`     | Not equal        | `5 != 3` → True |
| `>`      | Greater than     | `5 > 3` → True  |
| `<`      | Less than        | `5 < 3` → False |
| `>=`     | Greater or equal | `5 >= 5` → True |
| `<=`     | Less or equal    | `3 <= 5` → True |

---

# 4️⃣ **Logical Operators**

Used with conditions.

| Operator | Meaning           | Example           | Output |
| -------- | ----------------- | ----------------- | ------ |
| `and`    | Both must be True | `5 > 2 and 3 > 1` | True   |
| `or`     | At least one True | `5 > 10 or 3 > 1` | True   |
| `not`    | Reverse result    | `not(5 > 2)`      | False  |

---

# 5️⃣ **Bitwise Operators**

Works on bits (0s and 1s).

Let `a = 6 (110)` and `b = 5 (101)`.

| Operator | Meaning     | Example  | Binary     | Output  |     |     |         |
| -------- | ----------- | -------- | ---------- | ------- | --- | --- | ------- |
| `&`      | AND         | `6 & 5`  | 110 & 101  | 100 (4) |     |     |         |
| `        | `           | OR       | `6         | 5`      | 110 | 101 | 111 (7) |
| `^`      | XOR         | `6 ^ 5`  | 110 ^ 101  | 011 (3) |     |     |         |
| `~`      | NOT         | `~6`     | ---        | -7      |     |     |         |
| `<<`     | Left shift  | `5 << 1` | 101 → 1010 | 10      |     |     |         |
| `>>`     | Right shift | `5 >> 1` | 101 → 10   | 2       |     |     |         |

---

# 6️⃣ **Membership Operators**

Checks if a value exists in a sequence (`list`, `string`, `tuple`).

| Operator | Meaning           | Example                   |
| -------- | ----------------- | ------------------------- |
| `in`     | Value present     | `"a" in "apple"` → True   |
| `not in` | Value not present | `3 not in [1,2,4]` → True |

---

# 7️⃣ **Identity Operators**

Checks if two variables refer to **same memory location**.

| Operator | Meaning         | Example      |
| -------- | --------------- | ------------ |
| `is`     | Same object     | `x is y`     |
| `is not` | Not same object | `x is not y` |

Example:

```python
a = [1,2,3]
b = [1,2,3]
c = a

# print(a is b)   # False (different memory)
# print(a is c)   # True  (same memory)
# ```

# ---

# # ⭐ Want a **diagram / PDF notes** for this?

I can generate:

✅ Colored table
✅ Full chapter notes
✅ Diagram of operator types

Just tell me: **"Make PDF notes"** or **"Give diagram"**.










#  Key Components of Python Memory Management


#______________________________________________________________________
# Memory Allocation

# Python divides memory into:



# Stack Memory: For static memory allocation (e.g., function calls, local variables).
# Heap Memory: For dynamic memory allocation (e.g., objects, data structures).

#Python’s memory manager handles the allocation of heap memory automatically.




# Private Heap Space
       # All Python objects and data structures are stored in a private heap.
       # This is managed by Python and not accessible directly to programmers.
       # The interpreter manages memory blocks within this heap.

# Garbage Collection
      # Python uses a garbage collector to free up memory from objects no longer in use.
      # Uses reference counting as the primary technique.
      # Also uses generational garbage collection to handle cyclic references (where two or more objects refer to each other).




# | Feature         | Stack Memory                                | Heap Memory                               |
# | --------------- | ------------------------------------------- | ----------------------------------------- |
# | Used For        | Function calls, local variables             | Objects, class instances, data structures |
# | Lifetime        | Temporary — lasts during function execution | Long-lived — until reference count = 0    |
# | Managed By      | Compiler/interpreter                        | Python memory manager & garbage collector |
# | Access Speed    | Fast (due to LIFO structure)                | Slower than stack                         |
# | Allocation Type | Static                                      | Dynamic                                   |



| Concept                | Description                                   |
| ---------------------- | --------------------------------------------- |
| Reference Counting     | Tracks how many references point to an object |
| Garbage Collection     | Reclaims memory from unreferenced objects     |
| Private Heap           | Storage for all Python objects                |
| PyMalloc               | Memory pool for small object allocation       |
| `gc` Module            | Interface to garbage collector                |
| `sys.getrefcount(obj)` | Shows reference count of an object            |





#_______________________________________________________________________



 Memory Storage of Variables in Python

1.Normal (Primitive) Variables
       Examples: integers, floats, strings, booleans

Stored in:

     Stack: Reference (name)
     Heap:  Actual object/data (in most cases)

Example:


x = 5
y = "hello"


`x` → reference on the stack → points to `5` in heap
`y` → reference on the stack → points to `"hello"` in heap

> 🔸 In CPython, **small integers (-5 to 256)** and some **strings** are **interned** (cached), so they may be shared in memory.


#_______________________________________________________________________

2. Complex Data (Lists, Dicts, Sets, Tuples, Custom Objects)

>Reference is stored in the stack
>Object is stored in the heap



Example:


a = [1, 2, 3]
b = {'key': 'value'}


* `a` → stack
* `[1, 2, 3]` → heap

* `b` → stack
* `{'key': 'value'}` → heap



#_______________________________________________________________________

#3. Function Variables (Local Scope)*

* Local variables are created on the **stack** during function calls.
* If they refer to complex data, the data is stored in the **heap**.


def my_func():
    x = 42             # stack
    y = [1, 2, 3]       # y (stack), list (heap)


* After function ends, the **stack frame is destroyed**.
* Heap data (`[1, 2, 3]`) is cleaned up only when no references remain.



#_______________________________________________________________________

4. **Global and Module-Level Variables**

* Names are stored in the **global namespace** (like a dictionary).
* Data they point to is still in the **heap**.


global_var = "I'm global"




#_______________________________________________________________________


## How Python Manages All This

* Python uses **reference counting** and a **garbage collector**:

  * When reference count drops to 0, memory is freed.
  * Circular references are handled by the garbage collector.



# Quick Summary

| Variable Type   | Stored In Stack? | Stored In Heap? |
| --------------- | ---------------- | --------------- |
| `int`, `float`  | ✅ (reference)    | ✅ (value)       |
| `str`           | ✅                | ✅               |
| `list`, `dict`  | ✅                | ✅               |
| custom objects  | ✅                | ✅               |
| function locals | ✅                | ✅ (if complex)  |
| global vars     | ✅ (global table) | ✅               |



#_______________________________________________________________________


What is an Object?

    An object in Python is a block of memory that contains:

    Type – What kind of object it is (int, str, list, etc.)

    Value – The actual data the object holds (like 5, "hello", etc.)

    ID (Address) – A unique identifier for the object in memory (what id(obj) returns)

    Reference Count – How many variables are pointing to it



x = 5
5 is an object of type int

x is a variable (reference) pointing to that object

The object 5 lives in heap memory, and x holds a reference to it in the stack

#_____________________________________

a = [10, 20, 30]



         Stack                   Heap
       ─────────           ───────────────────
       a ─────────►   ┌───▶ [10, 20, 30] (list object)
                      │
                    [Ref Count = 1]



#________________________________________________________

b = a


         Stack                   Heap
       ─────────           ───────────────────
       a ─────┐
              └─────► [10, 20, 30] (Ref Count = 2)
       b ─────┘

#_____________________________________________________________
          ┌─────────────────────────────┐
          │        Python Program       │
          └────────────┬────────────────┘
                       │
          ┌────────────▼────────────┐
          │     Memory Management   │
          └──────┬────────┬─────────┘
                 │        │
     ┌───────────▼──┐ ┌───▼───────────────────────┐
     │   Stack      │ │        Heap               │
     │ (Function    │ │  (Private memory for all  │
     │  calls,      │ │   objects & data)         │
     │  variables)  │ │                           │
     └──────────────┘ └────┬────────────┬─────────┘
                           │            │
               ┌──────────▼─┐   ┌───────▼──────────┐
               │ References │   │ Objects (lists,  │
               │ (pointers) │   │ dicts, strings)  │
               └────────────┘   └──────────────────┘
Variables live in the stack, but they point to actual objects stored in the heap.



#__________________________________________________________________


What is the role of the private heap in Python?

Explain reference counting. How does it work in Python?

What is cyclic reference? How does Python handle it?

Differentiate between stack and heap memory.

When would you use gc.collect() manually?

Is Python memory management fully automatic? Explain.



#_____________________________________________________________


https://www.cs.toronto.edu/~david/course-notes/csc110-111/06-memory-model/04-python-memory-model-1.html













MySQL



| Operation     | Command Example                                 |
| ------------- | ----------------------------------------------- |
| View Columns  | `DESCRIBE table_name;`                          |
| Add Column    | `ADD column_name TYPE DEFAULT ...;`             |
| Modify Column | `MODIFY column_name TYPE NOT NULL DEFAULT ...;` |
| Drop Column   | `DROP COLUMN column_name;`                      |
| Rename Column | `CHANGE old_name new_name TYPE;`                |
| Rename Table  | `RENAME TABLE old_name TO new_name;`            |



| Constraint    | Syntax Example                                               |
| ------------- | ------------------------------------------------------------ |
| `NOT NULL`    | `ADD Gender VARCHAR(10) NOT NULL`                            |
| `DEFAULT`     | `ADD Gender VARCHAR(10) DEFAULT 'Unknown'`                   |
| `CHECK`       | `ADD Gender VARCHAR(10) CHECK (Gender IN ('Male','Female'))` |
| `UNIQUE`      | `ADD Gender VARCHAR(10) UNIQUE`                              |
| `PRIMARY KEY` | `ADD Gender VARCHAR(10) PRIMARY KEY`                         |



| Task                            | Command Example                      |
| ------------------------------- | ------------------------------------ |
| Modify column type + constraint | `MODIFY Age INT NOT NULL;`           |
| Rename column + modify          | `CHANGE Age age INT NOT NULL;`       |
| Modify with default             | `MODIFY Age INT NOT NULL DEFAULT 0;` |
| Add new column                  | `ADD NewCol VARCHAR(50);`            |






-- Add
ALTER TABLE employees ADD CONSTRAINT unique_email UNIQUE (email);

-- Drop
ALTER TABLE employees DROP INDEX unique_email;

-- Modify (drop and re-add)
ALTER TABLE employees DROP CHECK chk_salary;
ALTER TABLE employees ADD CONSTRAINT chk_salary CHECK (salary >= 1000);




| Constraint Type                                 | Syntax Used                | Why?                     |
| ----------------------------------------------- | -------------------------- | ------------------------ |
| `NOT NULL`                                      | `MODIFY`                   | Alters column definition |
| `DEFAULT`                                       | `MODIFY` or `ALTER COLUMN` | Alters column default    |
| `UNIQUE`, `CHECK`, `FOREIGN KEY`, `PRIMARY KEY` | `ADD CONSTRAINT`           | Treated as named objects |





| SQL Statement                      | Valid?   | Why?                                                         |
| ---------------------------------- | -------- | ------------------------------------------------------------ |
| `MODIFY COLUMN day INT NOT NULL`   | ✅        | Correct way to alter a column to make it NOT NULL.           |
| `ADD CONSTRAINT ... NOT NULL (ID)` | ❌        | `NOT NULL` is not a named constraint; must use `MODIFY`.     |
| `ADD Gender VARCHAR(10) NOT NULL`  | ⚠️ Maybe | Works only if table is empty or a default value is provided. |



| Constraint Type | Can use `ADD CONSTRAINT`? | Why?                                                 |
| --------------- | ------------------------- | ---------------------------------------------------- |
| `PRIMARY KEY`   | ✅ Yes                     | Named object; table-level; can span multiple columns |
| `FOREIGN KEY`   | ✅ Yes                     | Named object; references other tables                |
| `UNIQUE`        | ✅ Yes                     | Named index; can be standalone or table-level        |
| `CHECK`         | ✅ Yes (MySQL 8+)          | Table-level logical rule                             |
| `NOT NULL`      | ❌ No                      | Part of column definition only                       |
| `DEFAULT`       | ❌ No                      | Stored as column-level default                       |


NOT NULL is like an internal setting on a device (per column) — you configure it individually.

FOREIGN KEY, UNIQUE, etc., are like external plugs (constraints) you attach to a system — they can be labeled and connected across the system.










#______________________________________________________________________________________________________







+------------------+---------------------------+-------------------------+--------------------------+
| Constraint Type  | Column-Level Allowed?     | Table-Level Allowed?    | Can Use ADD CONSTRAINT? |
+------------------+---------------------------+-------------------------+--------------------------+
| NOT NULL         | ✅ Yes (use MODIFY)        | ❌ No                   | ❌ No                   |
| DEFAULT          | ✅ Yes (use MODIFY)        | ❌ No                   | ❌ No                   |
| UNIQUE           | ✅ Yes                     | ✅ Yes                  | ✅ Yes                  |
| PRIMARY KEY      | ✅ Yes (1 col only)        | ✅ Yes (multi-col)      | ✅ Yes                  |
| FOREIGN KEY      | ❌ No (must be table-level)| ✅ Yes                  | ✅ Yes                  |
| CHECK            | ✅ Yes (MySQL 8.0+)        | ✅ Yes                  | ✅ Yes (MySQL 8.0+)     |
+------------------+---------------------------+-------------------------+--------------------------+








| Task                         | Correct Syntax Example                                                                      |
| ---------------------------- | ------------------------------------------------------------------------------------------- |
| Add NOT NULL                 | `ALTER TABLE users MODIFY name VARCHAR(100) NOT NULL;`                                      |
| Add DEFAULT                  | `ALTER TABLE users MODIFY age INT DEFAULT 18;`  


                                            
| Add UNIQUE                   | `ALTER TABLE users ADD CONSTRAINT unique_email UNIQUE (email);`                             |
| Add PRIMARY KEY (single col) | `ALTER TABLE users ADD PRIMARY KEY (user_id);`                                              |
| Add PRIMARY KEY (multi-col)  | `ALTER TABLE orders ADD PRIMARY KEY (order_id, product_id);`                                |
| Add FOREIGN KEY              | `ALTER TABLE orders ADD CONSTRAINT fk_cust FOREIGN KEY (cust_id) REFERENCES customers(id);` |
| Add CHECK                    | `ALTER TABLE employees ADD CONSTRAINT chk_salary CHECK (salary > 0);`   


                    |

| Drop UNIQUE                  | `ALTER TABLE users DROP INDEX unique_email;`                                                |
| Drop FOREIGN KEY             | `ALTER TABLE orders DROP FOREIGN KEY fk_cust;`                                              |
| Drop CHECK                   | `ALTER TABLE employees DROP CHECK chk_salary;`                                              |
| Drop PRIMARY KEY             | `ALTER TABLE users DROP PRIMARY KEY;`                                                       |





Error Code: 1138. Invalid use of NULL value
This means there are still NULL values in city_id, so you cannot apply NOT NULL.


| Goal                            | Use                                  |
| ------------------------------- | ------------------------------------ |
| Insert or update safely         | `INSERT ... ON DUPLICATE KEY UPDATE` |
| Fully replace a row (rare case) | `REPLACE INTO`                       |



| Feature                | `CREATE TABLE AS`              | `CREATE TABLE LIKE` |
| ---------------------- | ------------------------------ | ------------------- |
| Copies data            | ✅ Yes                          | ❌ No                |
| Copies structure       | ✅ Basic (column names & types) | ✅ Full structure    |
| Copies constraints     | ❌ No                           | ✅ Yes               |
| Copies indexes         | ❌ No                           | ✅ Yes               |
| Copies AUTO\_INCREMENT | ❌ No                           | ✅ Yes               |



-- Copies structure + data (but no keys or constraints)
CREATE TABLE employees_backup AS SELECT * FROM employees;

-- Copies only structure (with keys, constraints, etc.)
CREATE TABLE employees_clone LIKE employees;






| Feature        | **TABLE**                        | **VIEW**                                       |
| -------------- | -------------------------------- | ---------------------------------------------- |
| Definition     | A **physical** storage structure | A **virtual** table based on a query           |
| Data stored    | ✅ Yes (stored on disk)           | ❌ No (only the query is stored)                |
| Update support | ✅ Yes                            | ⚠️ Sometimes (if it's updatable)               |
| Use case       | Store real, persistent data      | Present filtered/combined data from tables     |
| Performance    | ✅ Faster (data is materialized)  | ❌ Slower (runs the underlying query each time) |
| Maintenance    | Needs explicit updates           | Auto-updates as source tables change           |



✅ Purpose:
The INFORMATION_SCHEMA is a read-only database in SQL-compliant systems (like MySQL, PostgreSQL, SQL Server) that provides metadata about the database objects such as:

Tables

Columns

Views

Indexes

Constraints

Users

Privileges

📘 Think of it as:
"A database about your databases."


SELECT schema_name 
FROM INFORMATION_SCHEMA.SCHEMATA;




| Feature                   | `INSERT INTO ... VALUES`            | `INSERT INTO ... SELECT`           |
| ------------------------- | ----------------------------------- | ---------------------------------- |
| Data Source               | Direct/manual input                 | From another table or query result |
| Inserts multiple rows?    | ✅ Yes (with multiple `VALUES` sets) | ✅ Yes (depends on `SELECT` result) |
| Use Case                  | Add known, specific data            | Copy or transform existing data    |
| Requires `SELECT` clause? | ❌ No                                | ✅ Yes                              |





| Feature                    | `DELETE`                                    | `TRUNCATE`                                 | `DROP`                                    |
| -------------------------- | ------------------------------------------- | ------------------------------------------ | ----------------------------------------- |
| **Purpose**                | Deletes **some or all rows** from a table   | Deletes **all rows** from a table          | Deletes the **entire table structure**    |
| **Can filter rows?**       | ✅ Yes, using `WHERE`                        | ❌ No, deletes all rows                     | ❌ No                                      |
| **Syntax**                 | `DELETE FROM table WHERE condition;`        | `TRUNCATE TABLE table;`                    | `DROP TABLE table;`                       |
| **Rollback (Undo)?**       | ✅ Yes, if within a transaction (InnoDB)     | ❌ No (in most databases; it's auto-commit) | ❌ No (immediate and permanent)            |
| **Speed**                  | Slower (row-by-row deletion, logs each row) | Faster (bulk operation, minimal logging)   | Fastest (just removes the table)          |
| **Affects structure?**     | ❌ No (only data)                            | ❌ No (only data)                           | ✅ Yes (structure + data gone)             |
| **Triggers invoked?**      | ✅ Yes (BEFORE/AFTER DELETE triggers)        | ❌ No                                       | ❌ No                                      |
| **Resets auto-increment?** | ❌ No (unless explicitly)                    | ✅ Yes (auto-increment counter resets)      | ✅ Yes (table is gone, so counter is gone) |


| Command  | Data Deleted? | Table Structure Deleted? | Conditional Deletion? | Can Rollback? | Resets Auto-Increment? |
| -------- | ------------- | ------------------------ | --------------------- | ------------- | ---------------------- |
| DELETE   | ✅ Yes         | ❌ No                     | ✅ Yes (WHERE)         | ✅ Yes         | ❌ No                   |
| TRUNCATE | ✅ Yes (All)   | ❌ No                     | ❌ No                  | ❌ No          | ✅ Yes                  |
| DROP     | ✅ Yes         | ✅ Yes                    | ❌ No                  | ❌ No          | ✅ Yes                  |


| Situation                | Use Command           |
| ------------------------ | --------------------- |
| Delete specific records? | `DELETE` with `WHERE` |
| Empty a table quickly?   | `TRUNCATE`            |
| Remove entire table?     | `DROP`                |



#_________________________________________________________________________________



#Section 1: DDL (Data Definition Language) Questions

##Conceptual Questions**

1. What is DDL? Name some DDL commands.
2. What is the difference between `DROP`, `DELETE`, and `TRUNCATE`?
3. What is the difference between `PRIMARY KEY` and `UNIQUE`?
4. What is the use of `AUTO_INCREMENT` in MySQL?
5. What is the difference between `CHAR` and `VARCHAR` data types?
6. What are the different types of constraints in MySQL?
7. How would you modify an existing column’s data type in a table?
9. Explain the purpose of the `INFORMATION_SCHEMA` database.
10. What is the difference between a `VIEW` and a `TABLE`?

##Query-Based DDL Questions**

1. Write a query to create a table called `employees` with the following fields:

   * id (primary key, auto-increment)
   * name (varchar 50)
   * department (varchar 30)
   * salary (float)

2. Write a query to add a new column `email` (VARCHAR(100)) to the `employees` table.

3. Write a query to rename the column `department` to `dept_name`.

4. Write a query to change the datatype of the column `salary` to `DECIMAL(10,2)`.

5. Write a query to drop the `email` column from the `employees` table.

6. Write a query to drop the `employees` table only if it exists.

---

#Section 2: DML (Data Manipulation Language) Questions

#Conceptual Questions

1. What is DML? Name common DML operations.

2. What’s the difference between `UPDATE` and `REPLACE`?

3. How does `DELETE` differ from `TRUNCATE` in terms of performance and rollback?

4. What is the difference between `INSERT INTO ... VALUES` and `INSERT INTO ... SELECT`?

5. What happens if you omit the `WHERE` clause in a `DELETE` or `UPDATE` statement?


DECIMAL(precision, scale)
precision: Total number of digits.

scale: Number of digits after the decimal point.



Query-Based DML Questions

1. Write a query to insert a new employee named “John” in the `employees` table with a salary of 50000 and department “IT”.

2. Write a query to increase the salary of all employees in the “HR” department by 10%.

3. Write a query to delete all employees who belong to the “Sales” department.

4. Write a query to update the name of the employee with id 3 to “Alice”.

5. Write a query to copy all data from the `employees` table into a new table `employees_backup`.

6. Write a query to insert multiple rows into the `employees` table using a single statement.



# Bonus Practice Task

* Create a table for a **Bookstore** with fields for `book_id`, `title`, `author`, `price`, and `category`.
* Insert 5 sample books into it.
* Write a query to:

  * Increase all book prices by 15%
  * Change the category of all books written by “Rowling” to “Fantasy”
  * Delete all books priced under 200



#_______________________________________________________________________________


| DBMS       | Can use auto-increment without PK? | Requirement                                          |
| ---------- | ---------------------------------- | ---------------------------------------------------- |
| MySQL      | ✅ Yes                              | Must be at least `UNIQUE`                            |
| PostgreSQL | ✅ Yes                              | Can use `SERIAL` or `GENERATED` freely               |
| SQLite     | ❌ No                               | Auto-increment only works with `INTEGER PRIMARY KEY` |



A VARCHAR cannot be auto-incremented directly because auto-increment is only supported for integer types. However, you can simulate auto-increment for a VARCHAR column using a stored procedure or trigger that:

Retrieves the last inserted value.

Increments the numeric part.

Concatenates it with a prefix.

Inserts the new row.




DELIMITER $$

CREATE PROCEDURE insert_employee (
    IN emp_name VARCHAR(100),
    IN emp_dept VARCHAR(50),
    IN emp_salary DECIMAL(10,2)
)
BEGIN
    DECLARE new_id VARCHAR(10);
    DECLARE last_id INT;

    SELECT IFNULL(MAX(CAST(SUBSTRING(employee_id, 4) AS UNSIGNED)), 0)
    INTO last_id
    FROM employees;

    SET last_id = last_id + 1;
    SET new_id = CONCAT('EMP', LPAD(last_id, 3, '0'));

    INSERT INTO employees (employee_id, name, department, salary)
    VALUES (new_id, emp_name, emp_dept, emp_salary);
END$$

DELIMITER ;





#__________________________________________________________________


2. GROUP BY
Used for: Grouping rows based on one or more columns.

When: Comes after WHERE and before HAVING.

Where: Works on selected rows after filtering.

Why: To aggregate values per group (e.g., sum, avg, count).


SELECT department, COUNT(*) FROM employees
WHERE salary > 50000
GROUP BY department;


#______________________________________________________________________________

3. HAVING
Used for: Filtering groups after aggregation.

When: After GROUP BY.

Where: Applies to aggregated results.

Why: WHERE cannot be used for aggregate functions like SUM(), AVG(), etc.


SELECT department, COUNT(*) as total
FROM employees
GROUP BY department
HAVING total > 5;


#_______________________________________________





| Clause        | Purpose                                       | Applies To              | Position in Query     | Aggregate?             |
| ------------- | --------------------------------------------- | ----------------------- | --------------------- | ---------------------- |
| `SELECT`      | Choose which columns or expressions to return | Columns or expressions  | 1st (after `FROM`)    | ✅ (can use COUNT, SUM) |
| `FROM`        | Specify the table(s) to query from            | Tables                  | After `SELECT`        | ❌                      |
| `WHERE`       | Filter rows before grouping/aggregation       | Individual rows         | After `FROM`          | ❌                      |
| `GROUP BY`    | Group rows to apply aggregate functions       | Group columns           | After `WHERE`         | ❌ (prepares for agg.)  |
| `HAVING`      | Filter groups after aggregation               | Aggregated groups       | After `GROUP BY`      | ✅                      |
| `ORDER BY`    | Sort the result set                           | Final result rows       | Last                  | ✅/❌                    |
| `LIMIT`       | Limit number of rows returned                 | Final result            | Very last             | ❌                      |
| `JOIN`        | Combine rows from multiple tables             | Tables                  | After `FROM`          | ❌                      |
| `ON`          | Join condition for tables                     | Join conditions         | With `JOIN`           | ❌                      |
| `AS`          | Rename columns or tables                      | Aliases                 | In `SELECT` or `FROM` | ❌                      |
| `DISTINCT`    | Remove duplicate rows                         | Selected rows           | After `SELECT`        | ❌                      |
| `IN`          | Match a value against a list or subquery      | In `WHERE`, `HAVING`    | With conditions       | ❌                      |
| `BETWEEN`     | Check if value lies within a range            | In `WHERE`, `HAVING`    | With conditions       | ❌                      |
| `LIKE`        | Pattern matching                              | In `WHERE`, `HAVING`    | With conditions       | ❌                      |
| `IS NULL`     | Check for NULL values                         | In `WHERE`, `HAVING`    | With conditions       | ❌                      |
| `CASE...WHEN` | Conditional logic                             | In `SELECT`, `ORDER BY` | Inside expressions    | ✅/❌                    |
| `UNION`       | Combine results of two queries                | Two result sets         | After both queries    | ❌                      |
| `EXISTS`      | Check if subquery returns rows                | In `WHERE`              | With subqueries       | ❌                      |
| `ALL`, `ANY`  | Compare values with subquery results          | In conditions           | With operators        | ❌                      |





 Suggested Order of SQL Execution:
FROM (and JOIN)

WHERE

GROUP BY

HAVING

SELECT

DISTINCT

ORDER BY

LIMIT



SELECT department, COUNT(*) AS emp_count
FROM employees
WHERE salary > 50000
GROUP BY department
HAVING COUNT(*) > 2
ORDER BY emp_count DESC
LIMIT 5;




| Step | Clause     | Explanation                                                                 |
| ---- | ---------- | --------------------------------------------------------------------------- |
| 1️⃣  | `FROM`     | Pulls data from the `employees` table.                                      |
| 2️⃣  | `WHERE`    | Filters only those employees where `salary > 50000`.                        |
| 3️⃣  | `GROUP BY` | Groups the remaining records by `department`.                               |
| 4️⃣  | `HAVING`   | Filters out groups where the number of employees is **not greater than 2**. |
| 5️⃣  | `SELECT`   | Selects the `department` name and the count of employees in that group.     |
| 6️⃣  | `ORDER BY` | Sorts the result based on the `emp_count` column in **descending order**.   |
| 7️⃣  | `LIMIT`    | Returns only the **top 5 departments** from the sorted list.                |




SELECT ...
FROM ...
WHERE ...
GROUP BY ...
HAVING ...
ORDER BY ...
LIMIT ...



SELECT category, AVG(price) AS avg_price
FROM products
WHERE stock > 0
GROUP BY category
HAVING AVG(price) > 100
ORDER BY avg_price DESC
LIMIT 3;


What it does:
Gets products in stock (WHERE)

Groups them by category (GROUP BY)

Filters those with average price > 100 (HAVING)

Displays the top 3 categories with the highest average price (ORDER BY, LIMIT)
_____________________________________



| Function/Concept    | Use Case                  |
| ------------------- | ------------------------- |
| `input()`           | Read user input           |
| `print()`           | Display output            |
| `str.format()`      | Format strings            |
| `f"{}` syntax\`     | Modern string formatting  |
| `open()`            | File read/write           |
| `split()` + `map()` | Process multiple inputs   |
| `sys.stdin.read()`  | Multi-line or large input |
| `flush=True`        | Real-time console output  |


| Format Type             | Syntax (f-string / `format`) | `%` Syntax  | Description                    | Example Output                     |
| ----------------------- | ---------------------------- | ----------- | ------------------------------ | ---------------------------------- |
| **Integer**             | `{:d}`                       | `%d`        | Decimal integer                | `f"{42:d}"` → `42`                 |
| **Float**               | `{:.2f}`                     | `%.2f`      | Float with 2 decimal places    | `f"{3.14159:.2f}"` → `3.14`        |
| **String**              | `{:s}`                       | `%s`        | String                         | `f"{'Hello':s}"` → `Hello`         |
| **Right Align**         | `{:>10}`                     | `%10s`      | Right-align in 10 spaces       | `f"{'Hi':>10}"` → `'        Hi'`   |
| **Left Align**          | `{:<10}`                     | `%-10s`     | Left-align in 10 spaces        | `f"{'Hi':<10}"` → `'Hi        '`   |
| **Center Align**        | `{:^10}`                     | N/A         | Center-align in 10 spaces      | `f"{'Hi':^10}"` → `'    Hi    '`   |
| **Zero Padding**        | `{:05d}`                     | `%05d`      | Pad integer with leading zeros | `f"{42:05d}"` → `00042`            |
| **Thousands Separator** | `{:,.2f}`                    | N/A         | Format number with commas      | `f"{12345.678:.2f}"` → `12,345.68` |
| **Hexadecimal**         | `{:x}` / `{:X}`              | `%x` / `%X` | Integer to hexadecimal         | `f"{255:x}"` → `ff`                |
| **Percentage**          | `{:.0%}`                     | N/A         | Convert float to percentage    | `f"{0.75:.0%}"` → `75%`            |




# 1.Arithmetic Operators

| Operator | Description         | Example  | Result |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `5 + 3`  | `8`    |
| `-`      | Subtraction         | `5 - 3`  | `2`    |
| `*`      | Multiplication      | `5 * 3`  | `15`   |
| `/`      | Division (float)    | `5 / 2`  | `2.5`  |
| `//`     | Floor Division      | `5 // 2` | `2`    |
| `%`      | Modulus (remainder) | `5 % 2`  | `1`    |
| `**`     | Exponentiation      | `2 ** 3` | `8`    |


##2. Assignment Operators

| Operator | Description             | Example   | Equivalent To |
| -------- | ----------------------- | --------- | ------------- |
| `=`      | Assign value            | `x = 5`   | -             |
| `+=`     | Add and assign          | `x += 3`  | `x = x + 3`   |
| `-=`     | Subtract and assign     | `x -= 2`  | `x = x - 2`   |
| `*=`     | Multiply and assign     | `x *= 3`  | `x = x * 3`   |
| `/=`     | Divide and assign       | `x /= 2`  | `x = x / 2`   |
| `//=`    | Floor divide and assign | `x //= 2` | `x = x // 2`  |
| `%=`     | Modulus and assign      | `x %= 2`  | `x = x % 2`   |
| `**=`    | Power and assign        | `x **= 2` | `x = x ** 2`  |



#3. Comparison (Relational) Operators


| Operator | Description              | Example  | Result |
| -------- | ------------------------ | -------- | ------ |
| `==`     | Equal to                 | `5 == 5` | `True` |
| `!=`     | Not equal to             | `5 != 3` | `True` |
| `>`      | Greater than             | `5 > 3`  | `True` |
| `<`      | Less than                | `3 < 5`  | `True` |
| `>=`     | Greater than or equal to | `5 >= 5` | `True` |
| `<=`     | Less than or equal to    | `3 <= 5` | `True` |



| Rule # | Concept                                                         |
| ------ | --------------------------------------------------------------- |
| 1      | Compared **element-by-element** from **left to right**          |
| 2      | **First unequal element** determines the result                 |
| 3      | If one is a **prefix** of the other, the **shorter is smaller** |


[ 1,  2,  3 ]
  |   |   |
  V   V   V
[ 1,  2,  4 ]

Step 1: 1 == 1 → continue  
Step 2: 2 == 2 → continue  
Step 3: 3 < 4 → result = True


Compare the following and fill in with <, ==, or >:

(3, 5) ___ (3, 4) → >

['cat'] ___ ['car'] → >

[2, 4, 6] ___ [2, 4, 6, 0] → <

['a', 'z'] ___ ['a', 'x'] → >

('a', 1) ___ ('a', 1) → ==








# 4. Logical Operators

| Operator | Description           | Example         | Result  |
| -------- | --------------------- | --------------- | ------- |
| `and`    | True if both are true | `True and True` | `True`  |
| `or`     | True if at least one  | `True or False` | `True`  |
| `not`    | Inverts the value     | `not True`      | `False` |


#5. Bitwise Operators

| Operator | Description | Example               | Result |         |       |     |
| -------- | ----------- | --------------------- | ------ | ------- | ----- | --- |
| `&`      | Bitwise AND | `5 & 3` → `101 & 011` | `1`    |         |       |     |
| \`       | \`          | Bitwise OR            | \`5    | 3`→`101 | 011\` | `7` |
| `^`      | Bitwise XOR | `5 ^ 3`               | `6`    |         |       |     |
| `~`      | Bitwise NOT | `~5`                  | `-6`   |         |       |     |
| `<<`     | Left shift  | `5 << 1`              | `10`   |         |       |     |
| `>>`     | Right shift | `5 >> 1`              | `2`    |         |       |     |



#6. **Membership Operators**

| Operator | Description                      | Example            | Result |
| -------- | -------------------------------- | ------------------ | ------ |
| `in`     | True if value exists in sequence | `'a' in 'apple'`   | `True` |
| `not in` | True if value does not exist     | `3 not in [1,2,4]` | `True` |

---

## 7.Identity Operator

| Operator | Description                       | Example      | Result       |
| -------- | --------------------------------- | ------------ | ------------ |
| `is`     | True if both refer to same object | `x is y`     | `True/False` |
| `is not` | True if not same object           | `x is not y` | `True/False` |



# 8. **Operator Precedence (Highest to Lowest)

| Precedence Level | Operators                                    |    |
| ---------------- | -------------------------------------------- | -- |
| 1 (Highest)      | `()`, function calls, indexing `[]`          |    |
| 2                | `**`                                         |    |
| 3                | `+`, `-` (unary), `~`                        |    |
| 4                | `*`, `/`, `//`, `%`                          |    |
| 5                | `+`, `-`                                     |    |
| 6                | `<<`, `>>`                                   |    |
| 7                | `&`                                          |    |
| 8                | `^`                                          |    |
| 9                | \`                                           | \` |
| 10               | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `in` |    |
| 11               | `not`                                        |    |
| 12               | `and`                                        |    |
| 13               | `or`                                         |    |
| 14 (Lowest)      | `=`, `+=`, `-=`, etc.                        |    |



## 🛠 Examples to Understand

```python
# Arithmetic
print(10 + 5)     # 15

# Comparison
print(10 >= 5)    # True

# Logical
print(10 > 5 and 5 > 3)  # True

# Bitwise
print(5 & 3)      # 1

# Membership
print('a' in 'cat')   # True

# Identity
x = [1, 2]
y = x
print(x is y)     # True


#Summary Diagram (Categories of Python Operators)


                 ┌────────────┐
                 │ OPERATORS  │
                 └────────────┘
                        ↓
      ┌────────────────┬────────────┬────────────┬────────────┐
      │ Arithmetic     │ Comparison │ Assignment │ Logical    │
      │ + - * / % ** //│ == != > <  │ = += -=    │ and or not │
      └────────────────┴────────────┴────────────┴────────────┘
                ↓
      ┌────────────┬──────────────┬────────────┐
      │ Bitwise    │ Membership   │ Identity   │
      │ & | ^ ~ << │ in, not in   │ is, is not │
      └────────────┴──────────────┴────────────┘





| Data Type       | Supported Operators                    | Notes                                          |
| --------------- | -------------------------------------- | ---------------------------------------------- |
| `int`, `float`  | All (`==`, `!=`, `<`, `>`, `<=`, `>=`) | Standard arithmetic comparisons                |
| `complex`       | `==`, `!=` only                        | `<`, `>`, etc. raise `TypeError`               |
| `str`           | All                                    | Lexicographical (based on Unicode values)      |
| `bool`          | All                                    | `True == 1`, `False == 0`, comparisons allowed |
| `list`, `tuple` | All                                    | Compared element-wise from left to right       |
| `NoneType`      | `==`, `!=` only                        | Other comparisons raise `TypeError`            |
| Mixed types     | Some                                   | E.g., `int` vs `float` ✅, `str` vs `int` ❌     |
| Custom class    | All if dunder methods defined          | Uses methods like `__eq__`, `__lt__`, etc.     |




| Data Type    | Supported Ops   | Notes                    |
| ------------ | --------------- | ------------------------ |
| int, float   | All             | Works as expected        |
| complex      | `==`, `!=` only | Others raise error       |
| str          | All             | Lexicographic            |
| bool         | All             | `True = 1`, `False = 0`  |
| list/tuple   | All             | Compared element-wise    |
| NoneType     | `==`, `!=`      | Others raise error       |
| mixed types  | Some            | e.g., str vs int = error |
| custom class | All if defined  | Use dunder methods       |
