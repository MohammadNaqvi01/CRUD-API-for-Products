from unicodedata import category
from rest_framework import serializers
from .models import *



        

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariant
        fields = '__all__' 
    
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorVariant
        fields = '__all__' 
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 
    


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','category','product_name','image','price','description','stock','color_type','size_type']
        depth = 1
    # def create(self, validated_data):
    #     category = validated_data.pop('category')
    #     products = Product.objects.create(**validated_data)
    #     for product in category:
    #         Category.objects.create(product=product, **category)
    #     return products