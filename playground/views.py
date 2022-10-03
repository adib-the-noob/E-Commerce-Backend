from django.shortcuts import render
from store.models import Product
from django.http import HttpResponse

def say_hello(request):
    query = Product.objects.all()
    for product in query:
        print(product)
    return render(request, 'hello.html', {'name': 'Mosh'})
