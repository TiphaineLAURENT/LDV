from django.test import TestCase, Client
from django.urls import reverse

from shopping.models import Vetement, User
from . import STATUS_CODE

class DetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "/shopping/{id}"
        self.username = "user"
        self.password = "password"
        self.user = User.objects.create_user(username=self.username, password=self.password)

        self.vetement = Vetement.objects.create(name="name", description="description", price=50)

    def test_get_not_logged(self):
        response = self.client.get(self.url.format(id=self.vetement.id), follow=True)

        self.assertEqual(response.status_code, STATUS_CODE.OK)
        self.assertEqual(self.user.items.count(), 0)

        self.assertTrue(hasattr(response, 'redirect_chain'))
        self.assertEqual(response.redirect_chain[-1][0].split("?")[0], reverse('login'))
        self.assertEqual(len(response.redirect_chain), 1)

    def test_get_logged(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(self.url.format(id=self.vetement.id))

        self.assertEqual(response.status_code, STATUS_CODE.OK)
        self.assertEqual(response.context['vetement'], self.vetement)

        self.assertEqual(self.user.items.count(), 1)
        self.assertEqual(self.user.items.first().vetement, self.vetement)

    def test_get_logged_invalid_id(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(self.url.format(id=42))

        self.assertEqual(response.status_code, STATUS_CODE.NOT_FOUND)
        self.assertFalse(response.context.get('vetement', False))

        self.assertEqual(self.user.items.count(), 0)

    def test_post_not_logged(self):
        response = self.client.post(self.url.format(id=42), follow=True)

        self.assertEqual(response.status_code, STATUS_CODE.OK)

        self.assertTrue(hasattr(response, 'redirect_chain'))
        self.assertEqual(response.redirect_chain[-1][0].split("?")[0], reverse('login'))
        self.assertEqual(len(response.redirect_chain), 1)

    def test_post_logged_invalid_id(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.post(self.url.format(id=42), follow=True)

        self.assertEqual(response.status_code, STATUS_CODE.METHOD_NOT_ALLOWED)

    def test_post_logged(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.post(self.url.format(id=self.vetement.id), follow=True)

        self.assertEqual(response.status_code, STATUS_CODE.METHOD_NOT_ALLOWED)
