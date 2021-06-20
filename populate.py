import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
# Import settings
django.setup()

import random
from first_app.models import AccessRecord,topic,webpage
from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.random()
        print(fake_name)
        



if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
