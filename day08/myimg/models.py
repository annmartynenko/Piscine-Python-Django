from django.db import models
from PIL import Image
from django import forms

# Create your models here.

class ImgModel(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="files")

    def __str__(self):
        return self.title

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImgModel
        fields = ['title', 'img']



