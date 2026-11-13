# **RAG Application Code Explanation (Part by Part)**

---


# -------------------------------------------------------
# **Part 1: Import Required Libraries**
# -------------------------------------------------------

```python
import os
import shutil
import chromadb
from flask import Flask, request, jsonify
import requests
import json
```




## **Purpose**
        Import all required modules.

### **os**
      Used to interact with the operating system.

```python
os.path.exists("db")
```

Checks whether a folder exists.

---

### **shutil**

Used for file and folder operations.

```python
shutil.rmtree("db")
```

Deletes an entire folder.

---

### **chromadb**

Vector database.

Used to store:

```text
Document
     ↓
Embedding
     ↓
Vector Database
```

---

### **Flask**

Used to create APIs.

Example:

```python
@app.route("/ask")
```

Creates an endpoint.

---

### **requests**

Used to call Ollama APIs.

Example:

```python
requests.post(...)
```

---

### **json**

Used to work with JSON data.

---

## **Summary**

| Library  | Purpose          |
| -------- | ---------------- |
| os       | Operating System |
| shutil   | File operations  |
| chromadb | Vector Database  |
| Flask    | Web API          |
| requests | API calls        |
| json     | JSON processing  |

---






# --------------------------------------------
# **Part 2: Auto Delete Old ChromaDB**
# -------------------------------------------

```python
DB_PATH = "db"
```

## **Purpose**

Specify where Chroma stores vectors.

---

### **Reset Existing Database**

```python
client = chromadb.PersistentClient(path=DB_PATH)
client.reset()
```

## **Purpose**

Clear all existing collections.

---

### **Delete Old Folder**

```python
shutil.rmtree(DB_PATH)
```

## **Purpose**

Delete physical database files.

---

### **Real-world Analogy**

Imagine a classroom.

Before starting a new semester:

```text
Erase Whiteboard
↓
Throw Away Old Notes
↓
Start Fresh
```

This section does exactly that.

---

## **Summary**

| Code            | Purpose           |
| --------------- | ----------------- |
| client.reset()  | Clear collections |
| shutil.rmtree() | Delete DB files   |
| DB_PATH         | Database location |

---



# -------------------------------------------------------
# **Part 3: Ollama Configuration**
# -------------------------------------------------------

```python
OLLAMA_URL = "http://localhost:11434/api"
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "llama3"
```

## **Purpose**

Configure Ollama models.

---

### **OLLAMA_URL**

```python
OLLAMA_URL = "http://localhost:11434/api"
```

Location of Ollama server.

---

### **Embedding Model**

```python
EMBED_MODEL = "nomic-embed-text"
```

Converts text into vectors.

Example:

```text
Python is easy
        ↓
[0.23, 0.44, 0.88, ...]
```

---

### **Chat Model**

```python
CHAT_MODEL = "llama3"
```

Generates answers.

---

## **Summary**

| Variable    | Purpose            |
| ----------- | ------------------ |
| OLLAMA_URL  | Ollama endpoint    |
| EMBED_MODEL | Generate vectors   |
| CHAT_MODEL  | Generate responses |

---




# -------------------------------------------------------
# **Part 4: Embedding Function**
# -------------------------------------------------------



```python
def ollama_embed(text):
```

## **Purpose**

Convert text into embeddings.

---

### **Call Ollama**

```python
resp = requests.post(
    f"{OLLAMA_URL}/embed",
    json={
        "model": EMBED_MODEL,
        "input": text
    }
)
```

---

### **Input**

```text
What is Python?
```

---

### **Output**

```text
[0.34, 0.21, 0.88, ...]
```

Vector representation.

---

### **Check Errors**

```python
if resp.status_code != 200:
```

If embedding generation fails.

---

### **Return Vector**

```python
return data["embeddings"][0]
```

---

## **Real-world Analogy**

Imagine converting a book into a barcode.

```text
Book
 ↓
Barcode
```

Embedding = AI Barcode.

---

## **Summary**

| Step             | Purpose            |
| ---------------- | ------------------ |
| POST /embed      | Generate embedding |
| status_code      | Error checking     |
| return embedding | Return vector      |

---


# -------------------------------------------------------
# **Part 5: Chat Function**
# -------------------------------------------------------

```python
def ollama_chat(prompt):
```

## **Purpose**

Send prompt to Llama3.

---

### **Call Chat API**

```python
requests.post(
    f"{OLLAMA_URL}/chat",
)
```

---

### **Prompt**

```text
What is AI?
```

Sent to Llama.

---

### **Streaming Enabled**

```python
"stream": True
```

Receive answer chunk by chunk.

---

### **Collect Response**

```python
final_answer += data["message"]["content"]
```

Combine chunks into one answer.

---

### **Return Answer**

```python
return final_answer
```

---

## **Real-world Analogy**

Imagine talking on a phone call.

```text
Question
   ↓
Teacher Thinking
   ↓
Answer arrives sentence by sentence
```

Streaming works similarly.

---

## **Summary**

| Step         | Purpose        |
| ------------ | -------------- |
| POST /chat   | Ask Llama      |
| stream=True  | Receive chunks |
| final_answer | Build response |

---

# -------------------------------------------------------
# **Part 6: Create ChromaDB Client**
# -------------------------------------------------------

```python
client = chromadb.PersistentClient(path=DB_PATH)
```

## **Purpose**

Connect to vector database.

---

### **PersistentClient**

Stores vectors permanently.

Even after application restart:

```text
Vectors remain saved.
```

---

## **Summary**

| Object           | Purpose             |
| ---------------- | ------------------- |
| PersistentClient | Database connection |

---


# -------------------------------------------------------
# **Part 7: Collection Management**
# -------------------------------------------------------



```python
def get_collection():
```

## **Purpose**

Get existing collection or create one.

---

### **Try Existing Collection**

```python
client.get_collection("rag_docs")
```

---

### **Create If Missing**

```python
client.create_collection(
    name="rag_docs"
)
```

---

### **Collection Meaning**

Think of it as a table.

```text
Collection
   ↓
Documents
   ↓
Embeddings
```

---

## **Summary**

| Function            | Purpose           |
| ------------------- | ----------------- |
| get_collection()    | Access collection |
| create_collection() | Create collection |

--

# --------------------------------------------------------

# **Part 8: Document Ingestion**
# -------------------------------------------------------

```python
def ingest_text(path):
```

## **Purpose**

Load documents into ChromaDB.

---

### **Read File**

```python
with open(path)
```

Load text file.

---

### **Chunking**

```python
CHUNK_SIZE = 1000
```

Split document.

Example:

```text
5000 Characters
       ↓
1000
1000
1000
1000
1000
```

---

### **Generate Embeddings**

```python
emb = ollama_embed(chunk)
```

Convert chunk into vectors.

---

### **Store In ChromaDB**

```python
collection.add(
    ids=[...],
    documents=[...],
    embeddings=[...]
)
```

Save:

```text
Chunk
 ↓
Embedding
 ↓
Database
```

---

## **Real-world Analogy**

Imagine a library.

```text
Book
 ↓
Pages
 ↓
Catalog Number
 ↓
Shelf
```

Chunk = Page

Embedding = Catalog Number

Chroma = Library Shelf

---

## **Summary**

| Step      | Purpose            |
| --------- | ------------------ |
| Read file | Load document      |
| Chunking  | Split content      |
| Embedding | Convert to vectors |
| Add       | Save in ChromaDB   |

---


# -------------------------------------------------------
# **Part 9: RAG Retrieval and Answering**
# -------------------------------------------------------



```python
def rag_answer(query):
```

## **Purpose**

Answer questions using stored documents.

---

### **Convert Question To Embedding**

```python
q_emb = ollama_embed(query)
```

---

### **Vector Search**

```python
collection.query(
    query_embeddings=[q_emb]
)
```

Find similar chunks.

---

### **Example**

Question:

```text
What is Flask?
```

Retrieved:

```text
Chunk 1:
Flask is a Python web framework

Chunk 2:
Flask provides routing
```

---

### **Build Context**

```python
ctx = "\n\n".join(docs[:5])
```

Combine top chunks.

---

### **Ask Llama**

```python
ollama_chat(
    f"Context:{ctx}
    Question:{query}"
)
```

---

## **RAG Flow**

```text
Question
    ↓
Embedding
    ↓
Vector Search
    ↓
Relevant Chunks
    ↓
Context
    ↓
Llama
    ↓
Answer
```

---

## **Summary**

| Step              | Purpose            |
| ----------------- | ------------------ |
| Query Embedding   | Search vector DB   |
| Similarity Search | Find relevant docs |
| Context Building  | Prepare prompt     |
| Llama             | Generate answer    |

---

# -------------------------------------------------------
# **Part 10: Flask Application Setup**
# -------------------------------------------------------



```python
app = Flask(__name__)
```

## **Purpose**

Create Flask application.

---

### **Home Route**

```python
@app.route("/")
```

Returns:

```text
RAG API is running
```

---

## **Summary**

| Route | Purpose      |
| ----- | ------------ |
| /     | Health check |

---

# **Part 11: Ingestion API**

```python
@app.route("/ingest", methods=["POST"])
```

## **Purpose**

Upload documents into ChromaDB.

---

### **Receive Path**

```python
path = request.json.get("path")
```

Example:

```json
{
  "path":"D:/docs/python.txt"
}
```

---

### **Ingest**

```python
ingest_text(path)
```

Store chunks.

---

## **Summary**

| Route   | Purpose        |
| ------- | -------------- |
| /ingest | Load documents |

---

# **Part 12: Ask API**

```python
@app.route("/ask", methods=["POST"])
```

## **Purpose**

Answer user questions.

---

### **Receive Question**

```python
q = request.json.get("question")
```

Example:

```json
{
  "question":"What is Flask?"
}
```

---

### **Call RAG**

```python
ans = rag_answer(q)
```

---

### **Return Answer**

```python
return jsonify({"answer": ans})
```

---

## **Summary**

| Route | Purpose       |
| ----- | ------------- |
| /ask  | Ask questions |

---

# **Part 13: Start Flask Server**

```python
if __name__ == "__main__":
```

## **Purpose**

Run application.

---

### **Start Server**

```python
app.run(
    debug=True,
    use_reloader=False
)
```

---

### **Access**

```text
http://127.0.0.1:5000
```

---

# **Complete RAG Workflow**

```text
Document
    ↓
Chunking
    ↓
Embedding (nomic-embed-text)
    ↓
ChromaDB Storage
    ↓

User Question
    ↓
Question Embedding
    ↓
Chroma Similarity Search
    ↓
Top Relevant Chunks
    ↓
Context Creation
    ↓
Llama3
    ↓
Final Answer
    ↓
Flask API Response
```

This is a complete **RAG (Retrieval-Augmented Generation) pipeline using Flask + Ollama + ChromaDB**.
