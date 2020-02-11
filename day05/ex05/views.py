from django.shortcuts import render
from .models import Movies
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
# Create your views here.
def insert_data(request):
    result = list()
    values = [[1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'],
              [2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'],
              [3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'],
              [4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'],
              [5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kutz, Rick McCallum', '1980-05-17'],
              [6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum',
               '1983-05-25'],
              [7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11']]
    for val in values:
        try:
            print(val[0])
            mov1 = Movies.objects.create(episode_nb=val[0], title=val[1], director=val[2], producer=val[3],
                      release_date=val[4])
            mov1.save()
            print(mov1)
            result.append('Ok')
        except Exception as e:
            result.append(val[1])
            result.append(e)
            print(e)
        continue
    return render(request, 'ex05/insert_data.html', {'result': result})

def display(request):
    table = Movies.objects.all()
    return render(request, 'ex05/display.html', {"table": table})

def remove(request):
    table = None
    table = Movies.objects.all()
    try:
        name = request.POST.get('name', "")
        print(name)
        object = get_object_or_404(Movies, title=name)
        print(object)
        object.delete()
        table = Movies.objects.all()
    except Exception as e:
        print(e)
        # table = e
    return render(request, 'ex05/remove.html', {'table': table})

