from django.urls import path
from . import views

urlpatterns = [
    path("", views.ferry_home, name="ferry_home"),
    path(
        "timetable/<str:country_departure>/<str:country_arrival>/",
        views.ferry_timetable,
        name="ferry_timetable",
    ),
]
