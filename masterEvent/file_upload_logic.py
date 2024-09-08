import pandas as pd
from peoples.models import Peoples
def eventbrite_file_upload(source, file):
    data = pd.read_excel(file)
    for _,item in data.iterrows():
        first_name = item['First Name']
        last_name = item['Surname']
        default_email = item['Email']
        db_result = Peoples.objects.filter(first_name = first_name,last_name=last_name, default_email=default_email)
        if not db_result:
            created = Peoples.objects.create(first_name = first_name,last_name=last_name, default_email=default_email)
            print(created)
        else:
            print("already exist")
    