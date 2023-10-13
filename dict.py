
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
