from blog.views import farming_practice, news_view, practice_details
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
    path('farmimng_practice.html', farming_practice, name='farming_practice'),
    path('detail/<slug:slug>', practice_details, name='practice_details'),
    path('contact.html', views.contact, name="contact-view"),
    path('news.html', news_view, name='news-view'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
