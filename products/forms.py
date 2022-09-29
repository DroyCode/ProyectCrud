from django import forms
from .models import Product
from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):