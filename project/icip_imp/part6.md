
# ------------------------------

# 6. Docker + AWS + CI/CD

Resume:

> Collaborated in Agile teams, integrating third-party systems and deploying applications using Docker, AWS, and CI/CD...

### Interviewer may ask:

* What is Docker?
* Docker image vs container?
* How do you deploy?
* What is CI/CD?
* What happens after Git push?
* Where do you store Docker images?
* How do you handle environment variables?
* How do you rollback?
* What AWS services did you use?



# ------------------------------

1. What is Docker?
Simple meaning

Docker is a containerization platform used to package an application along with its dependencies and run it consistently across different environments





# ------------------------------
Docker Image
# ------------------------------


Image is a read-only blueprint/template used to create containers.

Example:
python:3.12
FastAPI
requirements.txt
application code

These are packaged into an image.

# ------------------------------
Container
# ------------------------------


Container is a running instance of an image.
Docker Image
     ↓
  Container


One image can be used to create multiple containers.


# ------------------------------



Yes — **one Docker image can be used to create multiple containers because we want the same application setup to run consistently, while each container handles separate workload.**

### Simple example

Suppose your FastAPI application gets heavy traffic:

```text
             Docker Image
            fastapi:v1.0
                 │
       ┌─────────┼─────────┐
       ↓         ↓         ↓
 Container 1  Container 2  Container 3
   100 users    100 users    100 users
```

All 3 containers are created from the **same image**.

### Why not create 3 different images?

Because the application code and dependencies are the same.

If you create:

```text
Image 1 → Container 1
Image 2 → Container 2
Image 3 → Container 3
```

you unnecessarily duplicate the build process and can accidentally get different versions/configurations.

Instead:

```text
             One Image
                ↓
     ┌──────────┼──────────┐
     ↓          ↓          ↓
 Container    Container   Container
    #1           #2          #3
```

This gives us:

* **Consistency** — same application version
* **Scalability** — easily increase containers when traffic grows
* **Faster deployment** — build image once, run many containers
* **Easy rollback** — all containers can be switched to a previous image version
* **Resource isolation** — each container runs independently

### 🔥 Real production scenario

Imagine your insurance FastAPI API normally handles 100 requests/sec.

During peak time:

```text
100 req/sec
    ↓
Container 1
```

Not enough.

We can scale:

```text
                 Load Balancer
                      ↓
          ┌───────────┼───────────┐
          ↓           ↓           ↓
       Container    Container    Container
          1             2           3
```

All three use:

```text
claim-api:v1.5
```

The **image is the blueprint**, while containers are the **running copies**.

### Interview-ready answer

> **We create one Docker image and use it to run multiple containers because all containers need the same application code and dependencies. This gives consistency and allows horizontal scaling. For example, if traffic increases, we can run multiple containers from the same image behind a load balancer instead of creating separate images for each container.**

**Key concept to remember:**

> **Build once → Run many → Scale easily.**

# ------------------------------