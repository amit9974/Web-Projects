from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/",views.index,name="homepage"),
    path("signup/",views.SignUp,name="signup"),
    path("",views.SigninPage,name="signinpage"),
    path("signin/",views.SigninUser,name="signin"),
    path("contact/",views.contact_us,name="contact"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)