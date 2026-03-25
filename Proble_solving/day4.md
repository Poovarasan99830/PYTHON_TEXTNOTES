
## 🟢 **Day 4 – Kadane’s Algorithm**

### ⏱ Learn

* Why brute fails
* Current sum vs max sum

### 🧠 Problems

1. Maximum subarray sum
2. All negative array
3. Return subarray indices *(advanced)*

🎯 **Pattern:** Dynamic programming (local/global)

---



No problem at all 👍
**Zero level-la** explain panren.
Ippo ellam marandhutu, idha mattum read pannunga 👇

---

## 🧠 **First: “Maximum Sum Array” na enna?**

Actually correct term 👉 **Maximum Sum SUBARRAY**

### 🧩 Meaning:

> Array-la irukkura **continuous numbers**-la
> **sum romba perusa varra part** dhaan
> **maximum sum subarray**

---











## 🔢 **Simple Example (VERY IMPORTANT)**

### Array:

```
[4, -1, 2, 1]
```

---

## 🔍 **Possible subarrays (continuous parts)**

Namma ellaa possible continuous parts-um paapom 👇

* `[4]` → sum = 4

* `[4, -1]` → sum = 3

* `[4, -1, 2]` → sum = 5

* `[4, -1, 2, 1]` → sum = 6 ✅

* `[-1]` → -1

* `[-1, 2]` → 1

* `[-1, 2, 1]` → 2

* `[2]` → 2

* `[2, 1]` → 3

* `[1]` → 1

---

## 🏆 **Which sum is biggest?**

👉 **6 is the biggest**

So:

```
Maximum sum = 6
Maximum sum subarray = [4, -1, 2, 1]
```

---

## 🗣️ **VERY SIMPLE SENTENCE (Mind-la vechuko)**

> Array-la irukkura pakkathu pakkathu numbers-la
> yedhu add panninaa perusa varudho
> adhaan maximum sum subarray.

---

## ❌ **Common Confusion (Clear pannrom)**

❌ Maximum number ≠ Maximum sum subarray

Example:

```
[10, -100, 5]
```

* Max number = 10
* But max sum subarray = `[10]` (sum = 10)

---

## 🧠 **Ippo Kadane yen varudhu?**

Namma:

* Ella subarray-um manually calculate panna koodaadhu
* Romba slow

👉 **Kadane algorithm**:

* Walking pannitu
* Sum negative aana **cut**
* Positive irundha **continue**

---

## 🪜 **Ultra-Simple Real Life Example**

Think pannunga:

* Daily profit / loss list

```
[+4, -1, +2, +1]
```

Which days continuous-aa work pannina
profit romba varudhu?

👉 Answer = all days together = **6**

---

## ✅ **One-line Final Meaning**

> Maximum sum subarray means:
> continuous numbers-la irundhu
> biggest total sum edukkiradhu.







# ___________________________________________________________
Problem Statement:

Given an integer array arr, find the maximum sum of a contiguous subarray and return that sum.

# ___________________________________________________________

current_sum = max(current element,
                  current_sum + current element)

max_sum = max(max_sum, current_sum)


# ___________________________________________________________

def kadane(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# ___________________________________________________________


🧠 First, idhu enna variables?

current_sum
👉 Ippo nadakkura subarray-oda sum




max_sum
👉 Ippovaraikum kidaicha biggest sum


# ___________________________________________________________
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


| Element | current_sum     | max_sum |
| ------- | --------------- | ------- |
| -2      | -2              | -2      |
| 1       | max(1, -2+1)=1  | 1       |
| -3      | max(-3, 1-3)=-2 | 1       |
| 4       | max(4, -2+4)=4  | 4       |
| -1      | max(-1, 4-1)=3  | 4       |
| 2       | max(2, 3+2)=5   | 5       |
| 1       | max(1, 5+1)=6   | 6       |
| -5      | max(-5, 6-5)=1  | 6       |
| 4       | max(4, 1+4)=5   | 6       |


   3
   4
  -2
   1
  -2
current_sum = arr[0]


   4
   1
   1
  -2
max_sum = arr[0]

for each element: 

         3                   -1           4          -1
         4                  4           -2         4

         -2               -3          1          -3 
          1                1         -2           1
         -2               -2         -2          -2
    current_sum = max(element, current_sum + element)
 
                      
        4               4         -3
        4             1         4  
        1             1        -2                                           
        1            -2         1   
       -2            -2        -2
    max_sum = max(max_sum, current_sum)








def kadane_with_indices(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    start = 0
    best_start = 0
    best_end = 0

    for i in range(1, len(arr)):
        # Restart or continue
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            start = i   # restart point
        else:
            current_sum = current_sum + arr[i]

        # Update best result
        if current_sum > max_sum:
            max_sum = current_sum
            best_start = start
            best_end = i

    return max_sum, best_start, best_end, arr[best_start:best_end+1]


arr = [-2, 3, 4, -1, 5, -6]
result = kadane_with_indices(arr)

print("Max Sum:", result[0])
print("Start Index:", result[1])
print("End Index:", result[2])
print("Subarray:", result[3])
