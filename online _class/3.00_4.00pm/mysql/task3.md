

# ______________________________________________
# 🟦 **ONE-TO-ONE – INDUSTRIAL REQUIREMENTS**
# ______________________________________________





## **1. Employee → Employee Profile (HR System Requirement)**

**Requirement:**
The HR department needs to store basic employee data in one table and detailed personal information (address, DOB, ID proofs) in another table.
Each employee can have **only one** profile.

**Task:**
Design two tables: `employees` and `employee_profiles`
Link them using a **one-to-one** foreign key (unique).

---



## **2. Users → User Login Details (Authentication System Requirement)**

**Requirement:**
A company’s internal portal stores user information separately from login credentials.
Each user will have **exactly one** login record.

**Task:**
Create `users` and `user_login_details` tables.
Connect using a **unique foreign key** from login table → users table.

---





## **3. Patients → Medical Record (Hospital Requirement)**

**Requirement:**
Hospital wants to store patient information and their medical record separately.
Every patient must have **only one** medical record.

**Task:**
Create `patients` and `patient_medical_record`.
Link them using **one-to-one** relationship.

---


# ______________________________________________
# 🟧 **ONE-TO-MANY – INDUSTRIAL REQUIREMENTS**
# ______________________________________________






---

## **4. Product → Product Reviews (E-Commerce Requirement)**

**Requirement:**
An e-commerce company needs to store product details and many customer reviews.
Each product can have **multiple** reviews.

**Task:**
Create `products` and `product_reviews`.
Use **one-to-many** foreign key from reviews → products.

---




## **5. Category → Products (Inventory Requirement)**

**Requirement:**
A retail store wants products grouped under categories such as Electronics, Clothing, etc.
One category contains **many** products.

**Task:**
Create `categories` and `products`.
Link using a **foreign key** in products table.

---





## **6. Suppliers → Supply Items (Logistics Requirement)**

**Requirement:**
A warehouse receives supply items from multiple suppliers.
Each supplier sends **many** items.

**Task:**
Create `suppliers` and `supply_items`.
Link supply_items → suppliers (1–M).

---




# ______________________________________________
# 🟩 **MANY-TO-MANY – INDUSTRIAL REQUIREMENTS**
# ______________________________________________





---

## **7. Teachers ↔ Subjects (School Management Requirement)**

**Requirement:**
In a school, teachers can teach multiple subjects.
Each subject can also be taught by multiple teachers.




**Task:**

Create `teachers`, `subjects`, and junction table `teacher_subjects` (M–M).

---




## **8. Restaurants ↔ Food Items (Food Delivery App Requirement)**

**Requirement:**
A food delivery platform wants to store restaurant menus.
A restaurant serves many food items.
A food item (like "Burger") can appear in many restaurants.

**Task:**
Create `restaurants`, `food_items`, and `restaurant_menu` junction table.

---






## **9. Playlists ↔ Songs (Music Streaming App Requirement)**

**Requirement:**
A music streaming app stores user playlists with songs.
A playlist contains many songs, and a song can be added to many playlists.

**Task:**
Create `playlists`, `songs`, and `playlist_songs` junction table.




# ______________________________________________



Here are **ER diagrams (clean, simple, student-friendly)**.


---

# 🟦 **1. Employees → Employee Profiles (One-to-One)**

```
┌───────────────┐        1 ──────── 1        ┌────────────────────┐
│   employees    │────────────────────────────│ employee_profiles  │
├───────────────┤                            ├────────────────────┤
│ emp_id (PK)    │                            │ profile_id (PK)    │
│ emp_name       │                            │ emp_id (FK)(UNIQUE)│
│ email          │                            │ address            │
│ phone          │                            │ dob                │
└───────────────┘                            └────────────────────┘
```

---

# 🟦 **2. Users → User Login Details (One-to-One)**

```
┌──────────────┐        1 ──────── 1        ┌──────────────────────────┐
│    users      │────────────────────────────│  user_login_details      │
├──────────────┤                            ├──────────────────────────┤
│ user_id (PK)  │                            │ login_id (PK)            │
│ username      │                            │ user_id (FK)(UNIQUE)     │
│ full_name     │                            │ password_hash            │
└──────────────┘                            └──────────────────────────┘
```

---

# 🟦 **3. Patients → Medical Record (One-to-One)**

```
┌───────────────┐       1 ──────── 1        ┌──────────────────────────────┐
│   patients     │──────────────────────────│  patient_medical_record       │
├───────────────┤                           ├──────────────────────────────┤
│ patient_id(PK) │                           │ record_id (PK)               │
│ patient_name   │                           │ patient_id (FK)(UNIQUE)      │
│ age            │                           │ blood_group                  │
│ gender         │                           │ medical_history              │
└───────────────┘                           └──────────────────────────────┘
```

---

# 🟧 **4. Products → Product Reviews (One-to-Many)**

```
     1 ───────────< M
┌───────────────┐             ┌─────────────────────┐
│    products    │────────────│  product_reviews     │
├───────────────┤             ├─────────────────────┤
│ product_id(PK) │             │ review_id (PK)       │
│ product_name   │             │ product_id (FK)      │
│ price          │             │ rating               │
└───────────────┘             │ comments             │
                              └─────────────────────┘
```

---

# 🟧 **5. Categories → Products (One-to-Many)**

```
     1 ───────────< M
┌────────────────┐               ┌─────────────────┐
│   categories    │──────────────│    products      │
├────────────────┤               ├─────────────────┤
│ category_id(PK) │               │ product_id (PK) │
│ category_name   │               │ product_name    │
└────────────────┘               │ category_id (FK)│
                                └─────────────────┘
```

---

# 🟧 **6. Suppliers → Supply Items (One-to-Many)**

```
     1 ───────────< M
┌────────────────┐               ┌──────────────────────┐
│   suppliers     │──────────────│    supply_items       │
├────────────────┤               ├──────────────────────┤
│ supplier_id(PK) │               │ item_id (PK)          │
│ supplier_name   │               │ supplier_id (FK)      │
│ contact         │               │ item_name             │
└────────────────┘               │ quantity              │
                                └──────────────────────┘
```

---

# 🟩 **7. Teachers ↔ Subjects (Many-to-Many)**

```
        M ───────< teacher_subjects >─────── M
          
┌───────────────┐        ┌────────────────────────┐        ┌───────────────┐
│   teachers     │        │   teacher_subjects     │        │   subjects    │
├───────────────┤        ├────────────────────────┤        ├───────────────┤
│ teacher_id(PK) │1     M│ teacher_id (FK, PK)     │M     1│ subject_id(PK)│
│ teacher_name   │────────│ subject_id (FK, PK)     │────────│ subject_name │
└───────────────┘        └────────────────────────┘        └───────────────┘
```










---

# 🟩 **8. Restaurants ↔ Food Items (Many-to-Many)**

```
        M ───────< restaurant_menu >─────── M

┌────────────────┐      ┌────────────────────────┐      ┌─────────────────┐
│  restaurants    │      │    restaurant_menu     │      │   food_items    │
├────────────────┤      ├────────────────────────┤      ├─────────────────┤
│ restaurant_idPK │1   M│ restaurant_id (FK, PK)  │M   1│ food_id (PK)     │
│ restaurant_name │──────│ food_id (FK, PK)        │──────│ food_name        │
│ location        │      └────────────────────────┘      │ price           │
└────────────────┘                                       └─────────────────┘
```

---

# 🟩 **9. Playlists ↔ Songs (Many-to-Many)**

```
        M ───────< playlist_songs >─────── M

┌───────────────┐      ┌────────────────────────┐      ┌───────────────┐
│   playlists    │      │     playlist_songs     │      │     songs      │
├───────────────┤      ├────────────────────────┤      ├───────────────┤
│ playlist_id PK │1   M│ playlist_id (FK, PK)    │M   1│ song_id  (PK)  │
│ playlist_name  │──────│ song_id (FK, PK)        │──────│ song_title      │
│ created_by     │      └────────────────────────┘      │ artist         │
└───────────────┘                                       │ duration       │
                                                        └───────────────┘
```

.

