from django.db import models
import datetime
from django.utils.timezone import now
from peoples.models import Peoples

class MembershipType(models.Model):
    membership_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.membership_type

class SubMembershipType(models.Model):
    main_membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE, related_name='sub_memberships')
    sub_membership_type = models.CharField(max_length=50)
    class Meta:
        unique_together = ("main_membership_type","sub_membership_type")

    def __str__(self):
        return self.sub_membership_type


def default_paid_till():
    return now() + datetime.timedelta(days=365)

class MembershipAssignment(models.Model):
    membership_ID = models.CharField(max_length=20, blank=True, null=True)
    membership_type = models.ManyToManyField(MembershipType, related_name='assignments')
    sub_membership_type = models.ForeignKey(SubMembershipType, on_delete=models.CASCADE, blank=True, null=True)
    member = models.ForeignKey(Peoples, on_delete=models.CASCADE, related_name='assignments')
    acceptance = models.DateField(default=now, blank=True)
    paid_till = models.DateField(default=default_paid_till, blank=True)

    @property
    def status(self):
        today = now().date()
        if self.paid_till < today or not (self.acceptance <= today <= self.paid_till):
            return 'Inactive'
        return 'Active'

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name}"


