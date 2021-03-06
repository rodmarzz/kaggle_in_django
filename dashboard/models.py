from django.db import models
from django.utils import timezone

class Dashboard(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    beginning = models.DateField(default=timezone.now)
    deadline = models.DateField()
    max_daily_uploads = models.IntegerField(default=5)
    wait_time_uploads = models.IntegerField(default=60) # Minutes
    train = models.FileField(upload_to='files', blank=True, null=True) # Big one
    test = models.FileField(upload_to='files', blank=True, null=True) # Small one
    private = models.FileField(upload_to='files', blank=True, null=True) # With predictions
    participants = models.IntegerField(default=0)
    author = models.TextField()

class Ranking(models.Model):
    container = models.ForeignKey('Dashboard', related_name='rankings', db_index=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    submission = models.FileField(blank=True, null=True)
    points = models.FloatField(default=0)
    
    class Meta:
        ordering = ['points']
