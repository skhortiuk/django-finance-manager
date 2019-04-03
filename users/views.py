from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(UserLoginView, self).get(request, *args, **kwargs)


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(SignUp, self).get(request, *args, **kwargs)
