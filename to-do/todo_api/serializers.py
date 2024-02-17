from rest_framework import serializers
from .models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):
    # this is the meta data describing the model
    class Meta:
        model = Customer
        fields = ['name', 'code']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['item', 'amount', 'time']