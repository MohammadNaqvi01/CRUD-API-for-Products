from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'products', ProductView,basename="products")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
   
]



