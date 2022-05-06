import csv
from random import randrange
from unicodedata import decimal
from django.db import models
from pathlib import Path
from shop.models import Customer,Product,Cart,Order
from django.contrib.auth.models import User
from faker import Faker
import random
import decimal
from django.core.management.base import BaseCommand, CommandError
class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):
        Customer.objects.all().delete()
        Product.objects.all().delete()
        Cart.objects.all().delete()
        Order.objects.all().delete()
        

        print("Table dropped successfully")

        fake = Faker()

        BASE_DIR = Path(__file__).resolve().parent.parent.parent
        print(BASE_DIR)
        data_link = str(BASE_DIR) + '/csv_file/movie.csv'

        with open(data_link, encoding='latin-1') as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for row in reader:
                product = Product.objects.create (
                    title=row[2],
                    genre=row[4],
                    poster=row[5],
                    score =float(row[3]),
                    price = int(decimal.Decimal(random.randrange(155,899))/100),
                    )
             
                    
              
                product.save()
             


        for row in range(60):
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = first_name+last_name,
            username = username[0]
            user = User.objects.create(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = fake.ascii_free_email(), 
            password = 'p@ssw0rd')
            customer = Customer.objects.create(user = user)
            customer.address = fake.address(),
            customer.address = str(customer.address[0])
            customer.save()


        
        print("data parsed")
        




            
            
    

   
