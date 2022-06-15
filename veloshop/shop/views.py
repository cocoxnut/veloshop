from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from . import serializers
from . import models
from . import pagination


class BannerViewSet(ModelViewSet):
    queryset = models.Banner.objects.all()
    serializer_class = serializers.BannerSerializer
    pagination_class = pagination.BannerPagination

class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class AboutViewSet(ModelViewSet):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer


class RegistrationViewSet(ModelViewSet):
    queryset = models.Registration.objects.all()
    serializer_class = serializers.RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductsViewSet(ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer
    pagination_class = pagination.BannerPagination


class BuyerViewSet(ModelViewSet):
    queryset = models.Buyer.objects.all()
    serializer_class = serializers.BuyerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrderItemViewSet(ModelViewSet):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer


class CartViewSet(ModelViewSet):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer