from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('', views.index, name='index'),

    path('toactifp', views.toactifp, name = 'toactifp'),
    path('processactif', views.processactif, name = 'processactif'),
    path('towaitingp', views.towaitingp, name='towaitingp'),
    path('processwaiting', views.processwaiting, name = 'processwaiting')

]
