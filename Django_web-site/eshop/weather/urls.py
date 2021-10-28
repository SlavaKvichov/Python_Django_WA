from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather),
    path('result/', views.weather_result)
]