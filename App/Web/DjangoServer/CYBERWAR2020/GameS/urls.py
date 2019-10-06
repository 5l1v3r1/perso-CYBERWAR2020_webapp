from django.urls import path

from . import views

app_name = 'GameS'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name = 'login'),
    path('connections', views.connections, name = 'connections'),
    path('confirmnewid', views.confirmnewid, name = 'confirmnewid'),

    path('toactifp', views.toactifp, name = 'toactifp'),
    path('processturn', views.processturn, name = 'processturn'),
    path('towaitingp', views.towaitingp, name='towaitingp')

]
