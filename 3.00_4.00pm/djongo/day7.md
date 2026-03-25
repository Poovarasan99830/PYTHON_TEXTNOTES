

# ______________________________________________________________
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

# ---


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





