<!-- Alright — I’ll give you **problem-solving questions** that require using **lists, tuples, and any other data structure or algorithm** in Python.
I’ll make sure they range from **easy to challenging**, so they’re good for practice.

---

## **Problem-Solving Questions**

### **Beginner Level**

1. **List Sum & Average**
   Given a list of numbers, calculate the sum and average without using built-in `sum()` or `statistics` module.

2. **Unique Elements**
   Given a list with duplicate values, return a new list with only unique values **in the same order** they appeared.

3. **Tuple Swap**
   You have two tuples:

   ```python
   t1 = (1, 2, 3)  
   t2 = (4, 5, 6)
   ```

   Swap their values without using extra variables.

---

### **Intermediate Level**

4. **List Rotation**
   Rotate a list to the right by `k` steps.
   Example:

   ```
   Input: [1, 2, 3, 4, 5], k=2  
   Output: [4, 5, 1, 2, 3]
   ```

5. **Student Marks System**
   Given a list of tuples with `(student_name, marks)`, find:

   * The student with the highest marks
   * The average marks of the class
   * All students scoring above average

6. **Matrix Transpose**
   Given a 2D list (matrix), return its transpose.
   Example:

   ```
   [[1,2,3],[4,5,6]] → [[1,4],[2,5],[3,6]]
   ```

---

### **Advanced Level**

7. **Leaderboard Ranking**
   Given a list of tuples `(player_name, score)`, return the **ranked leaderboard** sorted by score descending, and assign ranks properly even if scores are tied.

8. **Bank Transactions Tracker**
   Maintain a transaction history using a **list of tuples** where each tuple contains: `(transaction_type, amount, balance_after_transaction)`.
   Implement deposit and withdrawal functions with balance updates.

9. **Path Finder in Grid**
   You have a 2D grid represented as a list of lists, where `0` is open path and `1` is blocked.
   Write an algorithm (DFS or BFS) to check if there’s a path from the top-left to bottom-right corner.

10. **Movie Recommendation (Data Filtering)**
    You are given a list of tuples: `(movie_title, genre, rating)`.
    Write a function that takes a preferred genre and a minimum rating, and returns all matching movies sorted by rating.

---

📌 If you want, I can **pick one problem** (like the leaderboard ranking) and solve it step-by-step with **list, tuple, sorting, and algorithm logic** so students can see how to think through it.

Do you want me to prepare that worked-out example?









Alright — here are the **harder versions** of those three problems with explanations.

---

## **1. List Sum & Average with Nested Lists**

We’ll calculate the sum and average from a list that contains **lists inside it**.

```python
numbers = [[10, 20], [30, 40, 50], [60]]

total = 0
count = 0

for sublist in numbers:
    for num in sublist:
        total += num
        count += 1

average = total / count

print(f"Sum: {total}")
print(f"Average: {average}")
```

**Output:**

```
Sum: 210
Average: 35.0
```

---

## **2. Unique Elements for a List of Tuples**

Here, each element is a **tuple**, and we want to keep only the first occurrence of each tuple.

```python
data = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4)]
unique_list = []

for tup in data:
    if tup not in unique_list:
        unique_list.append(tup)

print(unique_list)
```

**Output:**

```
[(1, 2), (3, 4), (5, 6)]
```

---

## **3. Tuple Swap for Tuples of Different Sizes**

Swapping works even if tuple lengths differ — Python doesn’t care.

```python
t1 = (1, 2, 3)
t2 = (4, 5)

t1, t2 = t2, t1  # Tuple unpacking

print("t1:", t1)
print("t2:", t2)
```

**Output:**

```
t1: (4, 5)
t2: (1, 2, 3)
```

---

If you want, I can now combine **all three concepts** into **one single problem** that uses:

* Nested lists
* Tuples inside lists
* Swapping
  …so your students solve them together in a realistic task. Would you like me to prepare that? -->


<!-- n = 5
for i in range(1, n+1):
   print(' ' * (n - i) + '*' * (2 * i - 1)) -->