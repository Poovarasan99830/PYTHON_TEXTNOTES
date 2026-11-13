## **Testing FastAPI – Interview Notes (Quick Revision)**

* **Testing** in **FastAPI** ensures APIs work correctly using **`pytest`** and **`TestClient`** by verifying request handling, responses, and business logic before deployment.
* Purpose: Detect bugs early, validate **API endpoints**, **database operations**, **authentication**, and ensure application reliability through **Unit Tests** and **Integration Tests**.
* **Working Flow:** **Test Case (`pytest`) → `TestClient` Sends Request → FastAPI API → Validate Response → Pass/Fail Result**.
* **ICIP Scenario:** In the **Insurance Claim Intelligence Platform**, we wrote tests for APIs such as **Claim Upload**, **Policy Verification**, **JWT Authentication**, and **Claim Approval**. We verified expected **status codes**, **response data**, and **database updates** before deploying the application.
* **Code:**

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_claim():
    response = client.get("/claims/101")

    assert response.status_code == 200
    assert response.json()["status"] == "Approved"
```

> **💡 Project Explanation:** In our **Insurance Claim Intelligence Platform**, we used **`pytest`** with **`TestClient`** to automate API testing. **Unit tests** validated individual components such as claim validation and authentication logic, while **Integration tests** verified the complete workflow—from **claim submission**, **OCR processing**, **database operations**, and **AI analysis** to the final API response—ensuring the system worked correctly before every release.
