# ----------------------------------

# Recursion & Backtracking – Interview Notes

# ----------------------------------

## What is Recursion?

# --------------------------------

```
Recursion is a technique where a function
calls itself again and again to solve smaller problems.
```

### Real World Analogy

# -------------------------------

```
Imagine standing between two mirrors.

The image repeats infinitely.

Function calling itself is similar to that.
```

Another Example:

```
Climbing stairs.

To reach step 5,
you first reach step 4,
then step 3,
then step 2...
```

# Main Idea of Recursion

# --------------------------------

1. Break problem into smaller subproblems
2. Function calls itself
3. Stop using Base Condition
4. Return result back step by step

# Structure of Recursion

# ----------------------------------

```python
def recursion():

    # Base condition
    if condition:
        return

    # Recursive call
    recursion()
```

# Important Terms

# ----------------------------------

| Term           | Meaning                 |
| -------------- | ----------------------- |
| Base Condition | Stops recursion         |
| Recursive Call | Function calling itself |
| Stack Memory   | Stores function calls   |
| Backtracking   | Undo previous choice    |

# Recursion Tree

# ----------------------------------

Example:
Factorial of 4

```text
factorial(4)
   |
factorial(3)
   |
factorial(2)
   |
factorial(1)
   |
return 1
```

Then returns:

```text
1 → 2 → 6 → 24
```

# Time Complexity

# ----------------------------------

| Problem      | Complexity  |
| ------------ | ----------- |
| Factorial    | O(n)        |
| Fibonacci    | O(2^n)      |
| Subsets      | O(2^n)      |
| Permutations | O(n!)       |
| N-Queens     | O(N!)       |
| Sudoku       | Exponential |

# --------------------------------

# Important Interview Points

# --------------------------------

## Why Base Condition is Important?

```
Without base condition,
recursion becomes infinite.
```

Example:

```python
def test():
    test()
```

This causes:

```text
RecursionError
```

## Recursion uses Stack Memory

# --------------------------------

Every function call waits in memory.

Example:

```text
f(3)
f(2)
f(1)
```

All stored in stack.

## Backtracking Meaning

# --------------------------------

```
Choose
Explore
Undo Choice
```

This is called Backtracking.

Used in:

* Sudoku
* N-Queens
* Maze problems
* Permutations

# Common Mistakes

# --------------------------------

## 1. Missing Base Condition

Wrong:

```python
def fun(n):
    return fun(n-1)
```

## 2. Changing Original Data Incorrectly

Always undo changes in backtracking.

Example:

```python
path.append(x)

# recursive call

path.pop()
```

## 3. Too Many Recursive Calls

Fibonacci recursive solution is slow because
same values are calculated again and again.

# Important Patterns

# ----------------------------------

| Problem Type | Pattern                |
| ------------ | ---------------------- |
| Factorial    | Single recursion       |
| Fibonacci    | Multiple recursion     |
| Subsets      | Include / Exclude      |
| Permutations | Swap technique         |
| Maze         | DFS + Backtracking     |
| N-Queens     | Safe position checking |
| Sudoku       | Try every possibility  |

# Interview Summary

# ----------------------------------

Recursion mainly works in:

* Tree problems
* Backtracking problems
* Divide and conquer
* DFS traversal
* Dynamic programming base

# ---------------------------------------------------

# Step 1: Problem and Definition

# ---------------------------------------------------

Find factorial of a number using recursion.

Example:
n = 5

Output:
120

# ---------------------------------------------------

# Factorial Program

# ---------------------------------------------------

```python
def factorial(n):

    # base condition
    if n == 0 or n == 1:
        return 1

    # recursive call
    return n * factorial(n - 1)


print(factorial(5))
```

# ---------------------------------------------------

# Fibonacci using Recursion

# ---------------------------------------------------

Definition:
Each number is sum of previous two numbers.

Example:
0 1 1 2 3 5 8

```python
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


for i in range(8):
    print(fibonacci(i), end=" ")
```

# ---------------------------------------------------

# Subsets Problem

# ---------------------------------------------------

Definition:
Find all possible subsets.

Example:
[1,2]

Output:
[]
[1]
[2]
[1,2]

```python
def subsets(nums, path=[], index=0):

    if index == len(nums):
        print(path)
        return

    # include
    subsets(nums, path + [nums[index]], index + 1)

    # exclude
    subsets(nums, path, index + 1)


subsets([1,2])
```

# ---------------------------------------------------

# Permutations Problem

# ---------------------------------------------------

Definition:
Arrange elements in all possible ways.

Example:
[1,2,3]

Output:
[1,2,3]
[1,3,2]
[2,1,3]
...

```python
def permutations(arr, start=0):

    if start == len(arr):
        print(arr)
        return

    for i in range(start, len(arr)):

        arr[start], arr[i] = arr[i], arr[start]

        permutations(arr, start + 1)

        # backtracking
        arr[start], arr[i] = arr[i], arr[start]


permutations([1,2,3])
```

# ---------------------------------------------------

# N-Queens Problem

# ---------------------------------------------------

Definition:
Place N queens on chessboard
without attacking each other.

Rules:

* No same row
* No same column
* No diagonal attack

```python
def is_safe(board, row, col, n):

    # upper column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):

    if row == n:

        for r in board:
            print(" ".join(r))
        print()

        return

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = 'Q'

            solve(board, row + 1, n)

            # backtracking
            board[row][col] = '.'


n = 4

board = [['.' for _ in range(n)] for _ in range(n)]

solve(board, 0, n)
```

# ---------------------------------------------------

# Sudoku Solver

# ---------------------------------------------------

Definition:
Fill empty cells with valid numbers.

Rules:

* Row should not repeat
* Column should not repeat
* 3x3 grid should not repeat

```python
def is_valid(board, row, col, num):

    for i in range(9):

        if board[row][i] == num:
            return False

        if board[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):

            if board[start_row+i][start_col+j] == num:
                return False

    return True


def solve(board):

    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:

                for num in range(1, 10):

                    if is_valid(board, row, col, num):

                        board[row][col] = num

                        if solve(board):
                            return True

                        # backtracking
                        board[row][col] = 0

                return False

    return True
```

# Quick Interview One-Line Answers

# ----------------------------------

## What is Recursion?

```
Function calling itself.
```

## What is Base Condition?

```
Condition used to stop recursion.
```

## What is Backtracking?

```
Try → Explore → Undo.
```

## Why Recursion is Costly?

```
Uses stack memory.
```

## Difference Between Recursion & Loop?

| Recursion              | Loop             |
| ---------------------- | ---------------- |
| Uses function calls    | Uses iteration   |
| Uses stack memory      | Less memory      |
| Easy for tree problems | Faster generally |

# Most Asked Interview Questions

# ----------------------------------

1. Factorial using recursion
2. Fibonacci recursion
3. Reverse string recursion
4. Generate subsets
5. Generate permutations
6. N-Queens
7. Sudoku solver
8. Tower of Hanoi
9. Maze path problems
10. Palindrome recursion
