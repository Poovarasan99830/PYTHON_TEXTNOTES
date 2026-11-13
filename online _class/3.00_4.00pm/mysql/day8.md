

# ______________________________________________________
# 🟦 **1. What Is a Stored Procedure? (TEACH MODE)**
# ______________________________________________________




### 👉 **Simple Definition:**

     A **Stored Procedure** is a **group of SQL statements** saved in the database, which you can run anytime by calling its name.

Think of it like:

   * A **function** in programming
   * But written **inside MySQL**

* Useful for **automation**, **repeated queries**, **business logic**, and **performance**

---



# ___________________________________________________
# 🟦 **2. Why Do We Use Stored Procedures?**
# ___________________________________________________



### ✔ **1. Reuse**

Instead of writing the same SQL again and again → write once → call anytime.

### ✔ **2. Performance**

MySQL **compiles and caches** the procedure → runs faster.

### ✔ **3. Security**

You can **hide complex business logic**.
Users only run the procedure, not see SQL inside.

### ✔ **4. Clean Code**

Application becomes smaller
Database holds more logic.

---

# ___________________________________________________
# 🟦 **3. How to Create a Stored Procedure**
# ___________________________________________________




# ___________________________________________________
### 🟩 **Syntax (TEACH MODE Example)**
# ___________________________________________________



```
DELIMITER $$

CREATE PROCEDURE procedure_name()
BEGIN
    -- SQL code here
END $$

DELIMITER ;
```




# ___________________________________________________
### ❗ Why do we change DELIMITER?
# ___________________________________________________



* By default, MySQL ends a query with `;`
* But procedures contain many `;`
* So we temporarily change it to `$$` or `//`

---

# ___________________________________________________
# 🟦 **4. SIMPLE EXAMPLE — No Input, Just a Task**
# ___________________________________________________




# ___________________________________________________
### ✔ **Example 1: Show all employees**
# ___________________________________________________



```
DELIMITER $$

CREATE PROCEDURE get_all_employees()
BEGIN
    SELECT * FROM employees;
END $$

DELIMITER ;
```

### ✔ Call the procedure:

```
CALL get_all_employees();
```

---
# ___________________________________________________
# 🟦 **5. Stored Procedure WITH INPUT Parameters**
# ___________________________________________________




### ✔ **Example 2: Get employee by ID**

```
DELIMITER $$

CREATE PROCEDURE get_employee_by_id(IN emp_id INT)
BEGIN
    SELECT * FROM employees WHERE id = emp_id;
END $$

DELIMITER ;
```

### ✔ Call:

```
CALL get_employee_by_id(10);
```

---


# ___________________________________________________
# 🟦 **6. Stored Procedure WITH OUTPUT Parameter**
# ___________________________________________________



### ✔ **Example 3: Return total employee count**

```
DELIMITER $$

CREATE PROCEDURE count_employees1(IN total INT)
BEGIN
    SELECT COUNT(*) INTO total FROM employees;
END $$

DELIMITER ;

```

### ✔ Call:

```
CALL count_employees(@result);
SELECT @result;
```

---

# ___________________________________________________
# 🟦 **7. Stored Procedure With IN & OUT Both**
# ___________________________________________________

Write a MySQL stored procedure named get_salary that accepts an employee ID as input and returns the employee’s salary as output. The procedure should take the employee ID as an IN parameter and return the salary using an OUT parameter.


```
DELIMITER $$

CREATE PROCEDURE get_salary
(
    IN emp_id INT, 
    OUT salary_amount DECIMAL(10,2)
)
BEGIN
    SELECT salary INTO salary_amount
    FROM employees
    WHERE id = emp_id;
END $$

DELIMITER ;
```

---

# ___________________________________________________
# 🟦 **8. Stored Procedure With IF, LOOP, Logic (Industrial Use)**
# ___________________________________________________




### ✔ **Example 4: Update salary based on grade**

```
DELIMITER $$

CREATE PROCEDURE update_salary(IN emp_id INT, IN grade VARCHAR(5))
BEGIN
    IF grade = 'A' THEN
        UPDATE employees SET salary = salary + 5000 WHERE id = emp_id;
    ELSEIF grade = 'B' THEN
        UPDATE employees SET salary = salary + 3000 WHERE id = emp_id;
    ELSE
        UPDATE employees SET salary = salary + 1000 WHERE id = emp_id;
    END IF;
END $$

DELIMITER ;
```

---

# ___________________________________________________
# 🟦 **9. Stored Procedure With INSERT (Industry Example)**
# ___________________________________________________




### ✔ **Example 5: Insert new order**

```
DELIMITER $$

CREATE PROCEDURE create_order(
    IN p_customer_id INT,
    IN p_amount DECIMAL(10,2)
)
BEGIN
    INSERT INTO orders(customer_id, amount, order_date)
    VALUES(p_customer_id, p_amount, NOW());
END $$

DELIMITER ;
```

---

# ___________________________________________________
# 🟦 **10. Stored Procedure With ERROR HANDLING**
# ___________________________________________________



### ✔ **Example 6: Check stock before placing order**

```
DELIMITER $$

CREATE PROCEDURE place_order(IN product_id INT, IN qty INT)
BEGIN
    DECLARE stock_qty INT;

    SELECT stock INTO stock_qty FROM products WHERE id = product_id;

    IF stock_qty < qty THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Insufficient stock!';
    ELSE
        UPDATE products SET stock = stock - qty WHERE id = product_id;
        INSERT INTO orders(product_id, quantity, order_date) VALUES (product_id, qty, NOW());
    END IF;
END $$

DELIMITER ;
```

---

# ___________________________________________________
# 🟦 **11. Industrial Real Requirements (Questions)**
# ___________________________________________________



### ✔ Q1: Create a stored procedure to return employees who joined in the last 30 days.

### ✔ Q2: Create a stored procedure to deactivate users whose login failed more than 5 times.

### ✔ Q3: Create a stored procedure to archive orders older than 1 year.

(If you want, I will create these procedures also.)

---


# ___________________________________________________
# 🟦 **12. Interview Points to Mention**
# ___________________________________________________



### ✔ Stored procedures reduce:

* network traffic
* repeated code
* security risks

### ✔ They run inside the database engine → faster.

### ✔ They support:

* variables
* loops
* conditions
* error handling
* transactions

