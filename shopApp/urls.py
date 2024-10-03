from django.contrib import admin
from django.urls import path,include
from django.conf import settings

api_prefix = settings.API_PREFIX

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{api_prefix}/', include([
        path('auth/', include('authentication.urls')),
        path('cart/', include('cart.urls')),
        path('category/', include('category.urls')),
        path('health/', include('health.urls')),
        path('payment/', include('payment.urls')),
        path('product/', include('product.urls')),
        path('search/', include('search.urls')),
    ])),
]
