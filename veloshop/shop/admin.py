from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_image',)
    list_display_links = ('id', )
    ordering = ('id',)

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='65', height='60'")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'select',)
    list_display_links = ('id', 'select', )
    ordering = ('id',)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id', )
    ordering = ('id',)


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email',)
    list_display_links = ('id', 'surname', 'email', )
    ordering = ('id','surname', 'email',)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'qty', 'price', 'category', 'get_image',)
    list_display_links = ('id', 'name', 'price',)
    ordering = ('id', 'name', 'price',)

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='65', height='60'")


class BuyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username',)
    list_display_links = ('id', 'username',)
    ordering = ('id', 'username',)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'item', 'qty', 'cost',)
    list_display_links = ('id', 'user_name', 'item',)
    ordering = ('id', 'user_name', 'item',)


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'order',)
    list_display_links = ('id', 'owner', 'order',)
    ordering = ('id', 'owner', 'order',)


admin.site.register(Banner, BannerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Cart, CartAdmin)
