from .serializer import *
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from rest_framework.permissions import IsAuthenticated


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category:
            queryset = Product.objects.filter(category__category_name=category)
        else:
            queryset = Product.objects.all()
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'count': len(serializer.data), 'data': serializer.data})
    






          


   