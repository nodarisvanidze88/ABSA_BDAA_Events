from django.db import models
import datetime
from django.utils.timezone import now

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
    
class Peoples(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    
    title = models.CharField(max_length=10, blank=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    default_email = models.EmailField()
    secondary_email = models.EmailField(blank=True)
    optional_email = models.EmailField(blank=True)
    default_chapter = models.CharField(max_length=50, blank=True)
    secondary_chapter = models.CharField(max_length=50, blank=True)
    optional_chapter = models.CharField(max_length=50, blank=True)
    default_state = models.CharField(max_length=50, blank=True)
    secondary_state = models.CharField(max_length=50, blank=True)
    optional_state = models.CharField(max_length=50, blank=True)
    business_name = models.CharField(max_length=200, blank=True)
    phone_home = models.CharField(max_length=100, blank=True)
    phone_work = models.CharField(max_length=100, blank=True)
    phone_mobile = models.CharField(max_length=100, blank=True)
    phone_fax = models.CharField(max_length=100, blank=True)
    default_address = models.CharField(max_length=300, blank=True)
    secondary_address = models.CharField(max_length=300, blank=True)
    optional_address = models.CharField(max_length=300, blank=True)
    class Meta:
        unique_together = ("first_name", "last_name","default_email")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

def default_paid_till():
    return now() + datetime.timedelta(days=365)

class MembershipAssignment(models.Model):
    membership_ID = models.CharField(max_length=20, blank=True, null=True)
    membership_type = models.ManyToManyField(MembershipType, related_name='assignments')
    sub_membership_type = models.ForeignKey(SubMembershipType, on_delete=models.CASCADE, blank=True)
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


