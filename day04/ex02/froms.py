from django import forms

class MyForm(forms.Form):
    subject = forms.CharField(label='subject', max_length=1000)

