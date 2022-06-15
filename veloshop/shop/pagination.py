from rest_framework.pagination import PageNumberPagination


class BannerPagination(PageNumberPagination):
    page_size = 1


class BikesPagination(PageNumberPagination):
    page_size = 9


class ScootersPagination(PageNumberPagination):
    page_size = 9