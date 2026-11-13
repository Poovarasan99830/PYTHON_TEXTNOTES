
from flask import Flask


app = Flask(__name__)


#___________________________
# basic_routes
# Rendering HTML templates 
#___________________________

@app.route('/one')
def home():
    return "Hello, World!"




if __name__ == "__main__":
    app.run(debug=True)



#What are Routes in Flask?

# "A route is the URL path that maps a user's request to a specific Python function. 
# When a user visits a URL, 
# Flask checks the route and executes the corresponding function, then returns the response.



#HTTP Methods in Flask:

# http://127.0.0.1:5000/one


# Browser
#    │
#    │ 1. Sends HTTP Request
#    ▼
# Flask Server
#    │
#    │ 2. Flask checks the Route
#    ▼
# Python Function
#    │
#    │ 3. Function executes
#    ▼
# Returns Response
#    │
#    │ 4. Flask sends HTTP Response
#    ▼
# Browser displays the result


# HTTP Request



# What is an HTTP Request?

# "An HTTP Request is a message sent by the client
#  (browser, mobile app, or Postman) to the server"
# " asking it to perform an action, such as retrieving, creating, updating, or deleting data."

#HTTP Methods:

# GET
# POST
# PUT
# DELETE



# //127.0.0.1  --->ip address of the local machine

# An IP (Internet Protocol) Address is a unique numerical address assigned to every device
# connected to a network. It helps devices identify and communicate with each other."

#5000 -->port number

# A port is a logical communication endpoint on a computer. It tells the 
# operating system which application or service should receive the incoming request




# ----------------------------------------------------


# | Part          | Meaning                                                                                                     |
# | ------------- | ----------------------------------------------------------------------------------------------------------- |
# | **http**      | **HTTP (HyperText Transfer Protocol)** – The communication protocol used between the client and the server. |
# | **127.0.0.1** | **IP Address** – Identifies the computer (localhost).                                                       |
# | **5000**      | **Port Number** – Identifies the Flask application running on the computer.                                 |
# | **/one**      | **Route (URL Path)** – Identifies the function that Flask should execute.                                   |

# http://127.0.0.1:5000/one
# │      │         │      │
# │      │         │      └── Route
# │      │         └───────── Port Number
# │      └─────────────────── IP Address
# └────────────────────────── Protocol


# HTTP tells how to communicate, the IP Address tells where to go, 
# the Port tells which application to use, and the Route tells which function to execute.


# ----------------------------------------------------