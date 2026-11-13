## **Event Handling – Interview Notes (Quick Revision)**

* **Event Handling** in **FastAPI** uses **Startup** and **Shutdown** events to execute code automatically when the application **starts** or **stops**.
* Purpose: Initialize **database connections**, **Redis**, **Kafka**, **AI models**, and release resources or close connections gracefully during application shutdown.
* **Working Flow:** **Application Starts → Startup Event → Initialize Resources → API Requests → Shutdown Event → Close Resources**.
* **ICIP Scenario:** In the **Insurance Claim Intelligence Platform**, during **Startup**, we initialized **PostgreSQL**, **Redis**, **Kafka**, and loaded **AWS Bedrock/Hybrid RAG configurations**. During **Shutdown**, we closed database connections, Redis clients, and Kafka producers to ensure proper resource cleanup.
* **Code:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup():
    print("Database and Redis Connected")

@app.on_event("shutdown")
async def shutdown():
    print("Database and Redis Disconnected")
```

> **💡 Project Explanation:** In our **Insurance Claim Intelligence Platform**, **Startup Events** prepared all required services (PostgreSQL, Redis, Kafka, and AI service configurations) before handling any claim requests. **Shutdown Events** safely released these resources, preventing connection leaks and ensuring the application shut down gracefully.
