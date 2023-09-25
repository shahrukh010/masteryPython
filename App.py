

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



