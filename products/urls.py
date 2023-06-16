from django.urls import path
from . import views


# URL -> products/

urlpatterns = [
    path('', views.index),
    path('new', views.new)
]