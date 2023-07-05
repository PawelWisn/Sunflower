from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Product
from .serializers import ProductListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class ProductViewSet(ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ("size",)
    search_fields = ("name",)
