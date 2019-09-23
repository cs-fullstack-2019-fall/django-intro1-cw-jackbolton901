from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('music/', views.music),
    path('ludacris/', views.ludacris),
    path('eminem/', views.eminem),
    path('donTrip/', views.donTrip),
]