from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import redirect

from saloon.models import Player


def index(request):
    # flush cookies and sess vars from last connected
    request.session.flush()
    return render(request, 'login/Login.html')


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

        return render(request, 'saloon/Connected.html')

    #if not, return a page to confirm creation new IDplayer. change to JS?
    else:
        return render(request, 'login/ConfirmNewID.html', {'name': nomJ, 'firstName': prenomJ})


def confirmnewid(request):
    nomJ = request.POST.get("name", "")
    prenomJ = request.POST.get("firstName", "")

    newPlID = Player.objects.count() + 1
    Player(idPlayer= newPlID, name=nomJ, firstName=prenomJ).save()

    request.session['name'] = nomJ
    request.session['firstName'] = prenomJ
    request.session['idPlayer'] = newPlID

    return redirect("login:connections")
