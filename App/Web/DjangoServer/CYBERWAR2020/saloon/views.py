from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from saloon.models import Player
from saloon.models import Game

# Create your views here.

def index(request):
    return redirect("login:login")
