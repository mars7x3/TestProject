from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(ProductData)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    max_num = 1000
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title', 'category')
