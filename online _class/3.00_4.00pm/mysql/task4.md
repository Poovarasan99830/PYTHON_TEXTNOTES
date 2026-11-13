
---

# 📘 SQL ASSESSMENT – DATABASE DESIGN & QUERIES

**Time:** 2 Hours
**Total Marks:** 100

---

## 🔹 PART A – TABLE CREATION (DDL)

*(40 Marks)*

### **1. Department Table**

Create a table named **`departments`** with the following columns:

* department_id (Primary Key)
* department_name

---

### **2. Employee Table**

Create a table named **`employees`** with the following columns:

* employee_id (Primary Key)
* employee_name
* salary
* join_date
* department_id (Foreign Key referencing departments)

---

### **3. Customer Table**

Create a table named **`customers`** with the following columns:

* customer_id (Primary Key)
* customer_name
* region

---

### **4. Product Table**

Create a table named **`products`** with the following columns:

* product_id (Primary Key)
* product_name
* price

---

### **5. Orders Table**

Create a table named **`orders`** with the following columns:

* order_id (Primary Key)
* customer_id (Foreign Key referencing customers)
* order_date
* total_amount

---

### **6. Order Items Table**

Create a table named **`order_items`** with the following columns:

* order_item_id (Primary Key)
* order_id (Foreign Key referencing orders)
* product_id (Foreign Key referencing products)
* quantity

---

### **7. Returns Table**

Create a table named **`returns`** with the following columns:

* return_id (Primary Key)
* order_id (Foreign Key referencing orders)
* return_date

---

---

## 🔹 PART B – SQL QUERY QUESTIONS

*(60 Marks)*

### **Employee & Department**

**8.** Write a SQL query to find **duplicate employee records** based on employee name.

**9.** Write a SQL query to retrieve the **second highest salary** from the employees table.

**10.** Write a SQL query to find **employees without any department** using LEFT JOIN.

**11.** Write a SQL query to retrieve **employees who joined in the year 2023**.

**12.** Write a SQL query to get the **top 3 highest-paid employees**.

**13.** Write a SQL query to find **employees hired on weekends**.

---

### **Customer, Orders & Products**

**14.** Write a SQL query to calculate the **total revenue per product**.

**15.** Write a SQL query to show the **count of orders per customer**.

**16.** Write a SQL query to find **customers who made purchases but never returned products**.

**17.** Write a SQL query to calculate the **average order value per customer**.

**18.** Write a SQL query to retrieve the **latest order placed by each customer**.

**19.** Write a SQL query to find **products that were never sold**.

**20.** Write a SQL query to identify the **most selling product**.

---

### **Advanced Analysis**

**21.** Write a SQL query to calculate **total revenue and number of orders per region**.

**22.** Write a SQL query to count **customers who placed more than 5 orders**.

**23.** Write a SQL query to retrieve **customers with orders above the average order value**.

**24.** Write a SQL query to get **monthly sales revenue and order count**.

**25.** Write a SQL query to find **customers who placed orders in every month of 2023**.

---

## ⭐ Bonus (Optional)

**26.** Write a SQL query to find the **highest-paid employee in each department**.

**27.** Write a SQL query to **rank customers based on total purchase amount**.

