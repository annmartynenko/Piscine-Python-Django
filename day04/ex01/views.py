from django.shortcuts import render

# Create your views here.
def dg(request):
    return render(request, 'ex01/django.html', {})

def aff(request):
    return render(request, 'ex01/affichage.html', {})

def temp(request):
    return render(request, 'ex01/templates.html', {})