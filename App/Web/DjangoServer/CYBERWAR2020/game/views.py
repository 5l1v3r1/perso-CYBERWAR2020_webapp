from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect
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
    return render(request, 'game/WaitingPlayer.html')

#(QUENTIN)
def processturn(request):
    #Retrieve data from turn form received
        # DATA RECEIVED: Carte choisie, Carte défaussée, carte remise, carte(s) jouée(s) et nouveau CD
    #And push them into DB
    return render(request, 'game/WaitingPage.html')
