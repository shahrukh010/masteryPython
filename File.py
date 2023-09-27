
import os;
import mysql.connector;
import json
#open and read file
file = open('data.txt','r');

content = file.read();
print(content);
file.close();

#open and write a something in file

write = open('data.txt','a');
content = '\nThis is three line\n'
write.write(content);

for data in os.listdir():
    write.write(data+'\n');

write.close();


#with open file and read content

with open('data.txt','r') as file:
    content = file.readline();
    content = content.strip(':');
    print(content);

with open('data.txt','r') as file:
    
    for line in file.readline():
        pass
#       print(line.strip('/'));



def save_user_data():
    name = input("Enter ur name");
    email = input("Enter ur email");
    contact = input("Enter ur contact");


    user_data = f'Name: {name}\nEmail: {email}\nContact: {contact}\n'
    with open('user_data','a') as file:
        file.write(user_data);

save_user_data();
