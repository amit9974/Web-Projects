from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.StudentRegister,name="register"),
    path("show/",views.ShowPage,name="show"),
    path("insert/",views.InsertData,name="insert"),
    path("index1/",views.Index1,name="index")

]
