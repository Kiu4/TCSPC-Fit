import pandas as pd
df = pd.read_csv('sample.txt', delim_whitespace=True, header = None, names = ['time', 'count'], skiprows = 1)  
print(df)