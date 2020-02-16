from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Chats, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic import DetailView

# Create your views here.
def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

class Logout(RedirectView):
    template_name = 'chat/login.html'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class LoginPage(FormView):

    template_name = 'chat/login.html'
    form_class = LoginForm
    success_url = 'list'
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        # form = LoginForm()
        form = self.form_class(initial=self.initial)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            print(name)
            password = form.cleaned_data.get("password")
            print(password)
            user = authenticate(username=name, password=password)
            print(user)
            if user is not None:
                print(user)
                login(request, user=user)
                return HttpResponseRedirect(reverse('list'))
        return render(request, self.template_name, {'form' :form})

class ChatList(TemplateView):
    template_name = 'chat/articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Chats.objects.all()
        return context

class Detail(DetailView):
    model = Chats