

# _______________________________________________________

## 1. Arrays / Lists (Same in Python)

   * Move zeros to end
   * Find max/min
   * Remove duplicates
## 2. Integers (Number-based problems)

   * Reverse a number 
   * Check palindrome number
   * Count digits
   * Sum of digits

## 3. HashMap / Dictionary
   
   * Count frequency of elements

## 4. Linked List

   * Reverse a linked list (concept)

## 5.Horizontal Scanning Technique with Prefix Reduction Method.
   * longest common prefix string
   * longest common suffix string


# _______________________________________________________


# Problem 1:Write a function to find the maximum and minimum number in a list?
<!-- 
Input:[4, 2, 9, 1, 5]
Output:Max = 9  
       Min = 1 -->

# DSA TOPICS:Linear Traversal (Single Pass) 
   # Oru array/list ah one time full ah traverse pannitu required result find pannradhu.


def find_max_min(nums):
    max_val = nums[0]
    min_val = nums[0]

    for num in nums:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val


max_val, min_val = find_max_min([4, 2, 9, 1, 5])
print("Max =", max_val)
print("Min =", min_val)








# _______________________________________________________

# Problem 2 (Maintain Order):Remove duplicates but maintain the original order.

<!-- input=[3, 1, 3, 2, 1, 4]
output=[3,1,2,4] -->

# DSA TOPICS:Hashing / Set-based Approach  (OR) Array Traversal with Membership Check
#           :Hashing-na data-a fast-a store and search panna use panra technique.

# Step 1: Understand the requirement
# Step 2: Identify constraints
# Step 3: Choose the right technique
# Step 4: Write clean, production-style code
# Step 5: Complexity analysis (important for experienced devs)
# Step 6: Pythonic one-liner (Senior-style thinking)



def remove_duplicates(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result


print(remove_duplicates([3, 1, 3, 2, 1, 4]))





# _______________________________________________________
# Problem 3
# Input:1234
# Output:4321

<!-- 1️⃣ Reverse a Number -->

# DSA Technique:Mathematical digit Manipulation


def reverse_number(n):
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    return rev


print(reverse_number(1234))




# _______________________________________________________

# Problem 4
# Given an integer n, return True if it is a palindrome.
# Do not convert the number into a string.

# DSA Technique:Mathematical Digit Manipulation

def is_palindrome(n):
    if n < 0:
        return False

    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    return original == rev


print(is_palindrome(121))



# _______________________________________________________
# Problem  5
# Given an integer n, return number of digits.
# DSA Technique:Mathematical Digit Manipulation

<!-- Input: 98765
Output: 5 -->

def count_digits(n):
    if n == 0:
        return 1

    n = abs(n)
    count = 0

    while n > 0:
        n = n // 10
        count += 1

    return count


print(count_digits(98765))




# _______________________________________________________
# Problem 6
# Return sum of digits of an integer.
# DSA Technique:Mathematical Digit Manipulation

<!-- Input: 1234
Output: 10 -->


def sum_of_digits(n):
    n = abs(n)
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10

    return total


print(sum_of_digits(1234))



# _______________________________________________________
# Problem 7
# Count frequency of each element.
# DSA Technique:Hashing + Iteration  and  Accumulation / Counting

<!-- arr = [1, 2, 2, 3, 1, 2, 4] -->
<!-- output={1: 2, 2: 3, 3: 1, 4: 1} -->


def frequency(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

arr = [1, 2, 2, 3, 1, 2, 4]
print(frequency(arr))








# _______________________________________________________
# Problem 7
# Write a function to reverse a linked list.
# DSA Technique:Two-pointer technique (or pointer manipulation in Linked List)
<!-- Input:  10 → 20 → 30 → 40
Output: 40 → 30 → 20 → 10 -->


def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next   # Step 1: Save next
        curr.next = prev        # Step 2: Reverse link
        prev = curr             # Step 3: Move prev forward
        curr = next_node        # Step 4: Move curr forward

    return prev
    

# __________________________________

prev=None
curr=10

    
20 ah marakkama save pannuvom
10 oda hand ah None ku maathuvom

prev = 10
curr = 20


20 ippove 30 ah hold pannitu irukku.
next_node = 30
prev = 20
curr = 30


Why two pointers?

Because:

One pointer (curr) traverses the list

One pointer (prev) builds the reversed list

So ithu efficient and in-place algorithm.



# _______________________________________________________


# Problem 8
# Given a list of strings strs, write a function to find the longest common prefix string among them.

# DSA Technique:Horizontal Scanning Technique with Prefix Reduction Method.


def longest_common_prefix(strs):
    # If list is empty, return empty string
    if not strs:
        return ""
    
    # Take first string as initial prefix
    prefix = strs[0]
    
    # Compare prefix with remaining strings
    for s in strs[1:]:
        # Shrink prefix until it matches the start of current string
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            
            # If prefix becomes empty, no common prefix
            if not prefix:
                return ""
    
    return prefix


# -----------------------
# Example Test Cases
# -----------------------

print(longest_common_prefix(["flower", "flow", "flight"]))   # Output: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))      # Output:
print(longest_common_prefix(["interspecies", "interstellar", "interstate"]))  # Output: "inters"
print(longest_common_prefix(["apple"]))  # Output: "apple"
print(longest_common_prefix([]))  # Output: ""




# _______________________________________________________


# Problem 8
#  Longest Common Suffix Function
# DSA Technique:Horizontal Scanning Technique with Prefix Reduction Method.




-------------------------------
# Longest Common Suffix Function
# -------------------------------
def longest_common_suffix(strs):
    if not strs:
        return ""
    
    # Step 1: Reverse all strings
    reversed_strs = [s[::-1] for s in strs]
    
    # Step 2: Find longest common prefix of reversed strings
    prefix = longest_common_prefix(reversed_strs)
    
    # Step 3: Reverse the result to get suffix
    return prefix[::-1]



# _______________________________________________________
