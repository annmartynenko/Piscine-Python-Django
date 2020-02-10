from django.shortcuts import render

# Create your views here.
def ex03(request):
    a = [float(i / 100.0) for i  in range(0, 100, 2)]
    print(a)
    return render(request, 'ex03/ex03.html', {'a':a})