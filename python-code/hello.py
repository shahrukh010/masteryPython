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
