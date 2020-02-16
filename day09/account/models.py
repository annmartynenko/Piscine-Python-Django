from django.db import models
from django import forms
# Create your models here.
class FormModel(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.login

class LoginForm(forms.Form):
    name = forms.CharField(label='Name', max_length=32)
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)



# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = FormModel
#         fields = ['login', 'password']
#
