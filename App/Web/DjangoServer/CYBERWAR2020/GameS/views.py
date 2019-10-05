from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from .models import Player
from .models import Game

# Create your views here.

def index(request):
    return redirect("GameS:login")

def login(request):
    # flush cookies and sess vars from last connected
    request.session.flush()
    return render(request, 'GameS/Login.html')

def connections(request):

    if 'name' not in request.session:
        nomJ = request.POST.get("name", "")
        prenomJ = request.POST.get("firstName", "")

    else:
        nomJ = request.session['name']
        prenomJ = request.session['firstName']

    PlInDB = Player.objects.filter(name = nomJ).filter(firstName = prenomJ).count()

    #if player in DB, connection and retrieve IDplayer from DB.
    if(PlInDB != 0):
        id = Player.objects.get(name = nomJ, firstName = prenomJ).idPlayer
        request.session['name'] = nomJ
        request.session['firstName'] = prenomJ
        request.session['idPlayer'] = id

        return render(request, 'GameS/Connected.html')

    #if not, return a page to confirm creation new IDplayer. change to JS?
    else:
        return render(request, 'GameS/ConfirmNewID.html', {'name': nomJ, 'firstName': prenomJ})

def confirmnewid(request):
    nomJ = request.POST.get("name", "")
    prenomJ = request.POST.get("firstName", "")

    newPlID = Player.objects.count() + 1
    Player(idPlayer= newPlID, name = nomJ, firstName = prenomJ).save()

    request.session['name'] = nomJ
    request.session['firstName'] = prenomJ
    request.session['idPlayer'] = newPlID

    return redirect("GameS:connections")

def toactifp(request):
    return render(request, 'GameS/ActifPlayer.html')

#(QUENTIN)
#def processturn(request):
    #Retrieve data from turn form received
        # DATA RECEIVED: Carte choisie, Carte défaussée, carte remise, carte(s) jouée(s) et nouveau CD
    #And push them into DB
