
## 🟢 **Day 2 – Move Zeros & Rotations**

### ⏱ Learn

# * Left & right rotation
# * Modulo trick
# * In-place operations

# ### 🧠 Problems

# 1. Move zeros to end
# 2. Rotate array by K
# 3. Rotate string *(if time)*

# 🎯 **Pattern:** Index manipulation

# ---


# _________________________________________________________________________

# ✅ Problem: Move Zeros to End
# 📘 Problem Statement

# You are given an integer array nums.
# Your task is to move all the zeros to the end of the array while maintaining the relative order of the non-zero elements.

# You must do this in-place, without making a copy of the array.



# Input:  [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

# _________________________________________________________________________





# Rendu pointer use pannuvom

# i → ellaa elements check panna

# j → next non-zero element enga podanum nu sollum

# Zero illa na → arr[j] place-la poduvom

# Last-la ellaa zero automatic-aa pogum

# 👉 Extra array use panna koodaadhu (in-place)




# def moveZeros(arr):
#     j = 0  # non-zero element place

#     for i in range(len(arr)):
#         if arr[i] != 0:
#             #     0        1
#             # arr[j], arr[i] = arr[i], arr[j]
#             #     0       1        1      0
#             j += 1

#     return arr


# # Test
# arr = [0, 1, 0, 3, 12]
# print(moveZeros(arr))


# [0, 1, 0, 3, 12]
#  ↑  j

# 1 found → swap → [1, 0, 0, 3, 12]
# 3 found → swap → [1, 3, 0, 0, 12]
# 12 found → swap → [1, 3, 12, 0, 0]



# Problem:
# Move all 0s to the end of the array without changing the order of non-zero elements.
# Example: [0,1,0,3,12] → [1,3,12,0,0]



# Pattern:
# Two Pointer technique (index manipulation)


# Key logic:
# Use one pointer (j) to track the position for next non-zero element.
# Traverse the array, whenever arr[i] != 0, swap it with arr[j] and increment j.
# This moves all non-zero elements to the front and zeros to the end in-place.


# Mistake I made:
# Initially thought of using a new array, but realized extra space is not needed.
# Also need to be careful to increment j only when a non-zero is found.


# Index manipulation means using
# array indexes to move, swap, rotate, or rearrange elements without using extra space.





# _________________________________________________________________________

# 🟢 Problem: Rotate Array by K (Right Rotate)

# arr = [1, 2, 3, 4, 5]
# k = 2
# _________________________________________________________________________

def rotateArray(arr, k):
    n = len(arr)
    k = k % n   # magic step


    # [5,4,3,2,1]
    # reverse whole array
    arr.reverse()

    # reverse first k elements
    # [5, 4]             [4, 5]
    arr[:k] = reversed(arr[:k])




    # reverse remaining elements
    # [3, 2, 1]           [1, 2, 3]
    arr[k:] = reversed(arr[k:])

    return arr


# Test
arr = [1,2,3,4,5]
k = 2
print(rotateArray(arr, k))




# Problem:
# Right rotate array by k positions.



# Pattern:
# Reverse technique + index manipulation.
(# Index manipulation means using
# array indexes to move, swap, rotate, or rearrange elements without using extra space.
)



# Key logic:
# Reverse full array, then reverse first k elements,
# then reverse remaining elements.

# Mistake I made:
# Forgot to use k % n when k is bigger than array length.



# _________________________________________________________________________
# 🟢 Problem: Rotate Array by K (Right Rotate   no reverse used)

# arr = [1, 2, 3, 4, 5]
# k = 2

# _________________________________________________________________________


def rotateArray(arr, k):
    n = len(arr)
    k = k % n   # safety step

    # Step 1: take last k elements
    last_part = arr[n - k:]

    # Step 2: take first n-k elements
    first_part = arr[:n - k]

    # Step 3: join them
    arr[:] = last_part + first_part

    return arr


# # Test
# arr = [1, 2, 3, 4, 5]
# k = 2
# print(rotateArray(arr, k))


# Problem:
# Right rotate array by k.

# Pattern:
# Index manipulation + slicing.

# Key logic:
# Take last k elements and move them to front.

# Mistake I made:
# Forgot k % n, caused index issue.



# _________________________________________________________________________