
 # Part-1 ==> form widget
 # part-2 ==>types of forms
 # part-3 ===>flow chart 


__________________________________________________________________________________________
______________________________PART 1____________________________________________________________

### 🔹 What is `widget`?

* A **widget** is how Django decides **what kind of HTML form field** to render for a given Python form field.
* It controls **how the field looks in HTML** (input, textarea, select box, checkbox, etc.) and **how it behaves** when receiving data.

---

### 🔹 Example

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()  
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

#### What happens:

* `name = forms.CharField()` → Default widget is `<input type="text">`
* `email = forms.EmailField()` → Default widget is `<input type="email">`
* `message = forms.CharField(widget=forms.Textarea)` → Rendered as `<textarea>...</textarea>`

---

### 🔹 Common Widgets in Django

| Django Field   | Default Widget  | Can Override With                       |
| -------------- | --------------- | --------------------------------------- |
| `CharField`    | `TextInput`     | `Textarea`, `PasswordInput`, etc.       |
| `EmailField`   | `EmailInput`    | `TextInput`, `Textarea`                 |
| `BooleanField` | `CheckboxInput` | `RadioSelect`                           |
| `ChoiceField`  | `Select`        | `RadioSelect`, `CheckboxSelectMultiple` |
| `DateField`    | `DateInput`     | `SelectDateWidget`                      |

---

### 🔹 Example with Multiple Widgets

```python
class ExampleForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput)
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    gender = forms.ChoiceField(
        choices=[('M', 'Male'), ('F', 'Female')],
        widget=forms.RadioSelect
    )
```

#### Rendered HTML:

```html
<input type="text" name="username" class="form-control">
<input type="password" name="password">
<textarea name="bio" rows="5" cols="30"></textarea>
<input type="radio" name="gender" value="M"> Male
<input type="radio" name="gender" value="F"> Female
```

---

✅ So in your case:

```python
message = forms.CharField(widget=forms.Textarea)

__________________________________________________________________________________________
__________________________________PART-2 ________________________________________________________


__str__() → When you print a Product object, you’ll see the product’s name.




class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

Plain form (not tied to DB).
Used for collecting info and sending emails.



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

ModelForm → automatically tied to Product model.
When you call form.save(), it inserts into the database.



__________________________________________________________________________________________
__________________________________part-3 ________________________________________________________


models -> views ->templates -> Urls

Forms → Views → Templates → Urls→ Output

Models → Forms → Views → Templates → Urls→ Output

__________________________________________________________________________________________
__________________________________part-4 ________________________________________________________
This snippet is a **Django template form**. Let’s break it down line by line:

```html
<form method="POST">
   {% csrf_token %}
        {{ get_form.as_p }}
        <button type="submit">Submit</button>
</form>
```

### 🔎 Explanation:

1. **`<form method="POST">`**

   * Creates an HTML form that will send data to the server.
   * The method is **POST**, which means the form data won’t be visible in the URL (unlike GET).
   * POST is usually used for actions like creating, updating, or deleting data.

---

2. **`{% csrf_token %}`**

   * A **Django template tag** that inserts a hidden security token.
   * CSRF = **Cross-Site Request Forgery** protection.
   * Django requires this to prevent malicious requests from other sites.
   * Without this, Django will reject the form submission.

---

3. **`{{ get_form.as_p }}`**

   * `get_form` is a Django **form object** passed from the view to the template.
   * `.as_p` is a method that renders each form field wrapped in a `<p>` tag for basic formatting.
     Example:

     ```html
     <p><label for="id_name">Name:</label> <input type="text" name="name" required id="id_name"></p>
     ```
   * Other rendering options:

     * `{{ form.as_table }}` → renders form fields in a `<table>`.
     * `{{ form.as_ul }}` → renders form fields inside `<li>` elements.
     * You can also render each field manually with `{{ form.field_name }}` for more control.

---

4. **`<button type="submit">Submit</button>`**

   * Adds a **submit button**.
   * When clicked, the form data is sent to the server using the POST method.

---

✅ **So in short**:
This code displays a Django form in paragraph style, ensures it’s protected against CSRF attacks, and provides a submit button to send data to the backend.

---___________________________________________________________________________________________







## ⚙️ **Step-by-Step Django CSRF Demo**

---

### 🧾 1️⃣ `views.py`

```python
from django.shortcuts import render
from django.http import HttpResponse

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return HttpResponse(f"✅ Form submitted successfully! Name: {name}, Email: {email}")
    return render(request, 'contact.html')
```

---

### 🧩 2️⃣ `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
]
```

---

### 🖋️ 3️⃣ `templates/contact.html`

```html
<!DOCTYPE html>
<html>
<head>
  <title>Contact Form</title>
</head>
<body>
  <h2>Contact Us</h2>
  <form method="post">
    {% csrf_token %}
    <input type="text" name="name" placeholder="Enter your name"><br><br>
    <input type="email" name="email" placeholder="Enter your email"><br><br>
    <button type="submit">Send</button>
  </form>
</body>
</html>
```

---

### 🧠 4️⃣ இதை browser-ல் open பண்ணும் போது (View Source)

Form பக்கம் source code-ல் இப்படிப் பாப்பீங்க 👇

```html
<form method="post">
  <input type="hidden" name="csrfmiddlewaretoken" value="1ab5f3kZ3cWq6I9xP7yT2vX0qL8rB9E3">
  <input type="text" name="name" placeholder="Enter your name"><br><br>
  <input type="email" name="email" placeholder="Enter your email"><br><br>
  <button type="submit">Send</button>
</form>
```

அதாவது 🔒
➡️ `{% csrf_token %}` → Django இதை **auto convert** பண்ணி ஒரு hidden input-ஆ சேர்க்குது.
➡️ `value` → இது தான் அந்த ரகசிய "முத்திரை" (CSRF security code).

---

### 🚫 5️⃣ `{% csrf_token %}` remove பண்ணிட்டீங்கன்னா?

நீங்க அந்த line-ஐ delete பண்ணிட்டீங்கனா,
form submit பண்ணும் போது browser-ல் இப்படி வரும் 👇

```
Forbidden (403)
CSRF verification failed. Request aborted.
```

அதாவது Django சொல்கிறது 🔐

> "முத்திரை இல்லாம form அனுப்ப முடியாது!"

---

### ✅ Summary

| நிலை                          | விளக்கம்                     | முடிவு           |
| ----------------------------- | ---------------------------- | ---------------- |
| `{% csrf_token %}` சேர்த்தால் | Hidden security token சேரும் | Form Submit OK ✅ |
| சேர்க்கலேன்னா                 | CSRF verification fail       | Error 403 ❌      |




🔐 CSRF Token – ஒரு எளிய ஒப்புமை

இது எப்படி என்றால் 👇

நீங்கள் ஒரு வங்கிக் கிளையில் form நிரப்புகிறீர்கள்.
அதிகாரி உங்களுக்கு ஒரு முத்திரை (seal) போட்டார் —
அந்த form கிளையிலிருந்து வந்தது என உறுதிப்படுத்த.

அதேபோல {% csrf_token %} என்பது Django-வின் முத்திரை (security seal) 🏦
---___________________________________________________________________________________________