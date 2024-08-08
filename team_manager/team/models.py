from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Coaches(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='team')
    last_team_id = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='last_team')
    photo = models.ImageField(upload_to='player_photos/', blank=True, null=True)
    position = models.CharField(max_length=100)
    age = models.IntegerField()
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Metric(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='metrics')
    date = models.DateField()
    speed = models.FloatField()
    stamina = models.FloatField()
    passing_accuracy = models.FloatField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name} '
    
    
class Lineup(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='lineups')
    date = models.DateField()
    formation = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, related_name='lineups')