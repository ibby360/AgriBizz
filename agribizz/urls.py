from django import urls
from django.contrib import admin
from django.urls import path, include
from blog.views import farming_practice, practice_details
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('mainApp.urls')),
    path('', include('blog.urls')),
    # path('farming_practice/', farming_practice),
    path('', views.index, name='index'),
    path('<id>/', practice_details, name='practice_details')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
