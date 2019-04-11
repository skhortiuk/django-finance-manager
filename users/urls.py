from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetView, \
    PasswordResetDoneView,PasswordResetCompleteView, \
    PasswordResetConfirmView, LogoutView

from users.views import SignUp
from users.views import UserLoginView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html', ), name='home'),
    path('signup/', SignUp.as_view(template_name='registration/signup.html', ),
         name='signup'),
    path('login/', UserLoginView.as_view(
        template_name='registration/login.html'), name='login'),

    path('logout/',
         LogoutView.as_view(template_name='registration/logout.html'),
         name='logout'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='registration/password_res_form.html'),
         name='reset_password'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='registration/password_res_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='registration/password_res_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='registration/password_res_complete.html'),
         name='password_reset_complete'),
]
