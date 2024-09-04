from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import MembershipAssignment,MembershipType,SubMembershipType

class SubMemberTypeAdmin(admin.ModelAdmin):
    list_display = ["main_membership_type", "sub_membership_type"]
    list_filter = ["main_membership_type", "sub_membership_type"]
    search_fields = ["main_membership_type", "sub_membership_type"]



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
admin.site.register(MembershipType)
