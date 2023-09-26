import random;
import os
from os import listdir;
import datetime


for data in range(1,5):
    nums = random.randint(10,21)
    print(nums);

for data in listdir():
    print(data);

today_date = datetime.date.today();
print(today_date);
current_time = datetime.datetime.now();
print(current_time);



