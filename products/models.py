from django.db import models

# Create your models here.
class Category(models.Model):
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
        
    def get_friendly_name(self):
        return self.friendly_name
    

class Product(models.Model):
    
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True) # TextField is not limited to a certain number of characters
    price = models.DecimalField(max_digits=6, decimal_places=2) # max_digits is the maximum number of digits allowed in the number, decimal_places is the number of decimal places to store
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True) # null=True, blank=True allows the field to be optional
    image_url = models.URLField(max_length=1024, null=True, blank=True) # URLField is a field for storing a URL
    image = models.ImageField(null=True, blank=True) # ImageField is a field for storing an image

    def __str__(self):
        return self.name
    
