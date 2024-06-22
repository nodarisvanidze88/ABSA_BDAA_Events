from django.contrib import admin
from django import forms
from .models import Event
from django.utils.html import format_html
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

    def formatted_event_start_time(self, obj):
        return obj.event_start_time.strftime('%I:%M %p')
    
    def formatted_youtube_link(self, obj):
        if obj.youtube_link:
            return format_html('<a href="{0}">{1}</a>', obj.youtube_link, "YouTube")
        else:
            return "-"
    formatted_youtube_link.short_description = 'YouTube Link'
    formatted_event_start_time.short_description = 'Event Start Time'
    list_display = ("webinar_title", "event_start_date", "event_end_date","formatted_event_start_time",
    "event_duration_time", "event_organisator", "quiz", "formatted_youtube_link","status", "price_for_members", "price_for_non_members")
    list_filter = ("webinar_title", "event_start_date", "event_end_date","event_start_time",
    "event_duration_time", "event_organisator", "quiz", "youtube_link", "status","price_for_members", "price_for_non_members")
    search_fields = ("webinar_title", "event_start_date", "event_end_date","status","event_start_time",
    "event_duration_time", "event_organisator", "quiz", "youtube_link", "price_for_members", "price_for_non_members")
    list_per_page = 10

admin.site.register(Event, EventAdmin)
