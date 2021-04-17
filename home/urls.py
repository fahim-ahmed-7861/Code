from django.contrib import admin
from django.urls import path

from .views import HomeView, home_index

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('test', home_index, name='home_func'),
]
