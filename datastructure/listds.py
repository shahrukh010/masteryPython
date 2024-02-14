
#convert string to list
string = "hello annie how are you";
list = string.split();
print(list);

#convert list to string;
string = ' '.join(list);
print(string);

#update list;

myList = [1,2,3,4,5];
print(myList);
myList[2] = 33;
print(myList);

#insert object at specificatino position

myList.insert(0,0);
print(myList);
myList.insert(5,10);
print(myList);


#adding two list
secondList = [100,200,300];
secondList.extend(myList);
print(secondList);
print(myList);
myList.extend(secondList);
print(myList);

#list of operation/function;

a = [0,1];
a = a*4;
print(a);

print(max(a));
print(min(a));
print(sum(a));


#find the average of given input;
total = 0;
count = 0;
#while True:
#   inp = input('Enter your input.');
#   if inp == 'done':break;
#   value = float(inp);
#   total = total + value;
#   count = count+1;
#   average = total/count;
#print(f'average: {average}');

#delete element

myList = ['a','b','c','d','e','f'];
print(myList);
myList.pop();#always last element
print(myList);
myList.pop(2);#based on index
print(myList);
del myList[0:3];#deleted based on index
print(myList);

myList.remove('e');#know object
print(myList);

#sort list;
myList = [5,2,1,3,4];
org = myList[:];
myList.sort();
print(myList);
print(org);
#sort list without modifying original list;
sorted_list = sorted(myList);
print(sorted_list);

#check object are present or not
myList = ['annie','hector','bridget','nic'];

isExists = 'hector' in myList;
print(isExists);
isExists = 'alex' in myList
print(isExists);

for index in range(len(myList)):
    myList[index] = myList[index]+' '+'khan';
print(myList);

#return the index of myList
print(myList.index('hector khan'));
