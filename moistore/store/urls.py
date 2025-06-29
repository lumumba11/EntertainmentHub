# store/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('account/', views.account_view, name='account'),
    path('add-product/', views.add_product_view, name='add_product'),
   # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('contact/', views.contact_view, name='contact'),
  #  path('privacy/', views.privacy_view, name='privacy'),
    path('privacy/', views.privacy_view, name='privacy'),

    #path('login/', views.login_view, name='login_view'),
]
