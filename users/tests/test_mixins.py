from django.contrib.auth import get_user_model

from finance_manager.constants import USERNAME, PASSWORD

__all__ = ['SetUpUserMixin']


class SetUpUserMixin(object):

    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create_user(username=USERNAME,
                                             password=PASSWORD)
