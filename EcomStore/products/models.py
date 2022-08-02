from django.db import models
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200 , blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.category_name





class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)
    
    def __str__(self):
        return self.color_name

class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.size_name


    
class Product(models.Model):
    category = models.ForeignKey(Category,  related_name='products',  on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/products', default='', null =True,)
    price = models.CharField(max_length=20)
    description = models.TextField()
    stock = models.IntegerField(default=100)
    
    color_type = models.ForeignKey(ColorVariant , blank=True, null=True , on_delete=models.PROTECT)
    size_type = models.ForeignKey(SizeVariant , blank=True, null=True , on_delete=models.PROTECT)
    
    class Meta:
        pass
        
    
    def __str__(self):
        return self.product_name
           