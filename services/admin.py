from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'status', 'created_at', 'updated_at',)
    list_display_links = ('id', 'title',)
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 50
    list_editable = ('price',)
    search_fields = ('price', 'title',)
    list_filter = ('price', 'status', 'created_at', 'updated_at',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'tx_ref', 'total', 'status', 'created_at',)
    list_display_links = ('id', 'tx_ref',)
    list_per_page = 50
    list_editable = ('status',)
    search_fields = ('full_name', 'total',)
    list_filter = ('total', 'status', 'created_at',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.unregister(Group)  # remove Group objects from admin page:  under[Authentication and Authorization]
