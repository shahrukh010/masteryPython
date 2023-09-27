import json;

data = {
    'name':'hector',
    'email':'hector@gmail.com',
    'contact':9999999,
    'address':'Hyderabad Hi-Tex,khanmet'
    }
save_data = json.dumps(data);

user_data = {
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": False
}

load_data = json.loads(json.dumps(user_data));
print(load_data.get('userId'));
print(load_data['title']);
print(load_data['completed']);



