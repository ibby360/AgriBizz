from django import urls
from django.contrib import admin
from django.urls import path, include
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

from blog.views import (farming_practice,
                        practice_details,
                        news_view)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),

    path('', views.index, name='index'),
    path('', farming_practice, name='farming_practice'),
    path('<int:pk>/', practice_details, name='practice_details'),
    path('', news_view, name='news'),
    path('', views.contact, name="contact")

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
