from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.edit import FormView
from my_app.models import Article, LoginForm, UserFavouriteArticle
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic import DetailView

# Create your views here.
class Home(RedirectView):
    pattern_name = 'articles'


class Articles(TemplateView):
    template_name = 'my_app/articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()
        return context

class LoginPage(FormView):

    template_name = 'my_app/login.html'
    form_class = LoginForm
    success_url = 'home'
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
                return HttpResponseRedirect(reverse('home'))
        return render(request, self.template_name, {'form' :form})


class Publications(TemplateView):
    template_name = 'my_app/publications.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        if self.request.user.is_authenticated:
            context['latest_articles'] = Article.objects.filter(author=self.request.user)
            return context
        else:
            context['latest_articles'] = 0
            return context


class Detail(DetailView):
    model = Article


class Logout(RedirectView):
    template_name = 'my_app/articles.html'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home'))


class Favourites(TemplateView):
    template_name = 'my_app/favourites.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        if self.request.user.is_authenticated:
            context['latest_articles'] = UserFavouriteArticle.objects.filter(user=self.request.user)
            return context
        else:
            context['latest_articles'] = 0
            return context
