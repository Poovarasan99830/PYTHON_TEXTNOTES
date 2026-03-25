

# __________________________________________________________________

## 🟢 **Day 10 – Sliding Window (Fixed Window)**

# __________________________________________________________________

### ⏱ Learn

* What is **Sliding Window**
* **Fixed window size (k)**
* Avoid recalculating sum → optimize

---

### 🧠 Problems

1️⃣ **Maximum sum subarray of size k**
2️⃣ **First negative number in every window**
3️⃣ **Count subarrays of size k**

---

### 🎯 **Pattern:** Fixed Window

👉 Window size always constant

```python
# Template
window_sum = sum(arr[:k])

for i in range(k, len(arr)):
    window_sum += arr[i]      # add next
    window_sum -= arr[i-k]    # remove old
```

---

### 💥 THANGGLISH

* Window size fix ah irukum (k)
* New element add pannuvom
* Old element remove pannuvom

👉 Full loop panna vendam (optimization)

---

---


# -----------------------------------------------

<!-- Maximum Sum Subarray of Size K -->

# Problem Statement
# Given an array and a number k,
# Find the maximum sum of any subarray of size k



# -----------------------------------------------
# Max sum subarray of size k means what?

<!-- “Max sum subarray of size k” na:
Oru array kudupanga
Oru number k kudupanga
Namma enna panna vendiyadhu na:

👉 k size ku equal ah irukum continuous elements la,
yendha group la sum adhigama iruko adha find pannanu -->




arr = [2, 1, 5, 1, 3, 2]
k = 3


[2,1,5] → sum = 8  
[1,5,1] → sum = 7  
[5,1,3] → sum = 9 ✅  
[1,3,2] → sum = 6  


<!-- 
Array la irundhu, 3 elements ah continuous ah eduthu eduthu,
ovvoru group oda sum calculate pannuvom.

Adhula yedhula sum perusa iruko, adha dhaan answer.” -->



<!-- ✔ Subarray = continuous elements -->
<!-- ✔ Size k = fixed number of elements -->
<!-- ✔ Max sum = highest total value -->


<!-- k size group la, biggest sum edhu nu find pannradhu -->




<!-- Final Idea (Core Principle) -->
<!-- window_sum = window_sum + new_element - old_element -->

<!-- Old remove + New add = Fast computation” -->


<!-- 
[2,1,5] → sum = 8

+1 -2 → [1,5,1] → 7  
+3 -1 → [5,1,3] → 9 ✅  
+2 -5 → [1,3,2] → 6 -->


<!-- Pattern Understanding -->


<!-- window_sum += arr[i]
window_sum -= arr[i-k]


👉 This is the core logic
👉 Reuse this in ALL fixed window problems -->




def max_sum_subarray(arr, k):
    # Step 1: first window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Step 2: slide window
    for i in range(k, len(arr)):
        window_sum += arr[i]      # add new element
        window_sum -= arr[i-k]    # remove old element
        
        max_sum = max(max_sum, window_sum)

    return max_sum


# Test
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))





