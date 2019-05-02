import datetime

from django.db import models
from django.db.models import PROTECT
from django.contrib.auth import get_user_model


class TypeOfCurrency(models.Model):
    name = models.CharField(max_length=3)
    description = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'TypeCurrency'

    def __str__(self):
        return f'{self.name}'


class Account(models.Model):
    type_of_currency = models.ForeignKey(TypeOfCurrency,
                                         related_name='user_type_of_currency',
                                         on_delete=PROTECT)
    user = models.ForeignKey(get_user_model(), related_name='user_account',
                             on_delete=models.CASCADE)
    count = models.DecimalField(max_digits=12, decimal_places=2)
    created = models.DateTimeField(default=datetime.datetime.now)
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.type_of_currency} - {self.count}'
