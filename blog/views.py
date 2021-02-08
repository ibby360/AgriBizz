from django.shortcuts import render

# Create your views here.

def farming_practice(request):
    return render(request, 'farming_practice.html', {})

def practice_details(request):
    return render (request, 'practice_details.html', {})