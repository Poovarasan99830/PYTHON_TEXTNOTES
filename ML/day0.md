

⏱ **Daily time:** ~2–3 hours
🎯 **Goal after 13 days:** You can clean real datasets & prepare data for ML models confidently.


--




# _______________________________________
## 🔁 DAILY ROUTINE (IMPORTANT)
# _______________________________________


| Time   | Task            |
| ------ | --------------- |
| 30 min | Concept reading |
| 1 hr   | Coding practice |
| 30 min | Mini exercises  |
| 30 min | Revise & notes  |

---


# _______________________________________
# ✅ 13-DAY NUMPY + PANDAS — DEV EXECUTION PLAN
# _______________________________________

> **Rule:**
> Every day =
> `read → type code → break code → fix code`

---



# _______________________________________
## 🔹 DAY 1 — NumPy Core Objects
# _______________________________________




```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])

np.zeros((2, 3))
np.ones((3, 3))
np.arange(0, 10, 2)
np.linspace(0, 1, 5)
```

✅ Checklist

* [ ] ndarray created
* [ ] Understand 1D vs 2D

---


# _______________________________________
## 🔹 DAY 2 — Shape / Indexing / Reshape
# _______________________________________






```python
arr = np.arange(12)

arr.shape
arr.ndim
arr.size

arr2 = arr.reshape(3, 4)

arr2[0, 1]
arr2[:, 2]
arr2[1:3, :]
```

✅ Checklist

* [ ] Slice rows & columns
* [ ] Reshape without error

---

# _______________________________________
## 🔹 DAY 3 — Vectorized Operations
# _______________________________________



```python
arr = np.array([10, 20, 30])

arr + 5
arr * 2
arr / 10

mask = arr > 15
arr[mask]
```

⚠️ **NO FOR LOOPS ALLOWED**

---

# _______________________________________
## 🔹 DAY 4 — Stats (ML foundation)
# _______________________________________





```python
X = np.array([[1, 2, 3],
              [4, 5, 6]])

np.sum(X)
np.mean(X)
np.mean(X, axis=0)  # feature-wise
np.std(X)
np.var(X)
```

✅ You must know **axis=0 vs axis=1**

---

# _______________________________________
## 🔹 DAY 5 — Linear Algebra (CRITICAL)
# _______________________________________






```python
X = np.array([[1, 2],
              [3, 4]])

w = np.array([0.5, 1.0])

np.dot(X, w)
X.T
np.matmul(X, X)
np.linalg.inv(X)
```

🔥 If this is weak → STOP ML

---


# _______________________________________
## 🔹 DAY 6 — NumPy Mini Project (MANDATORY)
# _______________________________________





```python
# fake dataset
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

# normalize
X_norm = (X - X.mean()) / X.std()

# manual linear regression (y = mx + c)
m = np.sum((X - X.mean()) * (y - y.mean())) / np.sum((X - X.mean())**2)
c = y.mean() - m * X.mean()
```

✅ You must understand **why this works**

---

# _______________________________________
# 🔹 PANDAS ZONE (REAL DATA STARTS)
# _______________________________________




---
# _______________________________________
## 🔹 DAY 7 — Load & Inspect Data
# _______________________________________

```python
import pandas as pd

df = pd.read_csv("data.csv")

df.head()
df.tail()
df.info()
df.describe()
```

❌ If `info()` confuses you → repeat day

---
# _______________________________________
## 🔹 DAY 8 — Select / Filter
# _______________________________________




```python
df['age']
df[['age', 'salary']]

df.loc[0]
df.iloc[0]

df[df['age'] > 25]
```

ML = selecting **right columns**

---
# _______________________________________
## 🔹 DAY 9 — Missing Data (REAL WORLD)
# _______________________________________




```python
df.isnull().sum()

df.dropna()

df['salary'].fillna(df['salary'].mean(), inplace=True)
```

🔥 If NaN enters ML → model dies

---
# _______________________________________
## 🔹 DAY 10 — Cleaning & Transform
# _______________________________________

```python
df['salary'] = df['salary'].astype(int)

df.rename(columns={'dept': 'department'}, inplace=True)

df['tax'] = df['salary'].apply(lambda x: x * 0.1)
```

Feature engineering starts here.

---
# _______________________________________
## 🔹 DAY 11 — Encoding (TEXT → NUMBER)
# _______________________________________




```python
df['city'] = df['city'].astype('category').cat.codes

pd.get_dummies(df, columns=['department'])
```

⚠️ ML **cannot read strings**

---
# _______________________________________
## 🔹 DAY 12 — GroupBy / Merge
# _______________________________________



```python
df.groupby('department')['salary'].mean()

emp = pd.read_csv("employees.csv")
dept = pd.read_csv("departments.csv")

pd.merge(emp, dept, on='dept_id')
```

Used in **production data pipelines**

---
# _______________________________________
## 🔹 DAY 13 — ML-READY DATASET (FINAL)
# _______________________________________




```python
from sklearn.model_selection import train_test_split

X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

🎯 If you reach here → **YOU ARE READY FOR ML**

---

# 🚫 HARD RULES

* ❌ No copy-paste without typing
* ❌ No skipping days
* ❌ No ML until Day 13 done

---

# ✅ NEXT STEP (AFTER THIS)

```text
Matplotlib → Statistics → Scikit-Learn
```

---

If you want next:

* 📁 **GitHub-style daily notebooks**
* 📄 **Printable checklist PDF**
* 🎯 **Interview questions from NumPy/Pandas**
* 🧠 **Tamil + English mix explanation**

Say the word.
