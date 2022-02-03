from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("master/", views.master, name='master'),
    path("", views.Index, name="index"),
    path("signup/",views.SignUp,name="signup"),
    path('accounts/',include('django.contrib.auth.urls')),


    # add to cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    # Contact-page
    path("contact/",views.Contact_us,name="contact"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

