

#_______________________________________________________
# Why python use interpreter....wha is difference between interpreter and compiler?
#_______________________________________________________





# Python is an interpreted language that first compiles source code 
# into bytecode and then executes it using the Python Virtual Machine.



# Compiler = teacher (first full check)
# Interpreter = live translator
# Python = Teacher + Translator
# Bytecode = middle language
# PVM = final runner

# Python direct-aa interpreter illa ❌
# Python first compile pannum,
# apram interpret pannum 😲

# Python Code (.py)
#      ↓
# Bytecode (.pyc)[0,1]   ← Compiler
  #    ↓
# Python Virtual Machine (PVM) ← Interpreter
#      ↓
# Output



# One-Line Meaning

# 👉 Python Virtual Machine na Python oda engine
# 👉 Bytecode-a read panni execute pannradhu


# PVM reads bytecode
# Executes line by line
# Produces output


#_______________________________________________________
#what are all mutable and imutable data tyeps:
#_______________________________________________________




# Mutable Types List
# list
# dict
# set
# bytearray


# Immutable Types List

# int
# float
# complex
# bool
# str
# tuple
# frozenset
# bytes

#_______________________________________________________
# break, pass, continue – Difference
#_______________________________________________________


# pass → mostly placeholder in empty functions, loops, classes

# break → exit early (good for search)

# continue → skip unwanted elements




#_______________________________________________________
# what types of decorator available and whix type if decorator used in django project...
#_______________________________________________________


# | Type                   | Usage in Django        | Example                             |
# | ---------------------- | ---------------------- | ----------------------------------- |
# | Function decorator     | View functions         | `@login_required`                   |
# | Class decorator        | Class-based views      | `@method_decorator(login_required)` |
# | Parametrized decorator | View with extra config | `@cache_page(60*15)`                |
# | Built-in Python        | Class/Method tweaks    | `@staticmethod`, `@property`        |



# Decorators used in Django Projects

# 1️⃣ View Decorators (Most common)

# @login_required → only logged-in user can see view

# @permission_required('app.add_model') → permission check

# @csrf_exempt → disable CSRF for view




# 2️⃣ Class-based view decorators

# @method_decorator(login_required, name='dispatch') → CBV

# Attach decorators to CBV methods like get or post



# 3️⃣ Middleware-like decorators

# @cache_page(60*15) → cache view for 15 mins

# @require_http_methods(["POST"]) → allow only POST request



#_______________________________________________________
# Why Python is Better Compared to Other Languages?

#_______________________________________________________

# Python is preferred over other languages because it is simple, readable, 
# interpreted, cross-platform, has huge libraries, supports rapid development, and is multipurpose



# Multipurpose

# Web apps → Django, Flask

# AI/ML → TensorFlow, PyTorch

# Automation → Scripts

# Game dev → Pygame

# One language → almost everything panna mudiyum

#_______________________________________________________


# What is an Exception?
# Exception handling is a way to catch and 
# handle errors at runtime using try, except, else, and finally so that the program doesn’t crash.


#_______________________________________________________
