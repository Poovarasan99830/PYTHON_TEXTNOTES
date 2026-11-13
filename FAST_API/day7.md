## **Security – Interview Notes (Quick Revision)**

* **Security** in **FastAPI** protects APIs using **OAuth2**, **JWT Authentication**, and **API Keys** to ensure only **authenticated** and **authorized** users can access protected resources.
* Purpose: Verify user identity (**Authentication**), control user permissions (**Authorization**), and secure APIs from unauthorized access using **JWT tokens** or **API Keys**.
* **Working Flow:** **Client Login → OAuth2 Verifies Credentials → JWT Token Generated → Client Sends Token/API Key → FastAPI Validates → API Logic → Response**.
* **ICIP Scenario:** In the **Insurance Claim Intelligence Platform**, users logged in using **OAuth2**, received a **JWT token**, and included it in every request. FastAPI validated the token before allowing operations like **Upload Claim**, **Policy Verification**, or **Claim Approval**. For third-party integrations (such as **OCR** or external insurance services), we secured APIs using **API Keys**.
* **Code:**

```python
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.get("/claims")
def get_claims(token: str = Depends(oauth2_scheme)):
    return {"message": "Authorized User"}
```

---

## **OAuth2 vs JWT vs API Key (Interview Difference)**

| **Feature**       | **OAuth2**               | **JWT**                   | **API Key**                 |
| ----------------- | ------------------------ | ------------------------- | --------------------------- |
| **Purpose**       | Authentication Framework | Token Format              | Identify Client/Application |
| **Used For**      | User Login               | Secure API Access         | Service-to-Service APIs     |
| **Contains**      | Login Flow               | User Information (Claims) | Secret Key                  |
| **Expiry**        | Uses Access Tokens       | Yes (Token Expiry)        | Usually No (Configurable)   |
| **Project Usage** | User Login               | Claim APIs                | OCR & Third-Party APIs      |

---

### **💡 Project Explanation (ICIP)**

In our **Insurance Claim Intelligence Platform**, **OAuth2** handled the user login process. After successful login, FastAPI generated a **JWT token**, which the client included in the **Authorization** header for every request. Each protected API validated the JWT token and checked **RBAC** permissions before processing the claim. For integrations with **OCR services** and other external systems, we used **API Keys** to authenticate trusted applications securely.
