from django.shortcuts import render, reverse
from django.views.generic.edit import FormView
from .models import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# class ShowAccount(FormView):
#     template_name = 'account/account.html'
#     form_class = LoginForm
#     success_url = '../account/'
#     initial = {'key': 'value'}
#     #
#     def get(self, request, *args, **kwargs):
#         # form = LoginForm()
#         form = self.form_class(initial=self.initial)
#         context = {'form': form}
#         return JsonResponse(form)
#     #
#     def post(self, request, *args, **kwargs):
#         form = LoginForm(request.POST)
#         # if self.request.is_ajax():
#         name = form.cleaned_data.get("name")
#         print(name)
#         password = form.cleaned_data.get("password")
#         print(password)
#         user = authenticate(username=name, password=password)
#         print(user)
#         if user is not None:
#             print(user)
#             login(request, user=user)
#             return JsonResponse(form)
#         return JsonResponse(form)
#
#     def form_invalid(self, form):
#         response = super(ShowAccount, self).form_invalid(form)
#         if self.request.is_ajax():
#             return JsonResponse(form.errors, status=400)
#         else:
#             return response
#
#     def form_valid(self, form):
#         response = super(ShowAccount, self).form_valid(form)
#         if self.request.is_ajax():
#             print(form.cleaned_data)
#             data = {
#                 'message': "Successfully submitted form data."
#             }
#             return JsonResponse(data)
#         else:
#             return response

class ShowAccount(FormView):

    template_name = 'account/account.html'
    form_class = LoginForm
    success_url = '/account'
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return render(request, 'account/logout.html', {"user":self.request.user.username})
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
                return self.get(request)
        return HttpResponseRedirect(reverse('home'))

@csrf_exempt
def my_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))