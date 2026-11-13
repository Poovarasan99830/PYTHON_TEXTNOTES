



PART 1 ✅ Python Data Structures
       ↓
PART 2 🔥 Functions
       ↓
PART 3 🔥 OOP
       ↓
PART 4 🔥 Exception Handling
       ↓
PART 5 🔥 Decorators / Generators
       ↓
PART 6 🔥 API + FastAPI
       ↓
PART 7 🔥 PostgreSQL + SQL
       ↓
PART 8 🔥 PyTest + BDD
       ↓
PART 9 🔥 Git + CI/CD
       ↓
PART 10 🔥 Docker + Kubernetes + Linux
       ↓
PART 11 🔥 Kafka + REST + gRPC
       ↓
PART 12 🔥 Networking + Security
       ↓
PART 13 🔥 YOUR PROJECT
       ↓
PART 14 🔥 SES JD-based Mock Interview





# --------------------------PART 1-------------------------------------

# Difference between List VS tuple VS set VS Dictionary


| Feature      | List       | Tuple          | Set               | Dictionary        |
| ------------ | ---------- | -------------- | ----------------- | ----------------- |
| Ordered      | Yes        | Yes            | No indexing       | Yes*              |
| Mutable      | Yes        | No             | Yes               | Yes               |
| Duplicates   | Yes        | Yes            | No                | Keys no           |
| Indexing     | Yes        | Yes            | No                | By key            |
| Main purpose | Sequence   | Fixed sequence | Unique values     | Key-value mapping |
| Lookup       | O(n)       | O(n)           | O(1) avg          | O(1) avg          |
| Common use   | Collection | Fixed data     | Membership/unique | Structured data   |


# --------------
# list
# --------------

  mutable, ordered collection
  List ordered Because each element has a position/index.
  Python lists are implemented as dynamic arrays
  use -->Multiple items + order maintain + modify
  
  Dynamic array = size can grow
  Index access = O(1)
  Append = O(1) amortized
  Resize = can be O(n)
  Search by value = O(n)




# --------------
# set
# --------------
   → Uniqueness + fast membership checkingO(1) uses hashing.
   → No indexing
   →it is not a sequence-based data structure or unordered collection.
   use -->Unique values + fast membership checking


   A set does not support indexing because it is not a sequence-based data structure. It is designed around uniqueness and hash-based membership lookup rather than positional access.

SET
→ Mutable ✅
→ Unique values ✅
→ No indexing ❌
→ Hash-based membership ✅
→ Hashable ❌
→ Dictionary key ❌



SET
 ↓
Mutable
 ↓
Cannot be dictionary key


FROZENSET
 ↓
Immutable
 ↓
Hashable
 ↓
Can be dictionary key




# ------
# tuple
# -----

Ordered
Immutable
Allows duplicates
Supports indexing


# ----------------
# dictionary:

# ----------------

What is Hash Collision?
   A hash collision occurs when two different keys or objects produce the same hash value.




Key A = "CLM101"
Key B = "CLM205"

       ↓ hash()

Key A → 500
Key B → 500

# ------------------------------------------



LIST
→ Order + modification
→ list[index] = O(1)
→ value search = O(n)
→ append = O(1) amortized

DICTIONARY
→ Key → Value
→ Meaningful key
→ Lookup = O(1) average

SET
→ Unique values
→ Membership checking
→ O(1) average

TUPLE
→ Fixed/unchanged data
→ Ordered
→ Immutable







# --------------------------PART 2-------------------------------------
# NEXT PREPARATION PART: Python Functions + OOP



# --------------------------
# What is a Decorator?
A decorator is a function that takes another function as input, adds or modifies its behavior, and returns a new function without changing the original function's source code.



# Why use Decorator?
I use decorators when I need to add common cross-cutting behavior such as authentication, logging, authorization or execution-time measurement without modifying the original function.



# --------------------------
# What is Generator?

A generator is a function that produces values one at a time using the yield keyword instead of returning all values at once.



# --------------------------

# What is a closure in Python?"

Say:

"A closure is a function that retains access to variables from its enclosing scope even after the enclosing function has completed execution. It is useful for maintaining state and creating functions with preserved context. Decorators are a common example where closures are used."

Tanglish:

"Closure-na inner function, enclosing function-oda variables-a remember panni access pannum, even outer function execution complete aana piragum. Closures mainly state preserve panna and context maintain panna useful. Decorators-la closure concept commonly use aagum."

State = current information/value
Preserve state = remember that information for later use.

# --------------------------