
data = {'uid':55555,'name':'amazon-voucher','price':200};
#print(data);
#print(data['uid']);
#print(data.get('name'));
#print(data.pop('name'));

#change price value
data['price'] = 100;

#added new filed and data into dictornary
data['denomination'] = [10,20,30]

#for key in data:
#    print(key,':',data[key]);



def search(dict,value):
    for key in dict:
        if dict[key] == value:
            return key,':',value;
    return 'there is not key exist';


def delete(dict,value):
    keys_to_delete = [];
    for key in dict:
        if dict[key] == value:
           #can not delete while iteration
           #dict.pop(value);
           keys_to_delete.append(key);
    #now key is deleting from list not dictionary.
    for k in keys_to_delete:
        dict.pop(k);
            
    return False;




print(search(data,'amazon-voucher'))
delete(data,'price');

print();
print();
print(data);


#del data;
#print(data);
#data.clear();
#print(data);

#shallow copy of dictonary.
data2 = data.copy();
print(data2);
import time;
timestamp = time.time();
formatted_date = time.strftime("%Y:%m:%d:%H:%M:%S",time.localtime(timestamp));

data2['created'] = formatted_date;
print(data2);
print(data);

#create  new dictonary using fromKeys()

new_dict = {}.fromkeys([1,2,3,],0)
print(new_dict);

#get(,,) if key is presentt then it will return key value else it will return specified value.
print(data2.get('price',1000));

#item() it is returing list of view tuple pair.
new_item = data2.items();
print(new_item);

#it will return view key object.(if data will change then it will reflect also
new_keys = data2.keys();
print(new_keys);


#popitems() it will pop item from back
print();
print(data2);
#data2.popitem();
print();
#print(data2);
data2.setdefault('price',100);
created = {'created':time.strftime("%Y:%m:%d:%H:%M:%S",time.localtime(timestamp))};
print(data);
#update basied merge two dictionary and make it single /update
data.update(created);
print(data);


