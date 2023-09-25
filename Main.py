
''' name = input("Enter ur name: ");

if name == 'hector':
    print(name);
    print('how are you!');
elif name == 'bridget':
    print('hello',name);
elif name == 'nic':
    print('hello',name);
else:
    print("how are you",name);

'''

'''first =int(input("Enter First Number"));
second=int(input("Enter Second Number"));

third =int(input("Ente third Number"));
fourth=int(input("Enter fourth Number"));

if first > second and third > fourth:
    print("first and condition is true",first);
elif second > first:
    print("second",second);
else:
    print("equal");
'''


'''loop'''

string  = 'hector';

for data in string:
    print(data);

input_data = input("Ente a input: ");

index = 0;
for data in input_data:
    print("The data present at[",index,"]",data);
    index = index+1;



for data in range(5):
    print("hello",data);


list = [1,2,3,4,5];

sum = 0;
for data in list:
    sum +=data;
print("list of sum: ",sum);



while sum<=20:
    print(sum);
    sum = sum+1;


for data in range(5):
    for index in range(5):
        if index == 2:
            break;
        print(data,index);



for data in list:
    if data >=3:
        break;
    print("break",data);


for data in list:
    if data==3:
        continue;
    print("continue",data);






def printSomeThing():
    for data in range(5):
        print('function',data);

printSomeThing();




def saySomeThing(a,b):

    return a,b;

a,b = saySomeThing("bridget","annie");
print(a,b);




#keyword argument
def speed(distance,time):
    print(distance/time);

speed(distance=100,time=2);
speed(time=2,distance=100);


def area(radius,pi=3.14):
    result = radius*radius*pi;
    return result;

def cost(circle_area,cost_per_sqm):
    total = circle_area * cost_per_sqm
    return total;

calculated_area = area(10,3.15);
print(calculated_area);
cost_total = cost(calculated_area,10)
#print(cost_total);

#nested function call
print(cost(area(3,3.16),2));
