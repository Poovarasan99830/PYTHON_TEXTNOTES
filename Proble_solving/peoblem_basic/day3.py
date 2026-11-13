# ## Second Largest — Interview Approach ⭐



def second_largest(numbers):

    largest = float('-inf')
    second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num

        elif largest > num > second:
            second = num

    return second


numbers = [10, 5, 8, 20, 15]

print(second_largest(numbers))










# ### What is the problem?

# Given a list of numbers, find the **second largest distinct number**.

# Example:

# ```python
# numbers = [10, 5, 8, 20, 15]
# ```

# Output:

# ```text
# 15
# ```

# Because:

# ```text
# Largest       = 20
# Second largest = 15
# ```

# ---

# ## Efficient approach — One Pass ⭐

# ```python
# def second_largest(numbers):

#     largest = float('-inf')
#     second = float('-inf')

#     for num in numbers:
#         if num > largest:
#             second = largest
#             largest = num

#         elif largest > num > second:
#             second = num

#     return second


# numbers = [10, 5, 8, 20, 15]

# print(second_largest(numbers))
# ```

# Output:

# ```text
# 15
# ```

# ### 🗣️ Thanglish — Behind the scenes

# We maintain **two variables**:

# ```text
# largest       → biggest number
# second        → second biggest number
# ```

# Initially:

# ```text
# largest = -∞
# second  = -∞
# ```

# For:

# ```text
# [10, 5, 8, 20, 15]
# ```

# ### `10`

# ```text
# 10 > largest
# ```

# So:

# ```text
# largest = 10
# second = -∞
# ```

# ### `5`

# ```text
# 5 > largest? ❌
# largest > 5 > second? ✅
# ```

# So:

# ```text
# largest = 10
# second = 5
# ```

# ### `8`

# ```text
# 10 > 8 > 5 ✅
# ```

# So:

# ```text
# second = 8
# ```

# ### `20`

# 20 is bigger than current largest:

# ```text
# second = 10
# largest = 20
# ```

# ### `15`

# ```text
# 20 > 15 > 10
# ```

# So:

# ```text
# second = 15
# ```

# Final:

# ```text
# largest = 20
# second = 15
# ```

# ---

# ## Why don't we sort?

# You might think:

# ```python
# numbers.sort()
# ```

# Then take the second-last element.

# But sorting takes:

# > **O(n log n)**

# We don't need to sort the entire list.

# We only need to know:

# > **Who is the largest and who is the second largest?**

# So we can find both in **one traversal**.

# ### DSA Pattern

# This is:

# > **Linear Traversal + Tracking**

# Same pattern we used for **Longest Word**.

# ```text
# Longest Word
# → track longest

# Second Largest
# → track largest + second largest
# ```

# ### Complexity

# **Time: O(n)**

# One loop through the list.

# **Space: O(1)**

# Only two variables are used.

# ### 🎯 Interview answer

# > **“I use a single-pass linear traversal and maintain two variables, `largest` and `second_largest`. Whenever I find a new largest value, I move the previous largest to second largest. Otherwise, if the current value lies between them, I update second largest. This gives O(n) time and O(1) extra space.”**

# ### Important: duplicates

# If:

# ```python
# [10, 20, 20, 15]
# ```

# and the question asks for **second largest distinct value**, answer is:

# ```text
# 15
# ```

# That's why this condition is important:

# ```python
# elif largest > num > second:
# ```

# It prevents another `20` from becoming the second-largest value.
