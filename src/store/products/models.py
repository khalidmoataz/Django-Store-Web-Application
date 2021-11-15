from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.db.models.query import QuerySet
from Categories.models import MainCategory,SubCategory1,SubCategory2

import os
import random

def get_file_name_ext(filepath):
    base = os.path.basename(filepath)
    name , ext = os.path.splitext(base)
    return name, ext

def new_image_path(instance, file):
    newfilename = random.randint(1,6782393)
    name, ext   = get_file_name_ext(file)
    final_filename = '{k}{newfilename}{ext}'.format(k='K',newfilename=newfilename,ext=ext)
    return 'products/{final_filename}'.format(newfilename=newfilename,final_filename=final_filename)

class ProductQuerySet(models.query.QuerySet): # Custom Query Set
    def search(self, query):
        lookup = Q(title__icontains = query) | Q(highlight__icontains = query)
        return self.filter(lookup).distinct()
    def filter_query_items(self, filter_items): # Filtering System
        q = Product.objects.all()
        if 'Sort' in filter_items:
            if filter_items['Sort'] == 'lowtohigh':
                q = q.order_by('price')
            elif filter_items['Sort'] == 'hightolow':
                q = q.order_by('-price')
        if 'PriceMin' in filter_items:
            q = q.filter(price__gte = filter_items['PriceMin'])
        if 'PriceMax' in filter_items:
            q = q.filter(price__lte = filter_items['PriceMax'])
        return q

class QueryProducts(models.Manager): # Custom Manager
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

#    def get_featured(self):
#        print(self)
#        return self.get_queryset().filter(featured=True)
    def search(self, query):
        return self.get_queryset().search(query)
    def filter_items(self, query):
        return self.get_queryset().filter_query_items(query)

class ColorANDSizeANDQuantity(models.Model):
    Size  = models.CharField(max_length=120)
    Color = models.CharField(max_length=120)
    Quantity  = models.CharField(max_length=120)

class Product(models.Model):
    title              = models.CharField(max_length=120)
    highlight          = models.TextField()
    Brand              = models.CharField(max_length=140,blank=True)
    CSQ                = models.OneToOneField(ColorANDSizeANDQuantity,null=True, blank=True,on_delete= models.CASCADE)
    OfferPercent       = models.DecimalField(decimal_places=2, max_digits=20,blank=True,null=True)
    offerprice         = models.DecimalField(decimal_places=2, max_digits=20,blank=True,null=True)
    price              = models.DecimalField(decimal_places=2, max_digits=20)
    express            = models.BooleanField(default=False)
    Images             = models.ImageField(blank=True,null=True,upload_to=new_image_path)
    featured           = models.BooleanField(default=False)
    slug               = models.SlugField(blank=True)
    MainCategory       = models.ForeignKey(MainCategory, null=True, blank=True, on_delete= models.CASCADE,related_name='main')
    SubCategory1       = models.ForeignKey(SubCategory1, null=True, blank=True, on_delete= models.CASCADE,related_name='sub1')
    SubCategory2       = models.ForeignKey(SubCategory2, null=True, blank=True, on_delete= models.CASCADE,related_name='sub2')
    objects            = QueryProducts()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return "/shop/{slug}/".format(slug=self.slug)


def product_before_save(sender, instance, *args,**kwargs):
    if instance.OfferPercent is not None:
        instance.offerprice = instance.price - instance.price * (instance.OfferPercent/100)

    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_before_save, sender=Product)
