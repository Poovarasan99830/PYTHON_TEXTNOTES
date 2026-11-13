

### **Pydantic – Interview Notes (Quick Revision)**


* **Pydantic** is a **data validation** library used in **FastAPI** to validate and parse request/response data using **BaseModel**.

* Purpose: Ensures **correct data types**, **required fields**, **default values**, and **validation rules** before executing API logic. Key components: **BaseModel**, **Field()**, **EmailStr**, **Optional**, **field_validator**, and **Response Model**.


* **Working Flow:** **Client Request → Pydantic Validation → FastAPI Logic → Database → Response Model → Client**.


* **Scenario:** During **User Registration**, if the user sends an invalid email or a non-integer age, **Pydantic** automatically returns a **422 Validation Error**, preventing invalid data from being stored.
* **Code:**



```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    name: str
    email: EmailStr
    age: int

@app.post("/register")
def register(user: User):
    return {
        "message": "User registered successfully",
        "data": user
    }
```
