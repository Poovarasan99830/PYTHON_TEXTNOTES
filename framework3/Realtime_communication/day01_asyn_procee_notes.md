

# **Week 7: Real-Time Communication**

**Goal:** Enable live updates without refresh.

| Day | Topic              | Mini Project                          | Outcome                   |
| --- | ------------------ | ------------------------------------- | ------------------------- |
| 29  | WebSockets Basics  | Build a live chat with Flask-SocketIO | Two-way communication     |
| 30  | Django Channels    | Live order tracking                   | Async Django              |
| 31  | Server-Sent Events | Build live stock ticker               | One-way streaming         |
| 32  | WebRTC Basics      | Peer-to-peer video chat               | Real-time media           |
| 33  | Integration        | Add real-time order updates in PWA    | Full-stack realtime       |
| 34  | Scaling            | Use Redis as WebSocket backend        | Multi-instance scaling    |
| 35  | Review             | Stress test real-time app             | Confidence in performance |




## **🚀 Quick-Learn Roadmap: Week 7**

### **Day 29 – WebSockets Basics**

* **Goal:** Understand two-way communication between client & server.
* **Must-Learn:**

  * WebSocket vs HTTP (persistent connection)
  * `socket.io` basics (Flask-SocketIO)
  * Emit & receive events
* **Mini Project Shortcut:**

  * Build **live chat**: 2 users can send messages instantly
* **Pro Tip:** Focus on **connect, emit, on, disconnect** events.

---

### **Day 30 – Django Channels**

* **Goal:** Async Django for live updates
* **Must-Learn:**

  * Install `channels` & `channels_redis`
  * Routing & Consumers (WebSocket consumer vs HTTP consumer)
  * `async` vs `sync` in Django context
* **Mini Project Shortcut:**

  * **Live order tracker**: status updates appear without refresh
* **Pro Tip:** Use **Redis** locally for channel layer, don’t focus on deployment yet

---

### **Day 31 – Server-Sent Events (SSE)**

* **Goal:** One-way streaming from server → client
* **Must-Learn:**

  * Difference SSE vs WebSocket
  * Flask/Django implementation
* **Mini Project Shortcut:**

  * **Live stock ticker**: server pushes updates every 1–2 seconds
* **Pro Tip:** SSE easier for **simple one-way updates**

---

### **Day 32 – WebRTC Basics**

* **Goal:** Real-time peer-to-peer media
* **Must-Learn:**

  * WebRTC concepts: PeerConnection, Offer/Answer, ICE candidates
  * Use STUN/TURN servers for NAT traversal
* **Mini Project Shortcut:**

  * Simple **video chat between 2 browsers**
* **Pro Tip:** Use **simple signaling server** (SocketIO) to exchange SDP

---

### **Day 33 – Integration**

* **Goal:** Combine front-end PWA + backend realtime
* **Mini Project Shortcut:**

  * Add **live order updates** in PWA
* **Must-Learn:**

  * Fetch API + WebSocket updates
  * DOM update in real-time
* **Pro Tip:** Reuse your **Day 30 channels setup**

---

### **Day 34 – Scaling**

* **Goal:** Multi-instance WebSocket backend
* **Must-Learn:**

  * Why multiple API instances break WebSocket connections
  * Redis as **Pub/Sub channel layer**
* **Mini Project Shortcut:**

  * Run **2 API containers**, all clients get same updates via Redis
* **Pro Tip:** Focus on **conceptual understanding** of Pub/Sub

---

### **Day 35 – Review & Stress Test**

* **Goal:** Ensure your real-time app is **robust and performant**
* **Tasks:**

  * Test **100+ simultaneous connections**
  * Check reconnect handling
  * Optimize message broadcast
* **Pro Tip:** Use **locust.io or wrk** for stress testing

---

## **🔥 Quick Learning Strategy**

1. **Day 29–31:** Learn **concept + small project** (chat, stock ticker)
2. **Day 32:** Just understand **WebRTC basics** (video call)
3. **Day 33–34:** Integration + scaling (re-use existing code)
4. **Day 35:** Review & stress test, fix issues

---

### **Shortcut Tools**

* **Flask-SocketIO** → Fast WebSocket setup
* **Django Channels + Redis** → Production-ready async updates
* **EventSource (SSE)** → simple one-way streaming
* **WebRTC** → P2P media
* **Redis Pub/Sub** → multi-instance sync

