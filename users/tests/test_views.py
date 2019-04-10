from django.test import TestCase
from django.urls import reverse

from finance_manager.constants import PASSWORD, USERNAME
from users.tests.test_mixins import SetUpUserMixin


class LoginViewTest(SetUpUserMixin, TestCase):

    def setUp(self):
        self.client.login(username=USERNAME, password=PASSWORD)

    def test_redirect_when_user_logged_in(self):
        response = self.client.post(reverse('login'), {'username': USERNAME,
                                                       'password': PASSWORD})

        self.assertEqual(response.status_code, 302)

    def test_redirect_to_home_page_if_the_user_tries_to_login(self):
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
