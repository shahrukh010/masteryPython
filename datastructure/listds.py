
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


#calculate the average of temprature.

#numDays = int(input("How many day's temperature?"));
#total = 0;
#
#for index in range(1,numDays+1):
#    nextDays = int(input("Day "+str(index)+"'s high temp:"));
#    total +=nextDays; 
#avg = round(total/numDays,2);
#print("\nAverage = "+str(avg));


#find the missing 1 to n

class Question:
    result = [];

    def find_all_missing(self,nums):
        start = nums[0];
        for index in range(1,len(nums)):
            miss = nums[index] - index;
            if miss !=start:
                mr = index+start;
                self.result.append(mr);
                start +=1;
                while start !=nums[index] - index:
                    mr = index+start;
                    self.result.append(mr);
                    start +=1;

    
    def find_pair_target(self,nums,target):

        result = [];
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i] + nums[j];
                if sum == target:
                    result.append(i);
                    result.append(j);
        return result;
#find the maximum product of two integer where all possible values are positive.
    def max_product(self,nums):
        result = [0,0];
        current_max = 0;
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product = nums[i] * nums[j];
                current_max = max(product,current_max);
                if product >=current_max:
                    result.clear();
                    result.append(nums[i]);
                    result.append(nums[j]);
                    p = nums[i]*nums[j];
                    result.append('product:'+str(p));


        return result;




question = Question();
nums = [1,2,3,5,7,8,11,15];
question.find_all_missing(nums);
#print(question.result);

nums = [1,2,3,5,6,7];
#result = question.find_first_miss(nums);
#print(result);

nums = [2,6,3,9,11];
result = question.find_pair_target(nums,9);
nums = [2,7,11,15];
result = question.find_pair_target(nums,9);
nums = [3,2,4];
result = question.find_pair_target(nums,6);
nums = [3,3];
result = question.find_pair_target(nums,6);
nums = [1,2,3,2,3,4,5,6];
result = question.find_pair_target(nums,6);
print(result);

#using in operator.
import numpy as np;

array = np.array([1,2,3,4,6,8,9]);

#target = int(input("Enter number to check"));
#print(target in array);

#for index in range(len(array)):
#    if target == array[index]:
#        print(True);
#    else:
#        print(False);
#    break;
#


array = np.array([1,4,3,6,7,0]);
array = np.array([-1, -3, -4, 2, 0, -5]);
array = np.array([1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21]);
result = question.max_product(array);
print(result);
    


