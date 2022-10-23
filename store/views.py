from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Collection, Product
from .serializers import ProductSerializer,CollectionSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Count


# Create your views here.

@api_view(['GET','PUT','DELETE'])
def product_details(request,id):
    product = get_object_or_404(Product,id=id)  
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)
        
    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        if product.orderitems.count() > 0:
            return Response({'error': "Product cannot be deleted, because it is assoicated with an order"},status=status.HTTP_400_BAD_REQUEST)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def product_list(request):
    if request.method == "GET":
        product = Product.objects\
            .select_related('collection')\
            .all()
        serializer = ProductSerializer(product, many=True,context={'request':request})
        return Response(serializer.data)


    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)




