

#passing list to function
def add(numbers):

    total = 0;

    for n in numbers:
        
        total = total + n;

    return total;

scores = [1,2,3,4,5];
result = add(scores);
print(result);





#return list from function

def remove_duplicates(numbers):

    new_list= [];

    for nums in numbers:
        
        if nums not in new_list:
            new_list.append(nums);
    return new_list

ids = [1,2,2,3,4,4,5,5];
result = remove_duplicates(ids);
print(result);



#Global variable

count = 0;

def increment():
    global count;
    count = count+1;
    return count;

result = increment();
print(result);



#Checking palindrome or not

palindrome_flag = True;
#inputs = "racecar";
inputs = "121";
l = len(inputs);

for index in range(l):

    if inputs[index] !=inputs[l - index -1]:
       palindrome_flag=False;
       break;
    else:
        palindrome_flag=True;


if palindrome_flag:
    print("Given input is palindrome")

else:
    print("Given input is not palindrome");





#variable length positional arguments
def add(*args):
    for data in args:
        print(data);

add(10,20,30,40);


#keyword argument

def product(**kwargs):
    
    for key,value in kwargs.items():
        print(key,":",value);

product(name="iphone",price=56000);
product(name="macbook",price=150000);

#decorator
#chaning behaviour of function

def chocolate():
    print("Chocolate");


def decorator(func):#passing function as argument
    def wrapper():
        print("Wrapper up side");
        func();
        print("Wrapper down side");
    return wrapper;


#chocolate = decorator(chocolate);

@decorator
def iceCream():
    print("Ice cream");


@decorator
def cake():
    print("Cake");

iceCream();
cake();



