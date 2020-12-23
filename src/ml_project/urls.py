"""ml_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django_registration.backends.one_step.views import RegistrationView
from users.forms import ShopUserForm
#from rest_framework_simplejwt.views import (
#    TokenObtainPairView,
#    TokenRefreshView,
#)
from users.api.views import ShopUserRUDView,ShopUserCreateAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('prediction/', include('ml_predict.api.urls')),
    path('auth/register/', RegistrationView.as_view(form_class=ShopUserForm, success_url="/"),name="django_registration_register"),
    path('auth/',include("django_registration.backends.one_step.urls")),
    path('auth/',include("django.contrib.auth.urls")),
    re_path(r'^api/cars/', include(('shop.api.urls','shop'),namespace='api-cars')),
    re_path(r'^api/users/', include(('users.api.urls','users'),namespace='api-users')),
    #re_path(r'^api/user/new', include(('users.api.urls','users'),namespace='api-users')),
    path('api/user/<int:pk>/',ShopUserRUDView.as_view(),name='user-detail' ),
    path('api/user/<int:pk>/new',ShopUserCreateAPIView.as_view(),name='user-create'),
    # Token Authorization
    # https://medium.aisultan.xyz/django-rest/django-rest-framework-jwt-authentication-94bee36f2af8
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
