from django.shortcuts import render, reverse
from django.views.generic.edit import FormView
from .models import ImageForm, ImgModel

# Create your views here.

class LoadImage(FormView):
    template_name = 'myapp/home.html'
    form_class = ImageForm
    success_url = 'home'
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        files = ImgModel.objects.all()
        context = {'form': form, 'files': files}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)
        files = ImgModel.objects.all()
        if form.is_valid():
            img = form.cleaned_data.get("img")
            title = form.cleaned_data.get("title")
            obj = ImgModel.objects.create(title=title, img=img)
            print(img)
            print(title)
            obj.save()
        else:
            form = ImageForm()
        return render(request, self.template_name, {'form': form, 'files': files})
