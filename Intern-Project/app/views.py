from email import message
from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def index(request):
    return render(request, "app/index.html")


def SignUp(request):
    if request.method == "POST":
        fname = request.POST['name']
        sname = request.POST['surename']
        gender = request.POST['gender']
        dob = request.POST['dob']
        email = request.POST['email']
        image = request.POST['pic']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        user = User.objects.filter(email=email)

        if user:
            message = "Email is already registerd."
            return render(request,'app/signup.html',{'msg':message})
        else:
            if password==cpassword:
                new_user = User.objects.create(name=fname,surename=sname,sex=gender,image=image,dob=dob,email=email,password=password)
                new_user.save()
                message = "User has been successfully registerd"
                return render(request,'app/signin.html',{'msg':message})
            else:
                message = "Password and Confirm Password doesn't match"
                return render(request,'app/signup.html',{'msg':message})     

    return render(request,"app/signup.html")


# Login page 
def SigninPage(request):
    return render(request,'app/signin.html')

# Login User view functions
def SigninUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(email=email)
        if user:
            if user.password == password:
                return redirect('homepage')
            else:
                message = "Password is incorrect!"
                return render(request,'app/signin.html')
        else:
            message = "User doesn't exist"
            return render(request,'app/signup.html',{'msg':message})
            

def contact_us(request):
    if request.method == "POST":
        contact = Contact(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        contact.save()      
    return render(request,'app/contact.html')

