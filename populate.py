import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'class_based_view.settings')
django.setup()
from basic_app.models import School, Student
from faker import Faker
import random


fakegen = Faker()
school_list = School.objects.all()


def populate(N=5):

    for i in range(N):
        school = random.choice(school_list)
        fake_name = fakegen.name()
        fake_age = random.randint(5,16)

        student = Student.objects.get_or_create(name = fake_name,age = fake_age,school = school)


if __name__ == '__main__':
    print('Populating')
    populate(20)
    print('Done')
