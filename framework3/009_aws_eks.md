



# -------------------------------------
# Real Industry Deployment Flow
# -------------------------------------


Local Development
        ↓
Docker Containerization
        ↓
EC2 Deployment (Basic Server Hosting)
        ↓
Kubernetes / EKS (Production Scale)






# 🔹 Step 1 — Local Development
# -----------------------------------

Here developers build the application.
Example:
 * Python
 * Django
 * Flask
 * FastAPI
 * React

You run project locally:
       python app.py
       or
       npm start





# Step 2 — Docker
# ----------------------------------
## What happens?
    Application + dependencies packed into one container.
    Without Docker:
      "Works on my machine" problem
    With Docker:
      Runs same everywhere


## Example

FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python","app.py"]


Build image:
docker build -t myapp .


Run container:
docker run -p 5000:5000 myapp



# 🔹 Step 3 — EC2 Deployment
# ----------------------------------


Now deploy Docker app inside AWS server.
Server = EC2 instance



## Why companies first use EC2?
Because:
 ✅ Simple
 ✅ Cheap
 ✅ Easy learning
 ✅ Good for small apps

## Flow

Laptop
   ↓
Docker Image
   ↓
Push to DockerHub / ECR
   ↓
Pull inside EC2
   ↓
Run container



# 🔹 Problems in EC2 Deployment
Suppose:
   * 1 lakh users come
   * Server crashes
   * Need scaling
   * Need auto-healing
   * Multiple containers needed
   
   EC2 alone becomes difficult.
   So companies move to:
      # Kubernetes




# 🔹 Step 4 — Kubernetes
# ----------------------------------
Kubernetes manages containers automatically.
It handles:
 ✅ Scaling
 ✅ Load balancing
 ✅ Auto healing
 ✅ Rolling updates
 ✅ High availability



# 🔹 What is EKS?
# ----------------------------------
     EKS = Elastic Kubernetes Service
     AWS-managed Kubernetes service.

   AWS manages:
     * Control plane
     * Cluster management
     * High availability

You manage:
  * Applications
  * Pods
  * Deployments


# 🔹 EKS Architecture

Users
   ↓
Load Balancer
   ↓
Kubernetes Service
   ↓
Pods
   ↓
Containers



# 🔹 Important EKS Concepts
# ----------------------------------

## 1️⃣ Cluster
     Group of worker machines.
     Think:Apartment Complex


## 2️⃣ Node
    EC2 machine inside cluster.
   Think: One apartment

## 3️⃣ Pod
    Smallest deployable unit.
    Contains container.
    Think: Room inside apartment

## 4️⃣ Deployment
    Manages pods automatically.
    Example:
    yaml
      replicas: 3-->Means:3 copies of app run always.




## 5️Service
   Exposes application.
   Types:
     * ClusterIP
     * NodePort
     * LoadBalancer



# 🔹 LoadBalancer
# ----------------------------------
    Very important in production.
    It distributes traffic.

Example:
  1000 users
      ↓
   Load Balancer
    ↙   ↓   ↘
   Pod1 Pod2 Pod3


Benefits:
  ✅ No overload
  ✅ Better performance
  ✅ High availability




# 🔹 IAM Roles
# ----------------------------------
      IAM = Identity and Access Management
           Used for permissions.
          
          Example:
          | Role             | Permission     |
          | ---------------- | -------------- |
          | EKS Cluster Role | Manage cluster |
          | Node Role        | Pull images    |
          | App Role         | Access S3      |


# 🔹 Real Production Setup
# ----------------------------------
Production companies use:
   GitHub
     ↓
   CI/CD Pipeline
      ↓
   Docker Build
      ↓
   Push to ECR
      ↓
   Deploy to EKS
      ↓
   LoadBalancer
      ↓
    Users


# 🔹 Tools Used in Industry
# ----------------------------------

| Tool                    | Purpose                       |
| ----------------------- | ----------------------------- |
| Docker                  | Containerization              |
| Amazon Web Services EKS | Kubernetes                    |
| Kubernetes              | Container orchestration       |
| GitHub                  | Source code                   |
| Jenkins                 | CI/CD                         |
| Terraform               | Infrastructure                |
| Helm                    | Kubernetes package management |




# 🔹 Why Learn EKS?
# ----------------------------------

Because modern companies use Kubernetes heavily.

Especially:
 * Product companies
 * SaaS companies
 * AI platforms
 * FinTech
 * EdTech




# 🔹 Real Interview Important Questions
# ----------------------------------


## Basic
  * What is Kubernetes?
  * Difference between Docker and Kubernetes?
  * What is EKS?
  * What is Pod?
  * What is Deployment?
  * What is Service?


## Intermediate
  * What is LoadBalancer?
  * What is Ingress?
  * What is Auto Scaling?
  * What is ConfigMap?
  * What is Secret?


## Advanced
  * Rolling updates
  * Blue-Green deployment
  * HPA (Horizontal Pod Autoscaler)
  * Monitoring
  * Logging
  * Helm charts



# 🔹 Best Learning Order


Linux
   ↓
Docker
   ↓
EC2 Deployment
   ↓
Kubernetes Basics
   ↓
kubectl
   ↓
YAML files
   ↓
EKS
   ↓
Helm
   ↓
CI/CD



# 🔹 Final Industry Understanding
# ----------------------------------

## Small Company--->App → EC2
## Medium Company--->App → Docker → EC2
## Large Company---->App → Docker → Kubernetes → EKS


# One-Line Summary
## Docker👉 Packs application
## EC2👉 Runs application
## Kubernetes👉 Manages many containers
## EKS👉 AWS-managed Kubernetes
