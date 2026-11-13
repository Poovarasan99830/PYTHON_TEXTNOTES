## **Asynchronous Programming – Interview Notes (Quick Revision)**

* **Asynchronous Programming** in **FastAPI** uses **`async def`** and **`asyncio`** to handle **non-blocking I/O operations**, allowing multiple requests to be processed concurrently without waiting.
* Purpose: Improve **performance**, **scalability**, and **response time** for I/O-bound tasks such as **database queries**, **API calls**, **file uploads**, and **AI service requests**.
* **Working Flow:** **Client Request → `async def` API → Non-Blocking I/O (`await`) → Process Result → Response**.
* **ICIP Scenario:** In the **Insurance Claim Intelligence Platform**, we used **`async def`** for APIs that called **AWS Bedrock**, **Hybrid RAG (Qdrant + Elasticsearch)**, and **OCR services**. While waiting for these external services to respond, FastAPI continued processing other incoming requests, improving overall throughput.
* **Code:**

```python
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/claim-analysis")
async def analyze_claim():
    await asyncio.sleep(2)   # Simulates external API/DB call
    return {"message": "Claim Analysis Completed"}
```

> **💡 Project Explanation:** In our **Insurance Claim Intelligence Platform**, we used **`async def`** for I/O-bound operations such as **calling AWS Bedrock**, **retrieving policy documents from Qdrant and Elasticsearch**, and **integrating OCR services**. This allowed FastAPI to handle multiple claim requests simultaneously without blocking the server. For **heavy background processing**, we used **Celery + Redis**, while **`async/await`** handled fast, non-blocking external calls efficiently.
