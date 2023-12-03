import pandas as pd

df = pd.read_csv('billionaires.csv')

# print(df.sort_values(by='name'))

# df.sort_values(by='name').to_csv('sorted_report',index=False)

df.sort_index(axis=1).to_csv('sorted_report_2.csv',index=False)