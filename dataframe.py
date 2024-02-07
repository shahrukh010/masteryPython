from tabulate import tabulate
from rich.console import Console
import pandas as pd

# Assuming 'df' is your DataFrame
df = pd.DataFrame({
    'Name': ['John', 'Jane', 'Jim', 'Jill'],
    'Age': [25, 30, 35, 40]
})


# Print the DataFrame using tabulate
console = Console();
#console.print(tabulate(df, headers='keys', tablefmt='fancy_grid'))



data = {
    'Name': ['John', 'Jane', 'Jim', 'Jill'],
    'Age': [25, 30, 35, 40],
    'Salary': [60000,50000,55000,70000],
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
data_frame = DataFrame(data);

console = Console(color_system='truecolor');
from rich.style import Style;
from rich.table import Table;
yellow_style = Style(color="yellow");
table = Table(tabulate(data_frame,headers='keys',tablefmt='fancy_grid'));
table.style = yellow_style;
#console.print(table);
#console.print(tabulate(data_frame,headers='keys',tablefmt='fancy_grid'),yellow_style);
print(data_frame);

from pandas import Series;
series = Series([1,2,3,4,5],index=[2,1,3,4,5]);
#console.print(series);
#sort index row-wise
series = series.sort_index();
#console.print(series);

new_data = data_frame.reindex([0,2,1,3]);
#console.print(tabulate(new_data,headers='keys',tablefmt='fancy_grid'));
#sort row wise
new_data = new_data.sort_index();
#console.print(tabulate(new_data,headers='keys',tablefmt='fancy_grid'));

#sort column wise;
new_data = new_data.sort_index(axis=1);
#console.print(tabulate(new_data,headers='keys',tablefmt='fancy_grid'));

#list only index column data
new_data = new_data.reindex(columns=['Name','Age','Location','Department','Salary','Bonus_Amt']);
#console.print(tabulate(new_data,headers='keys',tablefmt='fancy_grid'));

#sort column in descending order
new_data = new_data.sort_index(axis=1,ascending=False);
#console.print(tabulate(new_data,headers='keys',tablefmt='fancy_grid'));
#sort values on specific column
#new_data = new_data.sort_values(by='Salary',inplace=False);
#console.print(tabulate(new_data,headers='keys',tablefmt='fancy_grid'));


