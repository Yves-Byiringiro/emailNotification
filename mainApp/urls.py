from django.urls import path
from mainApp import views as mainApp_views
from .import views


urlpatterns = [

    path('', mainApp_views.home, name='home' ),
    path('signup/', mainApp_views.signup, name='signup'),

]

