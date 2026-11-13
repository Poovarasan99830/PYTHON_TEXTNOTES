

# -----------------------------------------------------------
## **Middleware – Interview Notes (Quick Revision)**
# -----------------------------------------------------------

* **Middleware** in **FastAPI** is a component that executes **before and after** every request/response to perform common tasks like **logging**, **CORS**, **authentication**, and **request tracking**.


* Purpose: Handle cross-cutting concerns such as **logging**, **CORS**, **authentication**, **request timing**, and **audit logging** without modifying every API.


* **Working Flow:** **Client Request → Middleware → JWT Authentication → API Logic → Middleware (Logging/Response) → Client**.


* **ICIP Scenario:** In the **Insurance Claim Intelligence Platform**, we used **Logging Middleware** to record every claim request, **CORS Middleware** to allow the React frontend to access FastAPI APIs, and **Authentication Middleware** to verify JWT tokens before processing claim requests.



* **Code:**

```python
from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()

    response = await call_next(request)

    process_time = time.time() - start
    print(f"{request.method} {request.url} - {process_time:.3f}s")

    return response
```


> **💡 Project Explanation:**
 In our **Insurance Claim Intelligence Platform**, middleware was used to **log every API request**, **validate JWT tokens**, **enable CORS** for the frontend, and **maintain audit logs** for claim processing. This improved security, monitoring, and troubleshooting.

---






# -----------------------------------------------------------
# **Security – Interview Notes (Quick Revision)**
# -----------------------------------------------------------

* **Security** in **FastAPI** protects APIs using **JWT Authentication**, **OAuth2**, **Role-Based Access Control (RBAC)**, **password hashing**, and **HTTPS** to ensure only authorized users can access resources.

* Purpose:
 Prevent **unauthorized access**, protect **sensitive claim data**, verify user identity, and enforce user permissions.

* **Working Flow:** 
**Client Login → JWT Token Generated → Client Sends Token → FastAPI Verifies Token → RBAC Check → API Logic → Response**.

* **ICIP Scenario:** 
In the **Insurance Claim Intelligence Platform**, users logged in to receive a **JWT token**. Every request included this token, and FastAPI validated it before allowing actions like **Upload Claim**, **Verify Policy**, or **Approve Claim**. **RBAC** ensured only **Claims Officers** or **Admins** could approve claims.



* **Code:**

```python
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.get("/claims")
def get_claims(token: str = Depends(oauth2_scheme)):
    return {"message": "Authorized User"}
```

> **💡 Project Explanation:** 
In our **Insurance Claim Intelligence Platform**, we implemented **JWT Authentication** for secure login and **RBAC** to control access based on user roles (**Customer**, **Claims Officer**, and **Admin**). This ensured only authorized users could perform sensitive claim operations while maintaining data security and compliance.


# -------------------------------
### **CORS – Full Form**
# -------------------------------

**CORS = Cross-Origin Resource Sharing**

---

### **Simple Explanation (Tanglish)**

**Cross-Origin** means **one website trying to access another website/server**.

Example:

* **Frontend (React):** `http://localhost:3000`
* **Backend (FastAPI):** `http://localhost:8000`

Here,

* **Origin 1** = `localhost:3000`
* **Origin 2** = `localhost:8000`

Since the **port numbers are different**, the browser treats them as **different origins**.

By default, the browser **blocks** this request for security.

**CORS** allows the backend to tell the browser:

> **"It's okay. I trust this frontend. Allow the request."**

---

### **Real-Time ICIP Example**

In your **Insurance Claim Intelligence Platform**:

* **React Frontend** → `http://localhost:3000`
* **FastAPI Backend** → `http://localhost:8000`

When the Claims Officer clicks **"Upload Claim"**, the React app sends a request to the FastAPI backend.

Without **CORS**, the browser blocks the request.

With **CORS Middleware**, FastAPI allows the React frontend to access its APIs.

**Flow:**

```text
React Frontend
(localhost:3000)
        │
        ▼
Browser checks Origin
        │
        ▼
FastAPI CORS Middleware
        │
        ▼
Origin Allowed?
        │
   Yes ─────► Request reaches API
   No  ─────► Browser blocks request
```

---

### **FastAPI Code**

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```


### **Interview Answer (30 Seconds)**

> **CORS (Cross-Origin Resource Sharing)** is a browser security mechanism that allows a frontend from one origin (for example, `localhost:3000`) to access a backend hosted on another origin (for example, `localhost:8000`). In FastAPI, we configure **`CORSMiddleware`** to specify which origins, HTTP methods, and headers are allowed. In our **Insurance Claim Intelligence Platform**, we used CORS to enable the React frontend to securely communicate with the FastAPI backend.
# -------------------------------