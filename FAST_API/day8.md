## **Error Handling – Interview Notes (Quick Revision)**

* **Error Handling** in **FastAPI** is used to return meaningful error responses using **`HTTPException`** or **custom exception handlers**, instead of crashing the application.
* Purpose: Handle **invalid requests**, **missing resources**, **authentication failures**, and **server errors** by returning appropriate **HTTP status codes** and error messages.
* **Working Flow:** **Client Request → Validation/Business Logic → Error Occurs → `HTTPException`/Custom Exception → Error Response → Client**.
* **ICIP Scenario:** In the **Insurance Claim Intelligence Platform**, if a user searched for a **Claim ID** that didn't exist, the API returned **404 Not Found**. If an unauthorized user tried to approve a claim, the API returned **403 Forbidden** instead of exposing internal application details.
* **Code:**

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/claims/{claim_id}")
def get_claim(claim_id: int):

    if claim_id != 101:
        raise HTTPException(
            status_code=404,
            detail="Claim Not Found"
        )

    return {
        "claim_id": claim_id,
        "status": "Approved"
    }
```

---

## **Common HTTP Status Codes (Interview)**

| **Status Code** | **Meaning**           | **Example**                    |
| --------------- | --------------------- | ------------------------------ |
| **200**         | OK                    | Data Retrieved Successfully    |
| **201**         | Created               | Claim Created                  |
| **400**         | Bad Request           | Invalid Input                  |
| **401**         | Unauthorized          | Invalid JWT Token              |
| **403**         | Forbidden             | No Permission to Approve Claim |
| **404**         | Not Found             | Claim ID Not Found             |
| **500**         | Internal Server Error | Unexpected Server Error        |

---

### **💡 Project Explanation (ICIP)**

In our **Insurance Claim Intelligence Platform**, we used **`HTTPException`** to return meaningful errors such as **404** when a claim or policy was not found, **401** for invalid JWT tokens, and **403** when a user without the **Claims Officer** or **Admin** role attempted to approve a claim. This provided clear error messages to the frontend while keeping the application secure and user-friendly.
