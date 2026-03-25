# __________________________________________________________________
## 🟢 **Day 8 – HashMap Target Problems**
# __________________________________________________________________

### ⏱ Learn

* Complement logic
* HashMap lookup
* Target pattern


### Problems

1️⃣ **Two Sum**
2️⃣ **Two Sum (return numbers)**
3️⃣ **Find pair with given sum**


🎯 **Pattern:**
`target - current number`

# _________________________________________________

Future la complement number vandha,
previously store pannina current number oda index um,
current complement number oda index um answer.

# _________________________________________________

nums = [2,7,11,15]
target = 9

# _________________________________________________

def two_sum(nums, target):

    hashmap = {}

  
# _________________________________________________
<!-- for number in array:
  complement = target - number
  check hashmap
  store number  for i in range(len(nums)):

        complement = target - nums[i]

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[nums[i]] = i
        
print(two_sum([2,7,11,15],9)) -->


# _________________________________________________
target = 9
current = 2
need = 7

Brain question:"7 already vandacha?"
YES → answer
NO → store 2

# _________________________________________________

Almost 70% hashmap interview problems follow this pattern.
target - current number

# _________________________________________________
Complement = target reach panna thevaiyana number



Complement calculate panninaalum,
that number array la irukanum.

Illana pair exist aagadhu.


# _________________________________________________
Store numbers you HAVE
Check numbers you NEED

have → 3
need → 7

So store:
3

# _________________________________________________
Store current number
Check complement

NOT : Store complement

# _________________________________________________



# 🧠 Main Idea (Two Sum Logic)

Algorithm la **2 steps dhaan** important.

```
1. complement calculate pannuvom
2. complement already vandacha nu check pannuvom
```

But **store panradhu current number** dhaan.

---

# 📌 Simple Memory Trick (Thanglish)

```
Store numbers you HAVE
Check numbers you NEED
```

Meaning:

```
HAVE → already paatha numbers
NEED → complement
```

---

# 📌 Example

```
nums = [3,5,8]
target = 10
```

### Step 1

```
current number = 3
```

Complement calculate pannuvom:

```
10 - 3 = 7
```

Think pannunga:

```
3 kooda add panna 10 varanum na
inna number venum?
```

Answer:

```
7
```

So

```
need = 7
```

But check pannuvom:

```
7 already vandacha?
```

Array la illa ❌

So store pannuvom:

```
3
```

Hashmap:

```
{3:0}
```

---

# Why Store 3 (Thanglish)

Because:

```
3 namma kitta iruku
7 namma kitta illa
```

So rule:

```
Irukura number store pannuvom
Thevaiyana number check pannuvom
```

---

# One Line Rule (Thanglish)

```
Current number store pannu
Complement check pannu
```

NOT

```
Complement store panna koodathu
```

Because complement **just calculation**,
array la irukum nu guarantee illa.

---

# Super Simple Brain Model

Think like this:

```
Past numbers → store
Future numbers → complement check
```

Example:

```
2 store
7 vandha → match
```

Answer:

```
[0,1]
```

---

# Ultra Simple Sentence

```
Already paatha numbers store pannuvom.
Next numbers vandha complement match pannuvom.
```



