




# AWS Lambda vs EC2

# -------------------------------
## 1️⃣ Purpose – Why we need this
# -------------------------------
    


### 🔹 AWS Lambda
         Used when you want to run code **without managing servers**.
    Best for:
     * Small tasks 
     * APIs
     * Automation
     * Event-based work
    Example:
     * Upload image → automatically resize image
     * User signup → send email


### 🔹 AWS EC2
      Used when you want a **full virtual server**.
      Best for:
          * Hosting websites
          * Running databases
          * Large applications
          * Full control over server
      Example:
         * Run Django app
         * Host Kubernetes cluster
         * Install software manually


# 2️⃣ Concept – What it does
# ------------------------------------
## 🔹 AWS Lambda
     AWS Lambda
     Lambda is a **serverless service**.
     You only upload code.
     AWS automatically:
        * Starts server
        * Runs code
        * Stops server
    You do NOT manage:* OS* RAM* CPU* Server maintenance



## 🔹 AWS EC2
# ------------------------------------
Amazon EC2
EC2 is a **virtual machine (server)** in cloud.
You manage:

* OS
* Software
* Security
* Scaling
* Updates

It behaves like a real computer in cloud.




# Real World Analogy
# --------------------------------

## 🔹 Lambda = Taxi
   * Use only when needed
   * Pay per ride
   * No maintenance

## 🔹 EC2 = Own Car
   * Full control
   * Can use anytime
   * Need maintenance




#  Main Difference
# -------------------------------

| Feature           | Lambda        | EC2                 |
| ----------------- | ------------- | ------------------- |
| Server Management | No            | Yes                 |
| Setup             | Very Easy     | Medium              |
| Scaling           | Automatic     | Manual/Auto Scaling |
| Billing           | Per execution | Per running time    |
| Best For          | Small tasks   | Full applications   |
| OS Access         | No            | Yes                 |
| Startup Time      | Fast          | Slower              |
| Long Running Apps | Not good      | Best                |





# 🔥 Example

## Lambda Flow
    def lambda_handler(event, context):
           print("Hello")

    AWS runs this only when triggered.



## EC2 Flow
   1. Launch server
   2. Install Python
   3. Install app
   4. Run application
   5. Maintain server



# Industry Usage
## Companies use Lambda for:
   * Notifications
   * Image processing
   * API backend
   * Automation
   * AI event triggers


## Companies use EC2 for:

    * Full web apps
    * Kubernetes
    * ML servers
    * Databases
     * Large backend systems



#  Simple One-Line Difference

## Lambda---> “Run code without managing server.”
## EC2---> “Rent a full server in cloud.”


# -----------------------------------------
#  Phase 4 (Days 71–90) — What You Actually Learn
# -----------------------------------------

This phase teaches:
     > “How real companies build scalable cloud applications.”

Before this phase:

* You deployed apps manually
* Pods run fixed count
* Servers always ON

After this phase:

* Auto scaling
* Serverless computing
* Automatic deployment
* Production-ready architecture





# -----------------------------------------
# Day 71–75 → Serverless Basics
# -----------------------------------------

## Goal
Learn:
  * AWS Lambda
  * API Gateway
  * Serverless deployment

# 🔹 What Happens Here?
      Normally Flask app runs like:
      User → EC2/Kubernetes → Flask App
      Now using Lambda:User → API Gateway → Lambda Function
      No server management.


# 🔹 Chalice vs Zappa
## 🔹 Chalice
     AWS Chalice
     AWS official Python framework for Lambda.
     Example:from chalice import Chalice
             app = Chalice(app_name='hello')
             @app.route('/')
             def index():
               return {'hello': 'world'}
    Deploy:
        chalice deploy


## 🔹 Zappa
      Zappa
      Deploy existing Flask/Django app directly to Lambda.
      Good for:
        * Flask
        * Django


# Why Companies Use Lambda?

Because:

* auto scaling
* low cost
* no server maintenance
* event-based execution

Used for:

* AI triggers
* notifications
* automation
* backend APIs






# -------------------------------
# Day 76–80 → Kubernetes HPA
# -------------------------------


## HPA Meaning
    Horizontal Pod Autoscaler
    Kubernetes

# 🔹 Problem Without HPA

Traffic ↑ But pod count same → App becomes slow



# 🔹 With HPA

Traffic ↑ CPU ↑ Kubernetes automatically creates more pods


# 🔹 metrics-server
      Kubernetes needs CPU metrics first.
      Install:kubectl apply -f metrics-server.yaml



# 🔹 Example HPA

kubectl autoscale deployment flask-app \
--cpu-percent=50 \
--min=2 \
--max=10


Meaning:

* if CPU > 50%
* create more pods
* minimum = 2
* maximum = 10


# Real Company Flow

Low Traffic  → 2 Pods
Medium       → 5 Pods
High Traffic → 10 Pods


Automatic scaling 😄



# -------------------------------
# Day 81–85 → Auto Deployment Pipeline
# -------------------------------

## Goal
  Learn CI/CD.
  CI/CD means:Code Push → Build → Test → Deploy Automatically


# 🔹 GitHub Actions
GitHub Actions
When you push code:
 * build Docker image
 * push to Docker Hub
 * deploy to Kubernetes
Automatically.


# 🔹 Real Industry Flow


Developer Push Code
        ↓
GitHub Actions
        ↓
Docker Build
        ↓
Push Docker Hub
        ↓
Deploy Kubernetes


# 🔹 Example Pipeline

name: Deploy
on: [push]
jobs:
 build:
 runs-on: ubuntu-latest


# Why Important?
Without CI/CD:
  * manual deployment
  * human mistakes
  * slow releases

With CI/CD:

  * fast deployment
  * automatic updates
  * production-ready workflow



# -------------------------------
# Day 86–90 → Final Capstone Project
# -------------------------------


## Goal

Build complete production architecture.

---

# 🔹 You Create

Microservices:

* User Service
* Product Service
* Order Service
* Auth Service

---

# 🔹 Architecture

```text id="7ff7ko"
Users
  ↓
Load Balancer
  ↓
Kubernetes Cluster
  ↓
Microservices Pods
  ↓
Database
```

---

# 🔹 Technologies Used

| Area          | Technology     |
| ------------- | -------------- |
| Backend       | Flask / Django |
| Container     | Docker         |
| Orchestration | Kubernetes     |
| Cloud         | AWS            |
| Scaling       | HPA            |
| CI/CD         | GitHub Actions |
| Registry      | Docker Hub     |

---

# 🔥 What You Learn Finally

By end of Phase 4 you understand:

✅ Serverless
✅ Auto Scaling
✅ CI/CD
✅ Production Kubernetes
✅ Cloud Deployment
✅ Microservices
✅ DevOps Workflow

---

# 🔥 Real Industry Understanding

This phase teaches:

> “How Netflix/Uber/Amazon style systems scale automatically.”

---

# 🔥 Super Simple Summary

| Topic          | Meaning                              |
| -------------- | ------------------------------------ |
| Lambda         | Run code without managing server     |
| HPA            | Auto-create pods during high traffic |
| GitHub Actions | Auto deploy code                     |
| Capstone       | Build real production project        |
# -------------------------------