# ---------------------------------------------------
### **📌 Two Pointers (Days 13–15)**
# ---------------------------------------------------






# ---------------------------------------------------
✅ What is Two Pointers?
# ---------------------------------------------------


Two Pointers is a technique where we use:
   Two indexes / pointers
   One pointer from left side
   Another pointer from right side




# ---------------------------------------------------

Instead of using nested loops, we move pointers smartly to reduce time complexity.

Problems:
  * Pair sum
  * 3-sum
  * Sort colors
  * Remove duplicates



# ---------------------------------------------------
# Step 1:problem and definition of the problem statement
# ---------------------------------------------------

Problem:
Pair Sum
This is one of the MOST ASKED two pointer interview questions.
Find two numbers whose sum equals target.
   arr = [1,2,3,4,6]
   target = 6

# ---------------------------------------------------
# step 2 -->real world analogy
# ---------------------------------------------------

Real World Analogy

Neenga rendu friends ah choose panna porenga.
Avanga rendu per salary add panna exact target amount vara num.


Example:
[1,2,3,4,6]
Target = 6

Left side friend 👉 1
Right side friend 👉 6

1 + 6 = 7 ❌
Target vida perusa iruku
So right pointer move pannuvom 👈

Now:
1 + 4 = 5 ❌
Target vida kammi
So left pointer move pannuvom 👉

Now:
2 + 4 = 6 ✅

Answer kedaichiduchu.

Two Pointer Meaning

Sum perusa irundha : 👉 right decrease pannuvom

Sum kammi irundha : 👉 left increase pannuvom

Correct target vandha : 👉 answer return pannuvom

# ---------------------------------------------------
# step 3 -->Solution of the Problem
# ---------------------------------------------------

#        1,2,3,4,6   6
def pair_sum(arr,   target):

    left = 0
    right = len(arr) - 1

#          0      4
    while left < right:
 
#          7           1            6
        current_sum = arr[left] + arr[right]

#          7           6
        if current_sum == target:
                       
            return [arr[left], arr[right]]

#               7               6      
        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return []

print(pair_sum([1,2,3,4,6], 6))
```

# ---------------------------------------------------
# step 3 -->Coding Explanation
# ---------------------------------------------------

1. `left = 0` and `right = len(arr)-1`

   * Left pointer start la irukum.
   * Right pointer end la irukum.

2. `while left < right:`

   * Two pointers cross aagura vara loop run aagum.

3. `current_sum = arr[left] + arr[right]`

   * Current two numbers add pannrom.

4. `elif current_sum < target:`

   * Sum kammi na left pointer increase pannuvom.
   * Bigger value venum.

5. `else: right -= 1`

   * Sum perusa na right pointer decrease pannuvom.
   * Smaller value venum.
   * Output = `[2,4]` because `2 + 4 = 6` ✅

# ----------------------------------------------------------



# ---------------------------------------------------

✅ Why Interviewers Ask This Question?

# ---------------------------------------------------

Indha question use pannitu interviewer check panrathu:

* Candidate logic thinking iruka?
* Nested loop avoid panna theriyuma?
* Optimized solution yosikka theriyuma?
* Two Pointer concept purinjiruka?
* Time Complexity reduce panna mudiyuma?

# ---------------------------------------------------

✅ What Actually They Are Asking?

# ---------------------------------------------------

Question:

```python
arr = [1,2,3,4,6]
target = 6
```

Meaning:

Array la irundhu rendu numbers choose pannanum.

Andha rendu numbers add panna target value vara num.

Here target = 6

So:

```python
2 + 4 = 6
```

Hence answer:

```python
[2,4]
```

# ---------------------------------------------------

✅ Why Not Use Normal Loop?

# ---------------------------------------------------

Normal ah na:

```python
for i:
   for j:
```

Ippadi nested loop use pannuvom.

But adhu slow ❌

Time Complexity:
O(n²)

Interviewers expect:
Smart solution ✅

So Two Pointer use pannrom.

# ---------------------------------------------------

✅ Main Idea of Two Pointer

# ---------------------------------------------------

One pointer left side la irukum.

One pointer right side la irukum.

Example:

```python
[1,2,3,4,6]
 L       R
```

Now check:

```python
1 + 6 = 7
```

Target = 6

7 perusa iruku ❌

So right side value decrease panna venum.

Hence:

```python
R move left
```

# ---------------------------------------------------

✅ Next Step

# ---------------------------------------------------

Now:

```python
[1,2,3,4,6]
 L     R
```

Check:

```python
1 + 4 = 5
```

5 kammi ❌

Target reach aagala.

So bigger value venum.

Hence:

```python
L move right
```

# ---------------------------------------------------

✅ Final Step

# ---------------------------------------------------

Now:

```python
[1,2,3,4,6]
   L   R
```

Check:

```python
2 + 4 = 6
```

Target match aagiduchu ✅

Answer:

```python
[2,4]
```
