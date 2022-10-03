from django.contrib import admin
from django.urls import path
from . import views
import debug_toolbar

admin.site.site_header = "Storefront Admin"
admin.site.site_title = "Storefront Admin Portal"



# URLConf
urlpatterns = [
    path('hello/', views.say_hello)
]
