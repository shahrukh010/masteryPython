
#squre
result  = (lambda x:x**2)(5)
#print(result);

#add
result = (lambda a,b:a+b)(5,5);
#print(result);

#keyword argumentt to lambda
result = (lambda a,b:a+b)(b=20,a=33);
#print(result);

#default argument
result = (lambda a=33,b=16:a-b)();
result = (lambda a=33,b=16:a-b)(a = 50);
#print(result);


#square of list of object
new_list = [2,3,4,5];
def square(x):
    return x**x;

result = list(map(square,new_list));
print(result);

