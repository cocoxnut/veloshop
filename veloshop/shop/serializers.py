from rest_framework.serializers import ModelSerializer

from .models import *

class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class BuyerSerializer(ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
