from django.db import models
from django import forms
# Create your models here.
class Chats(models.Model):
    name = models.CharField(max_length=42)

class LoginForm(forms.Form):
    name = forms.CharField(label='Name', max_length=32)
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)


