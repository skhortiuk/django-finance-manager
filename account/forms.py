from django import forms

from account.models import Account
from account.choices import TYPE_OF_CURRENCY_CHOICES


class AccountCreateForm(forms.ModelForm):
    type_of_currency = forms.ChoiceField(choices=TYPE_OF_CURRENCY_CHOICES)

    class Meta:
        model = Account
        fields = ['type_of_currency', 'count', 'is_active']
