from django.shortcuts import render
import mainApp.models as app_model
from django.views import generic



# Create your views here.


def index(request):
    return render(request, 'index.html', {})
