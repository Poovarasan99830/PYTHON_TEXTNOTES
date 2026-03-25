## 🟢 **Day 3 – Prefix Sum**

### ⏱ Learn

* Prefix sum idea
* Range sum

### 🧠 Problems

1. Build prefix sum
2. Subarray sum equals K
3. Equilibrium index *(optional)*

🎯 **Pattern:** Precomputation

---


# _____________________________________
Question 1: Build Prefix Sum Array
# _____________________________________



Problem Statement:
Given an array of integers, construct its prefix sum array.

A prefix sum array is an array where each element at index i stores the sum of all elements from index 0 to i of the original array.
# _____________________________________
Input:
arr = [1, 2, 3, 4, 5]

Output:
prefix = [1, 3, 6, 10, 15]

# _____________________________________





arr = [1, 2, 3, 4, 5]


          0     5 
prefix = [0] * len(arr)



prefix=[0,0,0,0,0]

  0            1
prefix[0] = arr[0]


prefix=[1,0,0,0,0]

1+arr[1]=3
3+arr[2]=6
6+arr[3]=10
10+arr[4]=15

                      5

for i in range(1, len(arr)):
           2          1           2
           1          0           1       
    prefix[i] = prefix[i-1] + arr[i]
           0          1+2
          (3) 
           0           3          3
          (6)
        
          




print(prefix)











