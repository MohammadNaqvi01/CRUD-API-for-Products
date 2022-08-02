
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status




class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]   
    

    def get_queryset(self):
        product = Product.objects.all()
       
        return product

    def create(self, request, *args, **kwargs):
        data = request.data
    
        try:
          
            new_product = Product.objects.create(category=Category.objects.get(category_name=data['category']),
            product_name=data['product_name'],image=data['image'],price=data['price'],description=data['description'],
            stock=data['stock'],color_type=ColorVariant.objects.get(color_name=data['color_type']),
            size_type=SizeVariant.objects.get(size_name=data['size_type']))
            new_product.save()
            serializer = ProductSerializer(new_product)
            return Response({'data':serializer.data, 'status':status.HTTP_201_CREATED})
        except Exception as e:
            return Response({'status':repr(e)})

    def update(self, request, *args, **kwargs):
        product = self.get_object()
      
        serializer = ProductSerializer(product, data=request.data)      
        
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'status':status.HTTP_201_CREATED})
        return Response({'error':serializer.errors, 'status':status.HTTP_400_BAD_REQUEST})
   
     
    def partial_update(self, request, *args, **kwargs):
        data = request.data
        product = self.get_object()
        try:
          
            product.category=Category.objects.get(category_name=data['category'])
            product.color_type=ColorVariant.objects.get(color_name=data['color_type'])
            product.size_type=SizeVariant.objects.get(size_name=data['size_type'])
        except KeyError:
           pass  

        product.product_name=data.get('product_name',product.product_name)
        product.image=data.get('image', product.image)
        product.price=data.get('price',product.price)
        product.description=data.get('description', product.description)
        product.stock=data.get('stock', product.stock)
          
        product.save()
        serializer = ProductSerializer(product)
        return Response({'data':serializer.data, 'status':status.HTTP_201_CREATED})
     

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        msg = {'msg':f'Object with id:{product.id} has been deleted'}
        product.delete()
        return Response(msg)
