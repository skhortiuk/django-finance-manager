from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

PASSWORD = 'qwerty123N'
USERNAME = 'insayrex'

__all__ = ['LoginViewTest']


class LoginViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create_user(username=USERNAME,
                                             password=PASSWORD)

    def setUp(self):
        self.client.login(username=USERNAME, password=PASSWORD)

    def test_redirect_when_user_logged_in(self):
        response = self.client.post(reverse('login'), {'username': USERNAME,
                                                       'password': PASSWORD})

        self.assertEqual(response.status_code, 302)

    def test_redirect_to_home_page_if_the_logged_on_user_tries_to_login(self):
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
