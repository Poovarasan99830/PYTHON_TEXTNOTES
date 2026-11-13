#______________________________________________________________________



𝟙. What is a String in Python?

A string is a sequence of characters enclosed in:

Single quotes 'Hello'

Double quotes "Hello"

Triple quotes '''Hello''' or """Hello""" (used for multi-line strings or docstrings)


#________________________________________________________


𝟚. String Properties

| Property         | Description                         |
| ---------------- | ----------------------------------- |
| Immutable        | Once created, it cannot be changed  |
| Iterable         | You can loop through each character |
| Indexed          | Characters are accessed using index |
| Ordered          | Keeps the order of characters       |
| Supports slicing | You can extract substrings          |



#________________________________________________________

𝟛. Escape Characters

| Escape | Meaning      | Example             |
| ------ | ------------ | ------------------- |
| `\n`   | New line     | `"Hello\nWorld"`    |
| `\t`   | Tab          | `"Name:\tJohn"`     |
| `\'`   | Single quote | `'It\'s nice'`      |
| `\"`   | Double quote | `"She said \"Hi\""` |
| `\\`   | Backslash    | `"C:\\path"`        |


#________________________________________________________


 𝟜. String Indexing and Slicing
 
What is a String in Python?
     A string is a sequence of characters, and like all sequences in Python, it supports:
     Indexing (accessing individual characters)
     Slicing (extracting substrings)


string[start:stop:step]
start: index to start from (inclusive)
stop: index to stop before (exclusive)
step: jump size (default is 1)


Forward Index :  0   1   2   3   4   5
                +---+---+---+---+---+---+
Characters     | P | Y | T | H | O | N |
                +---+---+---+---+---+---+
Backward Index : -6 -5  -4  -3  -2  -1



| Operation    | Example   | Result     |
| ------------ | --------- | ---------- |
| Single char  | `s[0]`    | `'P'`      |
| Substring    | `s[1:4]`  | `'YTH'`    |
| From start   | `s[:3]`   | `'PYT'`    |
| To end       | `s[2:]`   | `'THON'`   |
| Step slicing | `s[::2]`  | `'PTO'`    |
| Reverse      | `s[::-1]` | `'NOHTYP'` |

#________________________________________________________

𝟝. String Methods (Most Common)


 | Method                       | Use Case                       |
| ---------------------------- | ------------------------------ |
<!-- | `upper()`, `lower()`         | Convert case                   |
| `capitalize()`, `title()`    | Capitalize words               |
| `strip()`                    | Remove leading/trailing spaces | -->


| `replace(old, new)`          | Replace substring              |

| `split(separator)`           | Split string into a list       |

| `join(iterable)`             | Join list into a string        |

| `find(sub)`                  | Find first index of substring  |

| `count(sub)`                 | Count occurrences              |

| `startswith()`, `endswith()` | Check start/end of string      |

| `isalpha()`, `isdigit()`     | Validation                     |



#________________________________________________________


𝟞. String Formatting

% Operator (Old style)
.format() Method
f-Strings (Python 3.6+)




#________________________________________________________

𝟟. String Comparison and Identity

𝟠. Iterating Over a String



#_______________________________________________________

𝟡. Real-world Examples
    Count vowels in a string
    Palindrome check



#________________________________________________________


🔟 Practice Questions


Reverse a string without using slicing.

Count number of digits in a string.

Replace all spaces in a string with hyphens.

Write a function to count uppercase and lowercase letters.

Create a function to check if a string is an anagram.



#____________________________________________________________________

#task:



1. **Reverse the string using slicing.**
   Input: `"hello"` → Output: `"olleh"`

2. **Check if a string is a palindrome.**
   Input: `"madam"` → Output: `True`

3. **Replace all vowels with `*` using string methods only.**
   Input: `"apple"` → Output: `"*ppl*"`

4. **Return the first 3 and last 3 characters concatenated.**
   Input: `"abcdefg"` → Output: `"abcefg"`




5. **Check if a string starts and ends with the same character.**
   Input: `"radar"` → Output: `True`

6. **Remove all spaces from a string and convert it to lowercase.**
   Input: `" Hello World "` → Output: `"helloworld"`

7. **Repeat a string 3 times using the `*` operator.**
   Input: `"abc"` → Output: `"abcabcabc"`

8. **Swap the first and last characters of the string.**
   Input: `"python"` → Output: `"nythop"`

9. **Extract the middle character (assume odd length).**
   Input: `"apple"` → Output: `"p"`

10. **Check if the string contains only digits using a string method.**
    Input: `"12345"` → Output: `True`
    Input: `"12a45"` → Output: `False`


#________________________________________________________

| Topic      | Summary                            |
| ---------- | ---------------------------------- |
| Creation   | `'abc'`, `"abc"`, `'''abc'''`      |
| Immutable  | Strings cannot be changed in-place |
| Indexing   | `s[0]`, `s[-1]`                    |
| Slicing    | `s[1:4]`, `s[::-1]`                |
| Methods    | `upper()`, `split()`, `replace()`  |
| Formatting | `%`, `.format()`, `f-strings`      |



#__________________________________________________________________
 ______________________   STRING ALGORITHMS _______________________
#__________________________________________________________________

#prat2


 1. Basic String Algorithms

 a. String Reversal
 b. Palindrome Check
 c. Anagram Check


2. Pattern Matching Algorithms

a. Naive Pattern Search
b. KMP (Knuth-Morris-Pratt) Algorithm




3. String Compression (Run-Length Encoding)
4. Longest Common Substring / Subsequence
a. Longest Common Subsequence (DP)



1. Longest Substring Without Repeating Characters
2. Rabin-Karp Pattern Matching
3. Manacher's Algorithm (Longest Palindromic Substring in O(n))
4. Edit Distance (Levenshtein Distance)
5. Z-Algorithm (for Pattern Matching and Substring Search)


| Algorithm                    | Time Complexity | Purpose                             |
| ---------------------------- | --------------- | ----------------------------------- |
| Longest Substring w/o Repeat | O(n)            | Find length of unique substring     |
| Rabin-Karp                   | O(n+m) average  | Pattern search using hashing        |
| Manacher’s Algorithm         | O(n)            | Longest palindromic substring       |
| Edit Distance (DP)           | O(m×n)          | Minimum edits to convert one string |
| Z-algorithm                  | O(n)            | Fast pattern search                 |






#__________________________________________________________________
 ______________________   STRING PROBLEM SOLVING SKILLS __________
#__________________________________________________________________




Definition of Anagram:
Two strings are anagrams if they contain the same characters with the same frequency, but possibly in a different order.




🔁 Example:
"listen" and "silent" → ✅ Anagrams

"triangle" and "integral" → ✅ Anagrams

"hello" and "world" → ❌ Not Anagrams





s1 = "listen"
s2 = "silent"



count = {'l':1, 'i':1, 's':1, 't':1, 'e':1, 'n':1}



| char | count\[char] before | Action | count\[char] after |
| ---- | ------------------- | ------ | ------------------ |
| s    | 1                   | -1     | 0                  |
| i    | 1                   | -1     | 0                  |
| l    | 1                   | -1     | 0                  |
| e    | 1                   | -1     | 0                  |
| n    | 1                   | -1     | 0                  |
| t    | 1                   | -1     | 0                  |



| Line                                          | Meaning                                  |
| --------------------------------------------- | ---------------------------------------- |
| `if char not in count or count[char] == 0:`   | Check for invalid or overused characters |
| `count[char] -= 1`                            | Use up a matched character               |
| `all(value == 0 for value in count.values())` | Confirm perfect match                    |



#_______________________________________________________________________________

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}

    for char in s1:
        count[char] = count.get(char, 0) + 1

    for char in s2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return all(value == 0 for value in count.values())

# Simulated login
actual_password = "silent"
input_password = input("Enter your password (anagram-based): ")

if is_anagram(actual_password, input_password):
    print("✅ Login successful! You entered a valid anagram.")
else:
    print("❌ Login failed! Incorrect password or not an anagram.")




Enter your password (anagram-based): listen
✅ Login successful! You entered a valid anagram.




#_______________________________________________________________________________

✅ What is a Palindrome?
A palindrome is a word, phrase, or number that reads the same forward and backward.




Examples:
✅ "madam" → Palindrome

✅ "racecar" → Palindrome

❌ "hello" → Not a palindrome


Method 1: Using String Slicing


def is_palindrome(s):
    return s == s[::-1]

# Test
word = input("Enter a word: ")
if is_palindrome(word):
    print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")


#______________________________________________________________________________

Method 2: Using a Loop

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


#_______________________________________________________________________________


Method 3: Ignore Case and Spaces

def is_clean_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())  # Remove non-alphanumeric, make lowercase
    return s == s[::-1]

# Test
text = input("Enter a sentence: ")
if is_clean_palindrome(text):
    print("✅ It's a clean palindrome!")
else:
    print("❌ Not a clean palindrome.")



#_________________________________END________________________________________