from Gereedschapvoordetuin_Backend.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    ean_code = serializers.FloatField()
    product_id = serializers.CharField(max_length=200)
    product_name = serializers.CharField(max_length=200)
    product_description = serializers.CharField(max_length=400)
    product_price = serializers.FloatField()
    product_image = serializers.CharField(max_length=400)
    product_weight = serializers.CharField(max_length=200)
    product_height = serializers.CharField(max_length=200)
    product_length = serializers.CharField(max_length=200)
    product_width = serializers.CharField(max_length=200)
    product_url = serializers.CharField(max_length=400)

    class Meta:
        model = Product
        fields = ['ean_code', 'product_id', 'product_name', 'product_description', 'product_price', 'product_image',
                  'product_weight',
                  'product_height', 'product_length', 'product_width', 'product_url']