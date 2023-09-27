
from faker import Faker;

fake = Faker();

with open('namelist.txt','a') as file:
   for name in range(4):
#       n = fake.name();
        n = input("Enter ur friends name.");
        file.write(n+'\n');


