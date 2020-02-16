from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    synopsis = models.CharField(max_length=312)
    content = models.TextField()

    def __str__(self):
        return self.title


class UserFavouriteArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.article.title


class LoginForm(forms.Form):
    name = forms.CharField(label='Name', max_length=32)
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)

