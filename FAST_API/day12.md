## **API Versioning – Interview Notes (Quick Revision)**

* **API Versioning** is the practice of maintaining **multiple versions** of an API (such as **v1**, **v2**) so new changes don't break existing client applications.
* Purpose: Support **backward compatibility**, allow new features, and let old and new clients use different API versions simultaneously.
* **Working Flow:** **Client Request → `/api/v1` or `/api/v2` → FastAPI Router → Business Logic → Response**.
* **ICIP Scenario:** In the **Insurance Claim Intelligence Platform**, **v1** returned basic claim details, while **v2** included **AI Claim Analysis**, **Risk Score**, and **Hybrid RAG recommendations** without affecting existing clients using **v1**.
* **Code:**

```python
from fastapi import FastAPI, APIRouter

app = FastAPI()

v1 = APIRouter(prefix="/api/v1")
v2 = APIRouter(prefix="/api/v2")

@v1.get("/claims")
def get_claims_v1():
    return {"version": "v1", "message": "Basic Claim Details"}

@v2.get("/claims")
def get_claims_v2():
    return {
        "version": "v2",
        "message": "Claim Details with AI Analysis"
    }

app.include_router(v1)
app.include_router(v2)
```

> **💡 Project Explanation:** In our **Insurance Claim Intelligence Platform**, API versioning allowed us to introduce **AI-powered features** like **OCR**, **Hybrid RAG**, and **AWS Bedrock claim analysis** in **v2**, while existing applications continued using **v1** without any code changes. This ensured smooth upgrades and backward compatibility.
















