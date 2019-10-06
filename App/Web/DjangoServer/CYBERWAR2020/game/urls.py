from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('', views.index, name='index'),

    path('toactifp', views.toactifp, name = 'toactifp'),
    path('processturn', views.processturn, name = 'processturn'),
    path('towaitingp', views.towaitingp, name='towaitingp')

]
