from django.urls import path

from . import views

app_name = 'GameS'
urlpatterns = [
    path('connections', views.connections, name = 'connections'),
    path('confirmnewid', views.confirmnewid, name = 'confirmnewid')

]
