


# --------------------------------------
# Day 61–70: Cloud Database in Kubernetes
# --------------------------------------

##  Goal
   Learn how real companies use managed cloud databases with Kubernetes applications.
   You will learn:
     - What is Cloud Database
     - AWS RDS / GCP Cloud SQL
     - Why companies use managed DB
     - How Kubernetes connects to DB
     - Secure DB connection
     - Environment Variables & Secrets
     - Real production architecture


# 🔹 What is a Cloud Database?
# --------------------------------------
     A database hosted and managed by cloud providers.
    Examples:
     - AWS → RDS
     - GCP → Cloud SQL
    Instead of installing MySQL manually:
       sudo apt install mysql-server


Cloud provider manages:
  * Backup
  * Scaling
  * Security
  * Replication
  * Monitoring
  * Updates


# 🔹 Popular Managed Databases

| Cloud   | Service   |
| ------- | --------- |
| AWS     | RDS       |
| GCP     | Cloud SQL |
| Azure   | Azure SQL |
| MongoDB | Atlas     |




# 🔹 What is AWS RDS?
# --------------------------------------
   AWS RDS = Relational Database Service
              AWS creates and manages database servers for you.

Supported DB:
  * MySQL
  * PostgreSQL
  * MariaDB
  * Oracle
  * SQL Server



# 🔹 What is GCP Cloud SQL?
# --------------------------------------
GCP Cloud SQL is Google’s managed database service.
Supports:
  * MySQL
  * PostgreSQL
  * SQL Server



# 🔹 Real Industry Architecture
# --------------------------------------
    User
     ↓
   Load Balancer
     ↓
   Kubernetes Pods
     ↓
   Cloud Database (RDS / Cloud SQL)




# 🔹 Why Companies Use Managed DB?
# --------------------------------------

## ✅ Easy Maintenance--->No need to manage DB server manually.
## ✅ Automatic Backup--->Cloud automatically takes backups.
## ✅ High Availability-->If one DB server fails:Another DB server takes over.
## ✅ Security--->* Encryption->* Firewall->* IAM access->* Network rules
## ✅ Scalability-->Can increase:* CPU->* RAM->* Storage

without reinstalling DB.



# 🔹 Kubernetes + Cloud DB
# ------------------------
       Pods should NOT contain database inside them.
      ❌ Wrong:Pod → MySQL installed inside pod

Reason:

* Data loss risk
* Pod restart issue
* Hard to scale

✅ Correct:Pod → External Managed DB
                  Production companies always prefer this.





# 🔹 Connecting Pod to Cloud 
# ---------------------------
Application needs:
   * DB Host
   * Username
   * Password
   * Port
   * Database Name
Example:
    DB_HOST=mydb.abc123.rds.amazonaws.com
    DB_USER=admin
    DB_PASSWORD=secret
    DB_NAME=studentdb
    DB_PORT=3306


# 🔹 Kubernetes Secret
# -------------------------
      Never hardcode passwords inside YAML.❌ Bad:yaml --->password: admin123
      
✅ Use Secret:
    kubectl create secret generic db-secret \
  --from-literal=DB_USER=admin \
  --from-literal=DB_PASSWORD=admin12


# 🔹 Use Secret in Deployment
# ---------------------------

```yaml
env:
  - name: DB_USER
    valueFrom:
      secretKeyRef:
        name: db-secret
        key: DB_USER

  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: DB_PASSWORD
```

# 🔹 Security Best Practices
# -------------------------

  ## ✅ Use Private Network---->Allow DB access only from Kubernetes cluster.
  ## ✅ Use Security Groups / Firewall--->Allow only:-->Kubernetes Nodes → Database
  ## ✅ Enable SSL--->Encrypt DB traffic.
  ## ✅ Rotate Passwords--->Change passwords regularly.


# 🔹 AWS RDS Connection Flow
# --------------------------

   EKS Pod
     ↓
  RDS Endpoint
     ↓
  MySQL/PostgreSQL



# 🔹 GCP Cloud SQL Connection Flow
# ----------------------------
   GKE Pod
     ↓
   Cloud SQL Proxy
     ↓
   Cloud SQL



# 🔹 Important Kubernetes Concepts
# ------------------------------

| Concept    | Usage                   |
| ---------- | ----------------------- |
| Secret     | Store password          |
| ConfigMap  | Store non-secret config |
| Service    | Pod communication       |
| Ingress    | External access         |
| Deployment | Run app pods            |




# 🔹 Real Production Example
# ---------------------------

```text
Frontend Pod
Backend Pod
Redis Cache
RDS Database
S3 Storage
Load Balancer
```

This is close to actual company architecture.

---



# 🔹 Day 61–70 Practice Tasks

## ✅ Task 1

Create MySQL RDS instance.

---

## ✅ Task 2

Connect Python Flask app to RDS.

---

## ✅ Task 3

Store DB password in Kubernetes Secret.

---

## ✅ Task 4

Deploy app in Kubernetes.

---

## ✅ Task 5

Test DB connection from pod.

```bash
kubectl exec -it pod-name -- bash
```

---

# 🔹 Important Commands

## Check Secrets

```bash
kubectl get secrets
```

---

## Describe Secret

```bash
kubectl describe secret db-secret
```

---

## Apply Deployment

```bash
kubectl apply -f deployment.yaml
```

---

# 🔹 Interview Questions

## 1. Why use managed DB?

* Easy maintenance
* Backup
* Security
* High availability

---

## 2. Why not run DB inside pod?

* Data loss
* Restart issues
* Scaling problems

---

## 3. Difference between Secret and ConfigMap?

| Secret         | ConfigMap     |
| -------------- | ------------- |
| Sensitive data | Normal config |
| Passwords      | URLs          |
| Tokens         | Ports         |

---

## 4. How do pods connect to cloud DB?

Using:

* DB endpoint
* Username
* Password
* Network access

---

# 🔹 Real Industry Flow

```text
Developer
   ↓
Docker
   ↓
Kubernetes
   ↓
Managed Database
   ↓
Production
```


# 🔹 Final Understanding

By Day 70, you should understand:

✅ Managed Databases
✅ RDS / Cloud SQL
✅ Kubernetes Secrets
✅ Secure DB Connection
✅ Production Architecture
✅ Real Industry Deployment

