# Day 86–90: Final Capstone Project

## Goal
Build a **real production-style microservices application** using:
   * Flask/Django
   * Docker
   * Kubernetes
   * Cloud Deployment
   * Auto Scaling
    * CI/CD Pipeline

       This project combines everything learned in previous phases.



# ---------------------------------
# 🔹 What is a Capstone Project?
# ---------------------------------


A **Capstone Project** is a final real-world project.

Companies use this to check:

✅ Architecture knowledge
✅ Backend development
✅ DevOps skills
✅ Deployment knowledge
✅ Problem-solving ability


# ---------------------------------
# 🔹 Project Architecture
# ---------------------------------

You will create:
## 1️⃣ User Service
# ---------------------------------


Handles:
 * User profile
 * User details
 * Registration

Example APIs:
GET /users
POST /users


## 2️⃣ Product Service
# ---------------------------------


Handles:

* Product list
* Product details
* Product management

Example APIs:
GET /products
POST /products


## 3️⃣ Order Service
# ---------------------------------
Handles:
 * Orders
 * Purchase history

Example APIs:
GET /orders
POST /orders


## 4️⃣ Auth Service
# ---------------------------------

Handles:
 * Login
 * JWT Authentication
 * Token validation

Example APIs:
POST /login
POST /register

# 🔹 Why Microservices?
# ---------------------------------
Instead of one big application:
    ❌ Monolithic Application
We split into small services:

✅ Independent deployment
✅ Easier scaling
✅ Better maintenance
✅ Real company architecture


# 🔹 Project Flow
# --------------------------

Client
   ↓
API Gateway / Ingress
   ↓
--------------------------------
| User Service                |
| Product Service             |
| Order Service               |
| Auth Service                |
--------------------------------
   ↓
Database




# ---------------------------------
# 🔹 Step 1: Create Flask/Django Services
# ---------------------------------

Example Flask App:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "User Service Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

Create separate folders:

```text
project/
│
├── user-service/
├── product-service/
├── order-service/
└── auth-service/
```

---
# ---------------------------------
# 🔹 Step 2: Dockerize Services
# ---------------------------------

Each service gets its own Dockerfile.

Example:

```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

Build image:

```bash
docker build -t user-service .
```

Run container:

```bash
docker run -p 5000:5000 user-service
```

---
# ---------------------------------
# 🔹 Why Docker?
# ---------------------------------

Docker gives:

✅ Same environment everywhere
✅ Easy deployment
✅ Isolation
✅ Portable applications

---
# ---------------------------------
# 🔹 Step 3: Push Images to Cloud Registry
# ---------------------------------

Examples:

* Docker Hub
* Amazon Web Services ECR
* Google Cloud Artifact Registry

Push image:

```bash
docker tag user-service username/user-service

docker push username/user-service
```

---
# ---------------------------------
# 🔹 Step 4: Deploy to Kubernetes
# ---------------------------------

Create deployment YAML:

```yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: user-service

spec:
  replicas: 2

  selector:
    matchLabels:
      app: user-service

  template:
    metadata:
      labels:
        app: user-service

    spec:
      containers:
      - name: user-service
        image: username/user-service
        ports:
        - containerPort: 5000
```

Apply:

```bash
kubectl apply -f deployment.yaml
```

---
# ---------------------------------
# 🔹 Kubernetes Service
# ---------------------------------

Expose application:

```yaml
apiVersion: v1
kind: Service

metadata:
  name: user-service

spec:
  selector:
    app: user-service

  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000

  type: LoadBalancer
```

---

# 🔹 Why Kubernetes?

Kubernetes provides:

✅ Auto-healing
✅ Scaling
✅ Load balancing
✅ Container orchestration
✅ High availability

---
# ---------------------------------
# 🔹 Step 5: Enable Auto Scaling
# ---------------------------------

Horizontal Pod Autoscaler (HPA):

```bash
kubectl autoscale deployment user-service \
--cpu-percent=50 \
--min=2 \
--max=10
```

---
# ---------------------------------
# 🔹 What Happens Behind the Scenes?
# ---------------------------------

If traffic increases:

```text
More Users
     ↓
CPU Usage Increases
     ↓
HPA Detects Load
     ↓
Creates More Pods
```

If traffic decreases:

```text
Less Load
    ↓
Pods Reduced Automatically
```

---
# ---------------------------------
# 🔹 Step 6: Add CI/CD Pipeline
# ---------------------------------

## CI/CD Meaning

### CI → Continuous Integration

Automatically:

✅ Build code
✅ Run tests
✅ Check errors

### CD → Continuous Deployment

Automatically:

✅ Deploy application
✅ Update Kubernetes

---

# 🔹 Example GitHub Actions Pipeline

```yaml
name: Deploy

on:
  push:
    branches:
      - main

jobs:
  build:

    runs-on: ubuntu-latest

    steps:

    - uses: actions/checkout@v3

    - name: Build Docker Image
      run: docker build -t user-service .

    - name: Deploy
      run: kubectl apply -f deployment.yaml
```

---
# ---------------------------------
# 🔹 Step 7: Add Documentation
# ---------------------------------


Documentation should include:

## Project Overview

Explain:

* What project does
* Services used
* Architecture

---

## Installation Steps

```bash
git clone project-url

docker-compose up
```

---

## API Documentation

Example:

```text
GET /products
POST /orders
POST /login
```

---

## Deployment Steps

Explain:

* Docker build
* Kubernetes deployment
* CI/CD setup

---

# 🔹 Real Production Concepts Used

This project teaches:

✅ Backend Development
✅ REST APIs
✅ Authentication
✅ Docker
✅ Kubernetes
✅ Cloud Deployment
✅ Auto Scaling
✅ CI/CD
✅ DevOps Workflow



# ---------------------------------
# 🔹 Real Company Workflow
# ---------------------------------

```text
Developer Writes Code
        ↓
Git Push
        ↓
CI/CD Pipeline Triggered
        ↓
Docker Image Built
        ↓
Image Pushed to Registry
        ↓
Kubernetes Deploys App
        ↓
Users Access Application
```



# ------------------------
# 🔹 Final Outcome
# ------------------------


After completing this project, you can say:

✅ Built Microservices Architecture
✅ Deployed on Kubernetes
✅ Implemented Auto Scaling
✅ Configured CI/CD
✅ Worked with Cloud Deployment
✅ Created Production-style Backend System

---

# 🔹 Interview Questions
## 1️⃣ Why Microservices?

Answer:

* Independent services
* Easy scaling
* Better maintenance


## 2️⃣ Why Docker?

Answer:

* Portable environment
* Same setup everywhere

---

## 3️⃣ Why Kubernetes?

Answer:

* Auto scaling
* Auto healing
* Container orchestration

---

## 4️⃣ What is HPA?

Answer:

Horizontal Pod Autoscaler automatically increases/decreases pods based on CPU or memory usage.

---

## 5️⃣ What is CI/CD?

Answer:

Automated build, testing, and deployment pipeline.

---

# 🔹 Final Learning Result

By Day 90 you become familiar with:

✅ Backend Development
✅ Cloud Deployment
✅ DevOps Basics
✅ Kubernetes
✅ Production Architecture
✅ Real-world Deployment Workflow
