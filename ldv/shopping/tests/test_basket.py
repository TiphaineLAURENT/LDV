from django.test import TestCase, Client

from shopping.models import Vetement, User, Item
from . import STATUS_CODE

class DetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.csrf_client = Client(enforce_csrf_checks=True)
        self.url = "/shopping/basket"
        self.username = "user"
        self.password = "password"
        self.user = User.objects.create_user(username=self.username, password=self.password)

        self.vetement = Vetement.objects.create(name="name", description="description", price=50)
        self.item = Item.objects.create(user=self.user, vetement=self.vetement)

    def test_get_not_logged(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, STATUS_CODE.REDIRECTED)

    def test_get_logged(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, STATUS_CODE.OK)

        context = response.context
        self.assertEqual(len(context['items']), 1)

    def test_post_not_logged_no_csrf(self):
        response = self.csrf_client.post(self.url)

        self.assertEqual(response.status_code, STATUS_CODE.FORBIDDEN)

    def test_post_logged_no_csrf(self):
        self.csrf_client.login(username=self.username, password=self.password)

        response = self.csrf_client.post(self.url)

        self.assertEqual(response.status_code, STATUS_CODE.FORBIDDEN)

    def test_post_not_logged(self):
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, STATUS_CODE.REDIRECTED)

    def test_post_logged(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.post(self.url)

        self.assertEqual(response.status_code, STATUS_CODE.REDIRECTED)
        self.assertEqual(self.user.items.count(), 1)

    def test_post_logged(self):
        self.client.login(username=self.username, password=self.password)

        data = {
            self.item.id: 'on'
        }
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, STATUS_CODE.REDIRECTED)
        self.assertEqual(self.user.items.count(), 0)
        self.assertFalse(self.user.items.count())
