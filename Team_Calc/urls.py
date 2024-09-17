from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_member_form, name='team_member_form'),
    path('submit/', views.submit_team_members, name='submit_team_members'),
    path('game-selection/', views.game_selection, name='game_selection'),
    path('generate-lineups/', views.generate_lineups, name='generate_lineups'),
]