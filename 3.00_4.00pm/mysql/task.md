

# ✅ **1. WHERE, AND, OR, NOT**

1. Find employees whose salary > 40,000.
2. Find employees from IT department.
3. Find employees from Chennai OR Bangalore.
4. Show employees NOT from Sales department.
5. Find employees age between 25 and 35.

---

# ✅ **2. LIKE Operator**

6. Employees whose name starts with ‘A’.
7. Employees whose name ends with ‘r’.
8. Names containing ‘ra’.
9. Employees whose name has 5 letters.
10. Employees whose 2nd letter is ‘a’.

---

# ✅ **3. IN Operator**

11. Find employees in departments (‘IT’, ‘HR’).
12. Find employees in cities (‘Chennai’, ‘Delhi’, ‘Mumbai’).
13. Find employees whose job_role is Developer OR Accountant.

---

# ✅ **4. BETWEEN**

14. Find employees with salary between 30k and 60k.
15. Find employees between age 28 and 35.
16. Find employees who joined between 2019 and 2021.

---

# ✅ **5. ORDER BY**

17. Sort employees by name ascending.
18. Sort employees by salary descending.
19. Sort by department then salary.
20. Sort by city descending.

---

# ✅ **6. Aggregate Functions**

21. Find total salary of all employees.
22. Find average salary in each department.
23. Find highest salary in IT.
24. Count number of employees in HR.
25. Minimum salary in entire company.

---

# ✅ **7. GROUP BY**

26. Count employees in each department.
27. Total salary paid per department.
28. Average age per department.
29. Count employees per city.
30. Count job roles per department.

---

# ✅ **8. HAVING**

31. Departments having more than 2 employees.
32. Departments where total salary > 1,00,000.
33. Cities having more than 1 employee.
34. Job roles having avg salary > 50,000.
35. Departments with highest paid employee > 60,000.



Here are **beginner-friendly bank calculation tasks** using SQL + real-life banking scenarios.
Perfect for practice (SELECT, SUM, UPDATE, balance transactions, interest, deposits, withdrawals, etc.)

---

# 🏦 **BANK TABLE STRUCTURE (Use This for All Tasks)**

Create a simple bank table:

```sql
CREATE TABLE bank_accounts (
    acc_no INT PRIMARY KEY,
    name VARCHAR(50),
    account_type VARCHAR(20),
    balance DECIMAL(10,2),
    branch VARCHAR(30)
);
```

Sample data:

```sql
INSERT INTO bank_accounts VALUES
(1001, 'Ramesh', 'Savings', 15000, 'Chennai'),
(1002, 'Suresh', 'Current', 42000, 'Mumbai'),
(1003, 'Divya', 'Savings', 8000, 'Delhi'),
(1004, 'Priya', 'Savings', 25000, 'Chennai'),
(1005, 'Kiran', 'Current', 60000, 'Bangalore'),
(1006, 'Arun', 'Savings', 12000, 'Chennai');
```

---

# 🧮 **BANK CALCULATION TASKS (Base Level)**

## ✅ **1. Basic Balance Queries**

1. Show all accounts having balance more than 20,000.
2. Show accounts whose balance is between 10,000 and 50,000.
3. Show savings accounts only.
4. Show customers from the Chennai branch.

---

# 💵 **2. Deposit & Withdrawal Calculations (Using UPDATE)**

5. Deposit **5000** into account **1001**.
6. Withdraw **3000** from account **1003**.
7. Add **10,000** to account **1005** balance.
8. Deduct **1500** from account **1006**.

---

# 💰 **3. Interest Calculations**

Assume interest rates:
Savings = **5%**, Current = **2%**.

9. Calculate 5% interest for all **Savings** accounts.
10. Calculate 2% interest for **Current** accounts.
11. Show final amount after applying interest (do not update table).
12. Show interest amount for each customer based on account type.

---

# 🔄 **4. Monthly Transaction Summary**

13. Show total balance of all accounts.
14. Show average balance in each branch.
15. Find which branch has the highest total balance.
16. Count number of savings accounts in Chennai.
17. Show total money stored in Savings accounts only.
18. Show total money stored in Current accounts only.

---

# 🏧 **5. Mini Banking Operations (Important)**

19. Transfer **5000** from account 1004 to 1001 (two UPDATE statements).
20. Block account 1003 by setting balance = 0.
21. Add a new customer with opening balance 7000.
22. Increase balance of all accounts by 2% service reward.
23. Show top 3 highest balance accounts.
24. Show the lowest 2 balance accounts.

---

# 📊 **6. Analytical Banking Tasks**

25. Find the customer who has the highest balance.
26. Find the customer who has the lowest balance.
27. Show total customers in each account type.
28. Show branch-wise customer count.
29. Show branch-wise total balance, sorted high → low.
30. Show 2nd highest balance using LIMIT.

---

# 🔥 **7. Bonus Logical Tasks (Good for Interviews)**

31. Show customers whose name starts with 'R'.
32. Find accounts where balance is exactly divisible by 1000.
33. Find customers whose balance is 5-digit only.
34. Show customers whose account_type is NOT Savings.
35. Show customers whose branch name ends with 'i'.

---

# 📝 If you want:

✔ **Full SQL answers** for all 35 tasks
✔ **Intermediate / Advanced bank calculations**
✔ **Triggers for bank transactions**
✔ **Stored procedures for deposit/withdrawal**

Just say **“give answers also”** or **“give advanced tasks”**.




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


# ✅ **Why we *rarely* use CROSS JOIN in projects**

Because in real applications:

* Tables usually have **relationships** → we use **INNER, LEFT, RIGHT** joins.

* CROSS JOIN creates **huge results** (A × B rows), which can slow the system.

* Most project requirements don’t ask for *all possible combinations*.

So it is **not used daily**.

---




# 🌟 **BUT Cross Join is useful in some situations**

Even though rare, sometimes we **must** use it.

Here are the **actual practical cases** where companies use CROSS JOIN:

---





## 🟦 **1. Generate All Possible Combinations (Product Variations)**

Example: e-commerce

* Colors × Sizes
* Storage × Warranty
* Plans × Countries

👉 Required when creating product options.

---



---




## 🟦 **3. Generate Test Data**

When QA/Dev need thousands of rows quickly:

```sql
SELECT *
FROM numbers n
CROSS JOIN numbers m;
```

---




## 🟦 **4. Combine Two Tables Without Any Relationship**

If two tables have **no join condition**, INNER JOIN won’t work.

Example:

* Company wants every employee × every training course.

```sql
SELECT e.emp_name, c.course_name
FROM employees e
CROSS JOIN courses c;
```

---




## 🟦 **5. Special Analytics / Reports**

Data analysts sometimes calculate:

* All possible parameter combinations
* Probability calculations
* Statistical permutations

Example:

```sql
SELECT a.value, b.value
FROM tableA a
CROSS JOIN tableB b;
```

---

# 🟥 **So should YOU use CROSS JOIN?**

### ✔ Daily project work → **NO**

### ✔ Most CRUD tasks → **NO**

### ✔ Real-time apps → **NO**

### ✔ Only for special requirements → **YES**

---

# 🟢 Simple Explanation (1 Line)

👉 **We use CROSS JOIN only when we want all combinations of two tables — nothing else.**





# ✅ **Practice Dataset (Very Simple)**

## 🟦 **Table 1: colors**

```sql
CREATE TABLE colors (
  color_id INT PRIMARY KEY,
  color_name VARCHAR(20)
);

INSERT INTO colors VALUES
(1, 'Red'),
(2, 'Blue'),
(3, 'Green');
```

## 🟦 **Table 2: sizes**

```sql
CREATE TABLE sizes (
  size_id INT PRIMARY KEY,
  size_name VARCHAR(10)
);

INSERT INTO sizes VALUES
(1, 'S'),
(2, 'M'),
(3, 'L'),
(4, 'XL');
```

---

# 🎯 **Now you can practice ALL CROSS JOIN concepts**

## 1️⃣ Basic cross join

```sql
SELECT *
FROM colors
CROSS JOIN sizes;
```

---

## 2️⃣ Show only color–size combinations

```sql
SELECT c.color_name, s.size_name
FROM colors c
CROSS JOIN sizes s;
```

---

## 3️⃣ Create product variations (real example)

```sql
SELECT
  CONCAT(c.color_name, ' ', s.size_name) AS variation
FROM colors c
CROSS JOIN sizes s;
```

---

## 4️⃣ Count how many combinations

```sql
SELECT COUNT(*) AS total_combinations
FROM colors
CROSS JOIN sizes;
```

---

## 5️⃣ Use CROSS JOIN with WHERE filter

Example: Only size L and XL

```sql
SELECT c.color_name, s.size_name
FROM colors c
CROSS JOIN sizes s
WHERE s.size_name IN ('L', 'XL');
```

---

## 6️⃣ Use CROSS JOIN inside a subquery (exam type)

```sql
SELECT *
FROM (
    SELECT c.color_name, s.size_name
    FROM colors c CROSS JOIN sizes s
) AS t
WHERE color_name = 'Red';
```

---

