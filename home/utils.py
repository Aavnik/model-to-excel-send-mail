from faker import Faker
from .models import *
fake = Faker()
import random

def student_data():
    for i in range(0, 200000):
            Student.objects.create(
            student_name = fake.name(),
            student_age = random.randint(18 , 54),
            student_phoneno = fake.phone_number(),
            student_email = fake.email(),
            student_address = fake.address()
           
        )