from django.contrib import admin
from .models import EventReportFileUpload

class EventFileUploadAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'upload_date', 'report_source')
    actions = ['process_upload_file']

    def porcess_upload_file(self, request, queryset):
        for obj in queryset:
            try:
                result = obj.process_file()
                self.message_user(request, result)
            except Exception as e:
                self.message_user(request, f'Eroor processing file: {e}', level='error')
    
admin.site.register(EventReportFileUpload, EventFileUploadAdmin)