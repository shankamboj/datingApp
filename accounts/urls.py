from django.urls import path
from .views import register, home, dashboard
from .api_views import UserRegisterView, UserLoginView, UserLogoutView, HelloWorldView
from .views import UserProfileRegisterView, AllUsersView

urlpatterns = [
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('api/register/', UserRegisterView.as_view(), name='api_register'),
    path('api/login/', UserLoginView.as_view(), name='api_login'),
    path('api/logout/', UserLogoutView.as_view(), name='api_logout'),
    path('api/hello/', HelloWorldView.as_view(), name='api_hello'),  # New endpoint
    path('api/register-profile/', UserProfileRegisterView.as_view(), name='api_register_profile'),  # New registration endpoint
    path('api/all-users/', AllUsersView.as_view(), name='api_all_users'),
]
