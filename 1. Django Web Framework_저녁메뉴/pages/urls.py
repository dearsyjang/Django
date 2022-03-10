from django.urls import path
from . import views


urlpatterns = [
    path('throw/', views.throw, name='throw'),
    path('dinner/', views.dinner, name='dinner'),
]
