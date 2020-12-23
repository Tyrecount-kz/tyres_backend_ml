from .views import ShopUserListView,ShopUserPostCreateAPIView ,ShopUserRUDView,ShopUserPostsListView,ShopUserWishlistView
from django.urls import path,re_path,include
from rest_framework.routers import DefaultRouter
from users.api import views as wl


urlpatterns = [
    re_path(r'^$', ShopUserListView.as_view(), name='user-list'),
    re_path(r'^(?P<pk>\d+)/$', ShopUserRUDView.as_view(), name='user-detail'),
    re_path(r'^(?P<pk>\d+)/posts/$', ShopUserPostsListView.as_view(), name='user-posts'),
    re_path(r'^wishlist/$', ShopUserWishlistView.as_view(), name='user-wishlist'),
]
