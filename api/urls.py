from django.urls import path

from .views import foobar, home

urlpatterns = [
    path('foobar/', foobar),
    path('', home),
]
