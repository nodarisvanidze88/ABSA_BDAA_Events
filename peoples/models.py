from django.db import models

# Create your models here.
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