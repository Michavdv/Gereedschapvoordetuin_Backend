from django.db import models


class Product(models.Model):
    ean_code = models.FloatField()
    product_id = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=3600)
    product_price = models.CharField(max_length=200)
    product_image = models.CharField(max_length=400)
    product_weight = models.CharField(max_length=200)
    product_height = models.CharField(max_length=200)
    product_length = models.CharField(max_length=200)
    product_width = models.CharField(max_length=200)
    product_url = models.CharField(max_length=400)
    unit_type = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.product_name
