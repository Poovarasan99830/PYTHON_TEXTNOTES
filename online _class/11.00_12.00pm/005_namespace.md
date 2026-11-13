
# PART1--> Name space explain students notes

# Part2 --> difference b/w name space and variable

# part3 --> thanglish  explain in name space

#



____________________________________________________________________________
_______________________________part1________________________________________


# 🔹 What is Namespace in Python?

👉 **Namespace = A container (mapping) that holds a set of names (identifiers) as keys and the objects (values) they point to.**

* Every variable name, function name, class name → is stored in some **namespace**.
* Behind the scenes, it’s like a **dictionary**:

  ```python
  {"name": <object reference>}
  ```

---

## 🔹 Why Namespace?

* Prevents **name conflicts**.
* Example:

  ```python
  len = 100
  print(len("hello"))  # ❌ error because name conflict
  ```

  * Here your variable `len` shadows the built-in `len`.
* **Solution:** Python keeps **different namespaces** (local, global, built-in) to avoid such clashes.

---

## 🔹 Types of Namespaces in Python

1. **Built-in Namespace**

   * Comes with Python itself.
   * Contains functions like `print()`, `len()`, `sum()`.
   * Always loaded when Python starts.

   Example:

   ```python
   print(dir(__builtins__))  # shows built-in namespace
   ```

---

2. **Global Namespace**

   * Created when you run a Python file.
   * Holds names defined at the **top level** (variables, functions, classes).

   Example:

   ```python
   x = 10
   def greet():
       pass
   print(globals())  # shows global namespace
   ```

---

3. **Local Namespace**

   * Created whenever you call a function.
   * Stores names of function arguments and local variables.

   Example:

   ```python
   def my_func(a, b):
       c = a + b
       print(locals())  # shows local namespace
   my_func(2, 3)
   ```

---

4. **Enclosed Namespace**

   * Exists when functions are nested.
   * Inner function can access outer function’s namespace.

   Example:

   ```python
   def outer():
       x = "enclosed"
       def inner():
           print(x)   # uses enclosed namespace
       inner()
   outer()
   ```

---

## 🔹 Lifetime of Namespace

* **Built-in** → till Python interpreter runs.
* **Global** → till program/module ends.
* **Local** → till function call ends.
* **Enclosed** → till outer function ends.

---

## ✅ Polite Thunglish Analogy

👉 **"Namespace-na inga oru almirah (cupboard) maadhiri. Oru shelf la oru set of variable names + values irukkum. Python ku multiple cupboards irukkum: built-in cupboard, global cupboard, local cupboard. Oru variable thedi paakumbothu, Python cupboard by cupboard search pannidum (LEGB rule) until name kidaikkum."**





____________________________________________________________________________
_______________________________part2________________________________________








Inga konjam **clear-a differentiate pannalaam** 👇

---

## 🔹 Variable vs Namespace

* **Variable** → oru **single name** ku oru object attach pannirukkum.
  Example:

  ```python
  x = 10
  ```

  👉 `x` is a variable. It points to object `10`.

* **Namespace** → oru **collection (dictionary)** of many such name → object mappings.
  Example:

  ```python
  x = 10
  y = "Hello"
  z = [1,2,3]
  ```

  👉 Behind the scenes namespace looks like:

  ```python
  {
     "x": <int object 10>,
     "y": <str object "Hello">,
     "z": <list object [1,2,3]>
  }
  ```

---

✅ Polite Thunglish Summary:

* Variable = **single entry** (e.g., `"x" → 10`).
* Namespace = **whole dictionary** of all variable-function-class names and their object references.

👉 **So, namespace apdinu sonna, adhu oru variable illai, but antha ella variables, functions, classes names-oda “address book” collection.**

---

✨ Inga unga students ku solla simple analogy:

* **Variable = one contact** in your mobile (e.g., “Amal → 9876543210”).
* **Namespace = full contact list / phonebook** (all names with numbers).

---

____________________________________________________________________________
_______________________________part3________________________________________





# 🔹 Types of Namespaces

Python la 4 main namespaces irukku:

---

## 1️⃣ **Built-in Namespace**

* Python start aagumbodhu thaaney irukkura default names.
* Example: `print()`, `len()`, `id()`, `int`, `list` etc.
* Always available, inga import panna thevaila.

👉 Polite Thunglish analogy:
**"Built-in namespace-na Python oda thaay vazhi names — by default ellathukkum available."**

---

## 2️⃣ **Global Namespace**

* Module level la create aagura variables, functions, classes ellam inga store aagum.
* Example:

  ```python
  x = 10  # global variable

  def fun():
      pass
  ```

  👉 Namespace looks like:

  ```python
  {"x": 10, "fun": <function object>}
  ```

👉 Analogy:
**"Global namespace-na unga house main hall maadhiri — enga veetla ella periyavanga (module level objects) iruppanga."**

---

## 3️⃣ **Enclosed Namespace**

* Oru function kulla another function define panna, outer function oda scope la irukkura names.
* Example:

  ```python
  def outer():
      a = 5   # enclosed
      def inner():
          print(a)   # access from outer
      inner()
  outer()
  ```

👉 Analogy:
**"Enclosed namespace-na appa-amma room maadhiri — unga amma room la vachirukkura things unga kitta share panna mudiyum (inner function can access outer function variables)."**

---

## 4️⃣ **Local Namespace**

* Function execute aagumbodhu, function kulla define panna variables inga store aagum.
* Example:

  ```python
  def my_fun():
      x = 20   # local variable
      print(x)
  my_fun()
  ```

👉 Analogy:
**"Local namespace-na unga personal study table maadhiri — function execute aagumbodhu mattum use aagum, adhu mudinju delete aayidum."**

---

# 🔹 LEGB Rule (Order of search)

When you use a variable, Python will check in this order:

1. **L → Local**
2. **E → Enclosed**
3. **G → Global**
4. **B → Built-in**

👉 Polite Thunglish Summary:
**"Python oru name thedi search panna, adhu first local la paapum, kidaikala na outer la paapum, adhukuda kidaikala na global la paapum, last chance built-in la paapum."**

---

✨ Simple Example for LEGB:

```python
x = "Global"

def outer():
    x = "Enclosed"
    def inner():
        x = "Local"
        print(x)
    inner()

outer()
```

Output: `Local`



____________________________________________________________________________
_______________________________end________________________________________
