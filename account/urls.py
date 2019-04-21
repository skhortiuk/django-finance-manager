from django.urls import path

from account.views import AccountDetailView, AccountListView, \
    AccountDeleteView, AccountCreateView

urlpatterns = [
    path('', AccountListView.as_view(), name='account-list'),
    path('create/', AccountCreateView.as_view(),
         name='account-create'),
    path('delete/<int:pk>', AccountDeleteView.as_view(),
         name='account-delete'),
    path('<int:pk>', AccountDetailView.as_view(),
         name='account-detail'),
]
