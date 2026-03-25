


* Clear concepts
* Clean coding
* Time complexity awareness
* Real-world thinking

So you must prepare **concept + coding + explanation**.

# ___________________________________________________
## 1. Arrays / Lists (Same in Python)
# ___________________________________________________


### What you must know

* What is an array/list
* Insert, delete, search
* Time complexity





### Expected questions

1. What is the difference between list and array?
2. Time complexity of:

   * Insert
   * Delete
   * Access
3. Write a program:

   * Move zeros to end
   * Find max/min
   * Remove duplicates

### Example

```python
nums = [1, 2, 3]
nums.append(4)   # insert
nums.pop()       # delete
print(nums[1])   # access
```

---
# ___________________________________________________
## 2. Integers (Number-based problems)
# ___________________________________________________


### What they may ask

1. Reverse a number
2. Check palindrome number
3. Count digits
4. Sum of digits

Example:

```python
def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev
```

---
# ___________________________________________________
## 3. HashMap / Dictionary
# ___________________________________________________


### Must know

* Key-value storage
* Fast lookup
* O(1) average access time

### Expected questions

1. What is dictionary?
2. Why is it faster than list search?
3. Count frequency of elements

Example:

```python
nums = [1, 2, 2, 3]
freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1

print(freq)
```


# ___________________________________________________
## 4. Linked List
# ___________________________________________________

### Must know concept

* Node
* Next pointer
* Head

### Expected questions


1. What is linked list?
2. Difference between array and linked list
3. Reverse a linked list (concept)

# ___________________________________________________

Basic structure:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---
# ___________________________________________________
## 5. Binary Trees
# ___________________________________________________


### Must know concept only

* Root
* Left child
* Right child

### Expected questions

1. What is binary tree?
2. Difference between tree and list
3. What is traversal?

   * Inorder
   * Preorder
   * Postorder

Basic node:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

# ___________________________________________________
### Concept Questions
# ___________________________________________________


* Difference between list and dictionary
* When to use linked list?
* What is time complexity of dictionary lookup?
* What is a binary tree?


### Experience-based Questions

* How did you use Django ORM in project?
* Explain one API you built
* How do you handle errors in backend?
* How do you optimize database queries?






