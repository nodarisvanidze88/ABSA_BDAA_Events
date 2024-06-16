from django.db import models
from django.utils.timezone import now
# Create your models here.
class Event(models.Model):
    ORGANIZATORS = [('ABSA', 'ABSA'), ('BDAA', 'BDAA'),('ABSA/BDAA', 'ABSA/BDAA')]
    QUIZ_EXIST = [('YES', 'YES'), ('NO', 'NO')]
    
    webinar_title = models.CharField(max_length=200)
    event_start_date = models.DateField(default=now)
    event_end_date = models.DateField(default=now)
    event_start_time = models.TimeField(blank=True, null=True)
    event_duration_time = models.PositiveIntegerField(blank=True, null=True)
    event_organisator = models.CharField(max_length=10, choices=ORGANIZATORS)
    quiz = models.CharField(max_length=3, choices=QUIZ_EXIST, default='NO')
    quiz_URL = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    price_for_members = models.FloatField(blank=True, null=True)
    price_for_non_members = models.FloatField(blank=True, null=True)
    
    class Meta:
        unique_together = ('webinar_title','event_start_date')

    def __str__(self):
        return self.webinar_title

    
