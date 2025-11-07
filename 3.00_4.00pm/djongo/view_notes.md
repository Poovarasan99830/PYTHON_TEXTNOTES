# ------------------------------------------------------
# 🔹 IMPORTS
# ------------------------------------------------------
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, StudentRegistration
from .forms import StudentRegistrationForm
from django.db.models import Avg, Sum
from django.db.models.functions import Lower
# ❌ Remove: from turtle import pd (not required)
# ------------------------------------------------------



# ------------------------------------------------------
# 🔹 HOME VIEW — Send Dynamic Values to Template
# ------------------------------------------------------
def home(request, number):
    return render(request, 'home.html', {
        'get_number1': number,
        'get_number2': number + 1
    })



# ------------------------------------------------------
# 🔹 SIMPLE STATIC PAGE RENDERING
# ------------------------------------------------------
def about(request):
    return render(request, 'app1.html')

def order(request):
    return render(request, 'order.html')

def contact(request):
    return render(request, 'contact.html')



# ------------------------------------------------------
# 🔹 STUDENT INFO — Pass Dictionary Data to Template
# ------------------------------------------------------
def student_info(request, roll):
    student = {
        'name': 'Ravi',
        'roll': roll,
        'course': 'Python Full Stack'
    }
    return render(request, 'student.html', {'student': student})



# ------------------------------------------------------
# 🔹 COURSE LIST — Pass List + Dynamic Data
# ------------------------------------------------------
def course_list(request, data):
    courses = ['Python', 'Django', 'Flask', 'HTML', 'CSS']
    mark = data
    return render(request, 'student.html', {'courses': courses, 'mark': mark})



# ------------------------------------------------------
# 🔹 PRODUCT DETAIL — Using Local Python List
# ------------------------------------------------------
def product_detail(request, id):
    product = [
        {'id': 1, 'name': 'Laptop', 'price': 55000},
        {'id': 2, 'name': 'Mouse', 'price': 800},
        {'id': 3, 'name': 'Keyboard', 'price': 1500},
    ]
    result = next((item for item in product if item["id"] == id), "data not found")
    return render(request, 'product.html', {'get_product': result})



# ------------------------------------------------------
# 🔹 LOGIN PAGE — GET and POST Example
# ------------------------------------------------------
def login(request):
    print(request.method)
    print(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return render(request, 'login.html', {
            'username': username,
            'password': password
        })
    else:
        return render(request, 'login.html')



# ------------------------------------------------------
# 🔹 PRODUCT FORM — Save Data to Database
# ------------------------------------------------------
def product_list(request):
    if request.method == 'POST':
        get_name = request.POST.get('name')
        get_price = request.POST.get('price')
        get_description = request.POST.get('description')

        Product.objects.create(
            name=get_name,
            price=get_price,
            description=get_description
        )
        print(type(get_price))
        return HttpResponse("Data saved to Product table!")
    else:
        return render(request, 'product_list.html')
        # You can also show existing data:
        # return render(request, 'product_list.html', {'products': Product.objects.all()})



# ------------------------------------------------------
# 🔹 STUDENT REGISTRATION — Using POST (Manual Method)
# ------------------------------------------------------
def student_registration(request):
    print(request.POST)
    if request.method == 'POST':
        get_name = request.POST['name']
        get_email = request.POST['email']
        get_age = request.POST['age']
        get_course = request.POST['course']

        StudentRegistration.objects.create(
            name=get_name,
            email=get_email,
            age=get_age,
            course=get_course
        )
        return HttpResponse("Data saved to StudentRegistration table!")
    else:
        return render(request, 'stu_reg.html')



# ------------------------------------------------------
# 🔹 DJANGO FORM EXAMPLE (ModelForm)
# ------------------------------------------------------
def student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Data saved using Django Form!")
    else:
        form = StudentRegistrationForm()
    return render(request, 'django_stu_form.html', {'form': form})



# ------------------------------------------------------
# 🔹 STUDENTLIST — Django ORM Operations (CRUD)
# ------------------------------------------------------
def StudentList(request):

    # ------------------------------------------------------
    # 🔹 FILTER (name = "varun")
    # ------------------------------------------------------
    students = StudentRegistration.objects.filter(name="varun")
    for s in students:
        print(s.name)


    # ------------------------------------------------------
    # 🔹 FILTER (age >= 40)
    # ------------------------------------------------------
    students = StudentRegistration.objects.filter(age__gte=40)
    for s in students:
        print(s.name, s.age)


    # ------------------------------------------------------
    # 🔹 EXCLUDE (name != "varun")
    # ------------------------------------------------------
    students = StudentRegistration.objects.exclude(name="varun")
    for s in students:
        print(s.name)


    # ------------------------------------------------------
    # 🔹 GET (Fetch one object by ID)
    # ------------------------------------------------------
    s = StudentRegistration.objects.get(id=3)
    print(s.name)


    # ------------------------------------------------------
    # 🔹 UPDATE (Single object)
    # ------------------------------------------------------
    s.name = "ZOO"
    s.save()
    print("Updated single student:", s.name)


    # ------------------------------------------------------
    # 🔹 BULK UPDATE
    # ------------------------------------------------------
    StudentRegistration.objects.filter(name="sam").update(name="Television movie")
    print("Updated all 'sam' to 'Television movie'")


    # ------------------------------------------------------
    # 🔹 DELETE (Single record)
    # ------------------------------------------------------
    s = StudentRegistration.objects.get(id=1)
    s.delete()
    print("Deleted student with ID 1")


    # ------------------------------------------------------
    # 🔹 BULK DELETE
    # ------------------------------------------------------
    StudentRegistration.objects.filter(name="Television movie").delete()
    print("Deleted all students named 'Television movie'")


    # Optional: return some response or render data
    return HttpResponse("Student ORM operations executed successfully!")
