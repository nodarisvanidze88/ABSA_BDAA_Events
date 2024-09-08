from django.db import models
from events.models import Event
from .file_upload_logic import eventbrite_file_upload
# Create your models here.
class EventReportFileUpload(models.Model):
    REPORT_SOURCE_CHOICES = [
        ('Eventbrite','Eventbrite'),
        ('Zoom','Zoom'),
        ('Quiz_Form', 'Quiz_Form'),
    ]
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    file = models.FileField(upload_to='event_reports/')
    report_source = models.CharField(max_length=30, choices=REPORT_SOURCE_CHOICES, default='Eventbrite')
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.event_name.webinar_title
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.process_file()

    def process_file(self):
        if self.file.name.endswith('.xlsx') and self.report_source == 'Eventbrite':
            eventbrite_file_upload(self.report_source,self.file.path)

        
    