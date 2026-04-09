

# 🚀 **Kubernetes 2-Service App — PLAYBOOK (Tanglish Guide)**

---

## 🎯 GOAL

👉 Simple-a:

* 1️⃣ Frontend (UI)
* 2️⃣ Backend (API)

👉 Then:

* Deploy in Kubernetes
* Scale (2–5 pods)
* Load test using Locust

---

# 🧩 STEP 0 — Tech Stack (Keep it Simple)

👉 Beginner-friendly stack:

* Frontend → HTML + JS (or simple React optional)
* Backend → Python (Flask)

---

# 🏗️ STEP 1 — Build Backend (API)

## 📄 `app.py`

```python
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/api")
def hello():
    return jsonify({"message": "Hello from Backend!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## 📄 `Dockerfile`

```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install flask
CMD ["python", "app.py"]
```

---

## 🔥 Build & Push

```bash
docker build -t your-dockerhub/backend .
docker push your-dockerhub/backend
```

---

# 🎨 STEP 2 — Build Frontend

## 📄 `index.html`

```html
<!DOCTYPE html>
<html>
<body>
<h1>Frontend</h1>
<button onclick="callApi()">Call Backend</button>
<p id="output"></p>

<script>
function callApi() {
  fetch("http://backend-service:5000/api")
    .then(res => res.json())
    .then(data => {
      document.getElementById("output").innerText = data.message;
    });
}
</script>
</body>
</html>
```

---

## 📄 `Dockerfile`

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html
```

---

## 🔥 Build & Push

```bash
docker build -t your-dockerhub/frontend .
docker push your-dockerhub/frontend
```

---

# ☸️ STEP 3 — Deploy to Kubernetes

## 🔹 Backend Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
spec:
  replicas: 2
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
      - name: backend
        image: your-dockerhub/backend
        ports:
        - containerPort: 5000
```

---

## 🔹 Backend Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: backend-service
spec:
  selector:
    app: backend
  ports:
    - port: 5000
      targetPort: 5000



```

---

## 🔹 Frontend Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
spec:
  replicas: 2
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: frontend
        image: your-dockerhub/frontend
        ports:
        - containerPort: 80
```

---

## 🔹 Frontend Service (NodePort)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
spec:
  type: NodePort
  selector:
    app: frontend
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30007
```

---

# 📈 STEP 4 — Add Scaling

## 🔹 Manual

```bash
kubectl scale deployment backend --replicas=5
```

---

## 🔹 Best Practice ✅

👉 Always:

* Min pods = 2
* Max pods = 5
* Use HPA (auto scaling)

---

# 🧪 STEP 5 — Load Testing

Use Locust

👉 Test:

* `/` (frontend)
* `/api` (backend)

---

# 📊 STEP 6 — Observe (VERY IMPORTANT)

```bash
kubectl get pods
kubectl top pods
```

👉 Check:

* Pods increasing?
* CPU spike?
* Response slow aa?

---

# 🧠 BEST PRACTICES (PLAYBOOK RULES)

## 🔥 Architecture Rules

✔ Separate frontend & backend
✔ Never expose backend directly
✔ Use service-to-service communication

---

## ⚙️ Kubernetes Rules

✔ Always use Deployment (not plain Pod)
✔ Use Service for communication
✔ Keep replicas ≥ 2 (high availability)

---

## 📈 Scaling Rules

✔ Start small (2 pods)
✔ Load test before scaling
✔ Use auto scaling (HPA)

---

## 🔐 Networking Rules

✔ Use internal DNS (`backend-service`)
✔ Avoid hardcoding IPs ❌

---

## 🧪 Testing Rules

✔ Always simulate real users
✔ Break your app intentionally 😈
✔ Observe behavior under load

---

# 🚀 FINAL FLOW (Your Project Roadmap)

```text
1. Build backend API
2. Build frontend UI
3. Dockerize both
4. Deploy to Kubernetes
5. Expose frontend
6. Add scaling
7. Load test
8. Observe & improve
```

---

# 🔥 FINAL Tanglish Insight

👉
"Idhu oru mini real-world system 😎
Frontend → Backend connect aagum
Traffic vandha scale aagum
Load kudutha survive aaganum — adhan goal 🔥"




Perfect 👍 now I’ll give you **ALL important Kubernetes + Docker commands** (clean notes style 🔥)

---

# 🚀 🔥 COMPLETE COMMANDS CHEAT SHEET

---

# 🐳 1. Docker Commands

## 🔹 Build image

```bash
docker build -t edubot-app .
```

## 🔹 Run container

```bash
docker run -p 8501:8501 edubot-app
```

## 🔹 List images

```bash
docker images
```

## 🔹 List running containers

```bash
docker ps
```

## 🔹 Stop container

```bash
docker stop <container-id>
```

---

# ☸️ 2. Kubernetes Basic Commands

## 🔹 Check cluster

```bash
kubectl cluster-info
```

## 🔹 Check nodes

```bash
kubectl get nodes
```

---

# 📦 3. Deployment Commands

## 🔹 Apply deployment

```bash
kubectl apply -f deployment.yaml
```

## 🔹 Check deployments

```bash
kubectl get deployment
```

## 🔹 Describe deployment

```bash
kubectl describe deployment edubot
```

---

# 📦 4. Pod Commands

## 🔹 List pods

```bash
kubectl get pods
```

## 🔹 Detailed pods

```bash
kubectl get pods -o wide
```

## 🔹 Delete pod

```bash
kubectl delete pod <pod-name>
```

## 🔹 Pod logs

```bash
kubectl logs <pod-name>
```

## 🔹 Enter pod (PowerShell friendly)

```bash
kubectl exec -it <pod-name> -- sh
```

---

# 🌐 5. Service Commands

## 🔹 Apply service

```bash
kubectl apply -f service.yaml
```

## 🔹 List services

```bash
kubectl get svc
```

## 🔹 Describe service

```bash
kubectl describe svc edubot-service
```

---

# 🌍 6. Access App

## 🔹 NodePort

```text
http://localhost:30007
```

## 🔹 Port Forward (best)

```bash
kubectl port-forward service/edubot-service 8501:8501
```

---

# 📊 7. Scaling Commands

## 🔹 Scale up/down

```bash
kubectl scale deployment edubot --replicas=3
```

## 🔹 Watch live

```bash
kubectl get pods -w
```

---

# 🔄 8. Restart / Update

## 🔹 Restart pods

```bash
kubectl delete pod -l app=edubot
```

---

# 🔐 9. Environment & Secrets

## 🔹 Create secret

```bash
kubectl create secret generic groq-secret \
--from-literal=GROQ_API_KEY=your_key
```

---

## 🔹 Check env inside pod (PowerShell fix)

First get pod name:

```bash
kubectl get pods
```

Then:

```bash
kubectl exec -it pod-name -- printenv
```

---

# 🧹 10. Cleanup Commands

## 🔹 Delete deployment

```bash
kubectl delete deployment edubot
```

## 🔹 Delete service

```bash
kubectl delete service edubot-service
```

## 🔹 Delete all

```bash
kubectl delete all --all
```

---

# 🧠 FINAL FLOW COMMANDS (STEP BY STEP)

```bash
# 1. Build Docker
docker build -t edubot-app .

# 2. Deploy to K8s
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# 3. Check
kubectl get pods
kubectl get svc

# 4. Access
kubectl port-forward service/edubot-service 8501:8501
```

---

# 🎯 ONE-LINE MEMORY

```text
build → deploy → check → access → scale → debug
```

---

# 🚀 BONUS (MOST IMPORTANT DEBUG)

```bash
kubectl get pods
kubectl logs <pod-name>
kubectl describe pod <pod-name>
```

👉 These 3 commands solve 90% issues 🔥

---















Perfect 👍 — now you are **very close to real DevOps level understanding**.
I’ll give you **FULL NOTES (start → end) with all common errors + fixes** 🚀

You can save this — it’s like your **Kubernetes troubleshooting handbook**.

---

# 📘 ☸️ Kubernetes Deployment Notes (Start → End)

---

# 🧩 STEP 1 — Prerequisites

## ✅ Required Tools

* Docker
* Docker Desktop
* kubectl

---

## ❌ ERROR 1

```text
connection refused localhost:8080
```

### 🎯 Cause:

👉 Kubernetes cluster NOT running

---

## ✅ Fix:

👉 Enable Kubernetes in Docker Desktop:

```
Settings → Kubernetes → Enable
```

---

## 🔍 Verify:

```bash
kubectl get nodes
```

✅ Output:

```text
docker-desktop   Ready
```

---

# 🐳 STEP 2 — Docker Image Build

---

## ❌ ERROR 2

```text
image not found
```

### 🎯 Cause:

👉 Docker image not built

---

## ✅ Fix:

```bash
docker build -t edubot-app .
```

---

## 🔍 Verify:

```bash
docker images
```

---

# ☸️ STEP 3 — Deployment Apply

---

## ❌ ERROR 3

```text
error validating deployment.yaml
```

### 🎯 Cause:

* Cluster not running
* YAML syntax error

---

## ✅ Fix:

```bash
kubectl apply -f deployment.yaml
```

If validation issue:

```bash
kubectl apply -f deployment.yaml --validate=false
```

---

# 🚨 STEP 4 — Pod Errors (MOST IMPORTANT)

---

# ❌ ERROR 4 (YOUR CURRENT ISSUE)

```text
ImagePullBackOff
ErrImagePull
```

---

## 🎯 Cause:

👉 Kubernetes trying to pull image from internet
👉 But image is only in local Docker

---

## ✅ Fix (BEST for Docker Desktop)

👉 Add in deployment.yaml:

```yaml
imagePullPolicy: Never
```

---

## 🔄 Re-apply:

```bash
kubectl apply -f deployment.yaml
```

---

## 🔍 Verify:

```bash
kubectl get pods
```

✅ Output:

```text
Running
```

---

# ❌ ERROR 5

```text
CrashLoopBackOff
```

---

## 🎯 Cause:

* App crash
* Missing env variables
* Wrong command

---

## ✅ Fix:

```bash
kubectl logs <pod-name>
```

👉 Example fix:

```yaml
env:
- name: GROQ_API_KEY
  value: "your_key"
```

---

# 🌐 STEP 5 — Service Issues

---

## ❌ ERROR 6

```text
App not opening in browser
```

---

## 🎯 Cause:

* Service type wrong
* Port mismatch

---

## ✅ Fix 1 — NodePort

```yaml
type: NodePort
```

---

## 🔍 Check:

```bash
kubectl get svc
```

---

## Access:

```text
http://localhost:30007
```

---

## ✅ Fix 2 — Port Forward (BEST)

```bash
kubectl port-forward service/edubot-service 8501:8501
```

👉 Open:

```text
http://localhost:8501
```

---

# ❌ ERROR 7

```text
Connection refused / timeout
```

---

## 🎯 Cause:

* Pod not running
* Wrong port

---

## ✅ Fix:

Check:

```bash
kubectl get pods
kubectl describe svc edubot-service
```

---

# 🔐 STEP 6 — Environment Variables

---

## ❌ ERROR 8

```text
GROQ_API_KEY missing
```

---

## ✅ Fix:

### Option 1 (quick)

```yaml
env:
- name: GROQ_API_KEY
  value: "your_key"
```

---

### Option 2 (secure)

```bash
kubectl create secret generic groq-secret \
--from-literal=GROQ_API_KEY=your_key
```

---

# 🔍 STEP 7 — Debug Commands (VERY IMPORTANT)

---

## 🧠 Always remember these:

```bash
kubectl get pods
kubectl get svc
kubectl get nodes
```

---

## 🔍 Deep Debug:

```bash
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

---

# 🧠 FULL FLOW (FINAL UNDERSTANDING)

```
Docker build → Image created
        ↓
Kubernetes Deployment → Pods created
        ↓
Pods run container
        ↓
Service exposes app
        ↓
Browser access
```

---

# 🎯 ALL ERRORS SUMMARY

| Error              | Reason                | Fix                     |
| ------------------ | --------------------- | ----------------------- |
| connection refused | cluster not running   | enable k8s              |
| image not found    | not built             | docker build            |
| ImagePullBackOff   | image not in registry | imagePullPolicy: Never  |
| CrashLoopBackOff   | app crash             | check logs              |
| app not opening    | service issue         | NodePort / port-forward |
| env missing        | API key missing       | add env                 |

---

# 🔥 FINAL CHECKLIST (DO THIS ALWAYS)

✔ Docker image built
✔ Kubernetes running
✔ Deployment applied
✔ Pods = Running
✔ Service created
✔ Port correct
✔ App accessible

---

# 🎤 Interview-Level Summary

> Docker is used to build container images, Kubernetes is used to deploy and manage those containers, and common issues like ImagePullBackOff occur when Kubernetes cannot find the image, which can be resolved by using local images or pushing to a registry.

---

# 🚀 NEXT LEVEL (if you want)

I can help you with:

✅ Push to Docker Hub
✅ Deploy to cloud (AWS / GCP)
✅ CI/CD pipeline
✅ Ingress (real domain URL)

---

👉 If you want, I can also **check your deployment.yaml line-by-line and fix it perfectly** 👍



