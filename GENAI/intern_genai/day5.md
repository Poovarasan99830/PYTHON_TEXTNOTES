## **Day 5 — Large Language Models (LLMs)**

### Topics

* LLM
* Transformers
* Tokens & Context Window
* Self Attention
* GPT models
* Pretraining vs Fine-tuning
* RLHF basics








# ----------------------------------------
# Step 10 — Mini AI Chatbot
# ----------------------------------------

## What it does
# Simple chatbot using GPT-2.


from transformers import pipeline

# Create generator object
generator = pipeline("text-generation", model="Qwen 2.5 ")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot Ended")
        break

    response = generator(
        user_input,
        max_length=40,
        num_return_sequences=1
    )

    print("AI:", response[0]['generated_text'])






# ---------------------------------------------
# Step 1: Import the Pipeline

  # from transformers import pipeline
 Definition:
  Imports the pipeline function from the Transformers library.

 What Happens Internally?
   Python loads the Hugging Face Transformers library.
   Makes the pipeline() function available for use.
Purpose
   Used to create ready-made AI tasks such as:
     text generation
     translation
     summarization


# Step 2: Create the Text Generator
  # generator = pipeline("text-generation", model="gpt2")
               
               Creates a text-generation pipeline using the GPT-2 language model.
               What Happens Internally?
                  1. Loads GPT-2 model
                      The neural network architecture and trained weights are loaded.
                  2. Loads tokenizer
                      Tokenizer converts text into tokens.
                      Example:"Hello world"
                             → ["Hello", "world"]
                  3.Loads vocabulary
                     The model loads known words and token mappings.
                     Final Result: generator becomes an AI text-generation engine.


# Step 1: Infinite Loop  
   while True:

# Step 2: User Input
  user_input = input("You: ")

# Step 3: Exit Condition
  if user_input.lower() == "exit":
  
# Step 4: Print End Message
print("Chatbot Ended")


# Step 6: Generate AI Response

generator()--->This is HuggingFace pipeline model
           --->Text → Tokens → Transformer → Prediction → Text


Step 6.1: Tokenization
         
         "What is AI?"
         ["What", "is", "AI", "?"]
         words → token IDs
         [2061, 318, 9552, 30]

Step 6.2: Embedding
         IDs → vectors
         2061 → [0.2, 0.5, 0.8]

Step 6.3: Transformer Processing
           Transformer processing uses self-attention to analyze relationships between words and understand contextual meaning efficiently

Step 6.4: Next Word Prediction


# max_length=40
     max_length defines the maximum number of tokens (words/subwords) the AI model is allowed to generate in the output.
     
     * It controls the number of responses returned by the AI model.
     
     The model can generate up to 40 tokens before stopping.
     40 tokens/words varaikkum dhaan generate pannum
     why?
     Very long response avoid panna


# num_return_sequences=1
   num_return_sequences specifies how many different outputs or responses the model should generate for a single input.

   * It controls the number of responses returned by the AI model.
   
   num_return_sequences = 3
   The model generates 3 different responses for the same input.


# Step 7: Print Response
        
        response[0]['generated_text'] extracts the AI-generated text output from the model response

        example:
           response = [{'generated_text': 'AI is Artificial Intelligence'}]

           response[0]        -->Accesses the first response in the list.
           ['generated_text'] -->Retrieves the generated text from that response.

        or
        response is a list
        response = [
              {'generated_text': 'Hello'},
              {'generated_text': 'Hi there'},
              {'generated_text': 'Welcome'}
                   ]







User Input
    ↓
Tokenization
    ↓
Token IDs
    ↓
Embeddings
    ↓
Transformer Processing
(Self-Attention)
    ↓
Next Word Prediction
    ↓
Generated Text
    ↓
Print Output




# ---------------------------------------------

# Simple Explanation for Students

| Program              | Purpose                 |
| -------------------- | ----------------------- |
| Install transformers | Install AI libraries    |
| Load GPT-2           | Load pretrained LLM     |
| Token example        | Understand tokens       |
| Context example      | Understand AI memory    |
| Self-attention       | Word relationships      |
| Text generation      | AI creates text         |
| RLHF                 | Human feedback learning |
| Chatbot              | Real LLM application    |

---

# Expected Learning Outcome

* What LLMs are
* How GPT works
* Tokens & context
* Self-attention basics
* Hugging Face usage
* Simple AI chatbot creation





# ---------------------------------------------




Why Strange Output Came?
    GPT-2 old model 

    So:
     sometimes unrelated text generate pannum
     no RLHF
     no instruction tuning
     raw internet data

Input split into tokens
Tokens → vectors
Attention checks relationships
Model predicts next word
One word at a time generate pannum
GPT-2 old model → sometimes weird output


GPT-2 is very old model (2019).
That’s why output quality weak-

✅ BEST FREE MODELS FOR YOUR LAPTOP

| Model        | Best For        | Quality   | RAM Need |
| ------------ | --------------- | --------- | -------- |
| Qwen 2.5 7B  | 🔥 Best overall | Excellent | 8GB+     |
| Mistral 7B   | Fast + smart    | Very good | 8GB+     |
| Llama 3.2 3B | Lightweight     | Good      | 4GB+     |
| Phi-3 Mini   | Small laptop    | Good      | 4GB      |
| Gemma 2B     | Beginner        | Okay      | Low      |



Normal Laptop:
  * microsoft/phi-3-mini-4k-instruct
    Reason:
      Fast
      Better than GPT2
      Small model
      Instruction tuned
      Works in CPU also
   
If Good RAM + GPU:
  * Qwen/Qwen2.5-7B-Instruct  -->Very powerful





# **1. Types of LLM Models (Industry Classification)**




##  Proprietary (Closed-Source) LLMs**
       You cannot download them. You use them **online via API**.
   ### Examples:
       * **OpenAI GPT-4 / GPT-5**
       * **Anthropic Claude 3.5**
       * **Google Gemini 2**
       * **Microsoft Copilot Models**

   ### Best for:
      * Enterprise apps
      * High accuracy
      * Long context
      * Reliable uptime


## **B. Open-Source LLMs (Downloadable)**
           These models can run **online or offline**.
           ### Examples:
              * **Llama 3.1 / 3.2**
              * **Qwen 2.5**
              * **Mistral & Mixtral**
              * **Phi-3**
              * **DeepSeek R1**

          ### Best for:
              * Local systems
              * Private data
              * Custom fine-tuning


## Domain-Specific LLMs**
     Trained specifically for one industry.
     ### Examples:
        * **Medical** → Med-PaLM
        * **Finance** → BloombergGPT
        * **Legal** → LexisAI

     ### Best for:
         * High accuracy in one field



## **D. Small “Edge” Models (On mobile / laptops)**
           Lightweight models for low hardware.
           ### Examples:
              * **Gemma 2**
              * **Phi-3 mini**
              * **Llama 3.2 (1B / 3B)**

           ### Best for:
              * Phones
              * Browsers
              * Embedded devices

---

## 🟩 **E. Multimodal LLMs**
               Understand **text + image + audio + video**.

              ### Examples:

                    * **GPT-4o / GPT-5 Omni**
                    * **Gemini 2**
                    * **Claude 3.5 Sonnet**
                    * **LLaVA (open-source)**


        
# ---------------------------------------------
✅ EASIEST METHOD → USE OLLAMA
# ---------------------------------------------


Step 1: Install Ollama
        https://ollama.com/?utm_source=chatgpt.com



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

Before Ollama:
LLM run:
   complicated setup 
   Python knowledge 
   CUDA/GPU issue
   transformers config

✅ Ollama Solution
     One command-la model run 
     ollama pull llama3
     ollama run llama3

     Behind the Scenes
     ollama pull llama3
     ollama run llama3--->llama3 model already irukka?
                    --->If not present:HuggingFace / Ollama registry-lendhu download pannum
                    --->ex:llama3.gguf--Large AI weights file
                    --->Load into RAM --->RAM / GPU VRAM
                    --->Start Inference Engine -->AI brain ON aagum -->Inference = prediction process
                    -->User Prompt Accept pannum >>>>> Python is
                                                 -->Tokenization -->"Python is"→ tokens->Transformer Process 
                                                                                       -->Inside:

                                                                                           embeddings
                                                                                           self-attention
                                                                                           prediction
                                                 --->Next Word Generate--->Python is a powerful programming language...
# 🔷 Why Ollama Fast?
Because:
✅ optimized inference engine
✅ quantized models
✅ local execution

# Quantization (Very Important)
Original model:16GB
Quantized:4GB
Smaller + faster-->Without much quality loss

# 🔷 Ollama Architecture


User Prompt
      ↓
Ollama
      ↓
Load Model
      ↓
Tokenizer
      ↓
Transformer
      ↓
Prediction
      ↓
AI Response




| Benefit                | Explanation                                 |
| ---------------------- | ------------------------------------------- |
| **Privacy**            | No data leaves your laptop or server        |
| **Cost saving**        | No API charges like GPT/Claude              |
| **Full control**       | You choose the model, version, quantization |
| **Offline capability** | Works without internet                      |
| **Fast inference**     | Uses GPU/CPU efficiently                    |




🔷 Popular Models in Ollama

| Model   | Use                |
| ------- | ------------------ |
| llama3  | Best general AI    |
| phi3    | Small + smart      |
| qwen2.5 | Coding + reasoning |
| mistral | Fast responses     |
| gemma   | Lightweight        |


# __________________________________________________

Ollama Is NOT a Model — It Is a Platform

Ollama = local LLM engine
LLM = actual model (Llama, Qwen, etc.)


# __________________________________________________


| Movie World 🎬      | AI World 🤖              |
| ------------------- | ------------------------ |
| Netflix             | HuggingFace / Ollama Hub |
| Movie file (.mp4)   | Model file (.gguf)       |
| VLC Player          | Ollama                   |
| Play movie          | Run model                |
| Subtitle generation | AI text generation       |



# Movie Side:
Netflix
   ↓
Download Movie (.mp4)
   ↓
VLC Player
   ↓
Play Movie



# AI Side

HuggingFace / Ollama Hub
        ↓
Download Model (.gguf)
        ↓
Ollama
        ↓
Run AI Model



# __________________________________________________

HuggingFace
      ↓
Download Model (.gguf)
      ↓
Ollama
      ↓
Load into RAM
      ↓
Run Transformer
      ↓
Generate AI Response


# __________________________________________________

Ollama = VLC player for AI
Model file = movie file
Download model locally
Ollama loads and runs model
Generates AI responses locally 


# __________________________________________________
# WITH OLLAMA – FULL FLOW (Behind the Scenes)
ollama pull phi3
ollama run phi3
python app.py

User Prompt
     ↓
Python Requests API
     ↓
Ollama Server
     ↓
Model Loader
     ↓
Tokenizer
     ↓
Transformer Model
     ↓
Next Word Prediction
     ↓
Response API
     ↓
Python Output



Step 1: User Prompt

Step 2: Python Sends API Request
        requests.post()
        HTTP request send pannum--->localhost:11434 --->Idhu Ollama server address




# Real-Time Analogy
| Component   | Meaning    |
| ----------- | ---------- |
| Python code | Customer   |
| API request | Food order |
| Ollama      | Restaurant |
| Model       | Chef       |


Step 3: Ollama Receives Prompt
Ollama paakum:
    Model = phi3
    Prompt = Python is

Step 4: Model Check
    Ollama verify pannum:
       phi3 model installed irukka?
          If not:download pannum

Step 5: Load Model into RAM
    phi3.gguf -->RAM/GPU memory-ku load pannum

Step 6: Tokenization
   Inside model:"Python is"
                 → ["Python", "is"]

Step 7: Token IDs
   Python → 11361
   is → 318

Step 8: Embeddings
       Words → vectors
      11361 → [0.12, 0.67, 0.91 ...]    --->Deep meaning representation
       
 Step 9: Transformer Processing
        Inside transformer:
              self-attention
              feed-forward network
              normalization
        repeat aagum

Step 10: Self-Attention
        Model checks:Python ↔ programming ↔ coding
        Context understand pannum


Step 11: Next Word Prediction

        Python is ____ 
         
         | Word     | Probability |
         | -------- | ----------- |
         | a        | 40%         |
         | powerful | 20%         |
         | easy     | 10%         |

       Highest probability choose pannum

Step 12: Generate Response
         Python is a powerful programming language.

         stream=False   # Complete response at once
         stream=True    # Response token by token
         Real-Time Analogy ---->Imagine you order a biryani in a restaurant.


Step 13: Ollama Sends Response Back
          Ollama API returns:
           {
             "response": "Python is a powerful programming language."
            }




Step 14: Python Prints Output
        print(result["response"])




| Without Ollama       | With Ollama       |
| -------------------- | ----------------- |
| Manual model loading | Automatic         |
| Transformers setup   | Easy              |
| Need tokenizer code  | Internal          |
| More coding          | Simple API        |
| Complex              | Beginner friendly |


# BEST REAL-TIME ANALOGY

Restaurant Analogy

    Without Ollama 
        vegetables vangnum
        cooking pannnum
        stove setup pannnum
     everything manual

With Ollama
    Restaurant-ku order kuduthaa podhum
    "One biriyani please"---->Ready-made response varum


# __________________________________________________

| Feature     | Local Models      | Cloud Models                 |
| ----------- | ----------------- | ---------------------------- |
| Examples    | Ollama, LM Studio | OpenAI, Gemini, Grok, Claude |
| Internet    | Not Required      | Required                     |
| Cost        | Mostly Free       | Pay-per-use                  |
| Privacy     | High              | Depends on Provider          |
| Hardware    | Requires RAM/GPU  | No Local Hardware Needed     |
| Performance | Depends on Device | High Performance             |












| Tool         | Primary Purpose          |
| ------------ | ------------------------ |
| Ollama       | Run models locally       |
| LM Studio    | GUI for local models     |
| Hugging Face | Model repository         |
| OpenAI API   | Access GPT models        |
| Gemini API   | Access Gemini models     |
| Grok API     | Access Grok models       |
| Claude API   | Access Claude models     |
| vLLM         | Production model serving |






https://chatgpt.com/share/6a0e7daf-4be4-8320-b053-7347b440e87c