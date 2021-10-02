from django.urls import path,re_path
from . import views

urlpatterns = [
	path('', views.apiOverView, name="api-overview"),
	path('teams/', views.teamsList, name="teams-list"),
	path('recent-matches/<str:pk>/', views.teamRecentMatches)
]