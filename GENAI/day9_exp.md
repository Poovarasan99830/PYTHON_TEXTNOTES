


# -----------------------------------------
# 🔷 Context Window Limit
# -----------------------------------------





## 🧠 1. FIRST PRINCIPLE

👉 **Context window** =
Model-ku oru time-la **evlo text (tokens) padikka mudiyum** nu limit

---

### 🔹 Simple definition

```text
Context Window = Maximum tokens model can see at once
```

👉 Tokens = words illa,
**small pieces of words**

Example:

```
"I love AI" → 3–4 tokens
```

---

## 🔥 2. WHY IMPORTANT?

👉 Model:

* Past conversation
* Current question
* Retrieved documents

👉 Ella data-yum **one shot-la paakanum**

BUT ❌ limit irukku

---

## 🧠 3. Example (Very Clear)

### Assume:

👉 Model context window = 1000 tokens

---

### Situation:

* User question = 100 tokens
* Retrieved docs = 1200 tokens

👉 Total = 1300 tokens ❌

---

👉 Problem:

* Model full data padikka mudiyadhu
* Some part **truncate (cut)** aagum

---

## 🔥 4. Behind the Scene

👉 Model internally:

```text
Input tokens → Process → Output tokens
```

👉 If limit exceed:

* Old data remove pannum
  OR
* Extra text ignore pannum

---

## 🔥 5. Real-Time Analogy

### 🧠 Human Brain Example

👉 Teacher 10 pages kudutha:

* Neenga 2 pages dhaan padikka mudiyum
  👉 rest miss aagum

👉 Idhe dhaan:

> Context window limit

---

## 🔥 6. Why Chunking comes here

👉 Large document → split pannuvom

Why?

✔ Fit inside context window
✔ Only relevant chunk send pannuvom

---

## 🔹 Example Flow (RAG)

```text
Big PDF (5000 tokens)
        ↓
Chunking (500 tokens each)
        ↓
Retriever picks 2 chunks (1000 tokens)
        ↓
Fits inside context window ✅
```

---

## 🔥 7. Common Context Window Sizes

| Model    | Context Window |
| -------- | -------------- |
| GPT-3    | ~4K tokens     |
| GPT-4    | ~8K / 32K      |
| New LLMs | 100K+ tokens   |

---

## 🧠 8. Key Insight (Important)

👉 More context ≠ always better

Why?

* Noise increase
* Irrelevant info confuse pannum

👉 So:
✔ Right chunk selection = important

---

## ⚡ One-Line Answer (Interview)

👉
**“Context window limit is the maximum number of tokens an LLM can process at once, including input, retrieved data, and conversation history.”**

---

## 📌 /BRIEFLY

* Context window = model memory size
* Token-based limit
* Exceed pannina → data cut aagum
* Chunking → solution










# 🔷 🔍 Types of Retrieval (In-Depth Thanglish)

---

# 🔹 1. Keyword-Based Retrieval (Lexical Search)

## 🧠 Simple Meaning

👉 Query-la irukka **exact word match** pannum system

---

## 🔍 Example

```text
Query: "AI course"
```

👉 System search pannum:

* "AI" irukka?
* "course" irukka?

✔ match → return
❌ illa → ignore

---

## 🔥 Behind the Scenes

👉 Internally:

```text
Document → words split (tokens)
Query → words split
Compare → same words irukka?
```

👉 Use pannra algorithms:

* TF-IDF
* BM25

---

## ❌ Problem

👉 Meaning puriyaadhu

Example:

```text
Query: "car"
Doc: "vehicle"
```

❌ match aagadhu

---

## 🔥 Real-Life Analogy

👉 Phone contact search:

* "Ravi" nu type panna
  ✔ Ravi dhaan varum

❌ "Friend" nu type panna Ravi varadhu

---

# 🔹 2. Semantic Search (Vector Search)

## 🧠 Simple Meaning

👉 Words illa
👉 **Meaning match pannum system**

---

## 🔍 Example

```text
Query: "car"
Doc: "vehicle"
```

✔ match pannum (because meaning same)

---

## 🔥 Behind the Scenes (VERY IMPORTANT)

### 🧠 Step 1: Convert to vectors

```text
"car" → [0.2, 0.7, 0.1]
"vehicle" → [0.21, 0.69, 0.11]
```

👉 Close values → similar meaning

---

### 🧠 Step 2: Similarity check

👉 Cosine similarity use pannum:

```text
High similarity → relevant
Low similarity → ignore
```

---

### 🧠 Step 3: Top results return

👉 Best matching chunks edukkum

---

## 🔥 Real-Life Analogy

👉 Neenga Google-la search pannreenga:

```text
"How to fix bike"
```

👉 Result:
✔ "motorcycle repair guide"

👉 Same words illa
👉 Meaning match pannum

---

# 🔹 3. Hybrid Search

## 🧠 Simple Meaning

👉 Keyword + Semantic rendu combine pannum

---

## 🔍 Why needed?

👉 Keyword:
✔ exact match strong
❌ meaning weak

👉 Semantic:
✔ meaning strong
❌ exact word miss aagalam

---

## 🔥 Solution:

```text
Hybrid = Keyword + Semantic
```

---

## 🧠 Behind the Scenes

👉 System pannum:

1. Keyword score calculate pannum
2. Semantic score calculate pannum
3. Combine pannum
4. Final ranking kudukkum

---

## 🔥 Real-Life Analogy

👉 Job search:

* Resume-la keywords check pannuvanga
* Meaning (skills) check pannuvanga

👉 Rendu combine pannina dhaan best candidate 🔥

---

# 🔹 4. Dense vs Sparse Retrieval

---

## 🔹 Sparse Retrieval

👉 Keyword-based system

```text
Text → bag of words → count → match
```

👉 Example:

* TF-IDF
* BM25

👉 특징:
✔ Fast
❌ Meaning illa

---

## 🔹 Dense Retrieval

👉 Embedding-based system

```text
Text → vector → similarity
```

👉 특징:
✔ Meaning understand pannum
❌ Compute heavy

---

## 🔥 Comparison Table

| Feature  | Sparse            | Dense       |
| -------- | ----------------- | ----------- |
| Based on | Keywords          | Meaning     |
| Accuracy | Medium            | High        |
| Speed    | Fast              | Medium      |
| Example  | Google old search | ChatGPT RAG |

---

# 🧠 FINAL FLOW (Super Important 🔥)

```text
User Query
   ↓
Convert to vector
   ↓
Compare with DB vectors
   ↓
Rank results
   ↓
Top chunks return
```

---

# ⚡ One-Line Interview Answer

👉
**“Retrieval mechanisms use keyword-based, semantic, or hybrid approaches to find the most relevant data, with dense retrieval leveraging embeddings for meaning-based matching.”**

---

# 📌 /BRIEFLY (Thanglish)

* Keyword → exact word match
* Semantic → meaning match
* Hybrid → both combine
* Sparse → keywords
* Dense → embeddings

👉 Key idea:
✔ Correct retrieval = correct answer

---

If you want next 🔥
👉 Cosine similarity **math + visual explanation**
👉 FAISS internal working **step-by-step**





Got it 👍 — you want **that job-search analogy explained deeply** so you can map it clearly to **Hybrid Retrieval**. I’ll break it step-by-step in **Thanglish + technical depth** 👇

---

# 🔷 Hybrid Retrieval – Deep Understanding (Job Search Analogy)

---

# 🧠 Big Idea

👉 Hybrid Retrieval =
**Keyword Matching + Meaning (Semantic) Matching combine pannradhu**

---

# 🔥 Real Scenario: Company Hiring Process

Imagine pannunga 👇

## 👨‍💼 HR hiring pannraanga

Candidate resume vandhirukku

---

# 🔹 Step 1: Keyword Filtering (ATS System)

👉 HR first enna pannuvaanga?

✔ Resume-la **keywords check pannuvaanga**

Example job:

```text
"Python Developer"
```

👉 System check pannum:

* "Python" irukka?
* "Django" irukka?
* "API" irukka?

---

### 🧠 Internal Thinking

```text
Resume → words split
Job description → words split
Compare → same words irukka?
```

👉 If match:
✔ Pass

👉 If not:
❌ Reject

---

## ❌ Problem (Keyword-only system)

Candidate resume:

```text
"Worked on backend systems using Flask"
```

👉 Keyword:

* "Python" illa ❌
* Reject aagidum

BUT 😳
👉 Flask = Python framework

👉 So good candidate miss aagidum

---

# 🔹 Step 2: Semantic Understanding (Human HR)

👉 Ippo HR manual-a paathaa:

* Flask → Python related
* Backend → relevant skill

👉 HR yosikum:
✔ “Ithu correct candidate dhaan”

---

### 🧠 Internal Thinking

```text
Skills → meaning analyze pannum
Context → purinjukum
```

👉 Word match illa
👉 BUT meaning match irukku ✅

---

# 🔥 Step 3: Combine (Hybrid)

👉 Best system enna pannum?

```text
Keyword Score + Semantic Score → Final Score
```

---

### 🧠 Example Scoring

| Candidate        | Keyword Score | Semantic Score | Final   |
| ---------------- | ------------- | -------------- | ------- |
| A (Python exact) | 0.9           | 0.8            | 🔥 0.85 |
| B (Flask only)   | 0.3           | 0.9            | 🔥 0.75 |
| C (Irrelevant)   | 0.2           | 0.2            | ❌       |

👉 System top candidates select pannum

---

# 🔥 Mapping to Retrieval System

| Job System       | RAG System       |
| ---------------- | ---------------- |
| Resume           | Document         |
| Job description  | Query            |
| Keyword filter   | Sparse search    |
| HR understanding | Semantic search  |
| Final ranking    | Hybrid retrieval |

---

# 🧠 Behind the Scenes (Technical Flow)

## Step 1: Query processing

```text
User query → two ways process pannum
```

---

### 🔹 Path 1: Keyword Search

```text
Query → tokens → match words in documents
```

---

### 🔹 Path 2: Semantic Search

```text
Query → embedding → vector
Compare with DB vectors → similarity score
```

---

## Step 2: Score Combination

```text
Final Score = (alpha × keyword_score) + (beta × semantic_score)
```

👉 Example:

```text
0.5 × keyword + 0.5 × semantic
```

---

## Step 3: Ranking

👉 Highest score → top results

---

# 🔥 Why Hybrid is Powerful

## ❌ Keyword-only problem

* Meaning miss pannum

## ❌ Semantic-only problem

* Exact terms miss pannum

---

## ✅ Hybrid Solution

✔ Exact match + meaning match
✔ Better accuracy
✔ Real-world production system

---

# 🔥 Real System Usage

👉 Used in:

* Google Search
* ChatGPT RAG systems
* E-commerce search
* Enterprise knowledge bots

---

# 🧠 Final Insight (Important 🔥)

👉 Retrieval la **most important part = ranking**

Even if data correct-a retrieve pannalum:
❌ wrong order → wrong answer

👉 So:
✔ Score combination critical

---

# ⚡ One-Line Interview Answer

👉
**“Hybrid retrieval combines keyword-based matching and semantic similarity scoring to improve both precision and recall in information retrieval.”**

---

# 📌 /BRIEFLY (Thanglish)

* Keyword → exact words
* Semantic → meaning
* Hybrid → rendu combine
* Score calculate pannum
* Best result select pannum

---

If you want next 🔥
👉 Cosine similarity **step-by-step math + diagram**
👉 FAISS search **internals (indexing + retrieval)**
