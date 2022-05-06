from http import client
from django.test import TestCase, Client
from shop.models import Product,Cart,Order
from django.urls import reverse
from django.contrib.auth.models import User

class TestCustomerModel(TestCase):

    def setUp(self):
        self.data1 = Product.objects.create(name='django')


    def test_index_url(self):
    
        # Test  model URL reverse
        data = self.data1
        response = self.client.post(
            reverse('shop:index', args=[data.slug]))
        self.assertEqual(response.status_code, 200)


class TestProductsModel(TestCase):
    def setUp(self):
        Product.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                            slug='django-beginners', price='20.00', image='django')
        self.data2 = Product.products.create(category_id=1, title='django advanced', created_by_id=1,
                                             slug='django-advanced', price='20.00', image='django', is_active=False)