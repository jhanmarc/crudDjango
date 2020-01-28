from django.contrib import admin
from .models import Product, Favorite
# Register your models here.

# admin.site.register(Product)
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name','description' ,'categoria', 'price',)
    list_filter = ('categoria',)

@admin.register(Favorite)
class AdminFaverite(admin.ModelAdmin):
    list_display = ('user', 'product')
    list_filter = ('user', 'product',)