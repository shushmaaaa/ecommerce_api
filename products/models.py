from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
       self.slug = slugify(self.category_name)
       super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name
    
class ProductVariantType(models.Model):
    variant_type = models.CharField(max_length=100)
    variant_name = models.ForeignKey('ProductVariant', on_delete=models.PROTECT)

    def __str__(self):
        return self.variant_type

class ProductVariant(models.Model):
    variant_name = models.CharField(max_length=100)

    def __str__(self):
        return self.variant_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    product_name =models.CharField(max_length=100)
    image= models.ImageField(upload_to='static/products')
    price = models.CharField(max_length= 20)
    description = models.TextField()
    stock= models.IntegerField(default=100)
    variant_type= models.ForeignKey(ProductVariantType, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='static/products')

    def __str__(self):
        return self.product.product_name




