from django.urls import path
from .views import UserCreateView, ProfileView, LoginView, LogoutView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
