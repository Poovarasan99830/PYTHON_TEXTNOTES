Got it — you want a **WTForms-based CRUD (Create, Read, Update, Delete)** example.
I’ll make a **complete mini Flask app** that:

* Uses **WTForms** for form handling & validation
* Stores data in **in-memory list** (can replace with DB later)
* Supports **Add, View, Edit, Delete** operations

---

## **1. Install Dependencies**

```bash
pip install flask flask-wtf
```

---

## **2. Project Structure**

```
wtforms_crud/
│── app.py
│── templates/
│     ├── index.html
│     ├── form.html
```

---

## **3. app.py**

```python
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.secret_key = "secret"

# In-memory storage
customers = []  # Each item: {"id": int, "name": str, "email": str}
next_id = 1

# WTForms Form
class CustomerForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Save")

# Create & Read
@app.route("/", methods=["GET", "POST"])
def index():
    global next_id
    form = CustomerForm()
    if form.validate_on_submit():
        customers.append({"id": next_id, "name": form.name.data, "email": form.email.data})
        next_id += 1
        return redirect(url_for("index"))
    return render_template("index.html", form=form, customers=customers)

# Update
@app.route("/edit/<int:cid>", methods=["GET", "POST"])
def edit(cid):
    form = CustomerForm()
    customer = next((c for c in customers if c["id"] == cid), None)
    if not customer:
        return "Customer not found", 404
    
    if request.method == "GET":
        form.name.data = customer["name"]
        form.email.data = customer["email"]



# form → the form object instance you created from your WTForms class.

# form.name → the StringField (or any other field) named name inside your form class.

# .data → the actual value stored in that field.

# Setting .data pre-populates the HTML input when you render the form in your template.





    if form.validate_on_submit():
        customer["name"] = form.name.data
        customer["email"] = form.email.data
        return redirect(url_for("index"))
    
    return render_template("form.html", form=form, title="Edit Customer")

# Delete
@app.route("/delete/<int:cid>")
def delete(cid):
    global customers
    customers = [c for c in customers if c["id"] != cid]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
```

---

## **4. templates/index.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>WTForms CRUD</title>
</head>
<body>
    <h2>Add Customer</h2>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>{{ form.name.label }} {{ form.name(size=20) }}</p>
        <p>{{ form.email.label }} {{ form.email(size=20) }}</p>
        <p>{{ form.submit() }}</p>
    </form>

    <h2>Customer List</h2>
    <table border="1">
        <tr><th>ID</th><th>Name</th><th>Email</th><th>Actions</th></tr>
        {% for c in customers %}
        <tr>
            <td>{{ c.id }}</td>
            <td>{{ c.name }}</td>
            <td>{{ c.email }}</td>
            <td>
                <a href="{{ url_for('edit', cid=c.id) }}">Edit</a> |
                <a href="{{ url_for('delete', cid=c.id) }}">Delete</a>
            </td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

---

## **5. templates/form.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h2>{{ title }}</h2>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>{{ form.name.label }} {{ form.name(size=20) }}</p>
        <p>{{ form.email.label }} {{ form.email(size=20) }}</p>
        <p>{{ form.submit() }}</p>
    </form>
</body>
</html>
```

---

## **6. How It Works**

* **Create** → Add a customer via form on home page
* **Read** → List all customers in a table
* **Update** → Click "Edit" → Prefills form → Submit updates data
* **Delete** → Click "Delete" removes entry from list

---

If you want, I can **upgrade this to use MySQL** so students get **WTForms + CRUD + Database** in one go instead of just an in-memory list. That would make it production-like.
Do you want me to prepare that next?
