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


a =int(input("Enter first number"));
b =int(input("Enter second number"));

try:
    result = a/b;
except:
    'divison by zero';
else:#else block will be executed when exception not raise
    print(result);
finally:
    print("this code will executed no matter what");


