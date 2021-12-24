"""Scimox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Scimox import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage),
    path('about/', views.about),
    path('business/', views.business),
    path('businessbrief/', views.businessbrief),
    path('sector/', views.sector),
    path('candidates/', views.candidates),
    path('contact/', views.contact),
    path('scimox_policy/', views.scimox_policy),
    path('signup/', views.signup),
    path('loginpage/', views.loginpage),

  ]