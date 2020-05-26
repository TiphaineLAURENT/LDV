from django.test import TestCase, Client
from django.urls import reverse

from shopping.models import Vetement, User
from . import STATUS_CODE

class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.username = "user"
        self.password = "password"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_get_not_logged(self):
        response = self.client.get(self.url, follow=True)

        self.assertEqual(response.status_code, STATUS_CODE.OK)

    def test_get_logged(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(self.url, follow=True)

        self.assertEqual(response.status_code, STATUS_CODE.OK)

        self.assertTrue(hasattr(response, 'redirect_chain'))
        self.assertEqual(response.redirect_chain[-1][0], reverse('shop'))
