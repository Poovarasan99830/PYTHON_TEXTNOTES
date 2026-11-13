

# ----------------------------------------------------------------------------------
# * Reverse String

# ----------------------------------------------------------------------------------


# String

# p   y   t   h   o   n
# 0   1   2   3   4   5

# Loop

# i = 5 → n
# i = 4 → o
# i = 3 → h
# i = 2 → t
# i = 1 → y
# i = 0 → p

# Final Output

# nohtyp


# String = Immutable = New object every change ❌
# List = Mutable = Same object update ✅
# Large data → Use list + ''.join() 🚀



# Approach 1 (Most Common)

def reverse_string(s):
    result = ""

    for i in range(len(s) - 1, -1, -1):
        result += s[i]

    return result


text = input("Enter a string: ")
print("Reversed String:", reverse_string(text))


# Approach 3 (Using List)

def reverse_string(s):
    result = []

    for i in range(len(s) - 1, -1, -1):
        result.append(s[i])

    return "".join(result)

print(reverse_string("python"))


# Since Python strings are immutable, I'll create a new string, iterate from the last character to the first, append each character to the new string,
# and return the result. This approach has O(n) time complexity and O(n) space complexity\





# [::-1]
# reversed()
# .join()



# ----------------------------------------------------------------------------------

<!-- * Palindrome -->
# ----------------------------------------------------------------------------------


<!-- Oru pointer front-la irukkum.

Innoru pointer last-la irukkum.

Rendu characters compare pannuvom.

Equal na next.

Equal illa na Not Palindrome. -->


def pali(a):
    
    left=0
    right=len(a)-1
    
    
    while left<right:
        if a[left]!=a[right]:
            return "not palindrom"
        left+=1
        right-=1
        
    return "palindrom"
    
    
print(pali("one"))


<!-- "I'd choose the Two Pointer approach because it has O(n) time complexity and O(1) space complexity, making it more memory-efficient than creating a reversed copy of the string. -->

<!-- 
"Sir, Two Pointer technique-na rendu index variables use panni problem solve pannradhu. Usually oru pointer first element-la irukkum, innoru pointer last element-la irukkum. Rendu pointers-ai condition-ku based move pannuvom. Idhu extra data structure create panna vendiya avasiyam illa, so memory save aagum. Palindrome, Reverse Array, Two Sum, Move Zeros, Remove Duplicates madhiri problems-la Two Pointer technique romba common-a use pannuvanga. -->











# ----------------------------------------------------------------------------------

<!-- * prime Check-->
# ----------------------------------------------------------------------------------


<!-- "Sir, Prime Number-na 1-um and adhe number-um thavira vera yendha number-ala divide panna mudiyadhu." -->


<!-- "Sir, 1 ella numbers-um divide pannum. Adhanala prime check 2-lendhu dhaan start pannuvom -->






def prime_number(num):

    if num <= 1:
        return "Not Prime"

    for i in range(2, num):

        if num % i == 0:
            return "Not Prime"

    return "Prime"


num = int(input("Enter Number: "))
print(prime_number(num))





<!-- "13 chocolates-a 1 person-kum equal-aa kudukkalam, 13 persons-kum equal-aa kudukkalam. Aana 2-lendhu 12 varaikkum yaarukkum balance illaama equal-aa kudukka mudiyadhu. Adhanala 13 Prime Number." -->



<!-- Think of 13 chocolates:

Can 2 people share equally? → Check ✔
Can 3 people share equally? → Check ✔
...
Can 12 people share equally? → Check ✔
Can 13 people share equally? → Yes, but every number divides itself, so this doesn't help determine if it's prime.
Can 14 or more people share equally? → Impossible, so there's no point checking. -->




# ----------------------------------------------------------------------------------


<!-- What is Fibonacci Series?
"Sir, Fibonacci Series-la first rendu numbers 0 and 1. Adhuku apram vara ovvoru number-um previous rendu numbers-oda sum." -->


def fibonacci(n):

    a = 0
    b = 1

    for i in range(n):

        print(a, end=" ")

        c = a + b
        a = b
        b = c


num = int(input("Enter Number of Terms: "))
fibonacci(num)


<!-- I'd use the iterative (loop) approach because it runs in O(n) time with O(1) extra space. The recursive solution is elegant but inefficient because it recalculates the same Fibonacci values multiple times unless memoization is used -->


<!-- "Sir, Fibonacci Series-la first two numbers 0 and 1. Adhuku apram ovvoru number-um previous rendu numbers-oda sum. Naan a, b, c nu moonu variables use pannuren. c = a + b calculate pannitu, a = b and b = c update pannuren. Indha process-a n terms vara repeat pannuren. Indha iterative approach-oda Time Complexity O(n) and Space Complexity O(1), so recursion vida idhu efficient. -->



# -----------------------
# Factorial
# ------------------------

<!-- "Sir, factorial-la same multiplication operation repeated-aa nadakkudhu. Adhanala for loop use pannuren. Loop simple, faster, and O(1) space use pannum. Recursion-um use pannalaam, aana adhu function-ai thirumba thirumba call pannum. Ovvoru call-um call stack-la store aagum, so O(n) extra space use aagum. Production code-la usually loop approach dhaan prefer pannuvanga because it's more memory efficient -->


<!-- def fact(n):

    re = 1

    for i in range(re, n + 1):

        re = re * i

    return re

print(fact(3)) -->












# -----------------------
<!-- What is an Armstrong Number? !-->
# -----------------------
<!--

Armstrong Number-na, oru number-la irukkura ovvoru digit-ai, total digits count power-ku raise panni add pannumbodhu, original number vandha adhu Armstrong Number.

Formula
Sum of (Each Digit ^ Total Number of Digits)  -->



def armstrong(num):

    original = num

    digits = len(str(num))

    total = 0

    while num > 0:

        digit = num % 10

        total = total + (digit ** digits)

        num = num // 10

    if original == total:
        return "Armstrong Number"
    else:
        return "Not Armstrong Number"


num = int(input("Enter Number: "))
print(armstrong(num))

<!-- 
num = 153

        │
        ▼
digit = 153 % 10
        │
        ▼
digit = 3
        │
        ▼
3³ = 27
        │
        ▼
total = 27
        │
        ▼
num = 153 // 10
        │
        ▼
15

        │
        ▼
digit = 15 % 10
        │
        ▼
5³ = 125
        │
        ▼
total = 152
        │
        ▼
num = 15 // 10
        │
        ▼
1

        │
        ▼
digit = 1 % 10
        │
        ▼
1³ = 1
        │
        ▼
total = 153
        │
        ▼
num = 1 // 10
        │
        ▼
0

Loop Stops -->



# -------------------------------------------------------------------
<!-- Approach 1: Using While Loop (Interview Friendly)

Empty reverse number (reverse = 0) create pannunga.

Last digit-a %10 use panni edunga.

Existing reverse number-a 10-la multiply pannunga.

Last digit-a add pannunga.

Original number-la last digit-a //10 use panni remove pannunga.

Number 0 aagura varaikkum repeat pannunga. -->



def reverse_number(num):

    reverse = 0

    while num > 0:

        digit = num % 10

        reverse = reverse * 10 + digit

        num = num // 10

    return reverse


num = int(input("Enter Number: "))
print(reverse_number(num))




| num  | digit | reverse |
| ---- | ----- | ------- |
| 1234 | 4     | 4       |
| 123  | 3     | 43      |
| 12   | 2     | 432     |
| 1    | 1     | 4321    |


The confusing line is:

```python
reverse = reverse * 10 + digit
```

Let's understand it in the **simplest Tanglish**.

---

## Think Like This

Suppose you've already built the reverse number:

```text
reverse = 43
```

Now you extract the next digit:

```text
digit = 2
```

You want the new reverse to become:

```text
432
```

### Step 1: Multiply by 10

```python
reverse * 10
```

```text
43 × 10 = 430
```

**Tanglish:**

`*10` pannumbodhu, **last-la oru empty place (0)** create aagum.

```text
43

↓

430
```

---

### Step 2: Add the new digit

```python
430 + 2
```

```text
432
```

That's why we write:

```python
reverse = reverse * 10 + digit
```

---

## Another Example

Suppose

```text
reverse = 7
digit = 6
```

Calculation

```text
7 × 10 = 70

70 + 6 = 76
```

---

Suppose

```text
reverse = 76
digit = 5
```

Calculation

```text
76 × 10 = 760

760 + 5 = 765
```

---

## Dry Run

Original Number:

```text
1234
```

| Extracted digit | reverse before | reverse × 10 | + digit | reverse after |
| --------------- | -------------: | -----------: | ------: | ------------: |
| 4               |              0 |            0 |       4 |             4 |
| 3               |              4 |           40 |       3 |            43 |
| 2               |             43 |          430 |       2 |           432 |
| 1               |            432 |         4320 |       1 |          4321 |

---

## 🎤 Interview Explanation (Tanglish)

> **"Sir, `reverse * 10` use pannradhu existing reverse number-la irukkura digits-a one place left shift panna. Adhanala last-la oru empty place create aagum. Andha empty place-la current `digit`-a add pannuren. Example, `43 × 10 = 430`; `430 + 2 = 432`. Idhanala `reverse = reverse * 10 + digit` use pannrom."**

### 🔑 Easy Memory Trick

**Reverse build panna formula:**

```text
Old Reverse × 10 + New Digit = New Reverse
```

Example:

```text
0 × 10 + 4 = 4

4 × 10 + 3 = 43

43 × 10 + 2 = 432

432 × 10 + 1 = 4321
```

⭐ **Remember this one formula**:

> **"Multiply by 10 → Make space → Add the new digit."**

That's the easiest way to remember it during interviews.


# -------------------------------------------------------------------

# largest Three Numbers:


def largest(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c


a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

print("Largest Number:", largest(a, b, c))