from faker import Faker
import csv
import random

output = open('Maphlix_Trust_Ghana_Ltd_Data.CSV','w')
fake = Faker()

Company = "Maphlix Trust Ghana Ltd."
Ghana_regions = ["Ashanti", "Brong-Ahafo", "Central", "Eastern", "Greater Accra", "Northern",
                 "Upper East", "Upper West", "Volta", "Western", "Western North", "Ahafo", "Bono",
                 "Bono East", "North East", "Savannah"]
Services_list = ['Agricultural production', 'Agro-processing', 'Agronomy', 'Input supply']
Demographics_list = ['Greater Accra', 'Volta']
Customer_preference = 'Website'
Communications_list = ['Email','Phone']

header = ['Company', 'FullName', 'PhoneNumber', 'EmailAddress', 'CustomerAddress', 'Branch',
          'ServicesOrProducts', 'TransactionActivity', 'CustomerPreference', 'CommunicationMethod']
mywriter = csv.writer(output)
mywriter.writerow(header)

for r in range(100000):
    mywriter.writerow([Company, fake.name(), fake.phone_number(), fake.email(), random.choice(Ghana_regions),
                       random.choice(Demographics_list), random.choice(Services_list),
                       fake.random_int(min=1,max=9999, step=1),
                       Customer_preference, random.choice(Communications_list)])