## **ORM Choices – Interview Notes (Quick Revision)**

* **ORM (Object Relational Mapper)** lets us interact with the **database using Python classes and objects** instead of writing raw SQL queries.
* Purpose: Simplify **database operations**, improve code readability, and support **CRUD** with ORMs like **SQLAlchemy (sync)**, **Tortoise ORM (async)**, and **Gino (async PostgreSQL)**.
* **Working Flow:** **Client Request → FastAPI API → ORM → PostgreSQL/MySQL → Response**.
* **ICIP Scenario:** In the **Insurance Claim Intelligence Platform**, we used **SQLAlchemy** with **PostgreSQL** to manage **Claims**, **Policies**, **Users**, and **Audit Logs**, reducing manual SQL queries and improving maintainability.
* **Code:**

```python
from sqlalchemy import Column, Integer, String
from database import Base

class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True)
    policy_no = Column(String)
    status = Column(String)
```

> **💡 Project Explanation:** We chose **SQLAlchemy** because our ICIP project used **PostgreSQL** with complex relationships (Claims, Policies, Users) and integrated well with **Alembic** for database version control.

---

# **CRUD Operations – Interview Notes (Quick Revision)**

* **CRUD** stands for **Create, Read, Update, and Delete**, the four basic database operations performed through the ORM.
* Purpose: Manage application data without writing raw SQL by using ORM methods like **`add()`**, **`query()`**, **`commit()`**, **`update()`**, and **`delete()`**.
* **Working Flow:** **Client Request → FastAPI API → SQLAlchemy CRUD → PostgreSQL → Response**.
* **ICIP Scenario:** In the **Insurance Claim Intelligence Platform**, we performed CRUD operations for **Claim Registration**, **Policy Verification**, **Claim Status Updates**, and **Claim Deletion**.
* **Code:**

```python
# Create
db.add(claim)
db.commit()

# Read
claim = db.query(Claim).filter(Claim.id == 1).first()

# Update
claim.status = "Approved"
db.commit()

# Delete
db.delete(claim)
db.commit()
```

> **💡 Project Explanation:** Every claim submitted by a customer was **created**, claims were **retrieved** during verification, **updated** after AI analysis or officer approval, and deleted only by authorized administrators when required.

---

# **Migrations (Alembic) – Interview Notes (Quick Revision)**

* **Alembic** is the **database migration tool** for **SQLAlchemy**, used to track and apply database schema changes without losing existing data.
* Purpose: Version-control the database by creating and applying migrations whenever **tables**, **columns**, or **relationships** change.
* **Working Flow:** **Model Change → Alembic Migration → Database Schema Updated → Application Uses New Schema**.
* **ICIP Scenario:** In the **Insurance Claim Intelligence Platform**, whenever we added new fields like **claim_status**, **risk_score**, or **approved_by**, we generated an **Alembic migration** and updated the PostgreSQL database safely.
* **Code:**

```bash
alembic revision --autogenerate -m "Add claim_status column"
alembic upgrade head
```

> **💡 Project Explanation:** During ICIP development, the claim model changed multiple times as new business requirements were introduced. Instead of manually altering PostgreSQL tables, we used **Alembic** to generate migration scripts, ensuring all developers and environments stayed in sync with the latest database schema.




**Alembic** is the **database migration tool** for **SQLAlchemy**.

### Simple Meaning (Tanglish)

Imagine your database is already running.

Initially your **Claim** table looks like this:

```text
Claims
------
id
customer_name
amount
```

Later, the client asks:

> "We need a new column called `claim_status`."

Without Alembic:

* Open PostgreSQL manually.
* Write `ALTER TABLE` SQL.
* Every developer must do it manually.
* Production server must also be updated manually.

❌ Time-consuming and error-prone.

---

### With Alembic

You only change your SQLAlchemy model:

```python
class Claim(Base):
    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    amount = Column(Integer)
    claim_status = Column(String)
```

Then run:

```bash
alembic revision --autogenerate -m "Add claim_status"
alembic upgrade head
```

Alembic automatically generates the SQL and updates the database safely.

---

### Real-Time ICIP Example

In your **Insurance Claim Intelligence Platform**:

Initially:

```text
Claims
------
id
policy_number
claim_amount
```

New requirement:

* AI Risk Score
* Claim Status
* Approved By

Instead of manually updating PostgreSQL, you:

```bash
alembic revision --autogenerate -m "Add AI fields"
alembic upgrade head
```

Now every developer and every environment has the **same database structure**.

---

### Interview One-Liner

> **Alembic is the migration tool for SQLAlchemy that tracks database schema changes and updates the database safely without losing existing data. It provides version control for the database, just like Git provides version control for source code.**
