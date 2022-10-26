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
    
    unit_price = serializers.IntegerField()
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


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']



# class CartItemSerializer(serializers.ModelSerializer):
#     product = SimpleProductSerializer()
#     total_price = serializers.SerializerMethodField(method_name='get_total_price')

#     def get_total_price(self, cart_item: CartItem):
#         return sum([item.quantity * item.product.unit_price for item in CartItem.objects.filter(cart_id=cart_item.cart_id)])

#     class Meta:
#         model = CartItem
#         fields = ['id','quantity','product']



# class CartSerializer(serializers.ModelSerializer):
#     id = serializers.UUIDField(read_only=True)
#     items = CartItemSerializer(many=True, read_only=True)
#     class Meta:
#         model = Cart
#         fields = ['id','items']

