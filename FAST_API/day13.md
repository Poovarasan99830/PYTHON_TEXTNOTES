Understood. Going forward, I'll use this format by default, and I'll only switch to **Tanglish** when you explicitly ask for it.

### **WebSockets – Interview Notes (Quick Revision)**

* **WebSockets** provide a **persistent, full-duplex connection** between the **client** and **server**, enabling **real-time communication** without repeatedly sending HTTP requests.
* Purpose: Enable **live notifications**, **chat applications**, **live tracking**, **real-time dashboards**, and **status updates** by allowing the server to push data instantly to the client.
* **Working Flow:** **Client Connects → WebSocket Connection Established → Server Sends/Receives Real-Time Data → Client Receives Instant Updates**.
* **ICIP Scenario:** In the **Insurance Claim Intelligence Platform**, WebSockets can be used to send **real-time claim status updates**, **OCR progress**, **AI claim analysis status**, and **claim approval notifications** to the React frontend without requiring the user to refresh the page.
* **Code:**

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        message = await websocket.receive_text()
        await websocket.send_text(f"Status: {message}")
```

> **💡 Project Explanation:** In our **Insurance Claim Intelligence Platform**, WebSockets are ideal for **real-time claim tracking**. When a customer submits a claim, the frontend establishes a WebSocket connection. As the claim moves through **OCR**, **Hybrid RAG**, **AWS Bedrock AI analysis**, and **Claims Officer approval**, the backend pushes live status updates to the frontend instantly, providing a seamless user experience without continuous polling.
