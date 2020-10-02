from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('verify/', views.verify),
    path('send/', views.send),
]
