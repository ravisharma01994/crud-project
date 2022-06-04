from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','mail','password']
        
        widgets={'name':forms.TextInput(attrs={'class':"form-control"}),
        'mail':forms.EmailInput(attrs={'class':"form-control"}),
        'password':forms.PasswordInput(render_value=True, attrs={'class':"form-control"}),
        }
        
