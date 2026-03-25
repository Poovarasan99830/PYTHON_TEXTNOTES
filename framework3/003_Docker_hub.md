


#_______________________________________________
# **Docker + Git + Docker Hub – Complete Notes**




#_______________________________________________
## **1️⃣ Git Repository Issues**
#_______________________________________________




### Errors & Problems:

1. `error: src refspec feature-docker does not match any`

   * Cause: Branch `feature-docker` did not exist locally.
2. `remote: Permission to ... denied` (403)

   * Cause: GitHub account didn’t have permission to push to that repo.
   * Or wrong credentials cached.

### Solutions:

* Create a new branch before pushing:

```bash
git checkout -b feature-docker
```

* Add commits:

```bash
git add .
git commit -m "Your commit message"
```

* Push new branch:

```bash
git push -u origin feature-docker
```

* If permission denied → check **GitHub credentials** or use **Personal Access Token (PAT)**.

### Best Practices:

* Always check which **account is logged in** for GitHub (`git config user.name / user.email`)
* Create branches locally before pushing
* Use PAT instead of password

---


#_______________________________________________
## **2️⃣ Docker Build & Run**
#_______________________________________________




### Problems:

* Long build times due to large images or repeated installs
* Multiple images for services (`blog_service`, `user_service`)
* Port issues: default Flask/Django ports not accessible outside container

### Solutions:

* Use `python:3.11-slim` base image → smaller size
* Install only required packages
* Expose proper ports in `Dockerfile` and `docker-compose.yml`
* For example:

```dockerfile
EXPOSE 5001
EXPOSE 8000
```

* Use `docker-compose up --build` for rebuilding with changes

### Best Practices:

* Clean up layers to reduce image size:

```dockerfile
RUN apt-get update && apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
```

* Tag images properly with `username/repo:tag`
* Use environment variables for sensitive data

---

#_______________________________________________
## **3️⃣ Docker Hub Push Errors**
#_______________________________________________



### Errors:

1. `push access denied, repository does not exist or may require authorization`

   * Cause: Repo doesn’t exist in Docker Hub or wrong credentials
2. `failed to fetch oauth token: 401 Unauthorized`

   * Cause: Logged in with password instead of **access token**, or old cached login

### Solutions:

* Create repo manually on Docker Hub:

  * `user_service`
  * `blog_service`
* Use Access Token instead of password:

```bash
docker login -u iasupsc
# paste token as password
```

* Tag images before push:

```bash
docker tag local-image iasupsc/user_service:latest
docker tag local-image iasupsc/blog_service:latest
```

* Push images:

```bash
docker push iasupsc/user_service:latest
docker push iasupsc/blog_service:latest
```

### Best Practices:

* Always **create repositories first**
* Always use **access token** for CLI login
* Keep **image names consistent** (`username/repo:tag`)
* Check images locally:

```bash
docker images
```

---
#_______________________________________________
## **4️⃣ Accessing Docker Images on Another System**
#_______________________________________________



* **Option 1: Pull from Docker Hub**

```bash
docker pull iasupsc/user_service:latest
docker pull iasupsc/blog_service:latest
```

* **Option 2: Save & transfer image**

```bash
docker save -o user_service.tar iasupsc/user_service:latest
docker load -i user_service.tar
```

* Modify and rebuild in another system

---
#_______________________________________________
## **5️⃣ Common Mistakes / Pitfalls**
#_______________________________________________

| Mistake                               | Cause                                             | Solution / Best Practice                                       |
| ------------------------------------- | ------------------------------------------------- | -------------------------------------------------------------- |
| 401 Unauthorized / push access denied | Wrong credentials / repo missing / password login | Use Access Token, create repo manually                         |
| Branch doesn’t exist                  | Tried to push before creating branch              | `git checkout -b branch-name`                                  |
| Docker image too big                  | Installing unnecessary packages / large base      | Use `slim` images, clean apt cache                             |
| Docker port not accessible            | Container not exposing correct port               | Use `EXPOSE` in Dockerfile & map ports in `docker-compose.yml` |
| Using password for Docker CLI         | Docker Hub disabled password auth                 | Use **access token**                                           |
| Docker cached login                   | Login failed repeatedly                           | `docker logout` then login with token                          |

---
#_______________________________________________
## **6️⃣ Recommended Workflow**
#_______________________________________________

1. **Git Workflow**

```bash
git status
git add .
git commit -m "message"
git checkout -b feature-branch
git push -u origin feature-branch
```

2. **Docker Workflow**

```bash
docker build -t microservices_project-user_service .
docker build -t microservices_project-blog_service .
docker run -p 5001:5001 user_service
docker run -p 8000:8000 blog_service
```

3. **Push to Docker Hub**

```bash
docker login -u iasupsc
# use access token as password
docker tag microservices_project-user_service iasupsc/user_service:latest
docker tag microservices_project-blog_service iasupsc/blog_service:latest
docker push iasupsc/user_service:latest
docker push iasupsc/blog_service:latest
```

---
#_______________________________________________
✅ **Key Lessons Learned**
#_______________________________________________


* Always **verify repo exists** before pushing
* Always **use access tokens** for Docker Hub
* Tag images **properly** for namespace (`username/repo:tag`)
* Keep **base images small** to reduce push/pull time
* Maintain **branch discipline** in Git







#_______________________________________________
# **Complete Working Flow – Microservices Project**
#_______________________________________________




## **1️⃣ Local Development & Git Workflow**

1. Check the status:

```bash
git status
```

2. Stage changes:

```bash
git add .
```

3. Commit changes:

```bash
git commit -m "Add Docker files and microservices"
```

4. Create a branch (if needed):

```bash
git checkout -b feature-docker
```

5. Push branch to GitHub:

```bash
git push -u origin feature-docker
```

✅ **Outcome:** Your code + Docker files are now safely in GitHub.

---

## **2️⃣ Docker Workflow (Local)**

1. Build images for both services:

```bash
docker build -t microservices_project-user_service ./user_service
docker build -t microservices_project-blog_service ./blog_service
```

2. Run containers locally:

```bash
docker run -p 5001:5001 microservices_project-user_service
docker run -p 8000:8000 microservices_project-blog_service
```

3. Test your API locally:

* Flask user service → `http://localhost:5001/api/`
* Django blog service → `http://localhost:8000/api/`

✅ **Outcome:** Both services running locally and working.

---

## **3️⃣ Push Images to Docker Hub**

1. Login using **Docker Hub username + access token**:

```bash
docker login -u iasupsc
```

2. Tag images for Docker Hub:

```bash
docker tag microservices_project-user_service iasupsc/user_service:latest
docker tag microservices_project-blog_service iasupsc/blog_service:latest
```

3. Push to Docker Hub:

```bash
docker push iasupsc/user_service:latest
docker push iasupsc/blog_service:latest
```

✅ **Outcome:** Docker images are now on Docker Hub and accessible from any system.

---
#_______________________________________________
## **4️⃣ Access Project on Another System**
#_______________________________________________



1. Clone GitHub repository to another system:

```bash
git clone https://github.com/iasupsc/microservices_project.git
cd microservices_project
```

2. OR pull Docker images directly (if you only need to run):

```bash
docker pull iasupsc/user_service:latest
docker pull iasupsc/blog_service:latest
```

---

## **5️⃣ Run Docker Containers on Another System**

1. Run user service:

```bash
docker run -p 5001:5001 iasupsc/user_service:latest
```

2. Run blog service:

```bash
docker run -p 8000:8000 iasupsc/blog_service:latest
```

3. Test APIs:

* `http://localhost:5001/api/` → User Service
* `http://localhost:8000/api/` → Blog Service

✅ **Outcome:** Your microservices are now running on the new system exactly like your local environment.

---

## **6️⃣ Optional: Docker Compose for Multi-Service**

If you want **both services in one command**:

`docker-compose.yml` example:

```yaml
version: '3'
services:
  user_service:
    image: iasupsc/user_service:latest
    ports:
      - "5001:5001"
  blog_service:
    image: iasupsc/blog_service:latest
    ports:
      - "8000:8000"
```

Run all services:

```bash
docker-compose up
```

✅ **Outcome:** Both services start together with ports mapped.

---

## **7️⃣ Key Best Practices**

* Always **push Docker images after code changes**.
* Use **branches for new features**.
* Use **access tokens** for Docker Hub and GitHub CLI.
* Keep **Dockerfiles lightweight** (`slim` base images, clean cache).
* Test images locally before pushing.
* Use **docker-compose** for easy multi-service management.







Perfect 👍 this is a **must-know DevOps skill**.
I’ll explain **step-by-step**, very **clear & short**, plus **best practice**.

---

## 🔹 GOAL

Push your **Docker images** from your project to **Docker Hub**
So **any system** can pull and run them.

---

## ✅ STEP 1: Create Docker Hub account

👉 [https://hub.docker.com](https://hub.docker.com)
Create account (username matters).

Example:

```
Docker Hub username: poovarasan99830
```

---

## ✅ STEP 2: Login to Docker Hub (from terminal)

```bash
docker login
```

✔ Enter Docker Hub username
✔ Enter password
✔ Login success

---

## ✅ STEP 3: Check your local images

```bash
docker images
```

You will see something like:

```
microservices_project-user_service
microservices_project-blog_service
```

---

## ✅ STEP 4: Tag images (VERY IMPORTANT)

Docker Hub requires this format:

```
username/image_name:tag
```

### Example:

```bash
docker tag microservices_project-user_service poovarasan99830/user_service:latest
docker tag microservices_project-blog_service poovarasan99830/blog_service:latest
```

---

## ✅ STEP 5: Push images to Docker Hub 🚀

```bash
docker push poovarasan99830/user_service:latest
docker push poovarasan99830/blog_service:latest
```

⏳ Takes some time (first push)

---

## ✅ STEP 6: Verify on Docker Hub

Go to:

```
https://hub.docker.com/u/poovarasan99830
```

You should see:

* user_service
* blog_service

🎉 Done!

---

## 🧠 HOW TO USE THESE IMAGES ON ANY OTHER SYSTEM

### On another computer:

```bash
docker pull poovarasan99830/user_service:latest
docker pull poovarasan99830/blog_service:latest
```

Or via `docker-compose.yml`:

```yaml
services:
  user_service:
    image: poovarasan99830/user_service:latest
    ports:
      - "5001:5001"

  blog_service:
    image: poovarasan99830/blog_service:latest
    ports:
      - "8000:8000"
```

Then:

```bash
docker-compose up
```

---

## ⚠️ Common mistakes (remember)

| Mistake             | Fix                          |
| ------------------- | ---------------------------- |
| Forgot `docker tag` | Docker Hub requires username |
| Wrong image name    | Check with `docker images`   |
| Not logged in       | Run `docker login`           |
| Push denied         | Wrong Docker Hub username    |

---

## 🎯 Interview-ready answer

> “I tag Docker images with my Docker Hub username and push them using `docker push`, allowing the images to be reused across environments.”

---

## ⭐ Best Practices

* Use meaningful tags (`v1`, `v1.1`, `latest`)
* Don’t push secrets inside images
* Keep images small
* Use `.dockerignore`






Got it 👍 You want **ONLY the important Docker commands** — clean, short, and useful (no extra story).

Below is a **must-know Docker command list**, especially for **interviews + real projects**.

---

# ⭐ IMPORTANT DOCKER COMMANDS (CHEAT SHEET)

---

## 🔹 Docker Engine & Info

```bash
docker --version
docker info
```

---

## 🔹 Image Commands

### Build image

```bash
docker build -t image_name .
```

### List images

```bash
docker images
```

### Remove image

```bash
docker rmi image_name
```

### Pull image from Docker Hub

```bash
docker pull image_name
```

---

## 🔹 Container Commands

### Run container

```bash
docker run -d -p 8000:8000 image_name
```

### Run with container name

```bash
docker run -d --name my_container -p 8000:8000 image_name
```

### List running containers

```bash
docker ps
```

### List all containers

```bash
docker ps -a
```

### Stop container

```bash
docker stop container_id
```

### Start stopped container

```bash
docker start container_id
```

### Restart container

```bash
docker restart container_id
```

### Remove container

```bash
docker rm container_id
```

### Force remove running container

```bash
docker rm -f container_id
```

---

## 🔹 Logs & Debugging

### View container logs

```bash
docker logs container_id
```

### Follow logs (live)

```bash
docker logs -f container_id
```

### Enter container shell

```bash
docker exec -it container_id bash
```

---

## 🔹 Port & Process Debug (Windows)

### Check which process is using port

```bash
netstat -aon | findstr 8000
```

### Kill process by PID

```bash
taskkill /PID <PID> /F
```

---

## 🔹 Docker Compose (VERY IMPORTANT)

### Start services

```bash
docker-compose up -d
```

### Stop services

```bash
docker-compose down
```

### Rebuild images

```bash
docker-compose build
```

### Restart services

```bash
docker-compose restart
```

### View compose containers

```bash
docker-compose ps
```

---

## 🔹 Docker Hub (Push Images)

### Login

```bash
docker login
```

### Tag image

```bash
docker tag local_image username/image:tag
```

### Push image

```bash
docker push username/image:tag
```

---

## 🔹 Cleanup (VERY USEFUL)

### Remove unused containers

```bash
docker container prune
```

### Remove unused images

```bash
docker image prune
```

### Remove everything unused

```bash
docker system prune -a
```

---

## 🔹 One-Line Emergency Cleanup 😄

```bash
docker stop $(docker ps -aq) && docker rm $(docker ps -aq)
```

---

## 🎯 TOP 10 INTERVIEW-CRITICAL COMMANDS

If you remember only these 👇

```bash
docker build
docker images
docker run
docker ps
docker ps -a
docker stop
docker rm
docker logs
docker exec
docker-compose up -d
```

---



Team A (Build & Push)
        ↓
Docker Hub
        ↓
Team B (Pull & Run)







1. Project Start (Django + Docker)


2. mysqlclient Error (Major Problem)

    சரியான தீர்வு (Dockerfile)
    RUN apt-get update && apt-get install -y \
      pkg-config \
      default-libmysqlclient-dev \
      build-essential \
       && rm -rf /var/lib/apt/lists/*

3. DEFAULT_AUTO_FIELD Warning (Django Warning)
      class APPLIANCE(forms.ModelForm):
      class Meta:
         default_auto_field = 'django.db.models.BigAutoField' ❌
       Form-ல இது போடக்கூடாது

       class AppliancesConfig(AppConfig):
         default_auto_field = 'django.db.models.BigAutoField'  --->apps.py


4. Migrations Delete Problem (Windows)
     <!-- confued for linux and windows...commands -->
     rm -rf not recognized                              --->linux commands
     Remove-Item -Recurse -Force appliances\migrations  --->windows commands






5. Docker Run Working Fine
6. DockerHub Push Error

    # 1. Login
        docker login

    # 2. Build
       docker build -t django-app .

    # 3. Tag
       docker tag django-app divyadd6514240/django-app:latest

     # 4. Push
         docker push divyadd6514240/django-app:latest





IMPORTANT DOCKER COMMANDS (CHEAT SHEET)

🔹 Docker Engine & Info
🔹 Image Commands
🔹 Container Commands
🔹 Logs & Debugging
🔹 Port & Process Debug (Windows)
🔹 Docker Compose (VERY IMPORTANT)
🔹 Docker Hub (Push Images)
🔹 Cleanup (VERY USEFUL)
🔹 One-Line Emergency Cleanup




# _____________________________________________________________

wsl --install --->first time enable mandatory need WSL installation....


docker --version
docker info
docker build -t image_name .
docker images
docker rmi image_name



docker search django-mysql-docker                    ---->Check if the image exists
docker inspect iasupsc/django-mysql-docker-web       ---->How to Know If Image is Local Only




docker pull image_name
docker run -d -p 8000:8000 image_name
docker run -d --name my_container -p 8000:8000 image_name



docker ps       ---->check running containers
docker ps -a    ----->To see all containers (running + stopped):




docker stop container_id
docker restart container_id
docker rm container_id
docker rm -f container_id
docker rm -f container_id
docker logs container_id
docker logs -f container_id
docker exec -it container_id bash
docker exec -it container_id bash
netstat -aon | findstr 8000


taskkill /PID <PID> /F
docker-compose up -d
docker-compose down
docker-compose restart
docker login
docker tag local_image username/image:tag
docker push username/image:tag
docker container prune
docker image prune
docker system prune -a
docker stop $(docker ps -aq) && docker rm $(docker ps -aq)
docker build


docker images
docker run
docker ps
docker ps -a
docker stop
docker rm
docker logs
docker exec
docker-compose up -d


docker build -t image-name .
docker tag old-image new-image





# _______________________________________________________________



https://chatgpt.com/share/697c7ea6-a788-800a-84e5-0e40db34ec54



docker compose up
Docker will:

Build Django image
Pull MySQL image
Create network
Start MySQL
Start Django




Perfect 👍
Here’s a **FULL Django + MySQL + Docker + Docker Compose guide**, explained **from scratch → running**, mentor style.
This is **industry-level** and very similar to what you’ll see in real projects.

---

# 🎯 What we are building

✅ Django app
✅ MySQL database
✅ Django & MySQL in **separate containers**
✅ Connected via **Docker Compose**
✅ DB data **persisted with volumes**

---

# 📁 1️⃣ Project structure

Create a folder and files like this:

```
django-mysql-docker/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
│
├── project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
```

---

# 🧱 2️⃣ Create Django project (if not created)

```bash
django-admin startproject project .
```

---

# 📦 3️⃣ requirements.txt (MySQL driver is IMPORTANT)

```txt
Django>=4.2
mysqlclient
```

⚠️ **Do NOT use `MySQLdb` directly**
`mysqlclient` is the correct driver.

---

# 🐳 4️⃣ Dockerfile (Django container)

```dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

👉 Extra system packages are needed for **MySQL client**

---

# 🐬 5️⃣ docker-compose.yml (MOST IMPORTANT)

```yaml
version: "3.8"

services:
  web:
    build: .
    container_name: django_app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      DB_NAME: mydb
      DB_USER: admin
      DB_PASSWORD: admin
      DB_HOST: db
      DB_PORT: 3306

  db:
    image: mysql:8.0
    container_name: mysql_db
    restart: always
    environment:
      MYSQL_DATABASE: mydb
      MYSQL_USER: admin
      MYSQL_PASSWORD: admin
      MYSQL_ROOT_PASSWORD: root
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

---

# 🔥 6️⃣ MOST IMPORTANT RULE (many beginners fail)

❌ **WRONG**

```text
DB_HOST=localhost
```

✅ **CORRECT**

```text
DB_HOST=db
```

👉 Docker Compose provides **internal DNS**
Service name = hostname

---

# ⚙️ 7️⃣ Django settings.py (MySQL config)

Open `project/settings.py`

```python
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),  # db
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

---

# 🚀 8️⃣ Run everything (NO docker build needed)

```bash
docker compose up
```

Docker will:

1. Build Django image
2. Pull MySQL image
3. Create network
4. Start MySQL
5. Start Django

---

# ⏳ 9️⃣ Wait for MySQL (important)

First run may take **20–30 seconds**
If Django fails first time, just re-run:

```bash
docker compose up
```

(MySQL needs time to initialize)

---

# 🗄️ 1️⃣0️⃣ Run migrations

Open new terminal:

```bash
docker compose exec web python manage.py migrate
```

---

# 👤 1️⃣1️⃣ Create superuser

```bash
docker compose exec web python manage.py createsuperuser
```

Open:

```
http://localhost:8000/admin
```

---

# 💾 1️⃣2️⃣ Why volumes?

```yaml
volumes:
  - mysql_data:/var/lib/mysql
```

Without volume ❌

* Container stop → data lost

With volume ✅

* Data safe
* Restart safe

---

# 🔍 1️⃣3️⃣ Verify containers

```bash
docker ps
```

You should see:

* django_app
* mysql_db

---

# 🧠 1️⃣4️⃣ Behind the scenes (INTERVIEW GOLD)

* Django runs in **web container**
* MySQL runs in **db container**
* Docker creates **private network**
* Django connects via `db:3306`
* Volume keeps MySQL data persistent

---

# 🎯 1️⃣5️⃣ One-line interview answer

> Django and MySQL run in separate Docker containers and are connected using Docker Compose networking, where the database is accessed via the service name and data is persisted using volumes.

---

# ❌ Common mistakes (PLEASE AVOID)

❌ Using `localhost`
❌ Missing MySQL system packages
❌ Forgetting volume
❌ Running migrate outside container
❌ Hardcoding credentials

---

# 🧠 Final clarity

This setup is used in:

* Startups
* MNCs
* AWS ECS
* Kubernetes (same concept)

---

If you want next, I can teach:

* 🔥 Django + MySQL + Nginx + Gunicorn
* 🔥 Multiple Django apps → single MySQL
* 🔥 Production-ready Docker setup
* 🔥 Docker interview Q&A (real questions)

Just tell me 👍
