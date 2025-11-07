

# ---_______________________________________________________________________

## 🔹 2️⃣ K-Nearest Neighbours (KNN) — “Kooda irukura pasanga pola decide panra model”



### 🧩 1️⃣ **Real-World Intuition – Basic Thought**

Imagine you are a teacher in a new school.
A new student **Arun** joins.
You don’t know his character — whether he’s **studious** or **naughty**.

What do you do?

➡️ You look at **his friends**.
If most of his close friends are **studious**, you assume *Arun also studious.*
If most are **naughty**, then *Arun also naughty.*

👉 That’s exactly **KNN’s idea**.

> "Oru new data vandha, adha kooda irukura pasanga (nearest points) paathu decide pannum."



# ---_______________________________________________________________________




### ⚙️ 2️⃣ **Mechanism – How KNN Works (Step by Step)**

#### Step 1: Store Data (Training Phase)


KNN doesn’t “learn” any formula or pattern.
It simply **stores all training data points** in memory.

That’s why it’s called a **lazy learner** —
it does the real work only **when a new input** comes.




# ---_______________________________________________________________________



#### Step 2: New Input Arrives (Prediction Phase)

Suppose a new point ( x' ) comes in.

Now, KNN will:

1. Calculate the **distance** between ( x' ) and every training point ( x_i ).

   * Commonly, use **Euclidean Distance**:
     [
     d(x', x_i) = \sqrt{\sum_{j=1}^n (x'*j - x*{ij})^2}
     ]
   * Simple version: “Measure how far the new point is from each existing one.”

2. Sort all training points by **distance** (smallest first).

3. Choose **K nearest neighbours** (the top K smallest distances).


# --- _______________________________________________________________________

#### Step 3: Voting or Averaging

Now:

* For **classification** → pick the **majority class** among K.
* For **regression** → take the **average value** of K.

Example:
If K=5 and among 5 nearest, 3 are 🍎 (apple) and 2 are 🍊 (orange)
→ classify as **apple**.

# --- _______________________________________________________________________

#### Step 4: Output

That’s your predicted class/value for the new point.

---

### 🧮 3️⃣ **The Mathematical Core (in Simple Words)**

For a new input ( x' ):

[
\hat{y} = \text{Majority Vote}{ y_i : x_i \in N_K(x') }
]

Where:

* ( N_K(x') ) = K nearest training points to ( x' )
* ( y_i ) = their corresponding labels

# ---_______________________________________________________________________

### 📈 4️⃣ **Geometry – What’s Happening Visually**

Imagine 
red ❌ 
blue 🔵 

points on a 2D graph.

KNN divides the space into **regions**.
Each region belongs to the **majority color** of nearby points.

➡️ So, if you drop a new dot into that space,
it will **inherit the color of its closest neighbors.**

That’s why KNN often forms **curvy, non-linear boundaries** —
it simply follows the *shape* of the data.



# ---_______________________________________________________________________



### 🧠 5️⃣ **Key Intuitions (From First Principles)**

| Concept            | Simple Tanglish Explanation                                         |
| ------------------ | ------------------------------------------------------------------- |
| **Learning?**      | Illa, data save pannum (lazy learner).                              |
| **Decision?**      | Neighbours la majority yaar-nu paathu.                              |
| **Formula?**       | Just distance calculation (no weights, no training).                |
| **Complexity?**    | Training easy, testing time heavy (because distance to all points). |
| **Scaling issue?** | Yes — large data = more computation.                                |



# ---_______________________________________________________________________

### ⚖️ 6️⃣ **When to Use / Avoid**

| Use When                               | Avoid When                          |
| -------------------------------------- | ----------------------------------- |
| Small dataset                          | Very large dataset (slow)           |
| Data is numeric (distance makes sense) | Features have very different scales |
| You expect **local patterns**          | You need explainable formulas       |

# ---_______________________________________________________________________

### 🧩 7️⃣ **Example — Fruit Classification**

| Fruit     | Weight (g) | Sweetness | Type   |
| --------- | ---------- | --------- | ------ |
| 🍎 Apple  | 200        | 8         | Apple  |
| 🍊 Orange | 180        | 4         | Orange |
| 🍎 Apple  | 220        | 9         | Apple  |
| 🍊 Orange | 160        | 3         | Orange |

Now, new fruit: Weight=210, Sweetness=7

Compute distance to all points → pick **K=3** nearest →
if 2 are Apple, 1 Orange → classify as 🍎 Apple.

---

### 🧭 8️⃣ **Essence — One-Line Formula in Tanglish**

> “KNN = oru new data vandha, adha kooda irukura pasanga paathu decide pannum.”
> “No brain (training), only heart (neighbours).” ❤️

# ---_______________________________________________________________________

### 🧮 9️⃣ **Real-World Example**

* Recommender Systems:
  “Intha user ku pudicha movies maari vera yaar yaar pudichiruka?”
  → Similar users’ favourites recommend pannum.

* Image Classification:
  Pixel features la similar image find pannum.

# ---_______________________________________________________________________

### 🧱 10️⃣ **KNN From First Principles (Summary)**

| Step | Concept    | What Happens                        |
| ---- | ---------- | ----------------------------------- |
| 1    | Store Data | No model, just keep all data points |
| 2    | New Input  | Compute distances                   |
| 3    | Sort       | Find nearest K                      |
| 4    | Vote       | Choose majority class               |
| 5    | Output     | Return predicted class/value        |



# ---_______________________________________________________________________




