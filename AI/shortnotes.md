

_____________________________________________________________________________________

What is LLM ?
_____________________________________________________________________________________



“LLM learns language structure using transformers,
 but frameworks like LangChain give it logic, memory, and real-world control.” ⚙️


 _____________________________________________________________________________________

What is LongChain?
_____________________________________________________________________________________




# LangChain = the bridge between LLMs and real-world applications.


CAB
C=connecting external db,
  connect your llm(like open AI)to outside data sources(google search,SQl,pdf,api)

A=Add Memory(so its remembers what happened earlier)

B=Build chain step by step work flow(get data -->analyze--->return answer)

LLM brain, LangChain brain control system, RAG data memory, FastAPI frontend face





| Example          | Role                                                                                                  |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| 🗣️ **LLM**      | Like ChatGPT itself — understands and replies in language.                                            |
| 🧰 **LangChain** | Like a *project manager* who decides when to ask ChatGPT, when to call APIs, when to store data, etc. |




_____________________________________________________________________________________
 Draw data flow (user → LLM → response)?
_____________________________________________________________________________________



┌──────────────────────────────┐
│        AI Agent              │
│  (LangChain Framework)       │
├──────────────┬───────────────┤
│              │               │
▼              ▼               ▼
LLM            Tools           Memory
(GPT/Claude)   (APIs, DBs)     (Conversation Context)



───────────────────────────────────────────────
                USER

🧑‍💻  User asks:  "Show me latest AI research papers"
↓
───────────────────────────────────────────────
                LLM (GPT / Claude)

🧠  Understands question  
🤔  Decides: "I need to use the Arxiv Tool to find papers"
↓
───────────────────────────────────────────────
              LANGCHAIN TOOL

🔧 Tool Name:  ArxivQueryRun  
🧩 Function:   Uses ArxivAPIWrapper  
💬 Description: "Fetch papers from the arXiv database"

👉 The tool calls a **Python function or API** defined inside LangChain
↓
───────────────────────────────────────────────
              EXTERNAL API (REAL DATA)

🌐  API:  https://export.arxiv.org/api/query  
📚  Data Source:  Research papers repository  
⬅️  Returns: Titles, authors, abstracts, links
↓
───────────────────────────────────────────────
              LANGCHAIN TOOL

🧩 Receives JSON/XML data from arXiv  
📦 Parses and sends clean text back to LLM
↓
───────────────────────────────────────────────
                LLM (GPT / Claude)

🧠 Reads abstracts  
🪄 Summarizes papers  
🗣️ Prepares a natural-language answer
↓
───────────────────────────────────────────────
                    USER

💬 "Here are top 3 recent AI papers from arXiv:  
1️⃣ …  
2️⃣ …  
3️⃣ …"
streamlit run app.py



───────────────────────────────

🧭 CASE A: MEMORY MISS (First Time)
User Query
   ↓
Memory ❌ Not Found
   ↓
LLM → Uses Tool → API Call → Summarize
   ↓
Store Result → Return Response



───────────────────────────────
🧠 CASE B: MEMORY HIT (Later Query)
User Query
   ↓
Memory ✅ Found
   ↓
LLM → Uses Context → Generate Response
   ↓
Return Response (No Tool Needed)





# _____________________________________
     ***####  Memory ####*****
# _____________________________________





User Query
   │
   ▼
Check Memory
   ├── ✅ Found → Send context → LLM → Respond
   └── ❌ Not Found
           ↓
         LLM Reasoning
           ↓
        Decide Tool Call
           ↓
        TMDb API → Data
           ↓
        LLM Summarize + Store in Memory
           ↓
        Return Response


Memory check happens before LLM call.

LLM never calls tools if memory already satisfies the question.

Short-term memory = session context.

Long-term (Vector DB) = cross-session recall (knowledge retention).


1️⃣ when memory already has the answer, and
2️⃣ when no memory is found → LLM decides to use a Tool (like TMDb API).


🧠 Memory is always checked first.
If it fails → the LLM decides which tool (API, DB, etc.) to use → then the result is stored back into memory for next time.





| Layer               | Tool / Framework        | Description                     |
| ------------------- | ----------------------- | ------------------------------- |
| **Frontend**        | Streamlit / React       | User Interface                  |streamlit run app.py
| **API Layer**       | FastAPI / Flask         | Communication + Logic           |
| **Orchestration**   | LangChain               | Manages flow & prompt logic     |
| **LLM**             | GPT-5 / Claude / Gemini | Generates summaries             |
| **External Source** | arXiv API               | Paper data source               |
| **Database**        | SQLite / PostgreSQL     | Stores queries, papers, results |



| Layer                   | What Happens                                |
| ----------------------- | ------------------------------------------- |
| **LLM (GPT)**           | Thinks, reasons, and writes text            |
| **LangChain Engine**    | Controls the logic (who calls what)         |
| **Tool (Custom)**       | Sends real HTTP request to TMDb             |
| **External API (TMDb)** | Returns JSON data                           |
| **Response Path**       | API → Tool → LangChain → LLM → Backend → UI |

streamlit run app.py



_____________________________________________________________________________________
LANGCHAIN — CONCEPTS SUMMARY ?
_____________________________________________________________________________________



“LangChain is not an AI model — it’s the framework that helps manage how AI models (LLMs) interact with tools, memory, and external data in a structured, reusable way.


| Concept       | Role              | Analogy           |
| ------------- | ----------------- | ----------------- |
| LLM           | Brain             | Thinker           |
| Prompt        | Instruction       | Question format   |
| Chain         | Workflow          | Assembly line     |
| Memory        | Context storage   | Short-term memory |
| Agent         | Decision maker    | Manager           |
| Tool          | Helper function   | Worker            |
| Retriever     | Knowledge fetcher | Google search     |
| Output Parser | Formatter         | Data cleaner      |
| Callback      | Tracker           | Logger            |
| LangSmith     | Debugger          | QA Tester         |



https://chatgpt.com/share/69123a1b-8da8-800a-88af-51cbc57e962c

_____________________________________________________________________________________
Build LangChain + OpenAI mini chatbot ?
_____________________________________________________________________________________



# ────────────────────────────────────────────────────────
                      EduBot Architecture
# ────────────────────────────────────────────────────────

[User Browser / Streamlit UI]
  - sends user query (POST / via streamlit input)
  - receives rendered response

        │
        ▼

[Frontend (Streamlit app)]
  - collects user_input
  - displays chat history
  - calls local chat function `chat(user_input)` (no public API required)
  - reads environment variables at startup

        │
        ▼

[Application Logic Layer]
  - chatbot.bot_core.create_edubot() returns chat() function
  - manages in-memory or persistent history (ChatMessageHistory)
  - constructs message list (system prompt + history + user message)
  - handles LLM call + exceptions + fallback logic

        │
        ▼

[LLM Provider Adapter (langchain_groq)]
  - ChatGroq model invocation (model ID exactly matching provider)
  - uses GROQ_API_KEY from environment
  - possible responses: success | model_deprecated | rate-limit | quota error

        │
        ▼
[External LLM Service: Groq]
  - runs Llama models (e.g., llama-3.1-8b-instant)
  - returns text response or error codes (handle them gracefully)

        │
        ▼

[Optional: Persistence]
  - Save conversation to SQLite / Supabase / Firebase
  - Use for long-term memory, analytics, or per-user history

        │
        ▼

[Monitoring & Logging]
  - Console logs + file logs
  - Optionally use LangSmith / Sentry for observability






  
LangChain = toolkit
Groq API = communication channel
Model (llama-3.1) = actual brain
LLM = general term for that kind of AI brain
EduBot = your final assembled app that uses all of them.




| Principle                | Developer Reality                           | Analogy                 |
| ------------------------ | ------------------------------------------- | ----------------------- |
| **Architecture**         | Transformer design defines how model thinks | Brain wiring            |
| **Parameters (8B, 70B)** | Model capacity / intelligence               | Number of neurons       |
| **Tokenizer**            | Converts words ↔ numbers                    | Dictionary of syllables |
| **Context Window**       | How much text model “remembers”             | Short-term memory       |
| **Version / Flavor**     | Indicates speed / capability trade-offs     | Textbook editions       |
| **Hosted Model**         | API-managed LLM                             | Cloud classroom         |
| **API ID**               | Model’s code name                           | Product SKU             |







| Step    | Layer                  | Description                           | Example                         |
| ------- | ---------------------- | ------------------------------------- | ------------------------------- |
| **1️⃣** | Frontend               | User inputs query in Streamlit        | `"Explain Python decorators"`   |
| **2️⃣** | Prompt Builder         | LangChain builds conversation context | System + history + user         |
| **3️⃣** | LLM Wrapper (ChatGroq) | Converts prompt → API request         | model, temp, key                |
| **4️⃣** | Groq API               | Executes model inference              | `llama-3.1-8b-instant`          |
| **5️⃣** | Response Handling      | LangChain wraps + returns reply       | `AIMessage(content=...)`        |
| **6️⃣** | Frontend Display       | Streamlit shows output                | EduBot’s answer                 |
| **7️⃣** | Memory Update          | Adds both messages to history         | Enables conversation continuity |



# __________________________________________________________________________________
*          [ ] Day 8: Dissect 1 new library (ChromaDB) → folder + API flow
# __________________________________________________________________________________


ChromaDB stores **vectors**, **documents**, and **metadata**, enabling fast information retrieval based on meaning.



my_rag_app/
│
├── data/
│   └── chroma/            # ChromaDB persistent storage
│
├── src/
│   ├── ingest.py          # Add documents + embed
│   ├── query.py           # Query the DB
│   └── utils.py           # Helpers
│
└── requirements.txt





## **5. Core API Flow (Explained)**
          Raw Text → Embedding → Stored in ChromaDB → Semantic Search → Relevant Output





## **10. ChromaDB + LangChain Flow**
            Documents → Embeddings → Chroma Vector Store → LangChain Retriever → LLM




## **15. Architecture Diagram (Text-Based)**

```
              +------------------------+
              |      Your Dataset      |
              |  (PDF, TXT, HTML, etc) |
              +-----------+------------+
                          |
                          v
                 +--------+--------+
                 |  Text Splitter   |
                 |  (Chunking)      |
                 +--------+--------+
                          |
                          v
             +------------+-------------+
             |   Embedding Model        |
             | (OpenAI / HF / Others)   |
             +------------+-------------+
                          |
                          v
          +---------------+-----------------+
          |              ChromaDB           |
          |  - Store vectors                |
          |  - Store documents              |
          |  - Store metadata               |
          |  - Semantic search              |
          +---------------+-----------------+
                          |
                          v
                 +--------+--------+
                 |   Retriever     |
                 | (Top‑K Search)  |
                 +--------+--------+
                          |
                          v
            +-------------+--------------+
            |          LLM Model         |
            |   (GPT, Claude, etc.)      |
            |  Combines query + context   |
            +-------------+--------------+
                          |
                          v
                 +--------+--------+
                 |  Final Response  |
                 | (Answer Output)  |
                 +------------------+
```

##  One-Page Summary**


ChromaDB = Fast vector database for storing embeddings + semantic search.
           Perfect for RAG and LLM apps.



# __________________________________________________________________________________
* # Break code on purpose → fix & learn
# __________________________________________________________________________________


ollama run llama3




# **PART 1 — INGEST WORKFLOW**
          (You upload document → create chunks → embed → store in Chroma)



{
  "path": "D:/PYTHON FULL STACK DEVELOPMENT/DJANGO_FLASK_CLASS/AI/rag_project1/data/notes.txt"
}
{
  "question": "What is Python decorator?"
}


| Layer                      | Purpose                                          |
| -------------------------- | ------------------------------------------------ |
| **1. Embeddings (Ollama)** | Convert text into meaningful numbers             |
| **2. ChromaDB**            | Store those vectors and retrieve similar chunks  |
| **3. Chunking**            | Break big documents into small, searchable parts |
| **4. RAG Pipeline**        | Query → retrieve chunks → generate answer        |
| **5. Flask API**           | Expose everything as HTTP endpoints              |





# _________________________________________________________

What Is Ollama? 
    Ollama is an offline platform that lets you run LLM models locally on your own system.
    It does not require internet, and no data goes to any cloud.

✔ Runs fully offline
✔ Supports many open-source LLMs
✔ Works on Windows, macOS, Linux


# __________________________________________________
What Ollama Can Do
   ✔ Download open-source models

Like:
  Llama 3 / 3.1 / 3.2
  Qwen 2.5
  Phi-3
  Mistral / Mixtral
  DeepSeek-R1
  StarCoder2
  Gemma 2

# __________________________________________________

Why Companies Use Ollama

| Benefit                | Explanation                                 |
| ---------------------- | ------------------------------------------- |
| **Privacy**            | No data leaves your laptop or server        |
| **Cost saving**        | No API charges like GPT/Claude              |
| **Full control**       | You choose the model, version, quantization |
| **Offline capability** | Works without internet                      |
| **Fast inference**     | Uses GPU/CPU efficiently                    |


# __________________________________________________

Ollama Is NOT a Model — It Is a Platform

Ollama = local LLM engine
LLM = actual model (Llama, Qwen, etc.)


          Text documents
                 |
      [Embedding Model]
     (bge, e5, llama-embed)
                 ↓
         VECTOR embeddings
                 |
        Vector Database
                 |
         Query → Embedding
                 |
         Similarity Search
                 |
        Top chunks retrieved
                 |
      [Chat Model - GPT / Llama]
                 ↓
            Final Answer


Install **Python 3.10+**
python --version
[https://ollama.com](https://ollama.com)



# __________________________________________________



ollama --version
ollama pull llama3
ollama pull nomic-embed-text

ollama serve
   Error: listen tcp 127.0.0.1:11434: bind:
   Only one usage of each socket address is normally permitted

   Ollama server already background-la run aagudhu,
   models install pannita,
   ippo direct ah Flask RAG app run panna podhum

ollama list
   


python app.py


# __________________________________________________


chroma.sqlite3 is being used by another process
   👉 Your Flask app (Python) is still running
   👉 ChromaDB keeps chroma.sqlite3 OPEN
   👉 Windows does NOT allow deleting open files
    So PowerShell cannot delete db folder.

Windows-la file open irundha delete panna mudiyadhu
Flask + ChromaDB sqlite file use pannitu irukkum
CTRL+C / taskkill panna app stop aagi
apram Remove-Item work aagum



taskkill /IM python.exe /F  --use to  close powershell
Remove-Item db -Recurse -Force
python rag.py

DO NOT delete DB at app startup in production
You currently have code that resets Chroma every time.
That causes locks + crashes.

# __________________________________________________
FINAL TEST FLOW (Clean)

1️⃣ CTRL + C
2️⃣ Remove-Item db -Recurse -Force
3️⃣ python rag.py
4️⃣ /ingest
5️⃣ /ask




# __________________________________________________
client = chromadb.PersistentClient(path="db")



Idhu ChromaDB client
👉 path="db" kuduthurukkom na:

🔹 Data ellam hard disk-la save aagum
🔹 App stop pannalum data delete aagathu
🔹 Next time app start pannalum data irukkum
PersistentClient na ChromaDB-la data disk-la permanent-ah store pannra client



# __________________________________________________
client.reset()
print("🔥 Chroma reset successfully.")


ChromaDB-la already irukkura ellaa data / collections clear panna
WHY use pannrom?
Old vectors irukkum
Old embeddings mismatch aagum
Testing time-la confusion varum
“Fresh-ah start panna”



# __________________________________________________
shutil.rmtree(DB_PATH)
print("🔥 Old DB folder deleted.")



Disk-la irukkura old Chroma files delete pannrom
WHY?

SQLite file corrupt aagirukkalam
Old index mismatch
Fresh DB create panna easy
“Hard reset”





# __________________________________________________
except PermissionError:
    print("❌ Windows locked the DB folder.")


Meaning:
Flask / Python still DB use pannitu irundha
Windows delete panna allow pannaadhu
“File open irundha Windows lock pannum”

# __________________________________________________