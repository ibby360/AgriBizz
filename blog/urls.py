from django.urls import path
from blog import views



urlpatterns = [
    path('farming_practice.html', views.farming_practice, name="practice"),
    path('practice_details.html', views.practice_details, name="practice_details")
]
