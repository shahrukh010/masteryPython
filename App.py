

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
