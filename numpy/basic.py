import numpy as np;
a = np.array([1,2,3,4,5]);
print(a);

import numpy;

#two dimenstional array
ndarray = numpy.array([[1,2],[3,4]]);
print(ndarray);

for d in ndarray:
    for data in d:
        print(data);


#minimum dimension create
ndarray = numpy.array([[1,2,3],[10,20,30],[40,50,60]],ndmin=5);
print(ndarray);

ndarray = numpy.array([1,2,3,4,5],dtype=complex);
print(ndarray);


a = numpy.array([[1,2,3,],[4,5,6]]);
print(a);
a.shape = (3,2);
print(a);



a = numpy.arange(10);
print(a);
a.ndim
print(a);


print();
print();
print();
#reshape of one dimensional array
b = a.reshape(2,1,5);
print(b);


#create array with start,end,step

steparr = numpy.arange(10,20,2);
print(steparr);


#matrix representation
matrix3x3 = numpy.eye(3);
print(matrix3x3);

matrix3x5 = numpy.eye(3,5);
print(matrix3x5);

#creae daigonal

diagonal = numpy.diag([1,2,3]);
print(diagonal);
diagonal = numpy.diag([1,2,3],1);
print(diagonal);

vandermatrix = numpy.vander((1,2,3,4),4);
print(vandermatrix);

#general array creation.

zeroarr = numpy.zeros((2,3),dtype=int);
print(zeroarr);


#Generate random matrix

from numpy.random import default_rng;

rm = default_rng(42).random((2,3));
print(rm);
print(len(rm));



#create 2 dimensional array of size 2X3 composed of 4bytes integer element

x = numpy.array([[1,2,3],[4,5,6]],numpy.int32);
print(x);
print(type(x));

#index of ndarray
print(x[0,2]);#0 is first row ,2 is second index of row
print(x[1,1]);



#C-Contiguous(Row Major Order) 3X$

c_contiguous_array = numpy.array([[1,2,3,4],
                                  [5,6,7,8],
                                  [9,10,11,12]
                                 ])

#iterating order
for i in range(c_contiguous_array.shape[0]):
    for j in range(c_contiguous_array.shape[1]):
        print(f"ELement at index ({i}, {j}): {c_contiguous_array[i,j]}");


