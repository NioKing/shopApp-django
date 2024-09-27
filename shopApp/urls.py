from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('cart/', include('cart.urls')),
    path('category/', include('category.urls')),
    path('health/', include('health.urls')),
    path('payment/', include('payment.urls')),
    path('product/', include('product.urls')),
    path('search/', include('search.urls')),
]
