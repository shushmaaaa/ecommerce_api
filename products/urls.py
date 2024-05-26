from django.urls import path,include
from .views import *
from rest_framework import routers

router =routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
# router.register(r'demo', DemoViewSet)

urlpatterns = [
    path('',include(router.urls)),
]

