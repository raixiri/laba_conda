import numpy as np
import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn import preprocessing, svm
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

df = pd.read_csv('bottle.csv', low_memory=False)
df_binary = df[['Salnty', 'T_degC']]

# Taking only the selected two attributes from the dataset
df_binary.columns = ['Sal', 'Temp']
#display the first 5 rows
print(df_binary.head())
