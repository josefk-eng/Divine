from dataclasses import fields
import email
from unicodedata import name
from django import forms

from adwmi.models import Person
from django.contrib.auth.forms import UserCreationForm
from .models import Image

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ("title","image")
        

class Member(forms.ModelForm):
    
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        modal = Person
        fields = ['username','password']
        
        
