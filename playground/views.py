from django.shortcuts import render
from store.models import Product
# Create your views here.

def home(request):
    queryset = Product.objects.all()
    
    return render(request,'home.html')