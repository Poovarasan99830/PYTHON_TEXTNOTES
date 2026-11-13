

# LLM – INTERVIEW QUICK REVISION SUMMARY



# -----------------------------------------------
## 🔷 1. LLM (Large Language Model)

# -----------------------------------------------


👉 **One-line:**

> LLM predicts next word using probability based on previous words

👉 **Thanglish:**

* Language = pattern
* Model = guess next word
* Example:
  "AI is" → "future"

👉 **Use:**

* Chatbot, coding, content writing



# -----------------------------------------------
## 🔷 2. Transformer
# -----------------------------------------------

👉 **One-line:**

> Transformer processes all words at once using attention

👉 **Thanglish:**

* RNN → one-by-one ❌
* Transformer → full sentence same time ✅

👉 **Core parts:**

* Embedding
* Attention
* Encoder (understand)
* Decoder (generate)



# -----------------------------------------------
## 🔷 3. Self-Attention
# -----------------------------------------------

👉 **One-line:**
          --> Finds important words and relationships

👉 **Thanglish:**

* Ella words compare pannum
* Important word-ku high score kudukkum

👉 **Formula idea:**

```
Q × K → score → softmax → × V
```

👉 **Example:**
"it" → cat (correct mapping)



# -----------------------------------------------
## 🔷 4. Pretraining vs Fine-Tuning
# -----------------------------------------------

👉 **One-line:**

> Pretraining learns general language, Fine-tuning specializes for tasks

👉 **Thanglish:**

* Pretraining = school education 📚
* Fine-tuning = specialization 🎯

👉 **Example:**

* Base model → general
* Medical model → fine-tuned



# -----------------------------------------------
## 🔷 5. Instruction Tuning
# -----------------------------------------------

👉 **One-line:**

> Trains model to follow human instructions

👉 **Thanglish:**

* Command → Output
* "Translate this" → model respond pannum

👉 **Example:**

* ChatGPT type systems



# -----------------------------------------------
## 🔷 6. RLHF\
# -----------------------------------------------

👉 **One-line:**

> Improves model using human feedback and rewards

👉 **Thanglish:**

* Model answer kudukkum
* Humans rank pannuvaanga
* Best answer learn pannum

👉 **Flow:**

```
Generate → Feedback → Reward → Improve
```


# -----------------------------------------------
# 🔥 🔑 SUPER IMPORTANT CONNECTION (INTERVIEW GOLD)
# -----------------------------------------------

👉 Full pipeline:

```
Pretraining
   ↓
Fine-tuning
   ↓
Instruction tuning
   ↓
RLHF
   ↓
Final Smart Chatbot
```


# -----------------------------------------------
# 🧠 MEMORY TRICK (VERY IMPORTANT)
# -----------------------------------------------

👉 **P T I R → Flow**

* P → Pretraining
* T → Tuning (Fine-tuning)
* I → Instruction
* R → RLHF


# -----------------------------------------------
# ⚡ 30-SECOND INTERVIEW ANSWER
# -----------------------------------------------

👉
**“LLMs are based on Transformers that use self-attention to understand relationships between words. They are pretrained on large datasets to learn language patterns, then fine-tuned for specific tasks. Instruction tuning helps them follow user commands, and RLHF aligns outputs with human preferences.”**

---

# ✅ FINAL /BRIEFLY

* LLM → predict next word
* Transformer → fast + parallel
* Attention → find importance
* Pretraining → learn basics
* Fine-tuning → specialize
* Instruction → follow commands
* RLHF → improve with humans

# -----------------------------------------------