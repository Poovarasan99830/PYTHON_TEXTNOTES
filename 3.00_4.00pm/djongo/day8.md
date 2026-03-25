
# -----------------------------------
# Topic:  Middleware
# -----------------------------------


Middleware in Django acts as a layer between the request/response cycle and allows you to modify or process requests and responses globally.
 It’s an essential feature for
 handling authentication, session management, security,
  and many other tasks in a centralized and reusable manner.


# -----------------------------------
# Built-in Django Middleware:
# -----------------------------------

Django provides a number of built-in middleware classes that you can use or extend. Some common ones include:


SecurityMiddleware: Adds security headers and performs various checks to enhance security.

SessionMiddleware: Manages sessions across requests and stores session data.

AuthenticationMiddleware: Associates users with requests using session-based authentication.

CsrfViewMiddleware: Adds Cross-Site Request Forgery (CSRF) protection to POST requests.

CommonMiddleware: Adds various common utilities, like URL rewriting and handling ETag headers.

MessageMiddleware: Manages flash messages to be displayed to users.

GZipMiddleware: Compresses responses to reduce data transfer sizes.


# -----------------------------------------
How Middleware Works in Django
# ----------------------------------------

http request---middleware----->MVT---middleware---->http response


# -------------------------------------------------
Why Use Custom Middleware if Django Has Built-in?
# ------------------------------------------------

Django has built-in middleware like:

   AuthenticationMiddleware
   SessionMiddleware
   CSRF Middleware
   SecurityMiddleware

But built-in middleware handles general tasks.




We create custom middleware when we need:
     Custom validation logic
     Custom logging
     IP blocking
     Request timing
     Custom headers
     Role checking
     API key validation
     Maintenance mode




| Built-in           | Custom                   |
| ------------------ | ------------------------ |
| Provided by Django | Created by developer     |
| Common tasks       | Business-specific logic  |
| Already tested     | Custom behavior          |
| General purpose    | Project-specific purpose |


# -----------------------------------------


__init__ method

Runs ONLY ONCE when the server starts
get_response is the next layer (next middleware or view)
You store it to call later


__call__ method
    This method runs on every HTTP request.


your_app.middleware.CheckEven',  # 👈 custom middleware  settings.py
# -----------------------------------------

