

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