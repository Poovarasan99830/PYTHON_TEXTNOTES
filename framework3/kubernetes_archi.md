

# ___________________________________________________
# Kubernetes Architecture (High Level)
# ___________________________________________________




Kubernetes has **2 main parts**:

```
1. Control Plane (Master)
2. Worker Nodes
```

# ___________________________________________________
# 🧠 1. Control Plane (Brain of Kubernetes)
# ___________________________________________________



👉 This controls everything (decision making)

### Components:

---

## 🔹 API Server (kube-apiserver)

* Entry point of Kubernetes
* All commands go through this

👉 Example:

```bash
kubectl apply -f deployment.yaml
```

➡️ goes to API Server

### Simple:

👉 **API Server = Gate / Front Door**

---

## 🔹 etcd

* Database of Kubernetes
* Stores cluster data (pods, services, config)

### Simple:

👉 **etcd = Brain memory**

---

## 🔹 Scheduler (kube-scheduler)

* Decides **which node** will run your pod

👉 Based on:

* CPU
* Memory
* Availability

### Simple:

👉 **Scheduler = Job assign pannura HR**

---

## 🔹 Controller Manager

* Maintains desired state

👉 Example:

* You say: 2 pods
* 1 pod crash → automatically create new pod

### Simple:

👉 **Controller = Supervisor**

---


# ___________________________________________________
# 🖥️ 2. Worker Nodes (Where app runs)
# ___________________________________________________

👉 Actual application runs here

---

## 🔹 Kubelet

* Agent running on each node
* Talks to API server
* Ensures containers are running

### Simple:

👉 **Kubelet = Node manager**

---

## 🔹 Container Runtime

* Runs containers

👉 Examples:

* Docker (older)
* containerd (most used)

### Simple:

👉 **Runtime = Engine**

---

## 🔹 Kube Proxy

* Handles networking
* Load balances traffic

### Simple:

👉 **Kube Proxy = Network router**

---

# 📦 How everything works (Flow)

### Step-by-step:

1. You apply deployment

   ```
   kubectl apply -f deployment.yaml
   ```

2. API Server receives request

3. etcd stores configuration

4. Scheduler selects node

5. Kubelet creates pod on node

6. Container runtime runs app

7. Service + kube-proxy handles traffic

---

# 🧩 Diagram (Easy View)

```
        [ User / kubectl ]
                 |
          [ API Server ]
                 |
     -------------------------
     |    Control Plane     |
     | etcd | Scheduler | Controller |
     -------------------------
                 |
        -----------------
        |   Worker Node |
        |---------------|
        | Kubelet      |
        | Kube Proxy   |
        | Containers   |
        -----------------
```

---

# 🧠 Real-life analogy

🏢 Company structure:

* CEO → Control Plane
* HR → Scheduler
* Manager → Controller
* Workers → Pods
* Office → Worker Nodes
* Reception → Service

---

# 🔥 One-line summary

👉 **Control Plane manages everything**
👉 **Worker Nodes run your application**

---

# 🎯 Interview Answer (Short)

> Kubernetes architecture consists of a Control Plane (API server, scheduler, controller, etcd) that manages the cluster, and Worker Nodes (kubelet, container runtime, kube-proxy) that run the application workloads.


