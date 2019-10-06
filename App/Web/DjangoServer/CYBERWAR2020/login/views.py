from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse

def index(request):
    #uestion = get_object_or_404(, pk=question_id)
    return HttpResponse("Hello, world. You're at the login index.")

