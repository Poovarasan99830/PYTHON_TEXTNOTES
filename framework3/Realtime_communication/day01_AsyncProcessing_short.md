
# ___________________________
🔵 What is Celery?
# ___________________________

      Celery is a Python background task processing system.


# ___________________________
🔴 What is Redis?
# ___________________________

    Redis is a fast in-memory data store.


Celery = worker
Redis = message queue storage


# ___________________________
🟠 Where Celery Used in Real Projects?
# ___________________________

Email sending
Payment verification
Report generation
Data sync (your Flexi-DMS case)
Image processing
Notifications

# ___________________________
🟠 Celery Beat
# ___________________________

Celery Beat is the scheduler component of Celery that triggers periodic tasks at defined intervals, which are then executed by Celery workers




# ___________________________

Celery Beat → Redis → Celery Worker → Sync Logic → External API
Beat = schedule trigger pannum
Redis = task store pannum
Worker = execute pannu


# ___________________________

| Real World   | Celery System  |
| ------------ | -------------- |
| Bell machine | Celery Beat    |
| Office staff | Celery Worker  |
| Bell sound   | Task execution |


# ___________________________

Celery Beat → Redis → Celery Worker → Task execute

Celery Beat 15 minutes-ku oru thadava check pannum
Sync task Redis-ku anuppum
Worker adha eduthu sync pannum


# ___________________________



Software Engineering
   ↓
Backend Development
   ↓
System Design / Architecture
   ↓
Asynchronous Processing
   ↓
Task Queues
   ↓
Celery + Redis

# ___________________________


🔹 What is WebSocket?

      WebSocket is a protocol that enables persistent, bidirectional, real-time communication between a client and a    server over a single TCP connection.

      HTTP (Traditional Web Communication)--HTTP is stateless and request-response based.
      🔹 WebSocket-->WebSocket is stateful and full-duplex.
      
        TCP = Transmission Control Protocol

      Flask-SocketIO--->Used for adding real-time features in Flask.
      Django Channels--->Used to add WebSocket and async support to Django.
                            used with-->Used with:ASGI--->Redis (for scaling)

     
     connect → user join  --->When you open WhatsApp Web → you become online.
     emit → send message
     on → receive event
     disconnect → user leave


     User page open panra → connect event trigger aagum
     User message type panra → socket.emit()
     Server receive panra → @socketio.on()
     Server broadcast=True use panni ella users ku anupum
     Other users socket.on() use panni receive panra


     What is a Handshake?
        The process where client and server agree on how they will communicate.


    What is HTTP handshake?

          It is the initial HTTP request and response process used to establish or upgrade a connection between the client and server before communication begins.

   “How do you connect WebSocket in a project?”
        WebSocket connection starts with an HTTP handshake, then upgrades to a persistent TCP connection. After that, the client and server communicate using event-based messages. Flask uses Flask-SocketIO, and Django uses Django Channels.