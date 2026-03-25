



# ------------------------------------------------------
## Topic: Django Authentication + CRUD (Template-Based)
# ------------------------------------------------------

* Django traditional views 

* Forms
* Session Authentication
* Login / Logout
* CRUD operations
* Search / Filter / Ordering
* `@login_required` protection


# ------------------------------------------------------
# 🔹 1️⃣ User Registration (Form-Based)
# ------------------------------------------------------


### Concept:

Uses Django `ModelForm` to create a new user.

### 🔹 Flow:

1. Display registration form.
2. User submits data.
3. Validate form.
4. Hash password using `set_password()`.
5. Save user in database.

### 🔹 Important Theory:

* `commit=False` → Creates object without saving.
* `set_password()` → Hashes password securely.
* Django stores hashed passwords, not plain text.




# ------------------------------------------------------
# 🔹 2️⃣ Login System (Session Authentication)
# ------------------------------------------------------


Uses:


authenticate()
login()
logout()


### Concept:
Django uses **session-based authentication**.


### 🔹 Login Flow:

1. User enters username & password.
2. `authenticate()` verifies credentials.
3. `login()` creates session.
4. Session ID stored in browser cookie.

### 🔹 Logout:
* `logout()` clears session data.


# ------------------------------------------------------
# 🔹 3️⃣ @login_required Decorator
# ------------------------------------------------------


@login_required


### Purpose:

* Restricts access to logged-in users only.
* Redirects unauthenticated users to login page.

---

# 🔹 4️⃣ CRUD Operations (Student Model)

## CREATE

* Uses `ModelForm`
* Validates input
* Saves record to database

## READ

* Fetch all records using:

  ```python
  StudentRegistration.objects.all()
  ```

Includes:

* Search (`icontains`)
* Filter (`iexact`)
* Ordering (`order_by()`)

## UPDATE

* Fetch object using `get_object_or_404()`
* Pass `instance` to form
* Save updated data

## DELETE

* Fetch object
* Call `.delete()`
* Redirect to list page

# ------------------------------------------------------
# 🔹 5️⃣ Search Logic
# ------------------------------------------------------


Q(name__icontains=search_query)


### Concept:

* `Q()` allows complex queries.
* `icontains` → Case-insensitive search.
* Used for dynamic filtering.

---

# 🔹 6️⃣ Filtering

```python
students.filter(course__iexact=course_filter)
```

### Concept:

Filters records based on URL query parameter.

Example:

```
?course=python
```

# ------------------------------------------------------
# 🔹 7️⃣ Ordering
# ------------------------------------------------------


students.order_by(order_by)


* Allows dynamic sorting.
* Default sorting by name.


# ------------------------------------------------------
# 🔹 8️⃣ Architecture Flow
# ------------------------------------------------------

Browser
↓
User submits form
↓
Django view processes request
↓
Database operation
↓
HTML response returned

# ------------------------------------------------------
# 🔹 9️⃣ Authentication Type Used Here
# ------------------------------------------------------

This project uses:

> ✅ Session-Based Authentication

Difference from JWT:

| Session Auth             | JWT Auth      |
| ------------------------ | ------------- |
| Stores session on server | Stateless     |
| Uses cookies             | Uses token    |
| Good for web apps        | Good for APIs |

# ------------------------------------------------------
# 🔹 🔟 Key Concepts Covered
# ------------------------------------------------------

* Django Forms
* ModelForm
* Session Authentication
* CRUD operations
* Search & Filter
* QuerySet operations
* URL query parameters
* Access control


# ------------------------------------------------------
# 🔹 5-Line  Summary
# ------------------------------------------------------

This project implements a Django web application with session-based authentication.
It includes user registration, login, and logout functionality.
CRUD operations are implemented using ModelForms.
Search, filtering, and ordering are handled using QuerySets and Q objects.
Access control is managed using the @login_required decorator.

# ------------------------------------------------------
