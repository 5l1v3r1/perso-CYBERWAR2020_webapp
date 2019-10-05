from django.urls import path

from . import views

app_name = 'GameS'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name = 'login'),
    path('connection', views.connection, name = 'connection'),
    path('confirmnewid', views.confirmnewid, name = 'confirmnewid')

]
