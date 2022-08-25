from django.urls import path, include
from .views import FerryViewSet, PortViewsSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'ports', PortViewsSet, basename='ports')
router.register(r'ferries', FerryViewSet)
#print(router.urls)  # список всех url

urlpatterns = [
    path('authorization/', include('rest_framework.urls')),  # Авторизация
    path('', include(router.urls)),  #http://127.0.0.1:8000/api/ports/ + 1/
]
