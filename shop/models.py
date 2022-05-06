from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()

    # class Meta:
    #     db_table = 'customer'

    def __str__(self):
        return str(self.user.email)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.customer.save()

class LineItem(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    cart = models.ForeignKey('shop.Cart', on_delete=models.CASCADE)
    order = models.ForeignKey('shop.Order', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity},{self.product},{self.cart},{self.order},{self.created_date}'



class Product(models.Model):
    product_id = models.AutoField
    title = models.CharField(max_length=200)
    poster = models.URLField(max_length=1000)
    genre = models.CharField (max_length=1000)
    score = models.FloatField(default=0.0)
    price = models.DecimalField(max_digits=4, decimal_places=2) 
    address = models.CharField
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('shop/product_detail.html', args=[self.product_id])
    



class Cart(models.Model):
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'


    def __str__(self):
        return str(self.product)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    
    def __str__(self):
        return str(self.product)


