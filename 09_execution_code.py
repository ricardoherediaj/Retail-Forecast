# -*- coding: utf-8 -*-
"""09_Execution_Code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cMs43z0TqzZUDdUq1kLyrUprpIItQive
"""

import warnings
warnings.filterwarnings("ignore")

#Load auxiliary functions
from FunctionsRetail import *

#Load Data
root = '/content/drive/MyDrive/02_RETAIL'
data_file_name = 'DataForProduction.csv'
root_complete = root + '/02_Data/02_Validation/' + data_file_name
df = pd.read_csv(root,sep=';',parse_dates=['date'],index_col='date')

#Seldct only the used ones
final_variables = ['store_id',
                     'item_id',
                     'event_name_1',
                     'month',
                     'sell_price',
                     'wday',
                     'weekday',
                     'sales']

df = df[final_variables]

#Launch prediction
forecast = forecast_recursive(df)

forecast.sort_values(by = ['store_id','item_id'])