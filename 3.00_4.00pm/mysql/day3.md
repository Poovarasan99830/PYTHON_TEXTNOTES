


# _______________________________________________
# 🚀 **MYSQL CONSTRAINTS — COMPLETE NOTES (Combined & Clean)**
# _______________________________________________



1. **PRIMARY KEY** 
2. **FOREIGN KEY** 
3. **UNIQUE** 
4. **NOT NULL** 
5. **CHECK** 
6. **DEFAULT** 
7. **AUTO_INCREMENT**



# _______________________________________________
# ✅ **1️⃣ PRIMARY KEY**
# _______________________________________________




* Uniquely identifies each row
* Cannot be NULL
* Only **one** per table

### Syntax

```sql
id INT PRIMARY KEY
```

### Example

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
```


# _______________________________________________
# ✅ **2️⃣ UNIQUE**
# _______________________________________________




* Ensures all values are **different**
* **Allows one NULL**

### Syntax

```sql
email VARCHAR(100) UNIQUE
```

### Example

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);
```


# _______________________________________________
# ✅ **3️⃣ NOT NULL**
# _______________________________________________




* Value **must be provided**
* Cannot remain empty

### Example

```sql
name VARCHAR(50) NOT NULL
```

# _______________________________________________
# ✅ **4️⃣ FOREIGN KEY**
# _______________________________________________




* Links two tables
* Maintains **referential integrity**

### Syntax

```sql
FOREIGN KEY (column) REFERENCES table(column)
```

### Example

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

# _______________________________________________
# ✅ **5️⃣ CHECK** (MySQL 8+)
# _______________________________________________



* Validates values using a condition

### Example

```sql
age INT CHECK (age >= 18)
```

# _______________________________________________
# ✅ **6️⃣ DEFAULT**
# _______________________________________________




* Sets a default value if user doesn't provide one

### Example

```sql
status VARCHAR(20) DEFAULT 'ACTIVE'
```

---

# ✅ **7️⃣ AUTO_INCREMENT**

* Auto-generates increasing numbers
* Works only on integer + primary key

### Example

```sql
id INT PRIMARY KEY AUTO_INCREMENT
```

# _______________________________________________
# 🔥 **FULL TABLE WITH ALL CONSTRAINTS**
# _______________________________________________



```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    salary DECIMAL(10,2) DEFAULT 20000,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(id)
);
```

---

# 🧠 **MEMORY DIAGRAM**

```
PRIMARY KEY     → Unique + Not Null
UNIQUE          → Unique (allows 1 NULL)
NOT NULL        → Must have value
CHECK           → Condition must be true
DEFAULT         → Auto value if not provided
AUTO_INCREMENT  → Auto-increasing number
FOREIGN KEY     → Connects tables
```

---

# ___________________________________________
CONSTRAINT CREATION  WITH EXISTING TABLE
# ___________________________________________



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
