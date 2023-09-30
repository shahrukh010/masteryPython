
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



import numpy as np;

twoDarray = np.array([[1,2,3],[4,5,6],[7,8,9]]);
#print(twoDarray);

#insert element on column wise
newTwoDarray = np.insert(twoDarray,0,[[10,20,30]],axis=1);

#print(newTwoDarray);

#inset on row
newRow = np.insert(twoDarray,0,[[50,60,70]],axis=0);
#print(newRow);

#print(newRow[0][1]);

print("access element from two daimensional array");

def accessElement(array,row,col):
    if row>=len(array) or col>=len(array[0]):
        print("index is out of bound");
    else:
        print(array[row][col]);

accessElement(newRow,0,0);


def traverseTwoDarray(array):
    for row in range(len(array)):
        for col in range(len(array[0])):
            print(array[row][col],end=" ");
        print();


nums = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]);

traverseTwoDarray(nums);


