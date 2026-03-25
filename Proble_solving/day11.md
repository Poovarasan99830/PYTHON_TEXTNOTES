

# __________________________________________________________________

## 🟡 **Day 11 – Sliding Window (Variable Window)**

# __________________________________________________________________

### ⏱ Learn

* **Dynamic window size**
* Expand & shrink logic
* Use **set / hashmap**

---

### 🧠 Problems

1️⃣ **Longest substring without repeating characters**
2️⃣ **Longest subarray with sum ≤ k**
3️⃣ **Smallest subarray with given sum**

---

### 🎯 **Pattern:** Expand & Shrink

```python
left = 0

for right in range(len(arr)):
    
    # expand window
    
    while condition_break:
        # shrink window
        left += 1
```

---

### 💥 THANGGLISH

👉 Right pointer → expand
👉 Left pointer → shrink

* Duplicate vandha → shrink
* Condition satisfy aana → update answer

---

---

# 