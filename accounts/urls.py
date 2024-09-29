from django.urls import path
from .views import register, home
from .api_views import UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('api/register/', UserRegisterView.as_view(), name='api_register'),
    path('api/login/', UserLoginView.as_view(), name='api_login'),
    path('api/logout/', UserLogoutView.as_view(), name='api_logout'),
]
