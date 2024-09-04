from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Peoples


class PeoplesAdmin(admin.ModelAdmin):
    list_filter = ["gender","default_chapter","default_state"]
    list_display = ["title", "link_first_name", "last_name", "gender", "date_of_birth","default_email","default_chapter",
                    "default_state", "business_name", "phone_mobile", "default_address"]
    def link_first_name(self,obj):
        return format_html('<a href="{}">{}</a>', reverse('admin:peoples_peoples_change', args=[obj.id]), obj.first_name)
    
    link_first_name.short_description = 'First Name'

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        
        self.search_fields = self.get_all_field_names(model)

    def get_all_field_names(self, model):
        return [field.name for field in model._meta.get_fields() if not field.many_to_many and not field.one_to_many]
    list_per_page = 20
admin.site.register(Peoples, PeoplesAdmin)