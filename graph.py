import pandas as pd
import texttable

# Create a sample DataFrame
data = {'Name': ['John', 'Jane', 'Jim', 'Jill'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 55000, 70000]}

df = pd.DataFrame(data)

# Create a texttable object
table = texttable.Texttable()

# Set the headers and rows
table.add_rows([df.columns] + df.values.tolist())

# Print the table
print(table.draw())

