
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
    permission_classes = [IsAuthenticated]   
    

    def get_queryset(self):
        product = Product.objects.all()
       
        return product

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
 
        if serializer.is_valid():
         
            try:
              
                serializer.save()
               
            except Exception as e:
                return Response({'error':str(e)})

            return Response({'data':serializer.data,'status':status.HTTP_201_CREATED})
        return Response({'error':serializer.errors, 'status':status.HTTP_400_BAD_REQUEST})


    def update(self, request, *args, **kwargs):
        product = self.get_object()
      
        serializer = ProductSerializer(product, data=request.data)      
        
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'status':status.HTTP_201_CREATED})
        return Response({'error':serializer.errors, 'status':status.HTTP_400_BAD_REQUEST})
   
     
    def partial_update(self, request, *args, **kwargs):
        product = self.get_object()
        serializer = ProductSerializer(product, data=request.data)      
        
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'status':status.HTTP_201_CREATED})
        return Response({'error':serializer.errors, 'status':status.HTTP_400_BAD_REQUEST})

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        msg = {'msg':f'Object with id:{product.id} has been deleted'}
        product.delete()
        return Response(msg)
