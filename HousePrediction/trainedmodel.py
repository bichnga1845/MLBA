from sklearn import metrics
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle

#use pandas to read CSV dataset
df = pd.read_csv('USA_Housing.csv')
#call functions about get dataset information:
#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.columns)

plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap - USA Housing")
#plt.show()

#set X matrix
#df.columns[:5] meaning:
#['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
# 'Avg. Area Number of Bedrooms', 'Area Population']
X = df[df.columns[:5]]
y = df['Price']
# Printing for observation:
#print(X)
#print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

lm = LinearRegression()

lm.fit(X_train, y_train)

#print("Input 1:")
#print([X_test.iloc[0]])

predictions = lm.predict(X_test)

pre1 = lm.predict([X_test.iloc[0]])
#print("Housing Price prediction 1 =", pre1)

pre2=lm.predict([[66774.995817,5.717143,7.795215,4.320000,36788.980327]])
#print("kết quả 2 =",pre2)

# print the intercept
#print(lm.intercept_)
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
#print(coeff_df)

#print('MAE:', metrics.mean_absolute_error(y_test, predictions))
#print('MSE:', metrics.mean_squared_error(y_test, predictions))
#print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

#modelname="housingmodel.zip"
#pickle.dump(lm, open(modelname, 'wb'))


