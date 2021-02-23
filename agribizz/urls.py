from django.contrib import admin
from django.urls import path, include
from blog.views import farming_practice
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainApp.urls')),
    path('', include('blog.urls')),
    # path('farming_practice/', farming_practice),
    path('', views.index, name='index'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
