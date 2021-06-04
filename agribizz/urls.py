from os import name
from django import urls
from django.contrib import admin
from django.urls import path, include
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import (customer, dashboard, delete_product, products, register_page,
                            login_page, logout_user, sell_product, update_order, update_product
                            )
from crops.views import crops, crop_details
from marketing.views import market, order, post_product, single_product

from blog.views import (farming_practice,
                        practice_details,
                        news_view,
                        practice_intro,
                        news_details
                        )
from shop.views import checkout

handler404 = views.error_404

urlpatterns = [
    # Core
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),

    # Cart
    path('cart/', include('cart.urls', namespace='cart')),
    
    # Orders
    path('orders/', include('orders.urls', namespace='orders')),

    # Payment
    path('payment/', include('payment.urls', namespace='payment')),
    
    #Shop App
    path('shop/', include('shop.urls', namespace='shop')),

    # mainApp
    path('', views.index, name='index'),
    path('search', views.search_page, name='search'),
    path('contact', views.contact, name="contact-view"),
    path('about', views.about_us, name='about'),
    path('thank_you', views.thank_you, name='thanks-page'),

    # Blog
    path('farming_practice', farming_practice, name='farming_practice'),
    path('farming_practice/<slug:slug>',
         practice_details, name='practice_details'),
    path('news', news_view, name='news-view'),
    path('practice_intro', practice_intro, name='practice_intro'),
    path('news/<slug:slug>', news_details, name="news_details"),
    path('market', market, name='market'),

    # Crops
    path('crops', crops, name='crops'),
    path('crop_details/<slug:slug>', crop_details, name='crop_details'),

    # Marketing
    path('market', market, name='market'),
    path('post_product', post_product, name='post_product'),
    path('product/<int:pk>', single_product, name='single_product'),
    path('product_order/<int:pk>', order, name='product_order'),

    # Accounts
    path('register/', register_page, name="register"),
    path('login/', login_page, name="login"),
    path('logout/', logout_user, name="logout"),
    path('dashboard/', dashboard, name='dashboard'),
    path('products/', products, name='products'),
    path('delete_product/<str:pk>', delete_product, name='delete_product'),
    path('update_product/<str:pk>', update_product, name='update_product'),
    path('customer', customer, name='customer'),
    path('sell_product', sell_product, name='sell_product'),
    path('update_order/<str:pk>', update_order, name='update_order'),


    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
