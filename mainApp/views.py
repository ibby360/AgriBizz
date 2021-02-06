from django.shortcuts import render
import mainApp.models as app_model
from django.views import generic



# Create your views here.


def index(request):
    return render(request, 'index.html', {})

def farming_practice(request):
    return render(request, 'farming_practice.html', {})

def practice_detais(request):
    return render (request, 'practice_details.html', {})