## **Background Tasks – Interview Notes (Quick Revision)**

* **Background Tasks** in **FastAPI** use **`BackgroundTasks`** to execute **time-consuming operations asynchronously** after sending the API response, improving response time.
* Purpose: Run tasks like **sending emails**, **logging**, **notifications**, **file processing**, and **OCR** in the background without making the user wait.
* **Working Flow:** **Client Request → FastAPI API → Send Response → `BackgroundTasks` → Execute Background Task**.
* **ICIP Scenario:** In the **Insurance Claim Intelligence Platform**, after a customer uploaded a claim, the API immediately returned **"Claim Submitted Successfully"**. Then, **`BackgroundTasks`** started **OCR document extraction**, **claim verification**, and **notification processing** without blocking the user.
* **Code:**

```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def process_claim():
    print("Processing OCR and Claim Verification...")

@app.post("/claims")
def create_claim(background_tasks: BackgroundTasks):
    background_tasks.add_task(process_claim)
    return {"message": "Claim Submitted Successfully"}
```

> **💡 Project Explanation:** In our **Insurance Claim Intelligence Platform**, we used **`BackgroundTasks`** for lightweight tasks such as **OCR processing**, **sending email/SMS notifications**, and **audit logging** after a claim was submitted. For **long-running and scalable tasks**, such as bulk document processing and AI-based claim analysis, we used **Celery with Redis**, since `BackgroundTasks` is suitable only for simple in-process background work.
