from django.urls import path
from . import views

urlpatterns = [
    path('', views.SubscribeView.as_view(), name = 'subscribe_form'),
    path('done/', views.DoneView.as_view(), name = 'done'),

]
