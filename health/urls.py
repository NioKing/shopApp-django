from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('health_check.urls'))
]
