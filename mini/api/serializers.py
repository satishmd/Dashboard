from rest_framework import serializers
from .models import TeamDetails,TeamRecentMatches

class TeamDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = TeamDetails
		fields ='__all__'

class RecentMatchesSerializer(serializers.ModelSerializer):
	class Meta:
		model = TeamRecentMatches
		fields ='__all__'