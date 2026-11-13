# 3. Celery + Redis + Kafka

Resume:

> Orchestrated asynchronous processing pipelines using Celery, Redis, and Kafka, increasing background task throughput by 40% and cutting processing latency by 30%.

This is another **very high-probability target**.

### Interviewer:

> Why Celery?

> Why Redis?

> Why Kafka?

> Celery vs Kafka?

> What is asynchronous processing?

> What happens if a worker fails?

> How do you retry failed tasks?

> Why not process everything synchronously?







🎯 One-line definitions
Component	Simple meaning
Celery	Background task processing system
Celery Worker	Executes the background tasks
Redis	Message broker/queue used by Celery
Redis Queue	Holds pending tasks until workers process them
Kafka	Event-streaming platform for distributing events between services
🧠 Super easy memory

Celery = Task create/manage
Redis = Task queue/broker
Worker = Task execute
Kafka = Event communicate

Example:
“Process this document” → Celery + Redis + Worker

“Claim has been settled” → Kafka → Notification/Audit services






In our ICIP project, we used Celery for asynchronous background task processing, particularly for time-consuming operations that should not block the API. Redis acted primarily as the Celery message broker to queue and deliver tasks to workers. We used Kafka separately for event-driven communication between services. For example, after a claim status change or settlement, we published an event to Kafka, which could be consumed by notification and audit services. Celery's retry mechanism was used to handle transient task failures. This asynchronous architecture helped keep the APIs responsive and allowed background workloads to be processed independently and scaled through workers

Celery → “Do this work.”

Redis → “Hold/deliver this Celery task.”

Kafka → “This event happened.”

Worker → “Actually execute the task.”

Retry → “Try the failed task again.”

Asynchronous → “Don't make the API wait.”



FastAPI → receives request and creates a Celery task
Celery → sends the task to the broker
Redis → stores/queues the pending task
Celery Worker → picks up the task
Worker → actually executes OCR/processing

Thanglish

“First FastAPI request receive pannum → Celery task create pannum → Redis queue-la task store aagum → Celery Worker task-ai eduthu execute pannum.”


FastAPI
   ↓
Celery
   ↓
Redis Queue
   ↓
Celery Worker
   ↓
Claim Processed ✅
   ↓
Publish "CLAIM_PROCESSED" event
   ↓
Kafka
   ↓
 ┌───────────────┬──────────────┐
 ↓               ↓              ↓
Notification    Audit         Analytics
Service         Service       Service




# -----------------------------------------------



6. What happens if a worker fails?

Suppose:

Celery Worker
     ↓
OCR Task
     ↓
Worker crashes ❌

We don't want the task to disappear.

Depending on the task configuration, we can use:

Acknowledgement settings
Retries
Task time limits
Worker monitoring
Dead-letter/error handling patterns

A failed task can be retried by another available worker.

Interview answer

“If a worker fails while processing a task, we configure task acknowledgement and retry mechanisms so that the task can be retried instead of being permanently lost. We also monitor worker and task failures and route persistent failures for further investigation.”

Thanglish

“Worker fail aana task permanently lose aagama acknowledgement and retry mechanism configure pannuvom. Retry fail aagite irundha monitor panni investigation or manual handling-ku route pannuvom.”






Task acknowledgement na, Celery Worker oru task-ai successfully receive pannitu process panna start/complete pannirukku-nu broker-kku confirm pannura mechanism.

Simple example
FastAPI
   ↓
Redis Queue
   ↓
Celery Worker
   ↓
Task received
   ↓
ACK (Acknowledgement)

ACK means:

“Task enakku kidaichudhu; naan idha handle panren.”

Worker ACK pannaama fail aana?

Suppose:

Redis Queue
   ↓
Worker
   ↓
Task received
   ↓
Worker crashes ❌

Task properly acknowledged pannala na, configuration based on acknowledgement behavior, broker/task can make the task available for redelivery/retry.

Task
 ↓
Worker 1 ❌
 ↓
Redelivered
 ↓
Worker 2
 ↓
Success ✅
🗣️ Thanglish

“Task acknowledgement-na worker task-ai receive pannirukku-nu broker-kku confirmation kudukkuradhu. Worker acknowledgement kudukkura munnadi fail aana, task-ai marubadiyum available worker process panna mudiyum.”

⚠️ One important correction

Acknowledgement itself is NOT retry.

Think:

Acknowledgement (ACK) → “Task received/handled.”
Retry → “Task failed; try it again.”
Worker failure → ACK configuration determines whether the task can be redelivered.
🎯 Interview-la short answer

“Task acknowledgement is the confirmation sent by a Celery worker to the broker that it has received and is handling a task. If the worker fails before acknowledgement, the task can be redelivered depending on the acknowledgement configuration.”





Exactly — **you caught the important point.** There is a **redelivery** that can happen because of acknowledgement behavior, and there is an application-level **retry**. They can look similar, but they are triggered differently.

### 1. Worker crashes → Redelivery

Suppose:

```text id="4i6l7x"
Redis
 ↓
Task A
 ↓
Worker 1
 ↓
Processing...
 ↓
Worker 1 crashes ❌
```

If the task was not acknowledged and the Celery acknowledgement/requeue configuration allows it:

```text id="r8w2qz"
Task A
 ↓
Available again
 ↓
Worker 2
 ↓
Process Task A
```

This is **redelivery**.

The broker is essentially saying:

> “I didn't get the acknowledgement, so this message may not have been successfully handled.”

---

### 2. Task execution fails → Retry

Now suppose Worker 1 itself is healthy, but the task fails:

```text id="qj2m1a"
Worker 1
 ↓
Process Task A
 ↓
Call external API
 ↓
Network error ❌
```

Your code/Celery retry policy can say:

```text id="1w7n6x"
Wait 60 seconds
      ↓
Retry Task A
      ↓
Worker
      ↓
Success ✅
```

This is **retry**.

---

## 🔥 So why did I say “redelivery” earlier?

Because **worker crash and task failure are two different situations**.

### Worker crash

**Broker-level recovery:**

> No ACK → task can be redelivered.

### Application/task failure

**Application-level recovery:**

> Task raised an exception → Celery retry mechanism can execute it again.

---

### Simple Thanglish

> **“Worker crash aana, ACK receive aagala na broker task-ai redeliver pannalam. Adhu redelivery. But worker properly running irundhu task execution-la temporary error vandha, Celery retry mechanism use panni task-ai again execute pannuvom. Adhu retry.”**

### Best interview distinction

> **“Redelivery happens when the broker doesn't receive the expected acknowledgement, such as when a worker is lost. Retry is an explicit failure-handling mechanism used when a task execution fails and we want to attempt it again.”**

**Memory:**

**Worker dies → No ACK → Redelivery**

**Task fails → Retry policy → Retry**

And yes, **both can ultimately result in the task being executed again**, which is why they are easy to confuse.



| ACK                                            | Retry                                        |
| ---------------------------------------------- | -------------------------------------------- |
| Confirms task delivery/handling                | Attempts failed task again                   |
| Worker → Broker                                | Task execution → Retry                       |
| Related to message acknowledgement             | Related to failure handling                  |
| Prevents/controls unwanted redelivery          | Handles temporary failures                   |
| `task_acks_late=True` affects when ACK happens | `self.retry()` / retry policy triggers retry |






# -----------------------------------------------


7. How do you retry failed tasks?

Celery supports retries.

Conceptually:

Task
 ↓
Worker
 ↓
Failure ❌
 ↓
Retry
 ↓
Worker
 ↓
Success ✅

Example:

@app.task(bind=True, max_retries=3)
def process_document(self, document_id):
    try:
        # processing
        pass
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)

This means:

If the task fails, retry it after a delay, up to the configured limit.

Better production approach

Use exponential backoff for temporary failures:

1st retry → 1 minute
2nd retry → 2 minutes
3rd retry → 4 minutes

The exact timings depend on your configuration.

Interview answer

“We use Celery's retry mechanism for transient failures. We configure a maximum retry count and delay between retries, and for repeated failures we log the error and route the task for further investigation.”


**Transient failure** means a **temporary failure that may disappear if we try the same operation again after some time.**

### Example in your ICIP project

Suppose Celery worker calls an external OCR/AI service:

```text
Celery Worker
     ↓
AWS Textract API
     ↓
Temporary network problem ❌
     ↓
Wait 60 seconds
     ↓
Retry
     ↓
AWS Textract works ✅
```

That network problem is a **transient failure**.

### Common examples

* Temporary network timeout
* External API temporarily unavailable
* Temporary database connection failure
* Service temporarily overloaded
* Temporary rate-limit response

### Not usually transient

If your code has a permanent error:

```text
Invalid policy number
Missing required field
Programming bug
Invalid document format
```

Retrying 3 times probably won't fix it.

### 🗣️ Thanglish

> **“Transient failure-na temporary-ah varra problem. Konjam time wait panni retry pannina success aagura chance irukkum.”**

### 🎯 Interview one line

> **“A transient failure is a temporary error, such as a network timeout or temporary service unavailability, where retrying the operation after a delay may succeed.”**

So your sentence:

> **“We use Celery's retry mechanism for transient failures.”**

means:

> **“Temporary problem vandha, task-ai immediately fail pannama, konjam delay kuduthu again try pannuvom.”**

















