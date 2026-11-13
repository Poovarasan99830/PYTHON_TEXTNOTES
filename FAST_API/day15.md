## **Caching – Interview Notes (Quick Revision)**

* **Caching** stores **frequently accessed data** in **memory (Redis)** so that repeated requests are served quickly without querying the database every time. In FastAPI, **`fastapi-cache`** is commonly used with **Redis**.
* Purpose: Improve **performance**, **reduce database load**, **decrease response time**, and **handle high traffic** efficiently.
* **Working Flow:** **Client Request → Check Redis Cache → Cache Hit? → Yes: Return Cached Data → No: Query Database → Store in Redis → Response**.
* **ICIP Scenario:** In the **Insurance Claim Intelligence Platform**, we cached **insurance policy details**, **frequently searched policy information**, and **user session data** in **Redis**. When the same policy was requested again, FastAPI retrieved it from Redis instead of PostgreSQL, significantly reducing response time.
* **Code:**

```python
from fastapi import FastAPI
from fastapi_cache.decorator import cache

app = FastAPI()

@app.get("/policies/{policy_id}")
@cache(expire=60)
async def get_policy(policy_id: int):
    return {
        "policy_id": policy_id,
        "status": "Active"
    }
```

> **💡 Project Explanation:** In our **Insurance Claim Intelligence Platform**, we integrated **Redis** as the caching layer to store frequently accessed **policy information** and **claim metadata**. Before querying **PostgreSQL**, FastAPI first checked Redis. If the data existed (**Cache Hit**), it returned the response immediately. Otherwise (**Cache Miss**), it fetched the data from PostgreSQL, stored it in Redis for future requests, and then returned the response. This reduced database load and improved API performance.
