 
# ------------------------------------------------------------------
 
 **Phase 3 (Days 46–70): Cloud Deployment**

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

# ------------------------------------------------------------------


**Day 46–50: Docker Image Hosting**

* Create a **Docker Hub** account.
* Push your local images to Docker Hub.

docker login
docker tag myapp username/myapp:v1
docker push username/myapp:v1


# Day 51–60: Cloud Kubernetes Deployment