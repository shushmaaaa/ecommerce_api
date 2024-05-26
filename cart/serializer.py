from rest_framework import serializers
from .models import *
from products.serializer import *

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        
    def validate(self, data):
        if data['quantity'] <=0:
            raise serializers.ValidationError("Quantity cannot be less than 1")
        return data
        
        
class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = '__all__'

        
    
        