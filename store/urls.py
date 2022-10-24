from urllib import request
from . import views
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()

router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)

urlpatterns = router.urls