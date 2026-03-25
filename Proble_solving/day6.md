

# __________________________________________________________________
## 🟢 **Day 6 – Palindrome + Revision**
# __________________________________________________________________

### ⏱ Learn

* Palindrome logic
* Two-pointer on strings

### 🧠 Problems

1. Palindrome string
2. Palindrome number
3. Valid palindrome *(ignore case/symbols)*

🎯 **Pattern:** Two pointers (again!)



# __________________________________________________________________
Problem 1: Palindrome String
# __________________________________________________________________

Question:
Check if a given string is a palindrome. A string is a palindrome if it reads the same forwards and backwards.

Input: "level"
Output: True

Input: "hello"
Output: False

# __________________________________________________________________
# method1
# __________________________________________________________________

def is_palindrome_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Test
print(is_palindrome_string("level"))  # True
print(is_palindrome_string("hello"))  # False

# __________________________________________________________________
# Method 2
# __________________________________________________________________
def palindrom_check(s):
    if s==s[::-1]:
        return "True"
    return "False"
    
    
print(palindrom_check("welcome"))




# __________________________________________________________________
Problem 2: Palindrome Number

Question:
Check if a given integer is a palindrome without converting it to a string.
# __________________________________________________________________
Input: 121
Output: True

Input: 123
Output: False


def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False  # Negative numbers are not palindrome

    original = x
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10

    return original == reversed_num

# Test
print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False



| Expression | Result | Reason                    |
| ---------- | ------ | ------------------------- |
| `5 % 10`   | `5`    | 5 < 10, so remainder is 5 |
| `9 % 10`   | `9`    | Same reason               |
| `10 % 10`  | `0`    | Exact division            |
| `15 % 10`  | `5`    | Last digit                |
| `123 % 10` | `3`    | Last digit                |

Any number less than 10 % 10 = same number
“n % 10 always return last digit of the number.




Seri 👍
**Tanglish-la super simple-aa explain panren**, especially **intha line** 👇

```python
reversed_num = reversed_num * 10 + digit
```

---

## 🧠 Context first

Nama **number reverse** panrom.
Example:

```
x = 123
reversed_num = 0
```

---

## 🔹 `digit = x % 10`

👉 Last digit eduka

```
123 % 10 = 3
```

So:

```
digit = 3
```

---

## ⭐ MAIN LINE (neenga ketadhu)

```python
reversed_num = reversed_num * 10 + digit
```

### 🤔 En `* 10` panrom?

👉 **Already iruka number-a left side-ku move panna**

---

## 🧪 Step by step example

### 🔸 First time

```
reversed_num = 0
digit = 3
```

Calculation:

```
0 * 10 + 3 = 3
```

👉 ippo `reversed_num = 3`

---

### 🔸 Second time

Now:

```
digit = 2
reversed_num = 3
```

Calculation:

```
3 * 10 = 30
30 + 2 = 32
```

👉 `reversed_num = 32`

---

### 🔸 Third time

```
digit = 1
reversed_num = 32
```

Calculation:

```
32 * 10 = 320
320 + 1 = 321
```

👉 `reversed_num = 321`

---

## 🔹 `x //= 10`

👉 Last digit remove panna

```
123 // 10 = 12
12 // 10 = 1
1 // 10 = 0
```

---

## 📊 Full dry run (123)

| x   | digit | reversed_num |
| --- | ----- | ------------ |
| 123 | 3     | 3            |
| 12  | 2     | 32           |
| 1   | 1     | 321          |
| 0   | stop  |              |

---

## 🧠 Simple memory trick (Tanglish)

* `% 10` → **last digit eduka**
* `* 10` → **number-a left-ku shift panna**
* `+ digit` → **pudhu digit add panna**
* `// 10` → **last digit remove panna**

---

## 🗣 Interview-ku easy explanation (Tanglish)

> “Modulo use panni last digit eduthu, reversed number-a multiply by 10 panni left shift panni, andha digit-a add panren.”

---

Venuma:

* Idha **diagram-oda explain**
* **Student practice questions**
* Same concept **string use pannama** optimize version

Sollunga 👍

# __________________________________________________________________