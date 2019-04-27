from django import forms

from account.models import Account
from account.choices import Type_OF_CURRENCY_CHOISES


class AccountCreateForm(forms.ModelForm):
    type_of_currency = forms.ChoiceField(choices=Type_OF_CURRENCY_CHOISES)

    class Meta:
        model = Account
        fields = ['type_of_currency', 'count', 'is_active']
