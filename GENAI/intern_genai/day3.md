# Day 3 — Machine Learning & Deep Learning Basics

# --------------------------
# 1️⃣ Supervised Learning
# --------------------------




## ✅ Step 1: Definition
# -----------------------------
      Supervised Learning means:
     👉 Model learns using input data + correct output labels.
      It learns patterns and predicts future outputs.




## ✅ Step 2: Real-World Analogy
# -----------------------------
### Student & Teacher Analogy

Teacher gives:

| Question | Answer |
| -------- | ------ |
| 2 + 2    | 4      |
| 5 + 3    | 8      |

Student learns from correct answers.

Later teacher asks:10 + 5 = ?
Student predicts:15


Same way:
ML model learns from labeled data.







## ✅ Step 3: Code
# -----------------------------



from sklearn.linear_model import LinearRegression
import numpy as np

# input data
x = np.array([1,2,3,4,5]).reshape(-1,1)

# output data
y = np.array([10,20,30,40,50])

# create model
model = LinearRegression()

# train model
model.fit(x,y)

# prediction
result = model.predict([[6]])

print(result)
```



## ✅ Step 4: Code Explanation



| Code               | Meaning              |
| ------------------ | -------------------- |
| LinearRegression() | Creates ML model     |
| fit(x,y)           | Trains model         |
| predict()          | Predicts output      |
| reshape(-1,1)      | Converts data format |














# 2️⃣ Unsupervised Learning
# -----------------------------



## ✅ Step 1: Definition
             
             Unsupervised Learning means:
               👉 Model learns without labeled outputs.
                It automatically finds hidden patterns.


## ✅ Step 2: Real-World Analogy
        
        ### 🛒 Shopping Mall Analogy
               Mall owner wants to group customers.
               But no labels available.

               AI automatically finds:
                * Teenagers
                * Office workers
                * Families
              based on shopping behavior.



## ✅ Step 3: Code


from sklearn.cluster import KMeans
import numpy as np

# data
x = np.array([[1],[2],[3],[10],[11],[12]])

# model
model = KMeans(n_clusters=2)

# training
model.fit(x)

# output groups
print(model.labels_)
```

---

## ✅ Step 4: Code Explanation

| Code         | Meaning              |
| ------------ | -------------------- |
| KMeans()     | Clustering algorithm |
| n_clusters=2 | Create 2 groups      |
| fit()        | Train model          |
| labels_      | Group outputs        |

---







# 3️⃣ Neural Networks
# ----------------------------------



## ✅ Step 1: Definition
        Neural Network is:
            👉 AI model inspired by human brain neurons.
       Used for:
         * Image recognition
         * ChatGPT
         * Voice assistants



## ✅ Step 2: Real-World Analogy
        
        
        ### Human Brain Analogy
        Human brain:
          * Receives information
          * Processes it
          * Gives response
        Neural Network:
          * Takes input
          * Processes patterns
          * Gives prediction



## ✅ Step 3: Code


import torch
import torch.nn as nn

# neural network
model = nn.Sequential(
    nn.Linear(1,5),
    nn.ReLU(),
    nn.Linear(5,1)
)

print(model)





## ✅ Step 4: Code Explanation

| Code         | Meaning             |
| ------------ | ------------------- |
| nn.Linear()  | Neural layer        |
| ReLU()       | Activation function |
| Sequential() | Layer sequence      |




# -------------------------------------------
# 4️⃣ Training vs Testing
# -------------------------------------------


# ✅ Step 1: Definition
     ### Training Data-->Used to teach model.
     ### Testing Data-->Used to check model accuracy.



## ✅ Step 2: Real-World Analogy
### Exam Analogy
   Training:-->Student studies books.
   Testing:-->Student writes exam.
    
   If student performs well:->Learning successful.
   Same for AI models.




## ✅ Step 3: Code

from sklearn.model_selection import train_test_split
import numpy as np

x = np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
y = np.array([10,20,30,40,50,60,70,80])

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.2
)

print("Training Data:",x_train)
print("Testing Data:",x_test)




## ✅ Step 4: Code Explanation

| Code               | Meaning        |
| ------------------ | -------------- |
| train_test_split() | Splits data    |
| test_size=0.2      | 20% testing    |
| x_train            | Training input |
| x_test             | Testing input  |





# -------------------------------------------
# 5️ Deep Learning Overview
# -------------------------------------------



## ✅ Step 1: Definition
    Deep Learning means:
      👉 Large neural networks with many hidden layers.
      Used for:* ChatGPT* Self-driving cars* AI image generation


## ✅ Step 2: Real-World Analogy
### Factory Analogy
    Factory has multiple sections:
      * Raw material processing
      * Quality checking
      * Packaging
      Each layer does one task.
      Deep Learning layers also process data step-by-step.


## ✅ Step 3: Code


import torch.nn as nn

deep_model = nn.Sequential(
    nn.Linear(10,20),
    nn.ReLU(),

    nn.Linear(20,30),
    nn.ReLU(),

    nn.Linear(30,1)
)

print(deep_model)


## ✅ Step 4: Code Explanation

| Code                   | Meaning      |
| ---------------------- | ------------ |
| Multiple Linear layers | Deep network |
| ReLU()                 | Activation   |
| Sequential()           | Layer flow   |



# 🛠 Tools Used

| Tool                                                            | Usage            |
| --------------------------------------------------------------- | ---------------- |
| [Scikit-learn](https://scikit-learn.org?utm_source=chatgpt.com) | Machine Learning |
| [PyTorch](https://pytorch.org?utm_source=chatgpt.com)           | Deep Learning    |

---

# 🎯 Final Outcome

Students can now:

✅ Understand ML basics
✅ Explain supervised learning
✅ Explain unsupervised learning
✅ Understand neural networks
✅ Differentiate training vs testing
✅ Understand deep learning basics
✅ Run simple ML models in Python
