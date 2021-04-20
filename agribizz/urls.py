from django import urls
from django.contrib import admin
from django.urls import path, include
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

from  products.views import product_details, products
from blog.views import (farm_management, farming_practice,
                        practice_details,
                        news_view,
                        practice_intro,
                        news_details
                        )

handler404 = views.error_404

urlpatterns = [
    # Core
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),

    # mainApp
    path('', views.index, name='index'),
    path('search', views.search_page, name='search'),
    path('contact', views.contact, name="contact-view"),
    path('about', views.about_us, name='about'),
    path('thank_you', views.thank_you, name='thanks-page'),

    # Blog
    path('farmimng_practice', farming_practice, name='farming_practice'),
    path('farming_practice/<slug:slug>', practice_details, name='practice_details'),
    path('news', news_view, name='news-view'),
    path('practice_intro', practice_intro, name='practice_intro'),
    path('news/<slug:slug>', news_details, name="news_details"),
    path('farm_management', farm_management, name='farm_management'),

    # Products 
    path('products', products, name='products'),
    path('product_details/<slug:slug>', product_details, name='product_details')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
