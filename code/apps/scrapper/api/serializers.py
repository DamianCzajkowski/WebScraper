from rest_framework import serializers
from apps.scrapper.models import Product, Scrapper


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'actual_price',)


class ScrapWebsiteSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Scrapper
        fields = ('url', 'product', )
