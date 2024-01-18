print("hello");

#declare multiple variable and initlaize multiple
a,b,c = 100,200,300;
print(a,b,c);
a,b,c=1,1,1
print(a,b,c);
#declare and initialize same values
a=b=c=1;
print(a,b,c);

#check the variable type
print(type(25));
print(type('Hello'));
print(type(25.5));
print(type([10,20,30]));

#check the size of memory taken by data;

product_id=45532324;
print(product_id.__sizeof__());#it will print 28bytes

x = True;
print(x)
x =int(x);
print(x);

#Base number conversion
a = 10;
print(bin(a));

#Type converion
x = 15;
print(float(x));
f = 20.00;
print(int(f));

s = '65';
print(int(s));
print(oct(20));

#while loop 
x = 10;
while x !=0:
#    print(x);
    x = x-1

print('iterating list');
data = [10,20,30,40,50,60,70];

while len(data) !=0:
    print(data.pop());



message = 'hello annie';

for x in message:
    print(x);


#for loop using range function


for x in range(1,5):
    print(x,end=',');

for x in range(1,10,2):
    print(x,end=',');




#Nested Loop

for i in range(0,5):
    for j in range(0,5):
        print('[',i,',',j,']')
