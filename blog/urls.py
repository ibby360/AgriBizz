from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('farming_practice.html', views.farming_practice, name="farming_practice"),
    path('practice_details.html', views.practice_details, name="practice_details"),
    path('news.html', views.news_view, name='news')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
