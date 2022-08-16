from django.urls import path
from . import views


urlpatterns = [
    path('', views.loginpage, name='login'),
    path('register', views.register, name='register'),
    path('index', views.index, name='index'),
    path('myproducts', views.myproducts, name='myproducts'),
    path('new', views.new),
    path('loginpage', views.loginpage),



]