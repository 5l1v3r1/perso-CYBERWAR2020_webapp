from django.shortcuts import render
from django.shortcuts import redirect

from django.urls import include
from django.http import HttpResponse
from django.template import loader

from saloon.models import Player
from saloon.models import Game

# Create your views here.

def index(request):
    return redirect("login:login")

def toactifp(request):
    request.session['actif'] = 1
    return render(request, 'game/ActifPlayer.html')

def towaitingp(request):
    request.session['actif'] = 0
    nb = [1, 2, 3, 4, 5]
    return render(request, 'game/WaitingPlayer.html', {"nb":nb})

#(QUENTIN)
def processactif(request):
    #Retrieve data from turn form received
        # DATA RECEIVED: Carte choisie, Carte défaussée, carte remise, carte(s) jouée(s) et nouveau CD
    #And push them into DB
    return render(request, 'game/WaitingPage.html')

#(QUENTIN)
def processwaiting(request):
    #Retrieve data from turn form received
        # DATA RECEIVED: Carte choisie, Carte défaussée, carte remise, carte(s) jouée(s) et nouveau CD
    #And push them into DB
    return render(request, 'game/WaitingPage.html')
