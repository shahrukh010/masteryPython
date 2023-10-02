

data = {
    'Name': ['John', 'Jane', 'Jim', 'Jill'],
    'Age': [25, 30, 35, 40],
    'Salary': [60000,50000,4000,3000],
    'Years_of_Experience': [3, 5, 7, 10],
    'Education': ['Bachelors', 'Masters', 'PhD', 'Bachelors'],
    'Position': ['Analyst', 'Manager', 'Director', 'Manager'],
    'Department': ['Finance', 'Marketing', 'Sales', 'Operations'],
    'Location': ['New York', 'San Francisco', 'Chicago', 'Los Angeles'],
#    'Years_in_Company': [2, 3, 5, 8],
#    'Performance_Rating': [4.2, 4.8, 4.5, 4.0],
    'Bonus_Amt': [5000, 8000, 10000, 7000],
}

from pandas import DataFrame;
from rich.console import Console;
from tabulate import tabulate;
from pandas import Series;

new_data = DataFrame(data);
console = Console();
console.print(tabulate(new_data,headers='keys',tablefmt='fancy_grid'));

series = Series([42,23,30],index=['a','b','b']);
print(series);
print(series.index.is_unique);

new_data = new_data.sum();
print(new_data);


import numpy as np;
series = Series([1,2,3,4,np.nan],index=['a','b','c','d','e']);
print(series);

#drop nan values only
series = series.dropna();
print(series);

data2 = {'speed':[101,np.nan,106],
         'Temp':[34,23,42],
         'Humidiyt':[4500,np.nan,5800]
        }

frame2 = DataFrame(data2);

#console.print(tabulate(frame2,headers='keys',tablefmt='facny_grid'));
console.print(tabulate(frame2,headers='keys',tablefmt='fancy_grid'));

#drop nan value from data frame
#frame2 = frame2.dropna();
#console.print(tabulate(frame2,headers='keys',tablefmt='fancy_grid'));
#assign value inplace of nan
frame2 = frame2.fillna(0);
console.print(tabulate(frame2,headers='keys',tablefmt='fancy_grid'));
#assign value inplace of nan


