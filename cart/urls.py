from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.get_cart_data, name="get-cart-data"),
]
