


# ------------------------
<!-- Rdies /Celery -->
# ------------------------


<!-- 
"User request vandha udane response kuduthu, time edukkura tasks (email, PDF, image processing, notifications) background-la run panna Celery use pannuvom. Andha task-a temporary queue-la store panna Redis use pannuvom. Celery worker Redis-la irundhu task eduthu execute pannum." -->


<!-- 
"Celery-ku tasks store panna oru message broker thevai. Naan Redis use pannirukken. User request vandha task first Redis queue-la store aagum. Celery worker continuous-a Redis-a monitor pannittu irukkum. New task vandha udane adha eduthu execute pannum. Redis memory-based database-nala romba fast. -->

<!-- Customer = User

Cashier = Django/FastAPI

Token = Redis

Chef = Celery Worker

Food = Email/PDF/SMS -->



# ------------------------
<!-- kfka -->
# ------------------------

<!-- Kafka  → Service-to-Service Communication

Celery → Background Task Execution

Redis  → Queue/Broker for Celery -->



<!-- | Kafka                                | Celery                         |
| ------------------------------------ | ------------------------------ |
| Microservice communication           | Background task execution      |
| Event streaming                      | Task queue                     |
| Producer → Topic → Consumer          | Task → Queue → Worker          |
| Multiple services consume same event | Worker executes task           |
| Decouples services                   | Prevents long-running requests | -->


<!-- "Enga project Insurance Claim Intelligence Platform (ICIP)-la, customer insurance claim submit pannumbodhu request first FastAPI Claim Service-ku varum. Claim details PostgreSQL-la save pannuvom. Save pannadhukku apram, Claim Service Kafka topic-ku Claim Created event publish pannum.

Kafka moolama Notification Service, Fraud Detection Service, Document Verification Service, Audit Service madhiri microservices ellam andha event-ah receive panni, avanga respective work-ah independently start pannuvanga. Idhanaala services direct-a depend panna vendiya avasiyam illa, application scalable-um fault-tolerant-um irukkum.

Next, Document Verification Service-ku OCR processing, AI document validation, PDF processing madhiri time edukkura tasks irukkum. Indha heavy tasks API request-kulla execute panna maatom. Instead, Celery task create pannuvom.

Celery andha task-ah Redis message broker (queue)-la store pannum. Celery workers Redis queue-la irundhu task-ah eduthu background-la execute pannuvanga. OCR complete aana result PostgreSQL-la update pannuvom. Theva na Notification Service moolama customer-ku email or SMS anuppuvom.

Indha architecture use pannadhunaala API response romba fast-ah return aagum, user wait panna thevai illa, heavy processing background-la nadakkum. -->


<!-- 

In our ICIP project, we used Kafka for event-driven communication between microservices. When a claim was created, the Claim Service published a Claim Created event. Services like Document Verification, Fraud Detection, Notification, and Audit consumed that event independently. For long-running tasks such as OCR, AI document validation, and PDF processing, we used Celery. Celery placed the tasks into Redis, which acted as the message broker. Celery workers picked up the tasks from Redis, processed them asynchronously, updated PostgreSQL, and triggered notifications. This architecture kept our APIs fast, scalable, and loosely coupled. -->

<!-- 

Customer
    │
    ▼
FastAPI - Claim Service
    │
    ├── Save Claim → PostgreSQL
    │
    └── Publish Event
            │
            ▼
        Kafka Topic
     ┌──────┼────────┬─────────┐
     ▼      ▼        ▼         ▼
Document  Fraud   Notification Audit
Service   Service    Service    Service
     │
     │ OCR / AI Validation (Heavy Task)
     ▼
Create Celery Task
     ▼
Redis (Message Broker / Queue)
     ▼
Celery Worker
     ▼
OCR / AI Validation
     ▼
Update PostgreSQL
     ▼
Notification Service
     ▼
Email / SMS to Customer -->

# ------------------------ ------------------------  ------------------------  ------------------------




Sure. This is the **overall production pipeline** that you can explain in an interview.

# Insurance Claim Intelligence Platform – Overall Pipeline

```text
                           Customer
                               │
                               ▼
                    Web / Mobile Application
                               │
                               ▼
                    FastAPI REST APIs
                               │
        ┌──────────────────────┴──────────────────────┐
        ▼                                             ▼
 JWT Authentication                             Claim APIs
      (RBAC)                                         │
        │                                             │
        └──────────────────────┬──────────────────────┘
                               ▼
                         PostgreSQL
      (Customers, Policies, Claims, Users, Status)
                               │
                               ▼
                  Customer Uploads Documents
                               │
                               ▼
                          OCR Service
                     (Extract Document Text)
                               │
                               ▼
                      Extracted Plain Text
                               │
              ┌────────────────┴────────────────┐
              ▼                                 ▼
      Elasticsearch                     Embedding Model
    (Keyword Indexing)               (Amazon Titan/OpenAI)
                                                │
                                                ▼
                                            Qdrant
                                       (Vector Database)
              └────────────────┬────────────────┘
                               ▼
                           Hybrid RAG
                (Keyword + Semantic Retrieval)
                               │
                               ▼
                    AWS Bedrock (Claude LLM)
                               │
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                      ▼
   Claim Analysis       Fraud Detection      Settlement Suggestion
                               │
                               ▼
                    AI Recommendation
                               │
                               ▼
                    Save Result in PostgreSQL
                               │
                               ▼
                    Celery + Redis Queue
                               │
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                      ▼
 Email/SMS              PDF Generation        Audit Logging
                               │
                               ▼
                             Kafka
                    (Publish Claim Events)
                               │
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                      ▼
 Notification Service   Settlement Service   Monitoring Service
                               │
                               ▼
                  Response Returned to Customer
```

---

# One-Line Responsibility of Each Component

| Component                | Responsibility                                                 |
| ------------------------ | -------------------------------------------------------------- |
| **FastAPI**              | Receives client requests and exposes REST APIs                 |
| **JWT + RBAC**           | Authenticates users and controls access                        |
| **PostgreSQL**           | Stores business data (customers, policies, claims, AI results) |
| **OCR**                  | Extracts text from uploaded documents                          |
| **Elasticsearch**        | Keyword-based document search                                  |
| **Embedding Model**      | Converts text into vector embeddings                           |
| **Qdrant**               | Stores embeddings for semantic search                          |
| **Hybrid RAG**           | Combines keyword and semantic retrieval                        |
| **AWS Bedrock (Claude)** | Generates AI analysis and recommendations                      |
| **Celery + Redis**       | Executes long-running tasks asynchronously                     |
| **Kafka**                | Sends events between microservices                             |
| **Docker**               | Containerizes and deploys the application                      |

---

## Interview Explanation (1 minute)

> "The customer submits a claim through the web or mobile application. FastAPI authenticates the user using JWT and RBAC, then stores the claim details in PostgreSQL. The uploaded documents are processed by an OCR service to extract text. The extracted text is indexed in Elasticsearch for keyword search and converted into embeddings that are stored in Qdrant for semantic search. During AI analysis, Hybrid RAG retrieves relevant policy documents and historical information from Elasticsearch and Qdrant and sends the retrieved context to Claude on AWS Bedrock. Claude generates claim analysis, fraud detection, and settlement recommendations. These AI results are stored back in PostgreSQL. Background tasks such as notifications, PDF generation, and audit logging are handled by Celery with Redis, while Kafka publishes claim events for other microservices. Finally, the processed result is returned to the customer or claims officer."




# ----------------------------------------------------------


# Insurance Claim Intelligence Platform - Overall Pipeline (Tanglish)

```text
Customer
   │
   ▼
Web / Mobile App
   │
   ▼
FastAPI
   │
   ▼
JWT Authentication + RBAC
   │
   ▼
PostgreSQL
(Store Customer, Policy, Claim)
   │
   ▼
Customer Upload Documents
   │
   ▼
OCR
(Extract Text)
   │
   ▼
Extracted Text
   │
   ├──────────────► Elasticsearch
   │               (Keyword Search)
   │
   └──────────────► Embedding Model
                         │
                         ▼
                     Qdrant
                 (Vector Database)
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
  Elasticsearch Search         Semantic Search
          └──────────────┬──────────────┘
                         ▼
                     Hybrid RAG
                         │
                         ▼
                AWS Bedrock Claude
                         │
                         ▼
           AI Recommendation
                         │
                         ▼
                 PostgreSQL
          (Store AI Result)
                         │
                         ▼
               Celery + Redis
      (Background Processing)
                         │
                         ▼
                      Kafka
      (Notify Other Services)
                         │
                         ▼
               Customer Gets Result
```

---

# Step 1 - Customer Upload Claim

Customer website-la login pannitu

* Claim Form
* Vehicle Image
* Policy Number
* Aadhaar

upload pannuvanga.

**FastAPI** request receive pannum.

---

# Step 2 - Authentication

JWT check pannum.

```text
Valid User ah?

↓

Yes

↓

Continue
```

RBAC check pannum.

```text
Customer

or

Claims Officer

or

Admin
```

Yaar login pannirukanga nu verify pannum.

---

# Step 3 - PostgreSQL

Ippo business data save pannuvom.

Example

```text
Customer Details

Claim Details

Policy Details

Claim Status
```

**Tanglish:**

> "Customer submit panna claim details ellam first PostgreSQL-la save pannuvom. Because PostgreSQL dhan namma main database."

---

# Step 4 - OCR

Customer upload panna PDF/Image-a OCR read pannum.

Example

Image-la irukku

```
Vehicle damaged due to flood.
```

OCR convert pannum

↓

Text

```
Vehicle damaged due to flood.
```

---

# Step 5 - Elasticsearch

OCR extract panna text

Elasticsearch-la store pannuvom.

Reason

Later

User search pannalam

```
Flood

Engine

Accident
```

Instant-a kandupidikkum.

**Tanglish**

> "OCR extract panna text Elasticsearch-la index pannuvom. Exact keyword search panna romba fast-a result kudukkum."

---

# Step 6 - Embedding Model

Adhe text

```
Vehicle damaged due to flood
```

Embedding model-ku pogum.

Embedding Model convert pannum

↓

```
[0.23,-0.44,0.91....]
```

---

# Step 7 - Qdrant

Indha vector-a

Qdrant-la save pannuvom.

**Tanglish**

> "Qdrant text-a save pannaadhu. Text-oda embedding (vector)-a save pannum."

Purpose

Meaning search.

Example

User ask pannrar

```
Heavy rain damaged my car.
```

Document-la

```
Flood Damage
```

nu irundhaalum

Qdrant

```
Heavy Rain

≈

Flood
```

same meaning nu identify pannum.

---

# Step 8 - Hybrid RAG

Hybrid RAG rendu place-la search pannum.

### Elasticsearch

Keyword search

```
Flood
```

### Qdrant

Meaning search

```
Heavy Rain

Water Damage

Natural Disaster
```

Rendu result combine pannum.

---

# Step 9 - Claude (AWS Bedrock)

Claude receive pannum

* Customer Claim
* Policy Documents
* Previous Claims
* Insurance Rules

Claude analyse pannum.

Output

```
Approve Claim

Fraud Score

Settlement Amount
```

---

# Step 10 - PostgreSQL

AI output permanent-ah save pannuvom.

Example

```
Claim ID

AI Recommendation

Fraud Score

Confidence

Status
```

**Tanglish**

> "AI output temporary illa. Future-la claim open pannumbodhu immediate-a kaatanum. Adhanala PostgreSQL-la save pannuvom."

---

# Step 11 - Celery + Redis

Background work

* Email
* SMS
* PDF
* Notification

API wait panna vendam.

Background-la run aagum.

---

# Step 12 - Kafka

Claim Approved

↓

Kafka Event

↓

Settlement Service

↓

Notification Service

↓

Audit Service

ellam receive pannum.

---

# Finally

Customer dashboard-la

```
Claim Status

Approved

Settlement Amount

AI Recommendation
```

display aagum.

---

# 🔥 Interview Flow (Very Easy to Remember)

```
Customer
      ↓
FastAPI
      ↓
JWT + RBAC
      ↓
PostgreSQL
      ↓
OCR
      ↓
Elasticsearch
      ↓
Embedding Model
      ↓
Qdrant
      ↓
Hybrid RAG
      ↓
Claude (AWS Bedrock)
      ↓
AI Recommendation
      ↓
PostgreSQL
      ↓
Celery + Redis
      ↓
Kafka
      ↓
Customer Response
```

💡 **Easy memory trick:**
**"Store → OCR → Search → AI → Save → Background → Notify."**

If you remember this 7-step sequence, you'll be able to explain the entire architecture confidently in interviews.

# ----------------------------------------------------------










This is an excellent question. **In a real production system, the uploaded document is NOT directly stored in Elasticsearch or Qdrant.**

## Correct Flow

```text
Customer Upload PDF
        │
        ▼
FastAPI
        │
        ▼
File Storage
(AWS S3 / Local Storage / Azure Blob)
        │
        ▼
PostgreSQL
(Store File Path + Metadata)
        │
        ▼
OCR
(Extract Text)
        │
        ▼
Extracted Text
        │
 ┌──────┴─────────┐
 ▼                ▼
Elasticsearch   Embedding Model
                   │
                   ▼
                Qdrant
```

---

## Step 1: Customer uploads PDF

Example:

```text
claim_form.pdf
```

The **actual PDF file** is usually stored in:

* AWS S3 ✅
* Azure Blob Storage
* Google Cloud Storage
* Local File System (development)

**Not inside PostgreSQL.**

---

## Step 2: PostgreSQL

PostgreSQL stores only the file information (metadata).

Example:

**documents table**

| id | claim_id | file_name | file_path             |
| -- | -------- | --------- | --------------------- |
| 1  | 1001     | claim.pdf | s3://claims/claim.pdf |

So PostgreSQL knows **where the file is**, but doesn't usually hold the file itself.

---

## Step 3: OCR

OCR reads the PDF.

Example:

```text
Vehicle damaged due to flood.
Repair cost: $5000
```

---

## Step 4: Elasticsearch

The extracted text is indexed.

```text
{
  "claim_id":1001,
  "text":"Vehicle damaged due to flood."
}
```

Purpose:

* Keyword search

---

## Step 5: Qdrant

The **same extracted text** is converted into an embedding.

```text
Vehicle damaged due to flood.
        │
Embedding Model
        │
        ▼
[0.23,-0.45,0.81...]
```

That vector is stored in Qdrant.

Purpose:

* Semantic search

---

# Important Difference

❌ **PDF is NOT stored in Qdrant.**

❌ **PDF is NOT stored in Elasticsearch.**

Only the **text extracted from the PDF** is stored there.

---

# Where is each thing stored?

| Data                    | Stored In             |
| ----------------------- | --------------------- |
| Original PDF/Image      | AWS S3 / File Storage |
| File path & metadata    | PostgreSQL            |
| Customer, Policy, Claim | PostgreSQL            |`
| OCR extracted text      | Elasticsearch         |
| Embedding of OCR text   | Qdrant                |
| AI Recommendation       | PostgreSQL            |

---

## Interview Answer (Tanglish)

> **"Customer upload panna original PDF-a naanga S3/File Storage-la save pannuvom. PostgreSQL-la andha file-oda path, claim ID, file name madhiri metadata save pannuvom. OCR andha PDF-la irundhu text extract pannum. Extract panna text Elasticsearch-la keyword search-ku index pannuvom. Adhe text embedding model use panni vector-a convert panni Qdrant-la store pannuvom semantic search-ku. Finally, Claude AI generate panna recommendation-a thirumba PostgreSQL-la save pannuvom."**

This is the architecture used in most real-world AI applications because each component is used for what it does best:

* **File Storage** → Original documents
* **PostgreSQL** → Transactional/business data and metadata
* **Elasticsearch** → Full-text keyword search
* **Qdrant** → Vector similarity search
