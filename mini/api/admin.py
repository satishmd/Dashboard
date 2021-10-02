from django.contrib import admin
from .models import TeamDetails,BannerUrls,TeamRecentMatches

# Register your models here.
admin.site.register(TeamDetails)
admin.site.register(BannerUrls)
admin.site.register(TeamRecentMatches)
