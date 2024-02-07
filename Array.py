
from array import *;

arr1 = array('i',[1,2,3,4,5]);
print(arr1);
#arr1.insert(6,10);
print(arr1);

arr2 = array('q',[10,20,30]);
#print(arr2);
#print(type(arr2));
#print(arr2[2]);


def traverseArray(array):
    for nums in array:
        print(nums,':');

#traverseArray(arr1);




def searchInArray(array,value):
    for i in array:
        if i == value:
            return array.index(value);
    return 'The vlaue is not exist in this array';


#print('result:',searchInArray(arr1,6));



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

#accessElement(newRow,0,0);


def traverseTwoDarray(array):
    for row in range(len(array)):
        for col in range(len(array[0])):#it will retun no of column
            print(array[row][col],end=" ");
        print();


#nums = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]);

#traverseTwoDarray(nums);
print();
print();
print();
print();




nums = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]]);

def searchFromArray(array,value):
    for row in range(len(array)):
        for col in range(len(array[0])):
            if array[row][col] == value:
                print("The value at",str(row),str(col));
    return 'the value not present in array';



print(nums);
searchFromArray(nums,17);

newArr = np.delete(nums,0,axis=0);#axis=0 means row
print(newArr);
newArr = np.delete(nums,0,axis=1);#axis=1 means col
print(newArr);
