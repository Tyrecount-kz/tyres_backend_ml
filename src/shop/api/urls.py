from .views import ShopCarRUDView, ShopCarListAPIView

from django.contrib import admin
from django.urls import path,re_path
from users.api.views import ShopUserPostCreateAPIView,ShopUserWishlistAddView,ShopUserWishlistDeleteView

urlpatterns = [
    re_path(r'^$', ShopCarListAPIView.as_view(), name='car-list'),
    re_path(r'^(?P<pk>\d+)/$', ShopCarRUDView.as_view(), name='car-rud'),
    re_path(r'^new/$', ShopUserPostCreateAPIView.as_view(), name='car-new'),
    re_path(r'^(?P<pk>\d+)/wishlist-add/$', ShopUserWishlistAddView.as_view(), name='add-wishlist'),
    re_path(r'^(?P<pk>\d+)/wishlist-del/$', ShopUserWishlistDeleteView.as_view(), name='del-wishlist'),
]
