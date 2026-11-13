


# __________________________________________________



| Thing                | Role             |
| -------------------- | ---------------- |
| IP                   | Server identify  |
| Port                 | Service identify |
| Domain (Host header) | Website identify |



Server → IP address
Service → Port
Website → Domain name



| Service    | Port |
| ---------- | ---- |
| HTTP       | 80   |
| HTTPS      | 443  |
| MySQL      | 3306 |
| PostgreSQL | 5432 |
| Redis      | 6379 |




| Component     | Role                   |
| ------------- | ---------------------- |
| DNS           | Domain → IP mapping    |
| Public IP     | Identify Google server |
| Port 443      | HTTPS service          |
| NAT           | Private ↔ Public IP    |
| Load Balancer | Traffic routing        |
| Web Server    | Request handling       |
| App Server    | Business logic         |
| Database      | Data storage           |
| TLS           | Security               |



443  → Internet Gate
8000 → App Engine
3306 → Data Room



# __________________________________________________

http://127.0.0.1:5000



Browser
   |
   |  http request
   |  IP   : 127.0.0.1
   |  Port : 5000
   v
Local Machine
   |
   v
Python App (Flask / Django)



👉 This is **NAT (Network Address Translation)**


# 🔐 Production vs Local

| Local      | Production       |
| ---------- | ---------------- |
| 127.0.0.1  | Public IP        |
| Port 5000  | Port 443         |
| Dev server | NGINX + Gunicorn |
| Not secure | HTTPS            |



# __________________________________________________



                Internet Users
                      |
                      | HTTPS Request (Port 443)
                      v
               +----------------+
               |   Load Balancer |
               +----------------+
                      |
                      | Forward request (HTTPS / 443)
                      v
               +----------------+
               |      NGINX     |
               | Reverse Proxy  |
               | SSL Termination|
               | Serve Static   |
               +----------------+
                      |
                      | Internal HTTP (Port 8000)
                      v
              +-------------------+
              |    Gunicorn       |
              | WSGI Server       |
              | Multiple Workers  |
              +-------------------+
              | Worker 1 | Worker 2 | Worker 3 |
              | Threads  | Threads  | Threads  |
              +--------------------------------+
                      |
                      | Calls Django / Flask App
                      v
               +----------------+
               |  Django / Flask |
               | Business Logic  |
               +----------------+
                      |
                      | Database Query (Port 3306, Internal)
                      v
               +----------------+
               |     MySQL DB    |
               | Private Network |
               +----------------+



Example in Google Cloud / AWS
Google Cloud: “HTTP(S) Load Balancer” is the actual load balancer.
AWS: “Elastic Load Balancer (ELB)” is the actual load balancer.
Users never connect directly to the servers; all traffic passes through the load balancer.




Cached content = pre-stored copy of your website resources, mainly static, delivered quickly to the user to reduce server work and improve speed.
First request: CDN fetches from main server (origin).
Subsequent requests: CDN serves cached copy from nearby server → much faster.



User requests image.jpg
       │
       ▼
CDN edge server (nearest to user)
       │
       ├─ If cached → serve directly ✅
       └─ If not cached → fetch from origin server, store in cache, serve to user



| Component          | Role                                          |
| ------------------ | --------------------------------------------- |
| DNS                | Maps domain to nearest data center IP         |
| CDN                | Serves cached static files (optional)         |
| Load Balancer      | **Distributes traffic to servers** ✅          |
| NGINX / Web Server | Handles requests, static files, reverse proxy |
| App Server         | Runs website code (business logic)            |
| Database / Cache   | Stores data for the app                       |


User requests image/logo.png
       │
       ▼
CDN Edge Server (nearest to user)
       │
       ├─ If cached → serve directly ✅
       └─ If not cached → fetch from origin server (your deployed project)
       │
       ▼
Serve cached copy to user & store for future requests




# ___________________________________________________


## 🧑‍💻 CLIENT SIDE (Your Laptop)




Browser
Private IP : 192.168.1.10
Source Port: 52344 (random)
       ↓
User types:
       ↓

https://www.example.com
       ↓

www.example.com
        ↓
DNS Server
        ↓
13.233.10.50   (AWS Server Public IP)
        ↓

[ Browser ]
SRC IP   : 192.168.1.10
SRC PORT : 52344
DST IP   : 13.233.10.50
DST PORT : 443
        ↓
NAT Translation
192.168.1.10  →  49.207.45.88
        ↓
Packet becomes:
        ↓
SRC IP   : 49.207.45.88
SRC PORT : 52344
DST IP   : 13.233.10.50
DST PORT : 443
        ↓
49.207.45.88  ─────────────▶  13.233.10.50
        ↓
AWS EC2 (Public IP: 13.233.10.50)
        |
        v
Security Group (Allow 443)
        |
        v
NGINX (Port 443)
        |
        v
Gunicorn (Port 8000)
        |
        v
Django Application
        |
        v
MySQL Database (Port 3306)
       ↓
Django Response
        |
        v
NGINX
        |
        v
SRC IP : 13.233.10.50
DST IP : 49.207.45.88
DST PORT : 52344
        ↓
49.207.45.88  →  192.168.1.10
       ↓
Browser (192.168.1.10)
HTML / JSON Response Loaded
       














Client (Private IP)
        ↓
Router (NAT → Public IP)
        ↓
Internet
        ↓
AWS Server (Public IP)
        ↓
Application
        ↓
Response
        ↑
Same Path Back (Reverse NAT)