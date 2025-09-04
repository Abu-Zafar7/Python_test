from django.urls import path
from .views import (
    PlayerListView, LikePlayerView, OverallRankingView,
    PositionRankingView, ClubRankingView, TopPlayersView,
    MostLikedPerClubView, RegisterUserView
)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('players/', PlayerListView.as_view(), name="player-list"), # List all players
    path('players/<int:pk>/like/', LikePlayerView.as_view(), name="like-player"), # Like a player

    # Rankings
    path('rankings/overall/', OverallRankingView.as_view(), name="overall-ranking"), # Overall ranking
    path('rankings/position/', PositionRankingView.as_view(), name="position-ranking"), # Position-based ranking
    path('rankings/club/', ClubRankingView.as_view(), name="club-ranking"), # Club-based ranking
    path('rankings/top/', TopPlayersView.as_view(), name="top-players"), # Top N players
    path('rankings/club/top/', MostLikedPerClubView.as_view(), name="most-liked-per-club"), # Most liked per club

     # Authentication endpoints
    path('auth/register/', RegisterUserView.as_view(), name='register'),  # user registration
    path('auth/token/', obtain_auth_token, name='api_token_auth'),  # obtain token for existing users
]
