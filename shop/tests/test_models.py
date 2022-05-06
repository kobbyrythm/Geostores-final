from http import client
from django.test import TestCase, Client
from shop.models import Customer,Product,Cart,Order

class TestCustomerModel(TestCase):

    def SetUp(self):
        client= Client()
        response = client.get('/')
        self.assertEqual(response.status_code,200)