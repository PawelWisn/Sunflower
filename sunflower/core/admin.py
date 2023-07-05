from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product


admin.site.unregister(Group)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "size", "quantity", "order")
    list_filter = ("size",)
    search_fields = ("name",)
