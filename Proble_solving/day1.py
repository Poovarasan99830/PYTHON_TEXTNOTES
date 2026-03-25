

# __________________________________________________________
# ✅ **Arrays & Strings – 6-Day Ultra-Focused Plan**

## 🕒 Daily Structure (Do this EVERY day)

# **0–20 mins → Learn ONE concept only**
# **20–60 mins → Solve 2–4 problems max**
# ❌ No YouTube rabbit holes
# ❌ No extra problems “just one more”


# What you SHOULD do instead:

# Rule #1: ONE source only

# One article OR

# One short video (≤ 20 mins) OR

# Written explanation + examples

# Stop immediately after learning the core idea.

# __________________________________________________________

# Write this in notebook or notes app:

# ```
# Problem:
# Pattern:
# Key logic:
# Mistake I made:
# ```

# This is **more valuable than solving extra problems**.

# __________________________________________________________

## 🚀 After 6 Days You Will:

# ✔ Instantly recognize array/string patterns
# ✔ Be confident with rotations & Kadane
# ✔ Explain logic clearly in interviews
# ✔ Be ready for hashing & sliding window next

# ---

# If you want next:
# 👉 **Exact LeetCode problem numbers**
# 👉 **Day 1 walkthrough with code**
# 👉 **Phase 2 plan (Hashing + Sliding Window)**


# __________________________________________________________







## 📅 **Day-wise Plan (1 Hour Each)**



## 🟢 **Day 1 – Array Traversal & Two Pointers**

### ⏱ Learn (20 mins)

# * Array indexing
# * Traversal using loop
# * Two-pointer technique

# ### 🧠 Problems (40 mins)

# 1. Reverse array
# 2. Find max & min
# 3. Print alternate elements *(optional)*

# 🎯 **Pattern learned:** Two pointers

# __________________________________________________________





# _____________________________________________________________________________________
# Array-a reverse pannanu (last element first-ku varanum).
# _____________________________________________________________________________________


# Input:  [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]



# 
data = [1, 2, 3, 4, 5]

i = 0
j = len(data) - 1

while i < j:
    data[i], data[j] = data[j], data[i]  # correct swap
    i += 1
    j -= 1

print(data)



# _____________________________________________________________________________________
# I used two pointer approach.
# Start and end indices are swapped using tuple swap.
# Loop runs while i < j.
# Time complexity is O(n) and space complexity is O(1) since it’s an in-place operation
# _____________________________________________________________________________________


# Two pointer approach 


# Oru array / string-la rendu pointers (index) use panni problem solve pannradhu dhaan Two Pointer Approach

# Why Two Pointer Use Pannrom?

# Fast solution venum
# Extra memory avoid panna
# O(n) time-la problem solve panna

# "Two pointer approach is a technique where we use two indices to traverse the array or string efficiently, 
# either from both ends or in the same direction



# _____________________________________________________________________________________
# ## 🔹 Explanation

# In-Place Algorithm na enna?
# 🧠 Meaning:

# Original array-laiye changes pannradhu
# New memory use pannama.

# Space Complexity = O(1)
# Because constant space mattum dhaan use pannrom.

# Time Complexity = O(n)
# Because array length-ku proportional-aa work nadakkudhu.



# _____________________________________________________________________________________



# Good question 👍
# **“Grows proportionally”** meaning-a **simple Tanglish + examples**-oda explain pannren.

# ---

# ## 🔹 “Grows Proportionally” – Meaning

# ### 🧠 Simple Meaning:

# > **Input size increase aagumbodhu,
# > work (time or steps) um same ratio-la increase aagum**

# Tamil + English-la:
# 👉 **Input perusa aana, work-um perusa aagum (same scale-la)**

# ---

# ## 🔹 Real Life Example 🚶‍♂️

# ### Example 1: Road Walk

# * 1 km walk → 10 minutes
# * 2 km walk → 20 minutes
# * 3 km walk → 30 minutes

# 👉 Distance double aana time-um double
# 👉 Idhu dhaan **grows proportionally**

# ---

# ## 🔹 Programming Example (Array)

# ```python
# for i in range(n):
#     print(i)
# ```

# ### Steps:

# * n = 5 → 5 steps
# * n = 10 → 10 steps
# * n = 100 → 100 steps

# 👉 Input size (n) increase aagumbodhu
# 👉 Operations um same amount-la increase aagudhu

# ✅ So we say:

# > **Time grows proportionally with input size**

# ---

# ## 🔹 Why idha O(n) nu sollrom?

# Because:

# * Work = n times
# * n increase aana work-um increase aagudhu

# 👉 That’s why:

# ```text
# O(n)
# ```

# ---

# ## 🔹 Contrast Example (Not Proportional ❌)

# ```python
# for i in range(n):
#     for j in range(n):
#         print(i, j)
# ```

# ### Steps:

# * n = 5 → 25 steps
# * n = 10 → 100 steps

# 👉 n double aana work **4 times** increase aagudhu

# ❌ Idhu proportional illa
# ✅ Idhu **O(n²)**

# ---

# ## 🔹 Easy Interview Definition 💡

# > **“Grows proportionally means, when input size increases, the number of operations increases at the same rate.”**

# Tanglish:

# > **Input size perusa aana, operations-um same scale-la increase aagum.**

# ---

# ## 🔑 Quick Memory Trick 🧠

# | Input Growth | Work Growth | Complexity |
# | ------------ | ----------- | ---------- |
# | Same ratio   | Same ratio  | O(n)       |
# | Square       | Very fast   | O(n²)      |
# | Constant     | No change   | O(1)       |

# ---

# 👉 Venumna **Big-O full chart**,
# 👉 Or **interview Q&A in Tanglish**,
# 👉 Or **real-time coding examples**


# ______________________________________________________________________________________