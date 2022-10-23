from rest_framework import serializers
from decimal import Decimal
from store.models import Product,Collection


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)



class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2,source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='get_price_with_tax')
    # serializer.PrimaryKeyRelatedField(queryset=Collection.objects.all()) will return the id of the collection
    # collection = serializers.StringRelatedField()
    collection = serializers.HyperlinkedRelatedField(
        queryset = Collection.objects.all(),
        view_name = 'collection_details',
    )

    def get_price_with_tax(self,prouct : Product):
        return prouct.unit_price * Decimal(1.2)