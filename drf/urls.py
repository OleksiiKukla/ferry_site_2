from django.urls import path, include
from .views import FerryApiView, PortViewsSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ports', PortViewsSet, basename='ports')
#print(router.urls)  # список всех url

urlpatterns = [
    path('ferry/', FerryApiView.as_view()),
    path('', include(router.urls)),  #http://127.0.0.1:8000/api/ports/ + 1/
]
