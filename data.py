from pandas import DataFrame
from pandas import Series;

data = {"Name":['annie','hector','bridget','nic'],
        "Age":[23,25,27,28],
        "Salary":[2000,2300,2600,3000]}

frame = DataFrame(data);
#print(frame);

series = Series(data);
print(type(series));
print(type([series]));
series_data = [series];
#print(series_data[0]);

series = Series([1,2,3,4,5]);
print(series);
print(series[0]);
print(series[4]);

#define own index;
series = Series([1,2,3,4,5],index=['a','b','c','d','e']);
print(series);
print(series['c']);

