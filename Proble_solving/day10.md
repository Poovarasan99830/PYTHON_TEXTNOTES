



### **📌 Sliding Window (Days 10–12)**

Learn: fixed window, variable window
Problems:

* Max sum window
* Longest substring without repeat
* Count anagrams
* Fruits into basket





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






# ---------------------------------------------------
### **📌 Sliding Window (Days 10–12)**

# ---------------------------------------------------
✅ What is Sliding Window?
# ---------------------------------------------------

Sliding Window is an optimization technique used for:

Arrays
Strings
Subarrays
Substrings



# ---------------------------------------------------
Instead of checking every possible combination, we maintain a “window” and move it efficiently.
   
   Learn: fixed window, variable window
   Problems:
     * Max sum window
     * Longest substring without repeat
     * Count anagrams
     * Fruits into basket


# ---------------------------------------------------
# Step 1:problem and definition of the problem statement
# ---------------------------------------------------

Problem:
   Longest Substring Without Repeating Characters
   This is one of the MOST ASKED sliding window questions.

Find longest substring without duplicate characters.
s = "abcabcbb"



# ---------------------------------------------------
# step 2 -->real world analogy
# ---------------------------------------------------

Real World Analogy
Neenga oru room la students ah allow panreenga.
Ore name rendu thadava irukka koodathu
Duplicate name வந்தா ❌

Example
 "abcabcbb"

 Ithu room ku students வர்ற மாதிரி imagine pannunga.

 [a]        Room la: a Duplicate illa --->Length = 1
 [a b]      Room la: a,b Duplicate illa --->Length = 2
 [a b c]    Room la: a,b,c Duplicate illa --->Length = 3

 Next character:  
 [a b c a]   Room la: a,b,c,a Duplicate a வந்துருச்சு ❌
 ✅ Solution:
       Left side la irundhu remove pannuvom.
       Remove first a
       Now:[b c a] --Ippo duplicate illa ✅

Sliding Window Meaning
   current active group
   Duplicate வந்தா    :👉 left side shrink pannuvom
   Duplicate இல்லனா :👉 right side expand pannuvom


# ---------------------------------------------------
# step 3 -->Solution of the Problem
# ---------------------------------------------------

def longest_substring(s):

    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        max_len = max(max_len, right-left+1)

    return max_len

print(longest_substring("abcabcbb"))




# ---------------------------------------------------
# step 3 -->Coding Explanation
## ---------------------------------------------------

1. `seen = set()`

   * Unique characters store panna use pannrom.
   * Duplicate vara koodathu.

2. `left = 0` and `for right in range(len(s))`

   * `left` = window start index
   * `right` = window end index
   * Ithu sliding window concept.

3. `while s[right] in seen:`

   * Current character already irundha duplicate nu meaning.
   * So left side character remove pannuvom.

4. `seen.add(s[right])`

   * Duplicate remove aana apram current character set la add pannrom.
   * Ippo substring unique ah irukum.

5. `max_len = max(max_len, right-left+1)`

   * Current substring length calculate pannrom.
   * Biggest length save pannuvom.
   * `"abcabcbb"` ku output = `3` because `"abc"` longest unique substring.


## ---------------------------------------------------