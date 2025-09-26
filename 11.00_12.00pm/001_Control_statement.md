


# What Are Control Statements?


#__________________________________________________________________

#conditional Statements (Decision Making)


#`if`, `if-else`, `if-elif-else`

#Syntax:


if condition:
    # Code A
elif another_condition:
    # Code B
else:
    # Code C



#Example:


x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")




#__________________________________________________________________
#Looping Statements (Repetition)

# `for` Loop

Used to iterate over a sequence (list, tuple, string, range).

for i in range(5):
    print(i)




#__________________________________________________________________
# `while` Loop

Runs  as long as a condition is true.

count = 0
while count < 5:
    print(count)
    count += 1




#__________________________________________________________________

#Loop Control Statements

| Statement  | Purpose                              |
| ---------- | ------------------------------------ |
| `break`    | Exits the loop immediately           |
| `continue` | Skips to the next iteration          |
| `pass`     | Does nothing (used as a placeholder) |




## break Example:



for i in range(10):
    if i == 5:
        break
    print(i)


# continue 


for i in range(5):
    if i == 2:
        continue
    print(i)


# pass

for i in range(3):
    pass  # Placeholder
print("Loop finished")




#__________________________________________________________________

# Common Mistakes

* Indentation errors.
* Forgetting `:` after `if`, `for`, etc.
* Infinite loops in `while`.



Loop with enumerate() (index + value)
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)

Loop with zip()
names = ['Tom', 'Jerry']
scores = [90, 85]
for name, score in zip(names, scores):
    print(name, score)





#__________________________________________________________________


| Task                                | Loop Type Used     |
| ----------------------------------- | ------------------ |
| Reading files line by line          | `for`              |
| Validating login attempts           | `while`            |
| Generating reports for each student | `for` with `zip()` |
| Web scraping multiple pages         | `while` or `for`   |
| Game development (main loop)        | `while True:`      |





#__________________________________________________________________
#Practice Questions (Problem Solving Focused)

#Level 1: Basic

1. Write a program to check if a number is **even or odd**.
2. Take input from the user and check if it is **positive, negative or zero**.


3. Print the **first 10 natural numbers** using a `while` loop.
4. Find the **sum of all numbers from 1 to 100** using a `for` loop.
5. Print a **multiplication table** for a number using a loop.



#__________________________________________________________________


# Level 2: Intermediate

6. Print all **even numbers between 1 to 50** using `continue`.
7. Count the number of **vowels** in a string using `for` loop.
8. Write a program to **reverse a number** using a `while` loop.
9. Use `break` to stop the loop when a number divisible by 7 is found in a list.
10. Create a simple **menu-driven** program using `if-elif-else`.



#__________________________________________________________________


# Level 3: Advanced Logic

11. Print all **prime numbers** between 1 and 100.
12. Print a **pattern**:

*
**
***
****


13. Check if a number is **Armstrong** or not (e.g., 153 = 1³ + 5³ + 3³).
14. Write a program to find the **factorial** of a number.
15. Write a program to print the **Fibonacci series** up to n terms.


#__________________________________________________________________


# Challenge Set – Problem Solving Drill

Try solving these without looking at the solution:

1. **FizzBuzz**: Print numbers 1 to 50. If divisible by 3 print "Fizz", by 5 print "Buzz", by both print "FizzBuzz".
2. Find the **greatest of three numbers** using `if-else`.
3. Given a list, print all numbers **greater than average** of the list.
4. Create a **login system** using `if` to check username and password.
5. Count **words and characters** in a string (excluding spaces).


#__________________________________________________________________

#Tips to Boost Problem Solving with Control Statements

* Break big problems into smaller conditions.
* Draw flowcharts or write pseudocode.
* Use `print()` for debugging inside loops and conditions.
* Use `range()`, `len()`, `enumerate()` effectively in loops.


#__________________________________________________________________




Mini Project Challenges

1. Student Grade Tracker
Input marks for 5 subjects

Calculate total, average

Use loops to validate inputs


#__________________________________________________________________


2. ATM Simulation
Menu using while True

Options: check balance, withdraw, deposit, exit

Use if-elif and loops





#__________________________________________________________________

3. Simple Quiz App
Use a loop to ask 5 questions

Track correct answers

Display result at the end




#__________________________________________________________________



# | Expression     | Meaning                         |
# | -------------- | ------------------------------- |
# | `number % 10`  | Gets the **last digit** (units) |
# | `number // 10` | Removes the last digit          |




#**********************************************************************************************

#________________________________________________________________________________________________
             #conditional Statements 1
#_______________________________________________________________________________________


# **If-Else Based Questions (Basic Logic)**

1. **Even or Odd Number**
   Input a number and print whether it is **even** or **odd**.

2. **Positive, Negative, or Zero**
   Check whether a number is **positive**, **negative**, or **zero**.

3. **Check for Leap Year**
   Given a year, check if it is a **leap year**.

4. **Check Voting Eligibility**
   Ask for age and check if the person is **eligible to vote** (age ≥ 18).

5. **Check Divisibility by 5 and 11**
   Print whether a number is divisible by **both 5 and 11**, only one, or neither.

6. **Find Maximum of Two Numbers**
   Input two numbers and print the **greater** one.

7. **Character is Vowel or Consonant**
   Check whether an entered character is a **vowel** or **consonant**.



#________________________________________________________________________________________________
             #conditional Statements 2
#_______________________________________________________________________________________




##*Elif-Based Questions (Multiple Conditions)**

8. **Grade Calculator**
   Input marks and print grade:

   * 90–100 → A
   * 80–89 → B
   * 70–79 → C
   * 60–69 → D
   * Below 60 → F

9. **Day of the Week**
   Input number 1–7 and print the corresponding **weekday**.

10. **Traffic Light System**
    Input a color (`red`, `yellow`, `green`) and display the action (Stop / Wait / Go).

11. **Month Days Checker**
    Input month number and return number of **days** (assume non-leap year).

12. **Number is Positive, Negative or Zero using Elif**
    Use `elif` instead of nested `if-else`.

13. **Check for Triangle Type**
    Input three sides and determine whether the triangle is:

* Equilateral
* Isosceles
* Scalene

14. **Simple Calculator**
    Input two numbers and an operator (`+`, `-`, `*`, `/`) and perform calculation using `elif`.

15. **Check Eligibility for Loan**
    Input age, income, and credit score. Based on conditions, print whether the person is **eligible** or **not eligible** for a loan.




#________________________________________________________________________________________________


#________________________________________________________________________________________________
             #while loop 1
#_______________________________________________________________________________________


### 🟢 **While Loop – Problem Solving Questions**

1. **Print Numbers from 1 to N**
   Input a number `n`, and print numbers from **1 to n** using a `while` loop.

2. **Sum of First N Natural Numbers**
   Input `n`, and find the **sum from 1 to n** using a `while` loop.

3. **Reverse a Number**
   Input a number like `1234`, and output `4321`.

4. **Count Digits in a Number**
   Input a number and count how many digits it has using a loop.

5. **Check Palindrome Number**
   Input a number (e.g., `121`) and check if it reads the same forward and backward.

6. **Find the Factorial of a Number**
   Input `n`, and find `n!` using a `while` loop.

7. **Print All Even Numbers Between 1 and N**
   Print only even numbers from 1 to a given number `n`.

8. **Sum of Digits of a Number**
   Input a number and find the **sum of its digits** using a `while` loop.

9. **Check Armstrong Number**
   A number is Armstrong if the sum of its own digits raised to the power of the number of digits equals the number (e.g., 153 → 1³ + 5³ + 3³ = 153).

10. **Generate Multiplication Table of a Number**
    Input a number, and print its **multiplication table up to 10** using `while`.

#________________________________________________________________________________________________


#________________________________________________________________________________________________
             #while loop 2
#_______________________________________________________________________________________



### 🟡 **While Loop – Additional Questions (11–20)**

11. **Find GCD of Two Numbers**
    Input two numbers and find their **Greatest Common Divisor (GCD)** using a `while` loop.

12. **Check Prime Number**
    Input a number and check if it's **prime** using a `while` loop.

13. **Print Fibonacci Series (First N Terms)**
    Generate the Fibonacci sequence up to `n` terms using a `while` loop.

14. **Number Guessing Game**
    Let the computer have a fixed number. Ask user to guess the number until they get it right. Use `while`.

15. **Menu-Driven Calculator**
    Repeatedly show options (`add`, `subtract`, etc.) until the user exits using a `while` loop.

16. **Find Power (a^b) Without Using `**`**
    Input `a` and `b`, and compute `a^b` using repeated multiplication inside a `while` loop.

17. **Print Digits Separately in Reverse**
    Input a number (e.g., `5623`) → Output: `3 2 6 5`

18. **Remove All Zeros from a Number**
    Input a number like `105020` and output `152`.

19. **Check if a Number is a Perfect Number**
    A number is perfect if the sum of its proper divisors equals the number (e.g., 28 → 1 + 2 + 4 + 7 + 14 = 28).

20. **Binary to Decimal Conversion**
    Input a binary number (e.g., `1011`) and convert it to decimal using a `while` loop.



#________________________________________________________________________________________________
             #for loop 1
#_______________________________________________________________________________________


#_____________________________________________________________________________



Print the Fibonacci sequence up to n terms.

Print a right-angled triangle pattern using * of n rows.

Count digits, letters, and special characters in a string.

Find the largest number in a list using for loop.

Reverse the digits of a number using for loop.

Print all prime numbers between 1 and 100.

Print a diamond pattern using * with an odd number of rows.

Check if a string is a palindrome using a for loop.

Sum the digits of a number using for loop.

Print numbers from 1 to 100 that are divisible by both 3 and 5





#_____________________________________________________________________________



Print the ASCII value of each character in a string using a for loop.

Generate a list of all palindromic numbers between 100 and 200.

Print a pattern like this for n = 5:


1
12
123
1234
12345



Create a dictionary from two lists (keys and values) using a for loop.

Print all numbers between 1 and 100 that are perfect squares.

Find the common elements in two lists using for loop.

Print the cumulative sum of a list: [1, 2, 3, 4] → Output: [1, 3, 6, 10]

Check if a number is an Armstrong number using for loop.

Print the frequency of each character in a string using a for loop.

Print numbers from 1 to 50, but skip multiples of 7.



#__________________________________________________________________________________


1. Print a right-angled triangle pattern using * of n rows

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print('*' * i)



#__________________________________________________________________________________


2. Count digits, letters, and special characters in a string

text = input("Enter a string: ")
digits = 0
letters = 0
special = 0

for char in text:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
    else:
        special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special Characters:", special)


#__________________________________________________________________________________


3. Find the largest number in a list using for loop

numbers = [12, 45, 23, 89, 77, 34]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("The largest number is:", max_num)



#__________________________________________________________________________________


 1. Create a dictionary from two lists (keys and values) using a for loop

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print(my_dict)



#__________________________________________________________________________________


2. Print all numbers between 1 and 100 that are perfect squares

print("Perfect squares between 1 and 100:")
for i in range(1, 101):
    if int(i ** 0.5) ** 2 == i:
        print(i, end=' ')




#__________________________________________________________________________________


3. Find the common elements in two lists using for loop

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []

for item in list1:
    if item in list2:
        common.append(item)

print("Common elements:", common)


#__________________________________________________________________________________

 1. Check if a number is an Armstrong number using for loop

num = int(input("Enter a number: "))
num_str = str(num)
power = len(num_str)
sum_of_powers = 0

for digit in num_str:
    sum_of_powers += int(digit) ** power

if sum_of_powers == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is NOT an Armstrong number.")



#__________________________________________________________________________________


 2. Print the frequency of each character in a string using a for loop


 text = input("Enter a string: ")
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character frequencies:")
for k, v in freq.items():
    print(f"{k} : {v}")



#__________________________________________________________________________________




## **1. Print the ASCII value of each character in a string using a for loop**




text = input("Enter a string: ")

for char in text:
    print(f"Character: {char} → ASCII: {ord(char)}")


**Example Input**: `Hi!`
**Output**:

```
Character: H → ASCII: 72  
Character: i → ASCII: 105  
Character: ! → ASCII: 33  
```

#_______________________________________________________________________________________________

## **2. Generate a list of all palindromic numbers between 100 and 200**


palindromes = []

for i in range(100, 201):
    if str(i) == str(i)[::-1]:
        palindromes.append(i)

print("Palindromic numbers between 100 and 200:", palindromes)




**Output**:

```
Palindromic numbers between 100 and 200: [101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
```

---______________________________________________________________________________________________

###*3. Print a pattern like this for `n = 5`:**

```
1
12
123
1234
12345
```


n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()  # New line after each row
```

#___________________________________________________________________________________________

Here are **different star (`*`) pattern programs** in Python, organized by type (with code and output):

---

### ⭐ 1. **Right-Angled Triangle**

```python
n = 5
for i in range(1, n+1):
    print('*' * i)
```

**Output:**

```
*
**
***
****
*****
```

---

### ⭐ 2. **Inverted Right-Angled Triangle**

```python
n = 5
for i in range(n, 0, -1):
    print('*' * i)
```

**Output:**

```
*****
****
***
**
*
```

---

### ⭐ 3. **Right-Aligned Triangle**

```python
n = 5
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * i)
```

**Output:**

```
    *
   **
  ***
 ****
*****
```

---

### ⭐ 4. **Pyramid Pattern**

```python
n = 5
for i in range(1, n+1):

                   4 + "*" 2*0=0==>*
                   3+"*"2*1=2===>**



    print(' ' * (n - i) + '*' * (2 * i - 1))
```

**Output:**

```
    *
   ***
  *****
 *******
*********
```

---

### ⭐ 5. **Inverted Pyramid**

```python
n = 5
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
```

**Output:**

```
*********
 *******
  *****
   ***
    *
```

---

### ⭐ 6. **Diamond Pattern**

```python
n = 5
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * (2*i - 1))
for i in range(n-1, 0, -1):
    print(' ' * (n - i) + '*' * (2*i - 1))
```

**Output:**

```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

---

### ⭐ 7. **Square Pattern**

```python
n = 5
for i in range(n):
    print('* ' * n)
```

**Output:**

```
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
```

---

### ⭐ 8. **Hollow Square**

```python
n = 5
for i in range(n):
      
       
       4==0      4==4
       3==0      3==4
       2==0      2==4
       1==0      1==4
       0==0      0==4
    if i == 0 or i == n - 1:
        print('* ' * n)
    else:
        print('*' + '  ' * (n - 2) + ' *')
```

**Output:**

```
* * * * * 
*       *
*       *
*       *
* * * * * 
```

---

### ⭐ 9. **Right-Aligned Hollow Triangle**

```python
n = 5
for i in range(1, n+1):
    if i == 1 or i == n:
        print(' ' * (n - i) + '*' * i)
    else:
        print(' ' * (n - i) + '*' + ' ' * (i - 2) + '*')
```

**Output:**

```
    *
   **
  * *
 *  *
*****
```

---

### ⭐ 10. **Hourglass Pattern**

```python
n = 5
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2*i - 1))
for i in range(2, n+1):
    print(' ' * (n - i) + '*' * (2*i - 1))
```

**Output:**

```
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
```

---

Would you like **interactive input support**, or star patterns using **numbers or alphabets** instead?






If you want to teach this concept to students, it’s best to break it down step-by-step so they understand **what’s happening in the loop** and **why the pattern is printed that way**, instead of just memorizing code.

Here’s a good teaching flow:

---

## **1. Start with the problem**

Write the desired output on the board:

```
*****
****
***
**
*
```

Ask students:
*"What do you notice about this pattern?"*

* Number of stars decreases each line
* First row has `n` stars, last row has 1 star

---

## **2. Explain the loop idea**

Tell them:

* Loops help repeat actions.
* We’ll use a loop to print stars multiple times, changing the count each time.

Show them how **range works** in reverse:

```python
range(n, 0, -1)
```

* **start = n** → begins at 5
* **stop = 0** → ends before 0
* **step = -1** → decreases by 1 each time

Write it out:

```
i = 5, 4, 3, 2, 1
```

---

## **3. Show how `'*' * i` works**

Before putting it in a loop, demonstrate:

```python
print('*' * 5)  # *****
print('*' * 4)  # ****
print('*' * 3)  # ***
```

Students see that multiplying a string by a number repeats it.

---

## **4. Combine loop and repetition**

Now put it together:

```python
n = 5
for i in range(n, 0, -1):
    print('*' * i)
```

Explain:

* `i` starts at 5, prints 5 stars
* `i` becomes 4, prints 4 stars
* Continues until `i = 1`

---

## **5. Add visual tracing**

Draw a **table** for loop execution:

| Iteration | i | Output     |
| --------- | - | ---------- |
| 1         | 5 | \*\*\*\*\* |
| 2         | 4 | \*\*\*\*   |
| 3         | 3 | \*\*\*     |
| 4         | 2 | \*\*       |
| 5         | 1 | \*         |

This helps them see the pattern formation.

---

## **6. Encourage experiments**

Let them try:

* Increasing pattern (`range(1, n+1)`)
* Different symbols (`'#' * i`)
* n from user input

---

If you want, I can make a **step-by-step animated diagram** showing how this code executes in memory so students can “see” the loop working. That makes this concept click much faster.



#list comprehension

Create a list of all even numbers between 1 and 20.
Given a list of words, extract only the words with more than 3 letters.


#Generator Expression (tuple comprehension)

Create a tuple of cubes of numbers from 1 to 5.
Convert all words in a list to uppercase and store them in a tuple.


#set comprehension

Get the unique letters from the word `"programming"`.
Create a set of squares for numbers between 1 and 10 that are divisible by 3.


#dictionary comprehension

Create a dictionary where the keys are numbers from 1 to 5 and the values are their squares.
Given a dictionary of students and their marks, create a new dictionary with only students who scored more than 50.