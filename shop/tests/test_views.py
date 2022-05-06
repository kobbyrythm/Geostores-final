from unittest import skip
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from importlib import import_module
from shop.models import Customer, Product,Cart,Order
from shop.views import index
from django.conf import settings

@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_exmaple(self):
        pass

class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
       
#Testing the host
    def test_url_allowed_hosts(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.c.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
       
        # Test homepage response status
       
        response = self.c.get('/index')
        self.assertEqual(response.status_code, 200)

    def test_product_list_url(self):
       
        # Test cover page response status
       
        response = self.c.get(
            reverse('shop:product_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
    
        #Test items response status
        
        response = self.c.get(
            reverse('shop:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
       
        # Example: code validation, search HTML for text
       
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Geostore</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
