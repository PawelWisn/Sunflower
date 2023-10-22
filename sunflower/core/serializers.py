from rest_framework.serializers import ModelSerializer, CharField
from .models import Product


class ProductListSerializer(ModelSerializer):
    size = CharField(source="get_size_display")

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "quantity",
            "picture",
            "size",
            "order",
        )
