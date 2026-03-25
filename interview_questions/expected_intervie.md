


# ______________________________________________________________
# 🔹 FRAMEWORK – 2
# ______________________________________________________________

## 1️⃣ Middleware

### 🎯 Interview Questions

1. What is middleware in web frameworks?

2. How middleware works in Flask vs Django?

3. Difference between middleware and decorators?
     👉 Middleware = Global request handler
     👉 Decorator = Function-specific modifier

4. Give real-time use cases of middleware.
      
     * Authentication & authorization
     * Logging requests/responses
     * Exception handling
     * Rate limiting

5. How request–response lifecycle works with middleware?

    The request-response lifecycle in Django flows through middleware layers before reaching the view and passes back through them in reverse order after the view returns a response. Middleware acts as a processing layer that can inspect, modify, or block requests and responses globally.



# ______________________________________________________________
### 📝 Notes (Quick Revision)
# ______________________________________________________________

* **Middleware** = component that sits **between request and response**
* Intercepts HTTP request before it reaches view/controller
* Can also modify response before sending to client

**Use cases**

* Authentication & authorization
* Logging requests/responses
* Exception handling
* Rate limiting

**Django**

* Middleware classes in `MIDDLEWARE` list
* Methods: `process_request`, `process_response`, `process_exception`

**Flask**

* No built-in middleware
* Use:

  * `@app.before_request`
  * `@app.after_request`
  * WSGI middleware



# ______________________________________________________________
## 2️⃣ Database Integration & ORM
# ______________________________________________________________

### 🎯 Interview Questions

1. What is ORM? Why do we need it?


2. SQLAlchemy vs Django ORM?

 Feature          | Django ORM       | SQLAlchemy                     |
| ---------------- | ---------------- | ------------------------------ |
| Type             | Built-in ORM     | External library               |
| Flexibility      | Medium           | Very High                      |
| Control over SQL | Limited          | Full control                   |
| Learning Curve   | Easy             | Moderate / Hard                |
| Query Style      | Pythonic, simple | Core + ORM modes               |
| Use With         | Django only      | Flask, FastAPI, any Python app |
| Raw SQL Support  | Basic            | Advanced                       |

3. How CRUD operations work using ORM?

    ORM translates these object-oriented operations into SQL queries internally and communicates with the
    database.

4. Advantages of ORM over raw SQL?
     ORM = Safe, Clean, Fast Development
     Raw SQL = Powerful, Full Control
       
5. How database migrations work?
     



# ______________________________________________________________
### 📝 Notes
# ______________________________________________________________

**ORM (Object Relational Mapping)**

* Maps **Python classes ↔ DB tables**
* Avoids writing raw SQL

**Flask – SQLAlchemy**

```python
user = User(name="Ram")
db.session.add(user)
db.session.commit()
```

**Django ORM**

```python
User.objects.create(name="Ram")
```

**CRUD**

* Create → `add() / create()`
* Read → `query / objects.get()`
* Update → modify object + save
* Delete → `delete()`

**Best Practices**

* Use migrations
* Index frequently searched columns
* Avoid N+1 query problem

---



# ______________________________________________________________
## 3️⃣ Authentication & Authorization
# ______________________________________________________________



### 🎯 Interview Questions

1. Authentication vs Authorization?
      Checks the person's identity to grant access to the system.

      Checks the person's privileges or permissions to access the resources.

2. What is JWT? How it works?
        



3. Session-based auth vs token-based auth?

     | Session                   | JWT               |
     | ------------------------- | ----------------- |
     | Server stores session     | No server storage |
     | Needs session DB          | Stateless         |
     | Good for traditional apps | Good for APIs     |

4. What is RBAC?
     Access is given based on role, not individual user.
      
5. OAuth flow explanation?
    * OAuth = Open Authorization
    * User to login using third-party services
      WITHOUT sharing password.






# ______________________________________________________________
### 📝 Notes
# ______________________________________________________________

**Authentication** → Who are you
**Authorization** → What you can access

**JWT**

* Header + Payload + Signature
* Stateless
* Stored in client (localStorage/cookies)

**Session-based**

* Session stored on server
* Session ID stored in cookie

**RBAC**

* Roles → Permissions
* Example:

  * Admin → all access
  * User → limited access

---


# ______________________________________________________________
## 4️⃣ Security Best Practices
# ______________________________________________________________



### 🎯 Interview Questions

1. What is SQL Injection?
2. What is XSS and CSRF?
3. How to prevent CSRF in Django?
4. How passwords should be stored?
5. What is input validation?

input Validation is the process of verifying that user input is correct, safe, and within expected format before processing. It helps prevent security vulnerabilities, maintain data integrity, and avoid application crashes.

### 📝 Notes

**SQL Injection**

* Prevent using ORM & parameterized queries

**XSS**

* Malicious JS injection
* Prevent by output encoding & escaping

**CSRF**

* Fake requests from authenticated users
* Django uses **CSRF tokens**

**Password Storage**

* Never store plain text
* Use:

  * `bcrypt`
  * `pbkdf2`
  * Django’s built-in hashing

---

# ______________________________________________________________
## 5️⃣ Testing & Automation
# ______________________________________________________________

### 🎯 Interview Questions

1. Types of testing?

Unit Testing – to test individual functions or methods.
Integration Testing – to test interaction between modules (like API + DB).
Regression Testing – to ensure new changes don’t break old functionality.
API Testing – using tools like Postman.
End-to-End Testing – using tools like Selenium when needed.

2. Unit test vs integration test?

3. Pytest vs unittest?

    Pytest -->Pytest fixture na test run panna munadi required setup ready pannura reusable function.”
            -->We use pytest in our project because it is more powerful and readable compared to unittest

    unittest -->More boilerplate
             -->Needs structure
             -->Limited



4. What is CI/CD?

       CI = Continuous Integration
       CD = Continuous Deployment (or Delivery)

       CI/CD na code push pannumbothu automatic ah test, build, deploy nadakkura process.

       If any test fail...does not allow merge the code...


5. How testing fits in CI pipeline?

. Whenever a pull request is raised, unit tests and integration tests run automatically. If any test fails, the pipeline blocks the merge.




# ______________________________________________________________


### 📝 Notes

**Testing Types**

* Unit → single function
* Integration → multiple modules
* End-to-End → full system

**Pytest**

* Simple syntax
* Powerful fixtures

**CI/CD**

* CI → build + test automatically
* CD → auto deployment

---
# ______________________________________________________________
## 6️⃣ Performance Optimization
# ______________________________________________________________

### 🎯 Interview Questions

1. What causes performance bottlenecks?
      Bottleneck = System la slowest point / traffic jam
                 = Bottleneck = Slowest point in system that limits overall speed”
      
      DB queries slow
      Heavy loops / code
      Network delay
      Large static files
      No caching
      Too much traffic

2. How caching improves performance?
     Caching = Temporary storage for faster access

     Per-view cache             → Whole page cache
     Template fragment cache    → Part of page
     Low-level cache            → Store any Python object
     Cache backend              → Redis, Memcached, in-memory


3. What is database indexing?
     


4. Lazy loading vs eager loading?
      Eager loading fetches related objects in advance using joins, reducing database hits but consuming more memory.”


5. How to scale web apps?
     Vertical Scaling-->RAM,CPU
     Horizontal Scaling -->multiple server
     Caching
     Database Optimization
     CDN
     Container & Auto Scaling

### 📝 Notes

* **Caching** → Redis, Memcached
* **Indexing** → faster queries
* **Lazy loading** → load data only when needed
* Use pagination for large data

---








# ______________________________________________________________
## 7️⃣ RESTful API Design
# ______________________________________________________________


### 🎯 Interview Questions

1. What is REST?
2. REST vs SOAP?

     SOAP = Simple Object Access Protocol

     REST
        Lightweight
        JSON mostly use pannum
        Easy to use
        Fast
     SOAP
       XML based
       Strict protocol
       More security features
       Heavy format

3. HTTP methods usage?
4. What is statelessness?
5. Status codes meaning?
     HTTP status codes are standard response codes returned by the server to indicate the result of a client’s request.

### 📝 Notes

* REST = Representational State Transfer
* Uses HTTP methods:

  * GET → Read
  * POST → Create
  * PUT → Update
  * DELETE → Remove
* Stateless → server stores no client state

---




## 8️⃣ Containerization & Deployment

### 🎯 Interview Questions

1. What is Docker?
2. Image vs Container?
3. Why Kubernetes?
4. Docker vs VM?
5. Deployment strategies?

### 📝 Notes

* **Docker** packages app + dependencies
* **Kubernetes** manages containers
* Scaling, auto-healing
* Cloud: AWS, Azure, GCP




# -----------------------------------------------------------
# 🔹 FRAMEWORK – 3
# -----------------------------------------------------------


## 1️⃣ Microservices Architecture

### 🎯 Interview Questions

1. What is microservices?

2. Monolith vs microservices?

3. Benefits & challenges?
        ❌ Challenges
              Complex architecture
              Network latency
              Distributed debugging difficulty
              Data consistency issues
              DevOps complexity (Docker, Kubernetes needed)

4. Service communication methods?
            Microservices communicate in 2 main ways:
                🔹 1. Synchronous Communication
                               REST APIs (HTTP)
                               gRPC

                🔹 2. Asynchronous Communication
                               Message Brokers->---🔹 Kafka
                                                       High throughput (Short time la romba adhiga work handle panna capacity)
                                                       Partition based parallel processing
                                                       Durable storage (data disk la save aagum)
                                                       Replay messages option irukku
                                                       Large distributed systems ku best

                                               ---🔹 RabbitMQ
                                                       Traditional message queue
                                                       Small to medium scale system
                                                       Lightweight
                                                      
                              
                                                       

                               Event-driven architecture
                                              Event-Driven Architecture is a design pattern where services communicate through events instead of direct calls. A service publishes an event when something happens, and other services subscribe and react to it. This provides loose coupling, scalability, and better fault isolation





               gRPC na Google Remote Procedure Call.

               REST:Order Service → HTTP request → Payment Service
                    Data format: JSON
                    Konjam slow

               gRPC:Order Service → gRPC call → Payment Service
                    Data format: Binary (protobuf)
                    Romba fast

### 📝 Notes

* Each service independent
* Own DB
* Communicate via REST / message broker

# -----------------------------------------------------------
## 2️⃣ Serverless Computing
# -----------------------------------------------------------



### 🎯 Interview Questions

1. What is serverless?
2. AWS Lambda use cases?
3. Benefits of serverless?
4. Cold start problem?

### 📝 Notes

* No server management
* Auto scaling
* Pay per execution

---

## 3️⃣ Progressive Web Apps (PWA)

### 🎯 Interview Questions

1. What is PWA?
2. Service worker role?
3. Offline support?
4. PWA vs native app?

### 📝 Notes

* Works offline
* Installable
* Faster load

---
# -----------------------------------------------------------
## 4️⃣ Real-Time Communication
# -----------------------------------------------------------

### 🎯 Interview Questions

1. WebSocket vs HTTP?
2. SSE vs WebSocket?
3. Use cases of WebRTC?
4. Real-time chat architecture?

### 📝 Notes

* WebSocket → full duplex
* SSE → server → client
    SSE (Server-Sent Events)
* WebRTC → video/audio


# -----------------------------------------------------------
## 5️⃣ Event-Driven Architecture
# -----------------------------------------------------------

### 🎯 Interview Questions

1. What is event-driven architecture?
2. Kafka vs RabbitMQ?
3. Pub/Sub pattern?
4. CQRS?

### 📝 Notes

* Loose coupling
* Async processing
* High scalability  



👉 Event-driven architecture = System reacts to events asynchronously.
👉 Kafka = Distributed event streaming platform.
👉 RabbitMQ = Traditional message broker for reliable messaging.
👉 Pub/Sub = Publisher sends message to topic, subscribers receive.
👉 CQRS = Separate read and write models.

---

## 6️⃣ Data Pipelines & ETL

### 🎯 Interview Questions

1. What is ETL?
2. Airflow vs Luigi?
3. Use cases of data pipelines?
4. Batch vs streaming?

### 📝 Notes

* ETL → Extract → Transform → Load
* Airflow uses DAGs
* Used in analytics & ML

---

## 7️⃣ Cross-Platform Development

### 🎯 Interview Questions

1. What is cross-platform development?
2. React Native vs Flutter?
3. Pros & cons?
4. When to use native?

### 📝 Notes

* Single codebase
* Faster development
* Platform-specific optimization needed

---

## 8️⃣ CI/CD (Advanced)

### 🎯 Interview Questions

1. CI/CD pipeline flow?
2. Jenkins vs GitHub Actions?
3. Blue-green deployment?
4. Rollback strategies?

### 📝 Notes

* Automates testing & deployment
* Faster releases
* Reduced human error

