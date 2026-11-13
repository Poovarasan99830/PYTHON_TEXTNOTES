### **Dependency Injection (`Depends()`) – Interview Notes (Quick Revision)**

* **Dependency Injection (DI)**:
 in **FastAPI** uses **`Depends()`** to automatically provide shared resources like **PostgreSQL database sessions**, **JWT authentication**, **RBAC**, and **OCR/RAG 
services** without writing the same code in every API.


* Purpose: 
Reuse common components, reduce duplicate code, improve **modularity**, **maintainability**,   and **testability** by sharing **database connections**, **authentication**, and **business services**.


* **Working Flow:** 
**Client Request → `Depends()` → JWT Authentication → PostgreSQL Session → Business Logic (OCR → Hybrid RAG → Claim Processing) → Response**.


* **ICIP Scenario:** 
In the **Insurance Claim Intelligence Platform**, APIs like **Upload Claim**, **Verify Policy**, and **Approve Claim** use **`Depends(get_db)`** for the **PostgreSQL connection** and **`Depends(get_current_user)`** for **JWT authentication** and **RBAC**, instead of creating them inside every endpoint.



* **Code:**

```python
from fastapi import FastAPI, Depends

app = FastAPI()

# Database Dependency
def get_db():
    return "PostgreSQL Connected"

# Authentication Dependency
def get_current_user():
    return {"username": "claims_officer"}

@app.get("/claims")
def get_claims(
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    return {
        "message": "Claims Retrieved Successfully",
        "db": db,
        "user": user
    }
```

> **💡 Project Explanation:**
 In our **Insurance Claim Intelligence Platform**, every claim-related API required **JWT authentication** and a **PostgreSQL database connection**. Instead of repeating the same authentication and database code in each API, we used **`Depends()`** to inject these shared dependencies automatically. This kept our code clean, secure, scalable, and easy to maintain.
