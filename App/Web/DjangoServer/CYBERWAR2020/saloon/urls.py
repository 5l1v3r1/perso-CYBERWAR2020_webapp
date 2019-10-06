from django.urls import path

from . import views

app_name = 'saloon'
urlpatterns = [
    path('', views.index, name='index'),

]
