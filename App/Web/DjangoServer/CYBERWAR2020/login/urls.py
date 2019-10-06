from . import views
from django.urls import path

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('connections', views.connections, name='connections'),
    path('confirmnewid', views.confirmnewid, name='confirmnewid'),

]
