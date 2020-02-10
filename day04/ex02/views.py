from django.shortcuts import render
from .froms import MyForm
import logging


# Create your views here.
logger = logging.getLogger(__name__)
def ex02(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            logger.debug(form.cleaned_data['subject'])
    else:
        form = MyForm()
    try:
        file = open("ex02/debug.log", "r")
        cont = file.readlines()
        file.close()
    except:
        print("Wrong file ")
    return render(request, 'ex02/ex02.html', {'form':form, 'cont':cont})