from django.contrib import admin
# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'description', 'price']
    search_fields = ['title', 'price', 'description']
    list_editable = ['price', 'description']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
