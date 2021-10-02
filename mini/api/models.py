from django.db import models

# Create your models here.
class TeamDetails(models.Model):
    name=models.CharField(max_length=50)
    id=models.CharField(max_length=30,primary_key=True)
    img=models.ImageField(upload_to='images',default='default.img')
    is_favourite = models.BooleanField(default=False)

class BannerUrls(models.Model):
    id=models.CharField(max_length=30,primary_key=True)
    url=models.CharField(max_length=150)

class TeamRecentMatches(models.Model):
    team=models.CharField(max_length=10)
    umpires=models.CharField(max_length=150)
    result=models.TextField( null=False)
    man_of_the_match=models.CharField(max_length=50)
    id=models.CharField(max_length=30,primary_key=True)
    date=models.DateField(default=None)
    venue=models.TextField( null=False)
    competing_team=models.CharField(max_length=150)
    competing_team_logo=models.TextField( null=False)
    first_innings=models.CharField(max_length=150)
    second_innings=models.CharField(max_length=150)
    match_status=models.CharField(max_length=20)














































































































