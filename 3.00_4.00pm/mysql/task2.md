
# 🔥 **Banking System – Project-Style Task Questions**

Below are **15 tasks** in proper order (DDL → DML → Queries → Reports).

---

# 🧱 **PART 1 — DDL TASKS (Table Creation Tasks)**

### **Task 1:**

Create a table named **customers** with the following columns (do NOT mention data types):

* Customer ID
* Name
* Account Type
* Balance
* Last Login Date

---

### **Task 2:**

Create a table named **transactions** with the following fields:

* Transaction ID
* Customer ID
* Type (Credit/Debit)
* Amount
* Transaction Date

---

### **Task 3:**

Create a table **branches** with columns:

* Branch ID
* Branch Name
* City

---

### **Task 4:**

Create a table **accounts** with:

* Account Number
* Customer ID
* Branch ID
* Opening Balance
* Opening Date

---

# 💾 **PART 2 — INSERT TASKS**

### **Task 5:**

Insert **5 customers** into the customers table with different account types (Savings / Current).

---

### **Task 6:**

Insert a few transaction records for customer 101:

* Credit 10,000
* Debit 2,500
* Debit 500

---



### **Task 7:**

Insert **3 branches** (Chennai, Bangalore, Mumbai).

---

### **Task 8:**

Insert at least **5 accounts** mapped to customers and branches.

---

# 🔄 **PART 3 — UPDATE & DELETE TASKS**

### **Task 9:**

Update customer **101** balance after:

* a debit of 500
* a credit of 1200

(Use two separate UPDATE queries.)

---

### **Task 10:**

Delete customers who have **not logged in for more than a year**.

---

### **Task 11:**

Increase balance of all **Savings accounts** by 5% interest.

---

# 🔍 **PART 4 — SELECT QUERY TASKS**

### **Task 12:**

Retrieve customers who have **balance more than 1 lakh**.

---

### **Task 13:**

Get all **debit transactions** for customer 101.

---

### **Task 14:**

List all accounts opened in **2024**.

---

### **Task 15:**

Generate a **mini-statement** for customer 101 (latest 5 transactions).

---

# 🛠️ Want JOIN-based tasks also?

If you want, I can give **JOIN tasks** like:

* Customer + Branch Join
* Customer + Transactions Join
* Accounts + Branch Join
* Highest balance customer per branch

Just say **"Give JOIN tasks"** and I’ll prepare them.




##  **ONE-TO-ONE RELATIONSHIP TASKS**


# **1. Employees ↔ Employee Profiles**

**Task:**
Create two tables:

* `employees`
* `employee_profiles`

Link them using a **one-to-one foreign key** from employee_profiles to employees.

#__________________________________________________
## **2. Users ↔ User Login Details**
#__________________________________________________

**Task:**
Create:

* `users` table
* `user_login_details` table

Use a **unique foreign key** to ensure each user has **exactly one login record**.


#_________________________________________________________
# **3. Patients ↔ Medical Records**
#__________________________________________________

**Task:**
Create:

* `patients`
* `patient_medical_record`

Link them with a **one-to-one foreign key** (each patient has one medical record).

#_____________________________________________________________
#  **ONE-TO-MANY RELATIONSHIP TASKS**
#_____________________________________________________________

## **4. Products ↔ Product Reviews**

**Task:**
Create:

* `products` table
* `product_reviews` table

Use a foreign key so **one product can have many reviews**.

#_____________________________________________________________
# *5. Categories ↔ Products**

#_____________________________________________________________

**Task:**
Create:

* `categories`
* `products`

Use a foreign key so **one category contains many products**.

#_____________________________________________________________
## **6. Suppliers ↔ Supply Items**

**Task:**
Create:

* `suppliers`
* `supply_items`

Use a foreign key so **one supplier supplies many items**.

#_____________________________________________________________

#  **MANY-TO-MANY RELATIONSHIP TASKS**

## **7. Teachers ↔ Subjects using Teacher_Subjects**

**Task:**
Create:

* `teachers`
* `subjects`
* A linking table `teacher_subjects` with a **composite primary key**.

This allows **one teacher to teach many subjects**, and **one subject to be taught by many teachers**.

#_____________________________________________________________

## **8. Restaurants ↔ Food Items using Restaurant_Menu**

**Task:**
Create:

* `restaurants`
* `food_items`
* A many-to-many table `restaurant_menu`.

A food item can be served in many restaurants, and each restaurant can have many items.


#_____________________________________________________________

## **9. Playlists ↔ Songs using Playlist_Songs**

**Task:**
Create:

* `playlists`
* `songs`
* A linking table `playlist_songs`.

# _____________________________________________________________