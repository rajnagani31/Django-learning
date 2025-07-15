from django.db import models

# model Proxy
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
class Product2(Product):
    class Meta:
        proxy=True
        ordering=['-price']    

    def price(self):
            return self.price >= 500