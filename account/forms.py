from django import forms

from account.models import Account


class AccountCreateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['type_of_currency', 'count', 'is_active']
