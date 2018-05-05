from rest_framework import serializers
from orders.models import Order


# class OrderSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#
#     def create(self, validated_data):
#         return Order.objects.create(**validated_data)