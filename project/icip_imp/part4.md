
# 4. JWT + RBAC + Audit Logging

Resume:

> Established JWT authentication, RBAC, audit logging, and secure REST APIs...

### Interviewer may ask:

* What is JWT?
* How does JWT work?
* Access token vs refresh token?
* What is RBAC?
* Authentication vs authorization?
* How did you secure APIs?
* What is audit logging?
* Where did you store audit information?
* How do you prevent unauthorized access?










Absolutely. Since these are based on your **ICIP project**, you should understand the difference between **JWT, RBAC, authentication, authorization, and audit logging** rather than memorizing separate definitions.

## 1. What is JWT?

**JWT = JSON Web Token.**

It is a token-based mechanism used to securely represent information about an authenticated user between the client and server.

A JWT generally has three parts:

```text id="3p3f8k"
JWT
 │
 ├── Header
 ├── Payload
 └── Signature
```

### Thanglish

> **“JWT-na JSON Web Token. User authenticate aana apram server token issue pannum. Client subsequent API requests-la andha token-ai use panni authenticated access request pannum.”**

---

# 2. How does JWT work?

Your project flow can be explained like this:

```text id="4n1q8v"
User Login
    ↓
FastAPI
    ↓
Validate Username + Password
    ↓
Generate JWT
    ↓
Access Token + Refresh Token
    ↓
Client
```

For the next API request:

```text id="7qk5ae"
Client
   ↓
Access Token
   ↓
FastAPI
   ↓
Verify Token
   ↓
Identify User
   ↓
RBAC Permission Check
   ↓
Allow / Reject
```

### Example

User sends:

```text
GET /claims/123
Authorization: Bearer <access_token>
```

FastAPI verifies the token.

If valid:

> “This request belongs to user X.”

Then RBAC checks:

> “Does user X have permission to view this claim?”

---

# 3. Access Token vs Refresh Token

### Access Token

Used to **access protected APIs**.

```text id="n4fh2m"
Client
 ↓
Access Token
 ↓
Protected API
```

It normally has a **short lifetime**.

### Refresh Token

Used to obtain a **new access token when the access token expires**.

```text id="f6t1ap"
Access Token expires
        ↓
Refresh Token
        ↓
Authentication Server
        ↓
New Access Token
```

### 🎯 Interview answer

> **“The access token is used to access protected APIs and usually has a short lifetime. The refresh token is used to obtain a new access token when the access token expires, so the user doesn't have to log in again.”**

### Thanglish

> **“Access token protected API access panna use pannuvom. Adhu expire aana refresh token use panni new access token obtain pannuvom; user again login panna thevai illa.”**

---

# 4. What is RBAC?

**RBAC = Role-Based Access Control.**

Instead of giving permissions individually to every user, we assign a **role**, and permissions are associated with that role.

Example:

```text id="x2b6p1"
Admin
 ├── Create User
 ├── View Claims
 ├── Approve Claim
 └── Reject Claim

Claims Officer
 ├── View Claims
 ├── Review Claim
 └── Recommend Decision

Customer
 └── View Own Claims
```

### Thanglish

> **“RBAC-na user-ku direct-ah individual permission kudukkaama, role based-ah permissions assign pannuradhu.”**

---

# 5. Authentication vs Authorization

🔥 Very common interview question.

### Authentication

**“Who are you?”**

Example:

```text
Username + Password
       ↓
Identity verified ✅
```

### Authorization

**“What are you allowed to do?”**

Example:

```text
User = Claims Officer
       ↓
Can review claim? ✅
Can manage users? ❌
```

### Easy memory

> **Authentication → Who are you?**

> **Authorization → What can you do?**

### Thanglish

> **“Authentication-na user yaaru-nu verify pannuradhu. Authorization-na authenticated user-ku enna permission irukku-nu check pannuradhu.”**

---

# 6. How did you secure your APIs?

For your ICIP project, don't just say **“JWT secured the APIs.”**

Explain the layers:

```text id="8c6u3e"
Client
  ↓
JWT Access Token
  ↓
Authentication
  ↓
RBAC Authorization
  ↓
Input Validation
  ↓
Business Rules
  ↓
Protected Resource
```

You can mention:

* JWT authentication
* Access/refresh token mechanism
* RBAC
* HTTPS/TLS
* Input validation
* Proper HTTP status codes
* Secure password hashing
* Token expiration
* Audit logging
* API-level permission checks

### 🎯 Interview answer

> **“We secured our REST APIs using JWT-based authentication and RBAC authorization. The access token was validated on protected requests, and after authentication we checked the user's role and permissions before allowing access to resources. We also used input validation, token expiration, HTTPS, secure password hashing, and audit logging as additional security measures.”**

---

# 7. What is Audit Logging?

**Audit logging means maintaining a record of important actions performed in the application.**

Example:

```text id="k7q4e2"
Who?       → Claims Officer
What?      → Approved Claim
Which?     → CLM1001
When?      → 2026-09-09 10:30
Action     → APPROVE
Result     → SUCCESS
```

This answers:

> **Who did what, when, and on which resource?**

### Thanglish

> **“Audit logging-na application-la important action yaar pannanga, enna action pannanga, eppo pannanga, endha resource mela pannanga-nu record maintain pannuradhu.”**

---

# 8. Where did you store audit information?

For your architecture, the straightforward answer is:

> **“We stored audit records in PostgreSQL because audit information is structured and needs to be queried reliably for compliance and traceability.”**

Example:

```text id="e0j2f4"
PostgreSQL - Audit Table

id
user_id
action
resource_type
resource_id
timestamp
status
metadata
```

You could also publish important audit events through Kafka if your architecture requires centralized/event-driven audit processing.

### Important distinction

**PostgreSQL:**

> Stores the audit record.

**Kafka:**

> Can distribute the audit event to another audit/logging service.

---

# 9. How do you prevent unauthorized access?

Think in two layers:

```text id="u5x2c7"
Request
  ↓
JWT Authentication
  ↓
Is token valid?
  ↓
YES
  ↓
RBAC Authorization
  ↓
Does role have permission?
  ↓
YES → Allow
NO  → 403 Forbidden
```

If token is missing/invalid:

```text id="m8x1q0"
Invalid / Missing Token
        ↓
401 Unauthorized
```

If token is valid but user doesn't have permission:

```text id="n7r4cw"
Valid Token
    ↓
No Required Permission
    ↓
403 Forbidden
```

### 🎯 Interview answer

> **“We prevent unauthorized access by first validating the JWT access token and then checking RBAC permissions for the requested resource. Invalid or missing authentication results in a 401 response, while an authenticated user without sufficient permissions receives a 403 response.”**

---

# 🔥 Complete ICIP security flow

This is the flow you should keep in your mind:

```text id="m0v5fd"
                User
                 ↓
              Login
                 ↓
          Username + Password
                 ↓
          Authentication
                 ↓
      Access + Refresh Tokens
                 ↓
             Client
                 ↓
       Protected API Request
                 ↓
          JWT Validation
                 ↓
       Identify Authenticated User
                 ↓
        RBAC Authorization
                 ↓
       ┌─────────┴─────────┐
       ↓                   ↓
   Permission             No Permission
      ✅                      ❌
       ↓                      ↓
 Access Resource          403 Forbidden
       ↓
 Important Action
       ↓
  Audit Logging
       ↓
 PostgreSQL / Audit Pipeline
```

## 🎯 45-second interview answer

> **“In our ICIP project, we secured REST APIs using JWT authentication and RBAC authorization. After login, the user receives an access token and refresh token. The access token is used for protected API requests, and when it expires, the refresh token is used to obtain a new access token. For every protected request, we validate the JWT and identify the user, then RBAC checks whether that user's role has permission to access the requested resource. We also maintained audit logs for important actions such as claim updates and approvals, storing structured audit information in PostgreSQL for traceability and compliance.”**

### 🧠 Super-easy memory

**JWT → Who is the user?**

**RBAC → What can the user do?**

**Access Token → Access API**

**Refresh Token → Get new access token**

**Audit Log → Who did what and when?**

**PostgreSQL → Store structured audit records**
