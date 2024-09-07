from celery import shared_task

from django.utils.timezone import now

from .models import MembershipAssignment

@shared_task
def update_membership_status():
    today = now().date()
    assignments = MembershipAssignment.objects.all()
    for assignment in assignments:
        if assignment.paid_till <today:
            assignment.status = "Inactive"

        else:
            assignment.status = 'Active'
        assignment.save()