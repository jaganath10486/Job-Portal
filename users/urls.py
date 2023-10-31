from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserView, FollwingView, FollowView, UserProfileView, unFollowView


urlpatterns = [
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'  ),
    path('register/', UserView.as_view() ),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh' ),
    # path('follwing/', FollwingView.as_view(), name='You are Follwing this'),
    path('follow/<int:id>', FollowView.as_view(), name='Follow View'),
    path('unfollow/<int:id>', unFollowView.as_view(), name='Un Follow View'),
    path('profile/', UserProfileView.as_view(), name='User Profile'),
]