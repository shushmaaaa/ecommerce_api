from rest_framework import serializers
from .models import *


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    variant_type = VariantSerializer()
    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ['id','stock']
