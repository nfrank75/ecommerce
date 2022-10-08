from django.contrib import admin
from .models import Product, Category, Order, Commande
# Register your models here.

admin.site.site_header = "E_commerce Web Site"
admin.site.site_title = "Shop Administration"
admin.site.index_title = "Shop Manager"


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'date_added'
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price',
        'description',
        'category',
        'slug',
        'date_added'
    )
    search_fields = (
        'title',
    )
    list_editable = (
        'price',
        'category'
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product',
        'date_orded'
    )


class CommandeAdmin(admin.ModelAdmin):
    list_display = (
        'items',
        'total',
        'nom',
        'email',
        'Address',
        'ville',
        'pays',
        'zipcode',
        'date_cmde',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Commande, CommandeAdmin)

