import datetime

from django.db import models

from django.contrib.auth import get_user_model


class Account(models.Model):
    type_of_currency = models.CharField(max_length=20)
    user = models.ForeignKey(get_user_model(), related_name='user_account',
                             on_delete=models.CASCADE)
    count = models.DecimalField(max_digits=12, decimal_places=2)
    created = models.DateTimeField(default=datetime.datetime.now)
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.type_of_currency} - {self.count}'
