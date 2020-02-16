from django.urls import path
from . import views



urlpatterns = [
    path('', views.returning_same, name = 'returning'),
]