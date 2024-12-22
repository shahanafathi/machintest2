from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from .models import CustomeUser
from django.urls import reverse
from .models import Employee
from django.http import JsonResponse
from .models import CustomeUser
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
     data=CustomeUser.objects.all()
    #  return render(request,'index.html')
     return render(request,'index.html',{"data": data})

def add_employee(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        department = request.POST.get("department")
        designation = request.POST.get("designation")
        date_of_joining = request.POST.get("date_of_joining")
        salary = request.POST.get("salary")
        image = request.FILES.get("image")

        
        if image:
            fs = FileSystemStorage()
            image_name = fs.save(image.name, image)
        else:
            image_name = None

       
        employee = CustomeUser.objects.create(
            first_name=first_name,
            username=first_name,
            last_name=last_name,
            Department=department,
            Designation=designation,
            doj=date_of_joining,
            salary=salary,
            Image=image_name,
        )
        employee.save()

        return redirect("index")
    else:  
        employees = CustomeUser.objects.all()
        return render(request, "index.html") 
    
def profile(request):
    data=CustomeUser.objects.all()
    return render(request,"index.html",{'data':data})