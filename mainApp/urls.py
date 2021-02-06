from django.urls import path
from . import views


urlpatterns = [
    path('index.html', views.index, name="index"),
    path('farming_practice.html', views.farming_practice, name="practice"),
    path('practice_details.html', views.practice_detais, name="practice_details")
]
