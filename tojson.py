import json;

while True:
    user_list = [];
    name = input('Enter ur name.');
    email= input('Enter ur email.');
    contact= input('Enter ur contact');
    q = input('Enter more data[y/n]');
    if q == 'n':
        break;

    user_data = {
            'name':name,
            'email':email,
            'contact':contact
            }
    user_list.append(user_data);
    with open('user_data.json','a') as file:
        json.dump(user_list,file);
    print('user data saved successfully');


    
