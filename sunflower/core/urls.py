from rest_framework.routers import SimpleRouter
from .api import ProductViewSet
from django.urls import path, include


router = SimpleRouter()
router.register("products", ProductViewSet, "core_products")


urlpatterns = [
    path("", include(router.urls)),
]
