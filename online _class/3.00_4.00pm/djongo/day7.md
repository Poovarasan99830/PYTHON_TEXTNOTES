



# API

API (Application Programming Interface) is a communication bridge that allows two applications to exchange data with each other.


Used for communication between:

Frontend ↔ Backend
Mobile ↔ Server
React ↔ Django
Angular ↔ Django


# Types of APIs


| Type     | Meaning           |
| -------- | ----------------- |
| REST API | Most common       |

| SOAP API | Old XML based     |
| GraphQL  | Flexible querying |



# HTTP Methods
    HTTP (HyperText Transfer Protocol) is a communication protocol used for transferring data between client and server.

    HTTP is like language used between two people.
    Example: 
       Client speaks request
       Server understands and replies
| Method | Use            |
| ------ | -------------- |
| GET    | Fetch data     |
| POST   | Create         |
| PUT    | Full update    |
| PATCH  | Partial update |
| DELETE | Delete         |




# HTTP Status Codes
| Code | Meaning      |
| ---- | ------------ |
| 200  | Success      |
| 201  | Created      |
| 400  | Bad request  |
| 401  | Unauthorized |
| 403  | Forbidden    |
| 404  | Not found    |
| 500  | Server error |



# Request & Response Request

# JSON
     JSON (JavaScript Object Notation) is a lightweight data exchange format used between frontend and backend.

     JSON is like a universal language both frontend and backend understand.

      {
       "name":"Rahul",
      "age":25
      }


# What is DRF?
    Django REST Framework is a toolkit used to build REST APIs in Django.


# Why Use DRF?
   Fast API development
   Authentication support
   Serialization
   Browsable API
   Token/JWT support
   Permissions
   Pagination
   Filtering

# What is REST API?
  REST API is a type of API that follows some standard rules to send and receive data using HTTP methods.

REST API follows standard rules like:
  ✅ Proper URLs
  ✅ Proper HTTP methods
  ✅ Stateless communication -->Server does NOT remember previous requests from client.
  ✅ JSON response

Why Stateless Important?
Because:
  ✅ Easy scaling
  ✅ Faster processing
  ✅ Multiple servers can handle requests
  ✅ No memory dependency



| Feature           | Normal API                  | REST API                 |
| ----------------- | --------------------------- | ------------------------ |
| Rules             | No fixed rules              | Follows REST rules       |
| HTTP Methods      | May or may not use properly | Uses GET POST PUT DELETE |
| URL Structure     | Random                      | Standard                 |
| Data Format       | Any format                  | Mostly JSON              |
| Scalability       | Less                        | High                     |
| Frontend Friendly | Difficult sometimes         | Very easy                |
| Widely Used       | Less                        | Very common              |


# ______________________________________________________
# **Topic: Django REST Framework + JWT Authentication**
# ______________________________________________________________


# _______________________________________________________________
# Installation Commands
# _______________________________________________________________

# pip install djangorestframework
# pip install djangorestframework-simplejwt




# _____________________________________
# 🔹 1️⃣ Django REST Framework (DRF)
# _____________________________________

# * DRF is a toolkit to build RESTful APIs in Django.
# * It converts Django models into JSON APIs.
# * It provides serializers, viewsets, authentication, and permission system.
# * Supports CRUD operations easily.



# _____________________________________
# 🔹 2️⃣ ModelViewSet
# _____________________________________

# * `ModelViewSet` provides automatic CRUD:

#   * GET → List / Retrieve
#   * POST → Create
#   * PUT/PATCH → Update
#   * DELETE → Destroy
# * Requires:

#   * `queryset`
#   * `serializer_class`
# * Reduces boilerplate code.



# _____________________________________
# 🔹 3️⃣ Serializer
# _____________________________________

# * Converts model data → JSON
# * Validates input data
# * Handles deserialization (JSON → Model object)


# _____________________________________
# Django REST Framework Complete Workflow
# _____________________________________

Browser / Postman
        │
        │ GET http://127.0.0.1:8000/api/
        ▼
urls.py
        │
        ▼
ProductViewSet.as_view({'get':'list'})
        │
        ▼
ProductViewSet.list()
        │
        ▼
queryset = Product.objects.all()
        │
        ▼
Database
        │
        ▼
Returns Product Objects
        │
        ▼
ProductSerializer(products, many=True)
        │
        ▼
Convert Model Objects
        │
        ▼
Python Dictionary
        │
        ▼
JSON Renderer
        │
        ▼
Response(JSON)
        │
        ▼
Browser / Postman







# _____________________________________
# 🔹 4️⃣ JWT Authentication
# _____________________________________

# JWT = JSON Web Token

# * Used for stateless authentication.
# * Server does NOT store session.
# * Client sends token in every request.

# ### Types of Tokens:

# * Access Token (short expiry)
# * Refresh Token (used to generate new access token)

# Header format:

# ```
# Authorization: Bearer <access_token>


# _____________________________________
# 🔹 5️⃣ APIView
# _____________________________________

# * Used for custom API logic.
# * Gives full control over HTTP methods.
# * Example: Registration, Profile API.



# _____________________________________
# 🔹 6️⃣ IsAuthenticated Permission
# _____________________________________

# * Allows only logged-in users.
# * Checks if valid token exists.
# * Prevents unauthorized access.



# _____________________________________
# 🔹 7️⃣ Registration Logic (Theory Flow)
# _____________________________________

# 1. Receive username & password
# 2. Validate data
# 3. Check if user exists
# 4. Create user
# 5. Generate JWT tokens
# 6. Return access & refresh token



# _____________________________________
# 🔹 8️⃣ Protected API Flow
# _____________________________________

# Client → Sends Request
# ↓
# Includes JWT in Header
# ↓
# DRF verifies token
# ↓
# Permission check
# ↓
# Returns response


# _____________________________________
# 9️⃣ Key Concepts Covered
# _____________________________________

# REST API
# CRUD operations
# Stateless authentication
# Token-based security
# Protected endpoints
# Basic authorization





Behind the scene:
<!-- 
ProductViewSet inherits from ModelViewSet, so Django REST Framework automatically provides CRUD operations (Create, Read, Update, Delete).

queryset = Product.objects.all() tells the ViewSet which records to fetch from the database.

serializer_class = ProductSerializer specifies how Product model instances are converted to JSON and how JSON is validated and converted back into model objects.

Based on the HTTP request (GET, POST, PUT, PATCH, DELETE), DRF automatically calls the appropriate method (list, retrieve, create, update, partial_update, or destroy).

You only configure the queryset and serializer; ModelViewSet handles the request processing, validation, database operations, and response generation automatically. -->