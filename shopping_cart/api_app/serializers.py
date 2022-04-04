from rest_framework import serializers
from .models import CartItem
from .calculate import calculateTotal


class CartItemSerializer(serializers.ModelSerializer):
    item = serializers.CharField(max_length=200)
    itemCategory = serializers.CharField(max_length=200)
    quantity = serializers.IntegerField(required=False, default=1)
    price = serializers.FloatField()

class CalculateSerializer(serializers.ModelSerializer)
    def calculateAmount(self, CartItem):

        total = calculateTotal.totalPricing(CartItem)

        return Response({"total": total['totalAmount'],"total tax" : total['totalTax'] })



    class Meta:
        model = CartItem
        fields = ('__all__')
