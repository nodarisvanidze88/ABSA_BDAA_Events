from django.contrib import admin
from django import forms
from .models import Event
from django_flatpickr.widgets import TimePickerInput
from django_flatpickr.schemas import FlatpickrOptions


class EventAdminForm(forms.ModelForm):
    event_start_time = forms.TimeField(widget=TimePickerInput(options=FlatpickrOptions(
        time_24hr = False,
        timeFormat = 'h:i K',
    )))
    
    class Meta:
        model = Event
        fields = '__all__'

class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = ("webinar_title", "event_start_date", "event_end_date","event_start_time",
    "event_duration_time", "event_organisator", "quiz", "quiz_URL", "youtube_link", "price_for_members", "price_for_non_members")
    list_filter = ("webinar_title", "event_start_date", "event_end_date","event_start_time",
    "event_duration_time", "event_organisator", "quiz", "quiz_URL", "youtube_link", "price_for_members", "price_for_non_members")
    search_fields = ("webinar_title", "event_start_date", "event_end_date","event_start_time",
    "event_duration_time", "event_organisator", "quiz", "quiz_URL", "youtube_link", "price_for_members", "price_for_non_members")
    list_per_page = 10

admin.site.register(Event, EventAdmin)
