# Python 2.x
from faker import Faker
import random
import csv


def create_person():
    interests = ['cats', 'dogs', 'children', 'jazz', 'castles', 'gardening', 'knitting', 'swim']
    person = {}
    fake = Faker()
    geo = fake.local_latlng(country_code="CH")
    person['lat'] = geo[0]
    person['lng'] = geo[1]
    person['birthyear'] = str(fake.date_of_birth(minimum_age=66, maximum_age=90))[:4]
    if bool(random.getrandbits(1)):
        person['gender'] = 'm'
        person['name'] = fake.name_male()
    else:
        person['gender'] = 'f'
        person['name'] = fake.name_female()

    if bool(random.getrandbits(1)):
        person['language'] = 'German'
    else:
        person['language'] = 'French'

    index = random.randint(0,len(interests)-1)
    personal_interests = []
    while index < len(interests):
        personal_interests.append(interests[index])
        index = index + random.randint(1,len(interests))

    person['interests'] = ';'.join(personal_interests)
    return person

with open('grannies_and_grandies2.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',lineterminator='\n')
    writer.writerow(['name','birthyear','language','lat','lng','gender','interests'])
    for x in range(100):
        person = create_person()
        array_in_order = [person['name'], person['birthyear'], person['language'], person['lat'], person['lng'], person['gender'], person['interests']]
        writer.writerow(array_in_order)