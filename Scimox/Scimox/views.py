from django.http import HttpResponse
from django.shortcuts import redirect, render


def HomePage(request):
    return render(request,"index.html")

def about(request):
    return render(request, "about.html")

def business(request):
    return render(request,"businesses.html")

def businessbrief(request):
    return render(request, "businessbrief.html")

def sector(request):
    return render(request, "sector.html")

def candidates(request):
    return render(request, "candidates.html")

def contact(request):
    return render(request, "contactus.html")

def scimox_policy(request):
    return render(request, "scimox_policy.html")

def signup(request):
    return render(request, "signup.html")

def loginpage(request):
    return render(request, "login.html")
    