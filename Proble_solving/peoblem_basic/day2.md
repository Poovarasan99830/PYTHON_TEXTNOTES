
# -----------------------------------------------------


Approach 1: Using Dictionary (Interview Friendly ⭐)Logic

<!-- 
Empty dictionary create pannunga.
String-la irukkura ovvoru character-a loop pannunga.
Character already dictionary-la irundha count increase pannunga.
Illana count = 1 assign pannunga.
Finally dictionary print pannunga. -->

<!-- * Character Frequency -->


def character_frequency(text):

    frequency = {}

    for char in text:

        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


text = input("Enter String: ")

print(character_frequency(text))


<!-- Approach 3: Using collections.Counter -->


from collections import Counter

frequency = Counter(text)

<!-- Time Complexity O(n),
Space Complexity O(k), -->






# -----------------------------------------------------



<!-- Approach 1: Using for Loop (Interview Friendly ⭐) -->

<!-- Count variable 0-la initialize pannunga.
String-la irukkura ovvoru character-a loop pannunga.
Character vowel-aa irukka check pannunga.
Vowel-na count increase pannunga.
Finally count print pannunga. -->

<!-- 
def count_vowels(text):

    count = 0

    vowels = "aeiouAEIOU"

    for char in text:

        if char in vowels:
            count += 1

    return count


text = input("Enter String: ")

print("Vowels =", count_vowels(text)) -->

Time Complexity:O(n)
String-la irukkura ovvoru character-a oru thadavai mattum check pannrom.

O(1) --->variables use pannrom.



<!-- Approach 3: Using List Comprehension -->







Why is this called a Generator?

<!-- Generator-na, values-a ellathayum ore time-la memory-la store pannaadhu. Thevaipadumbodhu (on demand) oru value mattum generate pannum. -->



<!-- [1 for x in data]   # List (stores all)

(1 for x in data)   # Generator (one by one)

sum(1 for x in data)  # Generator expression passed directly to sum() -->



<!-- st ([]) → "First store everything, then use." -->
<!-- Generator (()) → "Create one item, use it immediately, then create the next." -->
<!--  -->

<!-- | Generator Function                   | Generator Expression                      |
| ------------------------------------ | ----------------------------------------- |
| Uses `yield`                         | Uses `()`                                 |
| Defined using `def`                  | Defined in one line                       |
| Can have multiple `yield` statements | Generates values from a single expression |
| Best for complex logic               | Best for simple logic                     |
| More readable for large code         | Short and concise                         |
| Memory Efficient                     | Memory Efficient                          | -->

<!-- When to Use Which? -->

<!-- Generator Function

Use when

Multiple statements
Loops
Conditions
Business Logic -->


<!-- 

Generator Expression

Use when

Simple calculation. -->

Time Complexity-->o(n)
Space Complexity--->o(1)


<!-- One-line memory rule:"List stores everything first; Generator produces one item at a time." -->

<!-- What is Lazy Evaluation?
Interview Definition

Lazy Evaluation means values are not computed immediately. They are computed only when they are needed. -->
<!-- 
"Sir, Lazy Evaluation-na, values-a immediately calculate pannaama, thevai irukkumbodhu mattum calculate pannradhu. Generators idha use pannum. next() call pannumbodhu dhaan adutha value generate pannum. Idhanala memory save aagum and large datasets efficient-aa process panna mudiyum." -->

<!-- "Lazy Evaluation = Calculate only when needed, not before." 🚀 -->


# -----------------------------------------

<!-- * Remove Duplicates -->


# part1

numbers = [1, 2, 2, 3, 4, 4, 5]

result = []
seen = set()

for num in numbers:
    if num not in seen:
        result.append(num)
        seen.add(num)

print(result)

# -----------------------------------------

# part2

numbers = [1, 2, 2, 3, 4, 4]

result = dict.fromkeys(numbers)

print(result)


# Time = O(n)

# -----------------------------------------


<!-- * Anagram -->


from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

print(is_anagram("listen", "silent"))






def is_anagram(s1, s2):

    if len(s1) != len(s2):
        return False

    frequency = {}

    for char in s1:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    for char in s2:
        if char not in frequency:
            return False

        frequency[char] -= 1

    for count in frequency.values():
        if count != 0:
            return False

    return True


print(is_anagram("listen", "silent"))


So frequency dictionary is a natural data structure.

Time: O(n) average
Space: O(k) where k = distinct characters.

# -----------------------------------------



<!-- * First Non-Repeating Character -->

def first_non_repeating(text):

    frequency = {}

    # Count frequency
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    # Find first character with count 1
    for char in text:
        if frequency[char] == 1:
            return char

    return None


print(first_non_repeating("swiss"))



# -------------------------
Complexity

Time: O(n)

Two loops irundhaalum:

O(n) + O(n) = O(2n) = O(n)

Space: O(k)

k = distinct characters.

# -----------------------------------------


<!-- Longest Word -->

def longest_word(sentence):

    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


print(longest_word("I love Python programming"))


<!-- I use a linear traversal approach. I split the sentence into words and maintain the longest word found so far.
For each word, I compare its length with the current longest word and update it if necessary. 
This gives O(n) time complexity. -->


Complexity

If there are n words:

Time: O(n) — every word is checked once.

Space: O(n) because split() creates a list of words.

# -----------------------------------------

<!-- * String Compression -->

def compress_string(text):

    if not text:
        return ""
 
                   4
            3      3
            2   2  2
    count = 1   1  1



  
    for i in range(1, len(text)):


              c           
              c           c
              c           c
              c           c
              c           b
              b           b
              b           a
              a           a
              a           a                         
        if text[i] == text[i - 1]:
            count += 1
                                 b         2
        else:                    a         3
            result.append(text[i - 1] + str(count))
            count = 1

    result.append(text[-1] + str(count))

    return "".join(result)


print(compress_string("aaabbcccc"))


# -----------------------------------------

<!-- * Check Rotation -->


def check_rotation(s1, s2):

    if len(s1) != len(s2):
        return False

    return s2 in (s1 + s1)


print(check_rotation("abcd", "cdab"))


# -----------------------------------------



def remove_special_characters(text):

    result = []

    for char in text:
        if char.isalnum():
            result.append(char)

    return "".join(result)





<!-- * Remove Special Characters -->


Why is this better?

list.append() is O(1) amortized.

Then:

"".join(result)

combines everything efficiently in one operation.

So overall:

Time: O(n)
Space: O(n)

# -----------------------------------------