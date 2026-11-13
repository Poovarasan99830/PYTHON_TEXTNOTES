


# ----------------------------------
# Binary Search – Interview Notes
# ----------------------------------



## What is Binary Search?
# --------------------------------
    Binary Search is a searching technique used on **sorted data**.
    Instead of checking one by one, it divides the array into half.


### Real World Analogy
# -------------------------------
    Imagine searching a word in a dictionary.
  
  * You don’t start from page 1.
  * You open the middle page.
  * If the word comes before → go left.
  * If after → go right.
    
    This is Binary Search.


# Main Idea
# --------------------------------
  1. Find middle element
  2. Compare target with middle
  3. Move left or right
  4. Repeat until found



# Time Complexity
# --------------------------------

| Operation     | Complexity |
| ------------- | ---------- |
| Binary Search | O(log n)   |

Very fast compared to linear search O(n).




# --------------------------------
# Important Interview Points
## Why Binary Search is Fast?
    Every iteration removes half of the array.
    Example:
       1000 elements
       → 500
       → 250
       → 125 


# --------------------------------
# Common Mistakes


## 1. Wrong loop condition
# --------------------------------

Correct:
  while low <= high:

## 2. Infinite loop
# --------------------------------
Always update:
   * low
  OR
   * high

## 3. Mid overflow (important in Java/C++)
# --------------------------------
   mid = low + (high - low) // 2


# Important Patterns

| Problem          | Pattern                 |
| ---------------- | ----------------------- |
| Search element   | Normal binary search    |
| First occurrence | Move left after found   |
| Last occurrence  | Move right after found  |
| Peak element     | Compare with neighbor   |
| Rotated array    | Identify sorted half    |
| Square root      | Binary search on answer |



# Interview Summary

Binary Search mainly works in:

* Sorted arrays
* Monotonic functions
* Search spaces
* Answer optimization problems


Most asked only one questions

# ---------------------------------------------------
# Step 1:problem and definition of the problem statement
# ---------------------------------------------------
Given rotated sorted array:
arr = [4,5,6,7,0,1,2]
target = 0

Find target index.
Output:4

# --------------------------------------------------




def search_rotated(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        # target found
        if arr[mid] == target:
            return mid

        # left side sorted
        if arr[low] <= arr[mid]:

            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # right side sorted
        else:

            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


arr = [4,5,6,7,0,1,2]

print(search_rotated(arr, 0))






# -----------------------------------------------
      # [4,5,6,7,0,1,2]   0
def search_rotated(arr, target):
     4
    low = 0
      
      3
      4
      6       7
    high = len(arr) - 1
    
           4     3
           4     4
           4     6
           0     6
    while low <= high:
        
        4         4    4
        5        4    6   
        3        0    6        
        mid = (low + high) // 2

        # targe found
               0        0
               1        0        
               7        0
        if arr[mid] == target:
                    
            return mid

        # left side sorted
        
               0           0
               0           1
               4           7
        if arr[low] <= arr[mid]:
            
                  0          0       0
                  0          0       1
                  4          0       7
            if arr[low] <= target < arr[mid]:
                        
                  3      4
                  4     5  -1
                high = mid - 1
            else:
                 4    3    1
                low = mid + 1

        # right side sorted
        else:

            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


arr = [4,5,6,7,0,1,2]

print(search_rotated(arr, 0))


# ------------------------------------------------------
# Search in Rotated Sorted Array – Simple Notes
arr = [4,5,6,7,0,1,2]
target = 0
Output:4


Meaning:0 value index 4-la iruku

# Main Idea
    One side always sorted irukum.
    We check:* left sorted?OR* right sorted?



# Working Flow

## 1. Find Middle
    mid = (low + high) // 2
    Middle value check pannuvom.

## 2. Check Target Found
    if arr[mid] == target
    If target found:* return index

## 3. Check Left Side Sorted
     if arr[low] <= arr[mid]
     Meaning:Left side sorted
     Example:[4,5,6,7]

## 4. Check Target Inside Left Range
     if arr[low] <= target < arr[mid]
     Meaning:Target left sorted range-kulla iruka?
     If TRUE:high = mid - 1
     Move left.
     Else:low = mid + 1
     Move right.

## 5. Repeat Until Found
while low <= high
Repeat process until:* target found OR * search complete

# If Not Found
    return -1
   Meaning:Target array-la illa

# Time Complexity
O(log n)


# Important Interview Point
arr[low] <= arr[mid]


This condition identifies:
* left sorted side.



# ------------------------------------------------
https://chatgpt.com/share/6a0c9a5f-a6a8-8324-bc2b-400798ecb89c
# -----------------------------------------------