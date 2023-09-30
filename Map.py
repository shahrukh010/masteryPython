
myDict = {'name':'annie','age':24,'address':'hyderabad'};


def traverseDict(mydict):
    for key in mydict:
        print(key,':',mydict[key]);

traverseDict(myDict);

def searchFromDict(mydict,value):
    for key in myDict:
        if myDict[key] == value:
            return key,value;#tuple will be return
    return 'there is not data for';

print(searchFromDict(myDict,24));

clone = myDict.copy();
#jprint(clone);
#print(clone.pop("name"));
#print(clone.popitem());#delete item from last
print(clone);

newDict = {}.fromkeys([1,2,3],0);#creating dictonary.i.e 0 will be value for every[,,,]key
print(newDict);
print(newDict.get(1));

#print(newDict.items());
print(type(newDict.keys()));

print(myDict.setdefault('city','hyderabad'));#set new key if key is available.
print(myDict);

myDict['country'] = 'india';
print(myDict);


print('city' in myDict);#[True] in operator work for only key 
print('hyderabad' in myDict);#[False] in operator not work for value

print('hyderabad' in myDict.values());#[True]





