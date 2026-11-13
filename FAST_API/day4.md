### **Response Handling – Interview Notes (Quick Revision)**

* **Response Handling** in **FastAPI** controls **what data**, **status code**, and **response format** are sent back to the client after processing a request.

* Purpose: Return **JSON**, set **HTTP status codes** (200, 201, 404, etc.), or send custom responses using **JSONResponse**, **HTMLResponse**, and **FileResponse**.

* **Working Flow:** **Client Request → FastAPI API → Process Data → Generate Response → Client**.

* **Scenario:** After a user logs in successfully, the API returns **200 OK** with user details in **JSON**. If the user is not found, it returns **404 Not Found**.

* **Code:**

```python
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/login")
def login():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Login Successful",
            "user": "Arun"
        }
    )
```

### Common Response Classes

| **Response Class** | **Purpose**          | **Example Use Case**       |
| ------------------ | -------------------- | -------------------------- |
| **JSONResponse**   | Returns JSON data    | Login, CRUD APIs           |
| **HTMLResponse**   | Returns HTML content | Simple web page            |
| **FileResponse**   | Returns a file       | Download PDF, Image, Excel |
