from django.shortcuts import redirect, render
from markupsafe import re
from .models import *
# Create your views here.
def StudentRegister(request):
    return render(request,"app/index.html")


#Show page view
def ShowPage(request):
    return render(request,"app/show.html")



# fetch data from html page 
def InsertData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    password = request.POST['password']
    subject = request.POST['subject']
    semester = request.POST['semester']
    email = request.POST['email']
    phone = request.POST['phone']
    aadhar = request.POST['aadhar']
    roll = request.POST['roll']
    address = request.POST['address']
    exam = request.POST['exam']

    #Insert data into database table
    newuser = Student.objects.create(firstname=fname,lastname=lname,password=password,subject=subject,semester=semester,
                                        email=email,phone=phone,aadhar_number=aadhar,roll_number=roll,address=address,exam_center=exam)
    
    # After insert data we want move on next forward page..
    return render(request,"app/show.html")




# Index1 page

def Index1(request):
    return render(request,"app/index1.html")
    