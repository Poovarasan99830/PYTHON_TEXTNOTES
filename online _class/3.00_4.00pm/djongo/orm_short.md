Sure 👍
Below are **one-line, simple definitions** for **each Django ORM command** you listed — perfect for **exam / interview / quick revision**.

---

### **Basic ORM Queries**

* `StudentRegistration.objects.all()`
  👉 Fetch **all records** from the table.

* `StudentRegistration.objects.get(id=5)`
  👉 Fetch **one specific record** using a unique field.

* `StudentRegistration.objects.filter(name="varun")`
  👉 Fetch records **matching the given condition**.

* `StudentRegistration.objects.filter(age__gte=34)`
  👉 Fetch records where **age is greater than or equal to 34**.

* `StudentRegistration.objects.exclude(name="varun")`
  👉 Fetch records **except those matching the condition**.




 {# <!-- {% for student in get_students %}
        <p>{{ student.name }} - {{ student.age }} - {{ student.course }}</p>
    {% endfor %}
     --> #}


     

### **Update Operations**

* `students.name = "ssss"; students.save()`
  👉 **Update and save** a single object.

* `StudentRegistration.objects.filter(name="ssss").update(name="movie")`
  👉 **Bulk update** records without loading them.







### **Delete Operations**

* `students.delete()`
  👉 **Delete a single object**.

* `StudentRegistration.objects.filter(name="movie").delete()`
  👉 **Delete multiple records** at once.





### **Sorting & Ordering**

* `order_by('name')`
  👉 Sort records in **ascending order** by name.

* `order_by(Lower('name'))`
  👉 Sort records **case-insensitively** by name.





### **Filtering Variations**

* `filter(name__iexact="sam")`
  👉 Fetch records with **case-insensitive exact match**.

* `all()[:2]`
  👉 Fetch **first two records** (limit).

* `count()`
  👉 Return **total number of records**.

* `exists()`
  👉 Check **whether any record exists**.

---

### **Aggregation Functions**

* `aggregate(Avg('age'), Sum('age'))`
  👉 Calculate **average and sum** of age column.

---

### **Values & Distinct**

* `values('course').distinct()`
  👉 Fetch **unique course names** only.

* `values('course', 'name')`
  👉 Fetch **specific fields as dictionaries**.

* `values('age')`
  👉 Fetch **only age field values**.

---

### **Complex Queries (Q Objects)**

* `filter(Q(name="arun") | Q(age__gte=18))`
  👉 Apply **OR condition** in query.

* `filter(Q(name="Arun") & Q(age__gte=18))`
  👉 Apply **AND condition** in query.

---

### **One-Line Summary**

> Django ORM provides **database-independent, Pythonic queries** to perform **CRUD, filtering, sorting, aggregation, and complex conditions** efficiently.

