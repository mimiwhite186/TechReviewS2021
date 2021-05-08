from django.urls import path
from . import view
urlpatterns = [
    path('', views.index, name='index'),
]