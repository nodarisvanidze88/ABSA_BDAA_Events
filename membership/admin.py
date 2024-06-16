from django.contrib import admin
from .models import MembershipAssignment,MembershipType,Peoples,SubMembershipType

admin.site.register((MembershipAssignment,MembershipType,Peoples,SubMembershipType))
