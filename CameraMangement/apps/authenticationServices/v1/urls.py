from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()    //only use for view set not use for APIView
# router.register('authenticator', views.LoginUserApi, basename="authenticator")

urlpatterns = [
    path('authenticator/login/',views.LoginUserApi.as_view({'post': 'login'}) , name='login'),
    path('authenticator/register/',views.LoginUserApi.as_view({'post': 'register'}) , name='register'),
]