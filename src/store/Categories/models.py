from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

class AllCategory(models.Model):
    name   = models.CharField(max_length=50)
    slug   = models.SlugField(blank=True)
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return "/c/{slug}".format(slug=self.slug)

class MainCategory(models.Model):
    name   = models.CharField(max_length=50)
    slug   = models.SlugField(blank=True)

    def get_absolute_url(self):
        return "/c/{slug}".format(slug=self.slug)

    def __str__(self):
        return self.name

class SubCategory1(models.Model):
    name   = models.CharField(max_length=50)
    slug   = models.SlugField(blank=True)
    parent = models.ForeignKey(MainCategory, null=True, blank=True,on_delete=models.CASCADE)
    def get_absolute_url(self):
        return "/c/{slug}".format(slug=self.slug)

    def __str__(self):
        return self.name

class SubCategory2(models.Model):
    name   = models.CharField(max_length=50)
    slug   = models.SlugField(blank=True)
    parent = models.ForeignKey(SubCategory1, null=True, blank=True,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return "/c/{slug}".format(slug=self.slug)

    def __str__(self):
        return self.name

def pre_save_cat(sender, instance, *args, **kwargs):
    AllCategory.objects.update_or_create(name = instance.name,slug=instance.slug)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        return instance.slug


pre_save.connect(pre_save_cat,sender=SubCategory1)
pre_save.connect(pre_save_cat,sender=SubCategory2)
pre_save.connect(pre_save_cat,sender=MainCategory)
