from django.contrib import admin
from .models import Product, Promotion


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')


class PromotionAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'reduction')


admin.site.register(Product, ProductAdmin)
admin.site.register(Promotion, PromotionAdmin)
