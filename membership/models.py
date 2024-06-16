from django.db import models
import datetime
from django.utils.timezone import now

class MembershipType(models.Model):
    membershiptType = models.CharField(max_length=50)
    def __str__(self):
        return self.membershiptType

class SubMembershipType(models.Model):
    mainMembershipType = models.ForeignKey(MembershipType, on_delete=models.CASCADE, related_name='mainMembership')
    submembershiptype = models.CharField(max_length=50)
    def __str__(self):
        return self.submembershiptype
    
class Peoples(models.Model):
    GENDER_CHOICES = [('M','M'),
                      ('F','F')]
    title = models.CharField(max_length=10, blank=True)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50, blank=True)
    lastName = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    dateOfBirth = models.DateField(blank=True)
    defaultEmail = models.EmailField()
    secondaryEmail = models.EmailField(blank=True)
    optionalEmail = models.EmailField(blank=True)
    defaultChapter = models.CharField(max_length=50,blank=True)
    secondaryChapter = models.CharField(max_length=50, blank=True)
    optionalChapter = models.CharField(max_length=50, blank=True)
    defaultState = models.CharField(max_length=50,blank=True)
    secondaryState = models.CharField(max_length=50, blank=True)
    optionalState = models.CharField(max_length=50, blank=True)
    businessName = models.CharField(max_length=200, blank=True)
    phoneHome = models.CharField(max_length=100, blank=True)
    phoneWork = models.CharField(max_length=100, blank=True)
    phoneMobile = models.CharField(max_length=100, blank=True)
    phoneFax = models.CharField(max_length=100, blank=True)
    defaultAddress = models.CharField(max_length=300,blank=True)
    secondaryAddress = models.CharField(max_length=300, blank=True)
    optionalAddress = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
class MembershipAssignment(models.Model):
    membershipType = models.ManyToManyField(MembershipType)
    submembershipType = models.ForeignKey(SubMembershipType, on_delete=models.CASCADE, blank=True)
    member = models.ForeignKey(Peoples, on_delete=models.CASCADE, related_name='members')
    acceptance = models.DateField(default=now(),blank=True)
    paid_till = models.DateField(default=now()+datetime.timedelta(days=365),blank=True)
    def __str__(self):
        return f"{self.member.firstName} {self.member.lastName}"


