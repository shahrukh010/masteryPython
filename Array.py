
from array import *;

arr1 = array('i',[1,2,3,4,5]);
print(arr1);
#arr1.insert(6,10);
print(arr1);

arr2 = array('q',[10,20,30]);
print(arr2);
print(type(arr2));
print(arr2[2]);


def traverseArray(array):
    for nums in array:
        print(nums,':');

traverseArray(arr1);




def searchInArray(array,value):
    for i in array:
        if i == value:
            return array.index(value);
    return 'The vlaue is not exist in this array';


print('result:',searchInArray(arr1,6));
