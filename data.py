from pandas import DataFrame
from pandas import Series;

data = {"Name":['annie','hector','bridget','nic'],
        "Age":[23,25,27,28],
        "Salary":[2000,2300,2600,3000],
        "Profile":'Doctor',
        "Education":'MS'}

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

#rearrange column of data(but name should be same(it case sensetive)
new_data_frame = DataFrame(data,columns=['Name','Salary','Age','Profile']);
print(new_data_frame);

print('Retrive only specify data');
print(new_data_frame['Salary']);
#print(new_data_frame['Name']);

print(new_data_frame.loc[1]);
print(new_data_frame.iloc[3]);

print();
print();
print();

#new_frame = new_data_frame.T;
new_frame = DataFrame(data);
print(new_frame);


#reindex of data index
new_data = Series([50,100,200,250,300,350,400],index=['a','d','c','e','f','b','g']);
print(new_data);
new_data = new_data.reindex(['a','b','c','d','e','f','g']);
print("After reindex");
print(new_data);

print(frame);
#reindex of frame
frame = frame.reindex([0,2,1]);
print(frame['Profile']);
#change profie(change column data)
frame['Profile'] = 'Engineer';
print(frame);
#if column['Year'] not exist it will create new
frame['Year'] = 2023
print(frame);

#Transpose Frame[T] Transpose;

new_frame = frame.T;
print(new_frame);

new_frame = new_frame.T;
print(new_frame);


#drop row;
fram2 = new_frame.drop([1]);
print(fram2);

#remove column
frame2 = new_frame.drop(['Salary'],axis=1);
print();
print();
print(frame2);

print();
print();
print();

data1 = {'speed':[100,103,105],
         'temp':[68,23,44]
        }
data2 = {'speed':[100,103,105],
         'temp':[68,23,44],
         'humidity':[45,23,33]
        }



frame1 = DataFrame(data1);
print(frame1);
frame2 = DataFrame(data2);
print();
print(frame2);

add_frame = frame1 + frame2;
print(add_frame);
series2 = Series([100,200,300],index=['speed','temp','humidity'])
print('series2...');
print(series2);

from tabulate import tabulate
new_fram = frame2 - series2;
print(tabulate(new_fram,headers='keys',tablefmt='fancy_grid'));



