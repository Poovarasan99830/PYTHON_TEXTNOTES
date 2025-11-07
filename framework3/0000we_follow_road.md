
## **Phase 1 (Days 1–20): Foundations + Docker**

**Goal:** Be comfortable with Flask/Django microservices and package them into containers.




# ____________________________________________________________

**Day 1–5: Microservices Basics**

* Understand monolithic vs microservice architecture.
* Build a **simple Flask API** (e.g., user management).
* Build a **simple Django API** (e.g., blog posts) using Django REST Framework.
* Learn how to separate services (each has its own routes, DB, configs).



**Day 6–10: Docker Basics**

* Install Docker Desktop.
* Learn key concepts: Image, Container, Volume, Network.
* Write your first `Dockerfile` for a Flask API.
* Run and access the container via browser.



**Day 11–15: Docker Compose**

* Learn multi-container setup (API + MySQL/PostgreSQL).
* Use `docker-compose.yml` to start both.
* Connect containers via Docker network.



# ____________________________________________________________



**Day 16–20: Practice Project**

* Build **two Flask services**:

  1. `user-service` (manages users)
  2. `product-service` (manages products)
* Run both with Docker Compose.

---

## **Phase 2 (Days 21–45): Kubernetes**

**Goal:** Orchestrate multiple containers & scale them.

**Day 21–25: Kubernetes Basics**

* Install **Minikube**.
* Learn Pods, Deployments, Services.
* Deploy your Dockerized Flask service to Minikube.

**Day 26–30: Kubernetes Networking**

* Learn ClusterIP, NodePort, LoadBalancer.
* Create Kubernetes YAML files (`deployment.yaml`, `service.yaml`).

**Day 31–35: Scaling & Updates**

* Use `kubectl scale deployment`.
* Do **rolling updates** & rollbacks.
* Add **Ingress** for cleaner URLs.

**Day 36–45: Practice Project**

* Deploy your 2-service app from Phase 1 into Kubernetes.
* Add scaling (2–5 pods per service).
* Test with **load testing tool** (e.g., `locust`).

# ____________________________________________________________

## **Phase 3 (Days 46–70): Cloud Deployment**

**Goal:** Deploy your microservices to cloud Kubernetes.

**Day 46–50: Docker Image Hosting**

* Create a **Docker Hub** account.
* Push your local images to Docker Hub.

**Day 51–60: Cloud Kubernetes**

* Choose AWS EKS / GCP GKE / Azure AKS / DigitalOcean K8s.
* Deploy your app on cloud-managed Kubernetes.
* Expose with a LoadBalancer or Cloud Ingress.

**Day 61–70: Cloud Database**

* Use a managed DB (AWS RDS / GCP CloudSQL).
* Connect Kubernetes pods to cloud DB securely.

# ____________________________________________________________

## **Phase 4 (Days 71–90): Serverless + Auto-scaling**

**Goal:** Add efficiency & modern scaling.


**Day 71–75: Serverless Basics**

* Learn AWS Lambda.
* Deploy a small Flask API as a Lambda function using Zappa/Chalice.



**Day 76–80: Kubernetes HPA**

* Install **metrics-server**.
* Enable Horizontal Pod Autoscaler (scale pods based on CPU usage).




**Day 81–85: Auto-deployment Pipelines**

* Set up GitHub Actions to:

  1. Build Docker image.
  2. Push to Docker Hub.
  3. Deploy to Kubernetes automatically.




**Day 86–90: Final Capstone Project**

* Create **3–4 Flask/Django microservices** (User, Product, Order, Auth).
* Deploy with Docker → Kubernetes → Cloud.
* Enable auto-scaling + CI/CD pipeline.
* Write documentation.
# ____________________________________________________________