from django.contrib import admin
from django.utils.html import format_html

from apps.models import Product, Blog


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'dec', 'price', 'image_tag')
    fields = ('title', 'dec', 'price', 'image')

    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','image_tag','dec','image')
    fields = ('title', 'category','image','dec')


    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')
