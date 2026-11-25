from django.db import models

# Create your models here.
class productDb(models.Model):
    product_name = models.CharField(max_length=100)
    Product_code = models.IntegerField()
    Category = models.CharField()
    price = models.IntegerField()
    stock_quantity=models.IntegerField()

    def __str__(self):
        return self.product_name