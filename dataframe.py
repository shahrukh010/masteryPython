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
console.print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

