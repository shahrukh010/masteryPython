import numpy

import matplotlib.pyplot as pt;

#Create a Numpy array
data = numpy.array([[1,2,3],[4,5,6],[7,8,9]]);

#ploting heap map
pt.imshow(data,cmap='viridis');
pt.colorbar();
pt.show();



