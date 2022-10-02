from django.urls import path
from ordering.views import index

urlpatterns = [
    path('index/', index, name="index"),
]
