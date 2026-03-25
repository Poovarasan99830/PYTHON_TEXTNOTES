


Docker makes your project run the same way everywhere**, no matter the machine, OS, or environment.


# _______________________________________________________
**Q: Why do we create Docker for every project?**
# _______________________________________________________




## ⚙️ 1️⃣ Every Project Has Its Own Dependencies
## 🧰 2️⃣ Docker = Portable Environment
## 🔁 3️⃣ Every Project = Different Environment
## 🔐 4️⃣ Reproducibility & Stability
            Reproducibility means....our project to run anywhere and anytime even changes OS AND            dependencies
            simply we say it means future proof builds




## 🚀 5️⃣ Easy Deployment


| Reason                | Why it matters                        |
| --------------------- | ------------------------------------- |
| Isolation             | Each project gets its own environment |
| Portability           | Runs the same everywhere              |
| Dependency control    | No version clashes                    |
| Reproducibility       | Future-proof builds                   |
| Easier deployment     | Cloud-ready instantly                 |
| Microservice-friendly | Multiple small apps can run together  |


# _______________________________________________________

We create Docker for every project so it behaves like a 

*self-contained machine* — clean, portable, reproducible, and deployment-ready.

# _______________________________________________________


Image → App template

Container → Running app

Volume → Permanent data
         data are safe even we delete/restart the containers

Network → Container communication
        → it is comunications for one container to another container....which is use to solve data lose...

Compose → One command orchestration



# _______________________________________________________


Dockerfile → image create panna
docker build → image ready
docker run → container start
Container → running isolated app
Compose → multiple containers, one command

# _______________________________________________________


-->  Docker Image is a static template 
-->  👉 Like **class** in Python
--->  Read-only
--->  Example: `python:3.11-slim`
      Docker Container is a running instance of that template.

# _______________________________________________________

Can one image create multiple containers?
yes

why?


Ore Docker image irundhu multiple containers create pannradhu:

scale panna
isolate panna
different work panna
safe-aa deploy panna
production-la stable-aa run panna



Real-life example 🏪

Think like this:

  image = Idli maavu 🥣
  Containers = Individual idli 🥞🥞🥞

# _______________________________________________________

docker compose up automatically builds the image if a build option is defined and the image doesn’t exist.
We don’t need to run docker build manually.




# _______________________________________________________

Force rebuild (when code changes)
If you changed:

Dockerfile
requirements.txt
dependencies

docker compose up --build

# _______________________________________________________



A Dockerfile contains step-by-step instructions to build a Docker image.
Using docker build, Docker creates an image from the Dockerfile.
That image is then used to run one or more containers using docker run.


docker build -t user-service-image .


docker run user-service-image               ---run inside te container only not access via browser

docker run -p 9000:8000 user-service-image  ---run via browser
                                            --9000 system local ost port
                                            --8000  it is say app run ...which port(inside app port)

# _______________________________________________________

Why Docker Compose?

docker run flask-app
docker run postgres
docker run redis


Too many commands

Network manually set panna vendum
Dependency order manage panna kashtam
👉 Docker Compose solves this problem.


# _______________________________________________________

✅ What Docker Compose Does


Docker Compose allows us to define, configure, and run multiple related containers using a single YAML file.


Docker Compose is used to manage multi-container applications.
It allows us to define services, networks, volumes, and dependencies in a single docker-compose.yml file and start the entire application using one command.



version: "3.8"

services:
  user-service:
    build: ./user
    ports:
      - "5000:5000"

  product-service:
    build: ./product
    ports:
      - "8000:8000"

  db-service:
    image: postgres:15



docker compose up
# _______________________________________________________

| Local Image       | Docker Hub Image |
| ----------------- | ---------------- |
| Exists on your PC | Exists online    |
| `docker images`   | `docker search`  |
| Can run directly  | Must pull first  |
# _______________________________________________________


🏗 Real-World Flow

Developer builds image
Push to Docker Hub
Server pulls image
Container runs in production
This is how DevOps pipelines work.

| Step  | Command                      |
| ----- | ---------------------------- |
| Login | `docker login`               |
| Tag   | `docker tag old new`         |
| Push  | `docker push username/image` |
| Pull  | `docker pull username/image` |



# _______________________________________________________

docker build = creates image
docker tag = renames image



# _______________________________________________________
| Flag                              | Meaning                                         |
| --------------------------------- | ----------------------------------------------- |
| `-d`                              | Run container **in background** (detached mode) |
| `-p 8000:8000`                    | Map **host port 8000 → container port 8000**    |
| `iasupsc/django-mysql-docker-web` | Image name                                      |
