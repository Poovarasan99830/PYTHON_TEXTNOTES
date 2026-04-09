
# _____________________________
# Summary
# _____________________________



Docker = App box 📦
Pod = Small house 🏠
Deployment = Robot order 📜
Service = Gate 🚪
Scaling = More houses 📈
Rolling update = Safe change 🔄
Rollback = Undo 🔙
Ingress = Smart gate name 🌐
Kubernetes = Super robot 🤖



# _____________________________
# Kubernetes 
# _____________________________

Kubernetes is an open-source container orchestration platform used to automate deployment, scaling, and management of containerized applications



# _____________________________
# Day 21–25: Kubernetes Basics**
# _____________________________


Minikube    ---->  Small practice kingdom(Minikube is just a tool to run Kubernetes locally (on your laptop))

Docker      ---->  App box 

Pod         ---->  Small house (One house = One app copy)

Deployment   ----> En app 3 houses la irukanum
             ----> So immediately:3 pods build pannum
             ----> If one house collapse:King builds new house immediately
            
Service     ---->Main Gate---->Fixed address
                          ---->Auto update
                          ---->Load balancing

                          Main Gate (Service) does 2 jobs:
                             1️⃣ Permanent address kudukkum
                             2️⃣ Inside houses ku distribute pannum



What is Minikube
     Minikube is just a tool to run Kubernetes locally (on your laptop).
     It creates a single-node Kubernetes cluster for learning/testing.
    👉 It does NOT manage pods directly

Who actually recreates pods?
   Inside Kubernetes, there are controllers:
   1️⃣ Kubernetes Controllers
         These are responsible for maintaining desired state.
         Important ones:
             Deployment
             ReplicaSet
             StatefulSet

| Component  | Role                       |
| ---------- | -------------------------- |
| Minikube   | Runs Kubernetes locally    |
| Kubernetes | Manages cluster            |
| Deployment | Ensures pod always running |







Deployment ensures high availability by maintaining the desired number of pod replicas. If any pod fails or is deleted, it automatically recreates a new pod to match the desired state.

Who is the “King” here?
   The “King” = Deployment Controller

It continuously checks: 
    “Still 3 pods running ah?”


replicas: 3
“I want 3 houses (pods) always”

Kubernetes builds houses
    Creates:
        Pod 1 🏠
        Pod 2 🏠
        Pod 3 🏠
    Now system is stable

Now system is stable
   kubectl delete pod pod-1
   Now only 2 pods left

King reacts immediately
   Deployment checks:
      “Expected = 3, Current = 2 ❌”

   So it creates:
       New Pod 🏠
   Back to normal
       Again 3 pods running ✅

| Desired | Current | Action       |
| ------- | ------- | ------------ |
| 3 pods  | 2 pods  | Create 1 pod |
| 3 pods  | 4 pods  | Delete 1 pod |


“En app 3 houses la irukanum” → replicas: 3
King (Deployment) always check pannum
Oru house (pod) destroy aana:
👉 “dei 3 venum la!” nu
👉 pudhu house build pannum
👉 Athu than auto healing

# _____________________________
# Day 26–30: Kubernetes Networking
# _____________________________
     
     🟢 ClusterIP     = Internal Road
     🟡 NodePort      = Small Public Gate
     🔵 LoadBalancer  = Big Royal Gate
      
      All these rules write pannurathu:
          📄 YAML scrolls (deployment.yaml, service.yaml)
             These scrolls tell the king what to build.

      Cluster = Many servers working together as one team
                 Kubernetes always cluster mela dhaan run pannum.


# ---------------------------------------------------------------------------------
King = Kubernetes Control Plane which reads YAML and enforces the desired state
What does the King do?

The King (Kubernetes Control Plane) includes:
    API Server → receives your YAML 📄
    Controller Manager → checks rules (like Deployment)
    Scheduler → decides where pod should run

    Together, they act like a King who manages everything


Flow using your analogy
1️⃣ You write YAML (scroll 📄)---->“Enaku 3 houses venum”
2️⃣ King reads it----->👉 Kubernetes API Server accepts your YAML
3️⃣ King gives order---->👉 Deployment Controller says:“Build 3 pods!”
4️⃣ Workers build houses--->👉 Nodes (machines) create actual pods 🏠
# ---------------------------------------------------------------------------------


      Cluster Structure (Simple)
         Inside cluster rendu type servers irukkum:
             1️⃣ Control Plane (Brain) 🧠
             2️⃣ Worker Nodes (Workers) 👷

     One classroom computer = Server
     Full school with many classrooms = Cluster
     Principal = Kubernetes Brain

     Principal decide pannuva
     Teachers work pannuva

     Principal 👨‍🏫 = Control Plane (Brain)
     Teachers 👩‍🏫 = Worker Nodes

     Principal decide pannuva:
        Which class la teacher assign panna
        New teacher venuma
        Replace teacher venuma
        Teachers actual ah teaching pannuvaanga.





# --------------------------------------------------------------
## 1️⃣ 🏰 Control Plane (King 👑)
## 2️⃣ 🧑‍💼 Deployment Controller (Minister 📜)
## 3️⃣ 🖥️ Worker Nodes (Workers 👷)



# --------------------------------------------------------------
# 🧠 3 Important Components Difference

## 1️⃣ 🏰 Control Plane (King 👑)

👉 **Kubernetes Control Plane**

### What it does:

* Brain of Kubernetes
* Takes your YAML instructions
* Decides what should happen

### Contains:

* API Server
* Scheduler
* Controller Manager

### Example:

👉 You say: “3 pods venum”
👉 Control plane understands and plans




# --------------------------------------------------------------
## 2️⃣ 🧑‍💼 Deployment Controller (Minister 📜)

👉 Part of Control Plane

### What it does:

* Ensures **desired state = actual state**
* Manages pods using ReplicaSet

### Example:

* You set: `replicas: 3`
* It checks:

  * If 2 pods → creates 1 more
  * If 4 pods → deletes 1

👉 Auto-healing + scaling 💪



# --------------------------------------------------------------
## 3️⃣ 🖥️ Worker Nodes (Workers 👷)

👉 Machines where actual work happens

### What they do:

* Run pods (containers)
* Execute what control plane tells

### Inside worker node:

* Kubelet (agent)
* Container runtime (Docker / containerd)


# --------------------------------------------------------------
# 🔥 Full Flow (Simple)

1. You write YAML 📄
2. Control Plane (King 👑) reads it
3. Deployment Controller (Minister 📜) checks rules
4. Worker Nodes (👷) create pods


# --------------------------------------------------------------
# 📊 Easy Comparison Table

| Component             | Role     | Analogy     | Work                |
| --------------------- | -------- | ----------- | ------------------- |
| Control Plane         | Brain    | King 👑     | Decides everything  |
| Deployment Controller | Manager  | Minister 📜 | Maintains pod count |
| Worker Node           | Executor | Workers 👷  | Runs pods           |



# --------------------------------------------------------------
# 🧾 Thanglish Version

* Control Plane → “brain da” 🧠
* Deployment → “rule check pannura manager”
* Worker Node → “actual vela seiyura machine”

👉 Example:

* Nee: “3 pod venum”
* Control plane: “seri note panniten”
* Deployment: “3 iruka check pannuren”
* Worker node: “pod run panniten”


# --------------------------------------------------------------
# 🎯 Final One Line

👉 **Control Plane decides, Deployment ensures, Worker Nodes execute**


# --------------------------------------------------------------

# _____________________________
**Day 31–35: Scaling & Updates**
# _____________________________


# ________________________________________________
Scaling        → More pods when load increase
Rolling Update → Safe app update
Rollback       → Undo broken update
Ingress        → Clean public access
# ________________________________________________




# ________________________________________________
Scaling         = More workers 👷👷👷
Rolling update  = Change workers slowly 😎
Rollback        = Bring old workers back 🔙
Ingress         = Smart main gate 🚪
# ________________________________________________


SCALING – Traffic Increase Handle Pannradhu
HPA = Horizontal Pod Autoscaler
    = HPA automatically scales the number of pods based on CPU or memory usage to handle traffic efficiently.
    = Traffic adhigam aana automatic ah more pods create pannum
      Traffic kammi aana extra pods remove pannum



ROLLING UPDATES –---> Safe Version Change
                ----> Old pod remove panna munadi new pod ready pannidum — adhunaala downtime varadhu.



# ---------------------------------------------------------


Kubernetes cluster = Apartment building
🚪 Ingress = Security gate

Visitors (users) gateல வருவாங்க
Gate decide பண்ணும் யாரை எந்த flatக்கு அனுப்பணும்

Ingress-na oru security gate madhiri…
Outside traffic ellam check panni, correct service-ku anupum



# ---------------------------------------------------------
Without Ingress (Problem)
# ---------------------------------------------------------

Ingress இல்லாம இருந்தா:

    ஒவ்வொரு service-க்கும்
         separate LoadBalancer / NodePort expose பண்ணணும்
         Too many IPs / ports 😵
         Manage பண்ண ரொம்ப kashtam

    Tanglish:
          "Every service ku thani thani public IP kudutha… total mess aagidum 😅"




✅ With Ingress (Solution)

Ingress use பண்ணா:
     Single public IP / domain
     Inside Kubernetes: 
        Different services-ku route pannalam

example.com → frontend service
example.com/api → backend service
example.com/admin → admin service

"Oru single domain use pannitu, different paths moolama different services reach pannalam 🔥"



Ingress Controller (Main Brain 🧠)
     Ingress itself rules dhaan…
     Actual work pannradhu 👉 Ingress Controller


      Examples:
         NGINX Ingress
         Traefik

      Tanglish:
            "Ingress rules sollum… aana work panna oru controller venum (like NGINX) 😎"


Ingress → Service → Pod ku request pogum
User → Ingress → Service → Pod



Sample Ingress YAML (Simple)
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
spec:
  rules:
  - host: myapp.com
    http:
      paths:
      - path: /
        backend:
          service:
            name: frontend
      - path: /api
        backend:
          service:
            name: backend


Key Features of Ingress

1. Path-based Routing
2. Host-based Routing
3. SSL / HTTPS Support
4. Load Balancing




# --------------------------------------------------------
**Day 36–45: Practice Project**
# --------------------------------------------------------


# --------------------------------------------------------
# Docker Build Optimization
# --------------------------------------------------------


https://chatgpt.com/share/69d4789d-a830-83e8-aca7-5d4e61301e57




# How to optimize Docker build?

Say:
  Use slim base image
  Use layer caching (copy requirements first)
  Avoid reinstalling dependencies
  Use .dockerignore
  Reduce dependency size



# example

✅ Optimized Dockerfile (Production Style 🚀)

```dockerfile
# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only requirements first (for caching)
COPY requirements.txt .

# Upgrade pip + install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --prefer-binary -r requirements.txt

# Copy remaining files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```


docker build -t edubot-app .
docker run -p 8501:8501 -e GROQ_API_KEY=your_api_key_here edubot-app


.

# --------------------------------------------------------
# Deployment.yaml VS Service.yaml
# --------------------------------------------------------
https://chatgpt.com/share/69d32d61-03bc-83e8-87a6-72995234acbf




# Deployment.yaml VS Service.yaml

Deployment is used to manage application pods (scaling, updates, availability), while Service is used to provide stable networking and expose those pods to internal or external clients.

Deployment = Run the app
Service = Make app accessible


kubectl apply -f deployment.yaml
kubectl apply -f service.yaml



# How to access app (Docker Desktop Kubernetes)

kubectl get svc   ---->First check your service type
Example output:
    edubot-service   NodePort   10.x.x.x   <none>   8501:30007/TCP

Then open browser:
   http://localhost:30007
    
Use Port Forwarding
   kubectl port-forward service/edubot-service 8501:8501
   http://localhost:8501





# Locust 
For load testing EduBot, we expose a backend API endpoint and use Locust to simulate concurrent users sending requests, measuring response time, throughput, and system stability under load.



# Why 2 files? (Deployment + Service)

  1. Deployment → “Create & Manage Pods”
     
     kind: Deployment

     What it does:
        Pods create pannum (your app run aagum place)
        How many replicas (2 pods nu sonna → 2 copies run aagum)
        Auto restart if crash
        Scaling (increase/decrease pods)

     Deployment = App oda brain (manager)
        Real-life analogy:
           🏢 Factory manager madhiri
                  Workers (pods) assign pannuvaar
                  Worker down na replace pannuvaar

    2. Service → “Expose & Connect Pods”

       kind: Service

       What it does:
            Pods-ku stable network provide pannum
            Load balancing (2 pods irundha → traffic split)
            External/internal access allow pannum
       Important:
         👉 Pods IP change aagum (temporary)
         👉 Service gives fixed IP / DNS name
      
       Simple meaning:
          👉 Service = Reception / Router
        
        Real-life analogy:
             🏢 Office reception madhiri
             Outside people → inside correct employee-kku conne
             Employees change aanaalum reception number same

# ________________________________________________






1. Docker Commands


Build image                ---->docker build -t edubot-app .    
Run container              ---->docker run -p 8501:8501 edubot-app  
List images                ---->docker images
List running containers    ---->docker ps
Stop container             ---->docker stop <container-id>



2. Kubernetes Basic Commands

Check cluster    --->kubectl cluster-info
Check nodes      --->kubectl get nodes


3. Deployment Commands


Apply deployment --->kubectl apply -f deployment.yaml
Check deployments --->kubectl get deployment
Describe deployment --->kubectl describe deployment edubot


# ________________________________________________