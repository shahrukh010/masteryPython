


import pandas;
from pandas import DataFrame;
from pandas import DataFrame;
from rich.console import Console;
from tabulate import tabulate;

#data_frame = pandas.read_csv("apparel.csv");
data_frame = pandas.read_csv("home-and-garden.csv");

new_data = DataFrame(data_frame);
console = Console();
#console.print(tabulate(new_data,headers='keys',tablefmt='fancy_grid'));

#data_frame = data_frame.reindex(columns=['Handle','Title','Body (HTML)']);
data_frame = DataFrame(data_frame,columns=['Title','Handle','Body (HTML)']);
data_frame = data_frame.dropna();
console.print(tabulate(data_frame,headers='keys',tablefmt='fancy_grid'));

#drop rows
data_frame = data_frame.drop([0]);
data_frame = data_frame.drop([20]);
console.print(tabulate(data_frame,headers='keys',tablefmt='fancy_grid'));

#drop column
data_frame = data_frame.drop(['Handle'],axis=1);#axis=represent column
console.print(tabulate(data_frame,headers='keys',tablefmt='fancy_grid'));

#sort data;
data_frame = data_frame.sort_values(by='Title');
console.print(tabulate(data_frame,headers='keys',tablefmt='fancy_grid'));



