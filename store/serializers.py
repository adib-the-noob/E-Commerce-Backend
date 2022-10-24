from pyexpat import model
from rest_framework import serializers
from decimal import Decimal
from store.models import Product,Collection, Review



class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','slug','inventory','unit_price','price_with_tax','collection']
    
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

    
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','date','name','description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        review = Review.objects.create(product_id=product_id, **validated_data)
        return review