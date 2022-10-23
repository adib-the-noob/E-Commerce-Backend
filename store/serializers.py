from rest_framework import serializers
from decimal import Decimal
from store.models import Product,Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','unit_price','price_with_tax','collection']
    
    price_with_tax = serializers.SerializerMethodField(method_name='get_price_with_tax')
    # # serializer.PrimaryKeyRelatedField(queryset=Collection.objects.all()) will return the id of the collection
    # # collection = serializers.StringRelatedField()
    
    
    # This is for Collection of the products
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset = Collection.objects.all(),
    #     view_name = 'collection_details',
    # )

    def get_price_with_tax(self,prouct : Product):
        return prouct.unit_price * Decimal(1.2)
