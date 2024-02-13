import numpy

from datetime import datetime;

a = numpy.array([1,2,3]);
b = numpy.array([4,5,6]);

before = datetime.now();
result = numpy.dot(a,b);
print(result);

