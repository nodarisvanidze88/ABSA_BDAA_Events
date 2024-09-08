from django.db import models
from django.utils.timezone import now
class Event(models.Model):
    ORGANIZATORS = [('ABSA', 'ABSA'), ('BDAA', 'BDAA'),('ABSA/BDAA', 'ABSA/BDAA')]
    QUIZ_EXIST = [('YES', 'YES'), ('NO', 'NO')]
    STATUS_CHOICES = [('live', 'Live'), ('online', 'Online'), ('canceled', 'Canceled')]
    
    webinar_title = models.CharField(max_length=200)
    event_start_date = models.DateField(default=now)
    event_end_date = models.DateField(default=now)
    event_start_time = models.TimeField(blank=True, null=True)
    event_duration_time = models.PositiveIntegerField(blank=True, null=True)
    event_organisator = models.CharField(max_length=10, choices=ORGANIZATORS)
    quiz = models.CharField(max_length=3, choices=QUIZ_EXIST, default='NO')
    youtube_link = models.URLField(blank=True, null=True)
    price_for_members = models.FloatField(blank=True, null=True)
    price_for_non_members = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='live')
    
    class Meta:
        unique_together = ('webinar_title','event_start_date')

    def __str__(self):
        return self.webinar_title

class Quizes(models.Model):
    quizTitle = models.CharField(max_length=200)
    quiz_URL = models.URLField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='quizzes') 

    class Meta:
        unique_together = ('quizTitle','quiz_URL') 

    def __str__(self):
        return self.quizTitle 
