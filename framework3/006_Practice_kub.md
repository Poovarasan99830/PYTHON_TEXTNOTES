

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

