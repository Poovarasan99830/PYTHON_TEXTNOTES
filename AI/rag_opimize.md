# Mini RAG Project Internship Notes

## Retrieval-Augmented Generation (RAG) using Flask, Ollama, and ChromaDB

**Prepared For:** Internship Training Program
**Duration:** 2–4 Weeks
**Level:** Beginner to Intermediate AI/ML Students

---

# Table of Contents

1. Project Introduction
2. What is RAG?
3. Why RAG is Needed
4. Problems Solved by RAG
5. Project Architecture
6. Data Flow Diagram
7. Component Interaction Diagram
8. Technologies Used
9. Project Folder Structure
10. Step-by-Step Execution Flow
11. Detailed Code Explanation
12. ChromaDB Concepts
13. Ollama Concepts
14. Embedding Concepts
15. Retrieval Process
16. API Endpoints
17. Error Handling
18. Memory Management
19. Interview Questions & Answers
20. Viva Questions & Answers
21. Real-Time Industry Use Cases
22. Advantages and Limitations
23. Future Enhancements
24. Project Summary

---

# 1. Project Introduction

## What is RAG?

RAG stands for **Retrieval-Augmented Generation**.

It combines:

* Information Retrieval
* Large Language Models (LLMs)

Instead of relying only on the model's training data, RAG retrieves relevant information from external documents and uses it to generate answers.

---

## Real-World Analogy

Imagine a student writing an exam.

### Without RAG

The student answers from memory.

```text
Question
   ↓
Memory
   ↓
Answer
```

The answer may be incorrect.

### With RAG

The student first opens notes.

```text
Question
   ↓
Search Notes
   ↓
Read Relevant Pages
   ↓
Answer
```

This produces more accurate results.

---

# 2. Why RAG is Needed

Traditional LLMs have limitations.

| Problem              | Description                      |
| -------------------- | -------------------------------- |
| Hallucination        | Generates false information      |
| Outdated Knowledge   | Training data may be old         |
| No Company Knowledge | Cannot access internal documents |
| Limited Context      | Doesn't know user files          |

RAG solves these issues.

---




# 3. Problems Solved by RAG



## Problem 1: Hallucination

Without retrieval:

```text
Question → LLM → Guess
```

With retrieval:

```text
Question
   ↓
Document Search
   ↓
Relevant Content
   ↓
LLM
   ↓
Answer
```

---

## Problem 2: Internal Knowledge Access

Example:

A company has:

* HR Policies
* Product Manuals
* Technical Documentation

RAG allows the chatbot to answer from those documents.

---

# 4. Project Architecture

## High-Level Architecture

```text


Document
   ↓
Chunking
   ↓
Embedding Model
   ↓
Vector Database
   ↓
------------------
User Question
   ↓
Embedding
   ↓
Similarity Search
   ↓
Relevant Chunks
   ↓
Prompt
   ↓
LLM
   ↓
Answer
```

---

# 5. Data Flow Diagram

```text
User Uploads TXT File
          │
          ▼
      Read File
          │
          ▼
      Chunk Text
          │
          ▼
 Generate Embeddings
          │
          ▼
      ChromaDB
          │
          ▼
--------------------------------

 User Question
          │
          ▼
 Generate Embedding
          │
          ▼
 Similarity Search
          │
          ▼
 Top Matching Chunks
          │
          ▼
 Prompt Creation
          │
          ▼
      Phi3 Model
          │
          ▼
     Final Answer
```

---

# 6. Component Interaction Diagram

```text
+------------+
|   User     |
+------------+
      |
      v
+------------+
| Flask API  |
+------------+
      |
      v
+------------+
|  Ollama    |
| Embeddings |
+------------+
      |
      v
+------------+
| ChromaDB   |
+------------+
      |
      v
+------------+
| Phi3 Mini  |
+------------+
      |
      v
+------------+
|  Response  |
+------------+
```

---

# 7. Technologies Used

## Python

Python is the main programming language.

Responsibilities:

* API Development
* Data Processing
* ChromaDB Operations
* Ollama Integration

---

## Flask

Flask is a lightweight Python web framework.

Used for:

* `/ingest`
* `/ask`

API endpoints.

---

## ChromaDB

Vector Database used for:

* Storing embeddings
* Similarity search
* Retrieval

---

## Ollama

Runs AI models locally.

Benefits:

* No API cost
* Offline support
* Fast inference

---

## Embedding Model

Model:

```text
nomic-embed-text
```

Purpose:

Convert text into vectors.

---

## LLM Model

Model:

```text
phi3:mini
```

Purpose:

Generate answers.

---

# 8. Project Folder Structure

```text
project/
│
├── app.py
├── db/
├── documents/
├── requirements.txt
└── README.md
```

## app.py

Main application.

Contains:

* Flask API
* Embedding Logic
* Retrieval Logic
* Chat Logic

---

## db/

Stores ChromaDB files.

---

## documents/

Stores uploaded files.

---

## requirements.txt

Contains dependencies.

Example:

```text
flask
requests
chromadb
```

---

# 9. Step-by-Step Execution Flow

## Step 1: Upload Document

Request:

```json
{
  "path":"notes.txt"
}
```

---

## Step 2: Read File

```python
with open(file_path)
```

Reads document.

---

## Step 3: Chunking

Example:

```text
Large Document
```

Split into:

```text
Chunk 1
Chunk 2
Chunk 3
```

---

## Step 4: Embedding Generation

Each chunk becomes:

```text
Chunk
 ↓
Vector
```

Example:

```python
[0.21,0.55,-0.87,...]
```

---

## Step 5: Store in ChromaDB

```python
collection.add(...)
```

Stores:

* Text
* Vector
* ID

---

## Step 6: User Question

```text
What is Flask?
```

---

## Step 7: Question Embedding

Question becomes vector.

---

## Step 8: Similarity Search

```python
collection.query(...)
```

Finds nearest chunks.

---

## Step 9: Context Creation

```python
context = "\n".join(chunks)
```

---

## Step 10: Prompt Construction

```text
Context:
...

Question:
...

Answer:
```

---

## Step 11: Response Generation

Phi3 generates answer.

---

# 10. Detailed Code Explanation

## ollama_embed()

Purpose:

Generate embeddings.

### Input

```python
text
```

### Output

```python
vector
```

Workflow:

```text
Text
 ↓
Ollama
 ↓
Embedding
```

---

## ollama_chat()

Purpose:

Generate response.

Workflow:

```text
Prompt
 ↓
Phi3
 ↓
Answer
```

---

## ingest_text()

Purpose:

Store document vectors.

Workflow:

```text
Read
 ↓
Chunk
 ↓
Embed
 ↓
Store
```

---

## rag_answer()

Purpose:

Answer questions.

Workflow:

```text
Question
 ↓
Embedding
 ↓
Search
 ↓
Prompt
 ↓
Answer
```

---

# 11. ChromaDB Concepts

## Collection

Equivalent to SQL Table.

Example:

```python
collection = client.create_collection(...)
```

---

## Document

Actual chunk text.

---

## Embedding

Numerical representation.

---

## Metadata

Additional information.

Example:

```python
{
 "source":"notes.txt"
}
```

---

## Similarity Search

Finds nearest vectors.

---

# 12. Ollama Concepts

## Local LLM

Runs models locally.

Benefits:

* Privacy
* Offline
* Free

---

## Embedding Model

Converts text into vectors.

Example:

```text
nomic-embed-text
```

---

## Chat Model

Generates answers.

Example:

```text
phi3:mini
```

---

## API Calls

Embedding:

```text
/api/embed
```

Chat:

```text
/api/chat
```

---

# 13. Embedding Concepts

## What is Embedding?

A vector representation of text.

Example:

```text
Python
```

↓

```python
[0.12,0.45,-0.23,...]
```

---

## Why Use Vectors?

Computers compare numbers faster than text.

---

## Vector Dimensions

Typical dimensions:

| Model  | Dimensions |
| ------ | ---------- |
| Small  | 384        |
| Medium | 768        |
| Large  | 1536       |

---

## Similarity

Two similar meanings produce similar vectors.

---

# 14. Retrieval Process

## Top-K Search

```python
n_results=3
```

Returns top 3 matches.

---

## Cosine Similarity

Measures angle between vectors.

```text
1.0 = Similar
0.0 = Different
```

---

## Ranking

Results sorted by similarity.

---

## Context Retrieval

Top chunks become context.

---

# 15. API Endpoints

## /ingest

### Request

```json
{
 "path":"notes.txt"
}
```

### Response

```json
{
 "message":"Ingestion completed"
}
```

---

## /ask

### Request

```json
{
 "question":"What is Flask?"
}
```

### Response

```json
{
 "answer":"Flask is a micro web framework."
}
```

---

# 16. Error Handling

Common Issues:

| Error              | Cause             |
| ------------------ | ----------------- |
| File Not Found     | Wrong path        |
| Ollama Down        | Server stopped    |
| Collection Missing | ChromaDB issue    |
| Empty Result       | No matching chunk |

Troubleshooting:

1. Check Ollama running.
2. Check file path.
3. Verify collection exists.
4. Restart application.

---

# 17. Memory Management

## Conversation Memory

Stores previous chats.

Example:

```text
User: My name is John
Bot remembers
```

---

## Vector Memory

Stored inside ChromaDB.

---

## Persistence

Database remains after restart.

---

# 18. Interview Questions and Answers

### Q1: What is RAG?

Combines retrieval and generation.

### Q2: Why use embeddings?

To perform semantic search.

### Q3: What is ChromaDB?

A vector database.

### Q4: What is chunking?

Splitting documents into smaller parts.

### Q5: Why chunk data?

Improves retrieval quality.

### Q6: What is cosine similarity?

Measures vector similarity.

### Q7: What is semantic search?

Search by meaning.

### Q8: Why use Ollama?

Run models locally.

### Q9: What is Phi3 Mini?

Lightweight Microsoft LLM.

### Q10: What is an embedding model?

Model that converts text into vectors.

### Q11-Q30

1. Difference between SQL and Vector DB?
2. What is metadata?
3. What is retrieval?
4. What is prompt engineering?
5. What is context window?
6. What is hallucination?
7. What is Top-K?
8. Why use local models?
9. What is HNSW?
10. What is indexing?
11. What is vector dimension?
12. What is persistence?
13. Explain ingestion.
14. Explain retrieval.
15. Explain generation.
16. Explain Flask API.
17. Explain similarity search.
18. Explain ranking.
19. Explain embeddings.
20. Explain RAG architecture.

---

# 19. Viva Questions and Answers

### Q1

What is Flask?

A lightweight Python framework.

### Q2

What is ChromaDB?

Vector database.

### Q3

What is Ollama?

Local AI model runner.

### Q4

What is RAG?

Retrieval-Augmented Generation.

### Q5

What is chunking?

Splitting text.

### Q6-Q30

1. What is embedding?
2. What is vector?
3. What is retrieval?
4. What is prompt?
5. What is API?
6. What is JSON?
7. What is similarity?
8. What is ranking?
9. What is context?
10. What is metadata?
11. What is persistence?
12. What is cosine similarity?
13. What is Top-K search?
14. Why use vector DB?
15. Explain ChromaDB collection.
16. Explain Ollama API.
17. Explain Flask route.
18. Explain local LLM.
19. Explain Phi3.
20. Explain semantic search.
21. Explain ingestion pipeline.
22. Explain retrieval pipeline.
23. Explain prompt creation.
24. Explain context window.
25. Explain hallucination.

---

# 20. Real-Time Industry Use Cases

## Customer Support Bot

Answers customer questions using company documents.

---

## Company Knowledge Base

Search internal policies.

---

## Healthcare Assistant

Retrieve medical guidelines.

---

## Legal Document Search

Search contracts and legal documents.

---

## Enterprise Search

Find information from internal systems.

---

# 21. Advantages

| Advantage   | Benefit                    |
| ----------- | -------------------------- |
| Accurate    | Uses documents             |
| Low Cost    | Local models               |
| Fast Search | Vector DB                  |
| Scalable    | Large document collections |

---

# 22. Limitations

| Limitation       | Description     |
| ---------------- | --------------- |
| Retrieval Errors | Wrong chunks    |
| Context Limit    | Limited tokens  |
| Storage Cost     | Large vector DB |
| Chunk Dependency | Quality matters |

---

# 23. Future Enhancements

1. PDF Support
2. DOCX Support
3. Conversation Memory
4. User Authentication
5. Streaming Responses
6. Metadata Filtering
7. Hybrid Search
8. Re-ranking Models
9. Multi-Document Search
10. Web UI

---

# 24. Project Summary

This Mini RAG project demonstrates how modern AI systems combine vector databases and large language models to answer questions from custom documents.

Workflow:

```text
Document
 ↓
Chunking
 ↓
Embedding
 ↓
ChromaDB
 ↓
Retrieval
 ↓
Prompt
 ↓
LLM
 ↓
Answer
```

The project provides practical experience in:

* Python Development
* Flask APIs
* ChromaDB
* Ollama
* Embeddings
* Retrieval-Augmented Generation
* Local LLM Deployment

These skills are highly valuable for AI Engineer, Python Developer, and Generative AI roles.
