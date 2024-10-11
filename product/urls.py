from django.urls import path
from .views import *


urlpatterns = [
    path('', product_list_create, name="product-list-create"),
    path('<int:pk>/', product_retrieve_updata_delete, name="product-retrieve-update-destroy"),
]
