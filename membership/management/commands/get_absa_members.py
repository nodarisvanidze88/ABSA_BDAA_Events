import requests
import csv
import os
from io import StringIO
from datetime import datetime
from membership.models import MembershipAssignment, SubMembershipType, MembershipType
from peoples.models import Peoples
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from termcolor import colored
load_dotenv()
class Command(BaseCommand):

    def get_date_format(self, data):
        return datetime.strptime(data, "%d.%m.%Y").date() if data else None
    
    def handle(self, *args, **kwargs):
        url = os.getenv('ABSA_MEMBERSHIP_URL')
        data = requests.get(url)
        data_text = StringIO(data.text)
        csvData = csv.DictReader(data_text)

        for item in csvData:
            try:
                accep = self.get_date_format(item['BDAA Accep.'])
                paid = self.get_date_format(item['BDAA Paid'])
            except ValueError:
                print(colored(f"Invalid date format for {item['First Name']} {item['Surname']}: {item['BDAA Accep.']}", 'red'))
                print(colored(f"Invalid date format for {item['First Name']} {item['Surname']}: {item['BDAA Paid']}", 'red'))
                continue

            if item['E-Mail1']:
                try:
                    member = Peoples.objects.get(
                        first_name=item['First Name'],
                        last_name=item['Surname'],
                        default_email=item['E-Mail1']
                    )
                except Peoples.DoesNotExist:
                    print(colored(f"Member with name {item['First Name']} {item['Surname']} and email {item['E-Mail1']} does not exist", 'red'))
                    continue

                sub_membership_type = None
                if item['Member']:
                    try:
                        sub_membership_type = SubMembershipType.objects.get(sub_membership_type=item['Member'])
                    except SubMembershipType.DoesNotExist:
                        print(colored(f"Sub Membership Type {item['Member']} does not exist for {item['First Name']} {item['Surname']}", 'red'))
                        continue
                try:
                    membership_type = MembershipType.objects.get(membership_type='ABSA')
                except MembershipType.DoesNotExist:
                    print(colored(f"Membership Type 'BDAA' does not exist", 'red'))
                    continue
                assignment, created = MembershipAssignment.objects.get_or_create(
                    membership_ID=item['BDAA ID'],
                    sub_membership_type=sub_membership_type,
                    member=member,
                    defaults={
                        'acceptance': accep,
                        'paid_till': paid,
                    }
                )
                if created:
                    assignment.membership_type.set([membership_type])
                    print(f"Created membership assignment for {member.first_name} {member.last_name}")

            else:
                continue