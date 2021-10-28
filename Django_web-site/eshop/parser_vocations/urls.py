from django.urls import path
from . import views

urlpatterns = [
    path('', views.parser),
    path('search/', views.parser_search)
]