from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, \
    ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from account.models import Account
from account.forms import AccountCreateForm

__all__ = ['AccountListView', 'AccountCreateView', 'AccountDeleteView',
           'AccountDetailView']


class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = 'account_list.html'
    context_object_name = 'count_list'
    success_url = reverse_lazy('group_perm-list')

    def get_queryset(self):
        return self.request.user.user_account.all()


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    form_class = AccountCreateForm
    template_name = 'account_create.html'
    success_url = reverse_lazy('account-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    template_name = 'account_delete.html'
    success_url = reverse_lazy('account-list')


class AccountDetailView(DetailView, UpdateView):
    model = Account
    form_class = AccountCreateForm
    template_name = 'account_detail.html'

    def post(self, request, *args, **kwargs):
        user_id = self.request.POST['accountId']
        flag = not self.request.user.user_account.get(id=user_id).is_active
        self.request.user.user_account.filter(id=user_id).update(
            is_active=flag)
        return redirect('/counts/' + str(user_id))
