from email.headerregistry import Address
from itertools import zip_longest
from django.db import models
# from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField("Category Name", max_length=100)
    slug = models.SlugField(max_length=200, null = True, blank=True)
    date_added = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default=False)

    class Meta:
        # verbose_plural = "Categories"
        ordering = ('-date_added',)
        
    def __str__(self):
        return self.name


class Product(models.Model):
    title=models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(blank = True, null = True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000, null = True, blank=True)  # recuperer les images depuis sur internet
    slug = models.SlugField(max_length=200, null = True, blank=True)
    date_added = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default=False)

    class Meta:
        # verbose_name_plural = _("Products")
        ordering = ('-date_added',)

        
    def __str__(self):
        return self.title


class Order(models.Model):
    name=models.CharField('Order Name', max_length=100)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE, blank = True, null = True)
    date_orded = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        # verbose_plural="Orders"
        ordering = ('-date_orded',)  
        
    def __str__(self):
        return self.name


class Commande(models.Model):
    items = models.CharField('Items', max_length=100)
    total = models.CharField('Total', max_length=100)
    nom = models.CharField('Nom', max_length=100)
    email = models.EmailField('Email', max_length=100)
    Address = models.CharField('Address', max_length=100)
    ville = models.CharField('Ville', max_length=100)
    pays = models.CharField('Pays', max_length=100)
    zipcode = models.CharField('Zip Code', max_length=100)
    date_cmde = models.DateTimeField(auto_now_add = True)

    class Meta:
        # verbose_plural="Commandes"
        ordering = ('-date_cmde',)

    def __str__(self):
        return self.nom
    

    