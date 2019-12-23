import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
data = pd.read_csv('air_chengdu_2018.csv')
X = data[['PM','PM10','SO2','NO2','CO','O3']]
y = data[['AQI']]
print(X)
print(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print (y_test.shape)

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X_train, y_train)

print(linreg.intercept_[0])
print(linreg.coef_[0][0])
print(linreg.coef_[0][1])
print(linreg.coef_[0][2])
print(linreg.coef_[0][3])
print(linreg.coef_[0][4])
print(linreg.coef_[0][5])
import json
filename = 'city_air_2019.json'
with open(filename,encoding="utf-8") as f:
    city_air = json.load(f)

for key,value in city_air.items():
    print(value)
    AQI = linreg.intercept_ +\
          value[1] * linreg.coef_[0][0] +\
          value[2] * linreg.coef_[0][1] +\
          value[3] * linreg.coef_[0][2] +\
          value[4] * linreg.coef_[0][3] +\
          value[5] * linreg.coef_[0][4] +\
          value[6] * linreg.coef_[0][5]
    print(AQI)
    print("\n")
    city_air[key][0]=int(AQI[0])

print(city_air)

with open('city_air_2019.json''', 'w', encoding='utf-8') as f:
    json.dump(city_air, f)





