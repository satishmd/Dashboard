from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TeamDetailsSerializer,RecentMatchesSerializer
from .models import TeamDetails,TeamRecentMatches,BannerUrls
from django.http import JsonResponse

# Create your views here.
@api_view(['GET'])
def apiOverView(request):
    api_urls = {
		'List':'/teams-list/',
		# 'Detail View':'/task-detail/<str:pk>/',
		# 'Create':'/task-create/',
		# 'Update':'/task-update/<str:pk>/',
		# 'Delete':'/task-delete/<str:pk>/',
		}
    return JsonResponse(api_urls)

@api_view(['GET'])
def teamsList(request):
    teams = TeamDetails.objects.all()
    serializer = TeamDetailsSerializer(teams,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def teamRecentMatches(request,pk):
    recent_match=TeamRecentMatches.objects.filter(team=pk).order_by('date').reverse()
    team_url = BannerUrls.objects.get(id=pk)
    serializer = RecentMatchesSerializer(recent_match, many=True)
    details = {
    'url':team_url.url,
    'latest_match':serializer.data[0],
    'recent_matches':serializer.data,
    }
    return JsonResponse(details)
