from django.contrib import admin
from .models import MembershipAssignment,MembershipType,Peoples,SubMembershipType

class SubMemberTypeAdmin(admin.ModelAdmin):
    list_display = ["main_membership_type", "sub_membership_type"]
    list_filter = ["main_membership_type", "sub_membership_type"]
    search_fields = ["main_membership_type", "sub_membership_type"]

class PeoplesAdmin(admin.ModelAdmin):
    list_filter = ["gender","default_chapter","default_state"]
    list_display = ["title", "first_name", "last_name", "gender", "date_of_birth","default_email","default_chapter",
                    "default_state", "business_name", "phone_mobile", "default_address"]
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        
        self.search_fields = self.get_all_field_names(model)

    def get_all_field_names(self, model):
        return [field.name for field in model._meta.get_fields() if not field.many_to_many and not field.one_to_many]
    list_per_page = 20


class MembershipAssignmentAdmin(admin.ModelAdmin):
    list_display = ('member', 'membership_type_list', 'sub_membership_type', 'acceptance', 'paid_till', 'status')

    def membership_type_list(self, obj):
        return ", ".join([m.membership_type for m in obj.membership_type.all()])
    membership_type_list.short_description = 'Membership Type'

    def status(self, obj):
        return obj.status
    status.short_description = 'Status'
    search_fields = ['membership_ID', 'membership_type__membership_type', 'sub_membership_type__sub_membership_type', 'member__first_name', 'member__last_name', 'member__default_email']

admin.site.register(MembershipAssignment, MembershipAssignmentAdmin)

admin.site.register(SubMembershipType, SubMemberTypeAdmin)
admin.site.register(Peoples, PeoplesAdmin)
admin.site.register(MembershipType)
