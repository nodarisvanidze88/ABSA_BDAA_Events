import requests
import csv
import os
from io import StringIO
from datetime import datetime
from membership.models import Peoples
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from termcolor import colored
load_dotenv()
class Command(BaseCommand):
    def handle(self,*args, **kwargs):
        url = os.getenv('MEMBERSHIP_SPREADSHEET_URL')
        data = requests.get(url)
        data_text = StringIO(data.text)
        csvData = csv.DictReader(data_text)
        # Peoples.objects.all().delete()
        for item in csvData:
            dob_str = item['DOB']
            try:
                dob = datetime.strptime(dob_str, "%d.%m.%Y").date() if dob_str else None
            except ValueError:
                print(colored(f"Invalid date format for {item['First Name']} {item['Surname']}: {dob_str}", 'red'))
                continue
            if item['E-Mail1']:
                people, created = Peoples.objects.get_or_create(
                    first_name=item['First Name'],
                    last_name=item['Surname'],
                    default_email=item['E-Mail1'],
                    defaults={
                        'title': item['Title'],
                        'middle_name': item['Middle Name'],
                        'gender': item['Gender'],
                        'date_of_birth': dob,
                        'secondary_email': item['E-Mail2'],
                        'optional_email': item['E-Mail3'],
                        'default_chapter': item['Chapter 1'],
                        'secondary_chapter': item['Chapter 2'],
                        'optional_chapter': item['Chapter 3'],
                        'default_state': item['State 1'],
                        'secondary_state': item['State 2'],
                        'optional_state': item['State 3'],
                        'business_name': item['Business Name'],
                        'phone_home': item['Phone Home'],
                        'phone_work': item['Phone Work'],
                        'phone_mobile': item['Phone Mobile'],
                        'phone_fax': item['Fax Work'],
                        'default_address': item['Address 1'],
                        'secondary_address': item['Address 2'],
                        'optional_address': item['Address 3']
                    }
                )
                if created:
                    print(f"Created {people.first_name} {people.last_name} {people.default_email}")
            else:
                continue
            