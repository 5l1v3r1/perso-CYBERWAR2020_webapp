from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from .models import Player
from .models import Game

# Create your views here.

def index(request):
    return HttpResponse("c'est une bonne idée!")

def login(request):
    return render(request, 'GameS/Login.html')

def connections(request, nomJ = None, prenomJ = None):
    if not nomJ or prenomJ:
        nomJ = request.POST.get("name", "")
        prenomJ = request.POST.get("firstName", "")

    PlInDB = Player.objects.filter(name = nomJ).filter(firstName = prenomJ).count()

    #if player in DB, connection and retrieve IDplayer from DB.
    if(PlInDB != 0):
        id = Player.objects.get(name = nomJ, firstName = prenomJ).idPlayer
        return render(request, 'GameS/Connected.html',  {'idPlayer': id, 'name': nomJ, 'firstName': prenomJ})
    #if not, return a page to confirm creation new IDplayer. change to JS?
    else:
        return render(request, 'GameS/ConfirmNewID.html', {'name': nomJ, 'firstName': prenomJ})

def confirmnewid(request):
    nJ = request.POST.get("name", "")
    pJ = request.POST.get("firstName", "")

    newPlID = Player.objects.count() + 1
    Player(idPlayer= newPlID, name = nJ, firstName = pJ).save()

    return redirect("GameS:connections", nomJ = nJ, prenomJ = pJ)
