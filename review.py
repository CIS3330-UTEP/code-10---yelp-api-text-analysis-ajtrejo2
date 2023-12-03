import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('cars_dataset.csv')
car_brands = ['Mazda','Honda','Toyota']

car_df = df.query('Identification_Make == @car_brands')
cars_count = car_df.groupby(by='Identification_Make')['Identification_Make'].agg('count')
print(cars_count)



