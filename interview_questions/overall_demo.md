## 1. What was your role?

> “I worked as a Python Backend Developer. My responsibilities included developing REST APIs using FastAPI/Django, database integration, authentication implementation, backend logic development, API testing using Postman, and optimizing SQL queries. I also worked on AI feature integration and background task processing using Celery.”

---

## 2. What was your team size?

> “Our team size was around 5 to 8 members including backend developers, frontend developers, QA testers, and project manager.”

OR

> “Backend team had around 3 developers and we worked closely with frontend and testing teams.”

---

## 3. What architecture did you use?

> “We used Microservices Architecture for scalability and easier maintenance. Different services were separated for authentication, incident processing, notifications, and reporting.”

If interviewer asks simple:

> “Frontend and backend were separated using REST APIs.”

---

## 4. How many APIs did you develop?

> “I developed and maintained around 20+ REST APIs including authentication APIs, incident management APIs, reporting APIs, and integration APIs.”

---

## 5. Which database did you use?

> “Mostly PostgreSQL and MySQL. PostgreSQL was used for scalable production applications and MySQL for internal management systems.”

If asked ORM:

> “We used SQLAlchemy in FastAPI and Django ORM in Django projects.”

---

## 6. What challenges did you face?

### Good Answer:

> “One major challenge was handling large log data and improving API response time. We optimized SQL queries, added Redis caching, and moved heavy processing tasks to Celery background jobs.”

Another:

> “Maintaining real-time data synchronization with external systems like Tally was challenging. We implemented scheduled background jobs and validation handling.”

---

## 7. Why FastAPI instead of Django?

> “FastAPI provides high performance, asynchronous support, automatic Swagger documentation, and better suitability for API-based microservices. It is lightweight and faster compared to traditional Django architecture.”

Short version:

> “FastAPI is faster and better for scalable API services.”

---

## 8. Why Redis and Celery used?

> “Celery was used for background task processing like log analysis, notifications, and scheduled jobs. Redis was used as the message broker and caching layer to improve performance and reduce processing time.”

Simple:

> “Celery handles background tasks and Redis manages task queue and caching.”

---

## 9. How does JWT Authentication work?

> “JWT works using token-based authentication. After successful login, the server generates a token containing encoded user information. The client sends this token in every API request header. The backend validates the token before giving access to protected resources.”

Simple flow:

1. User login
2. Server generates JWT token
3. Client stores token
4. Token sent in Authorization header
5. Backend validates token
6. Access granted

---

## 10. Explain your AI Root Cause Analyzer project

> “The project analyzes system logs and incident data using LLM APIs to identify possible root causes of production issues. FastAPI is used for backend APIs, PostgreSQL for storage, Celery for asynchronous processing, Redis for queue management, and Docker for deployment consistency.”

---

## 11. Why did you use Docker?

> “Docker helps create consistent environments across development and production. It simplifies deployment and dependency management.”

---

## 12. What is REST API?

> “REST API is a communication method between frontend and backend using HTTP methods like GET, POST, PUT, and DELETE.”

---

## 13. Difference between Flask and FastAPI

> “Flask is lightweight and flexible, but FastAPI provides async support, automatic API documentation, and better performance for modern API applications.”

---

## 14. Explain Microservices in simple words

> “Instead of building one large application, microservices divide the system into smaller independent services. Each service handles a specific functionality and can be deployed separately.”

---

## 15. Why should we hire you?

> “I have 3+ years of backend development experience with Python frameworks like Django and FastAPI. I have hands-on experience in API development, database optimization, authentication systems, and AI-integrated applications. I can quickly adapt and contribute to scalable backend systems.”
