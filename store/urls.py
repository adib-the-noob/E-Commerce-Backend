from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:id>/', views.product_details),
    path('product/', views.product_list),
    path('collections/<int:pk>/', views.collection_details,name='collection_details'),
]   