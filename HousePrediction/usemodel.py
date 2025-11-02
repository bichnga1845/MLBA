import pickle

from pandas import Index

modelname="housingmodel.zip"
trainedmodel=pickle.load(open(modelname, 'rb'))

features=Index(['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population'],
      dtype='object')

prediction=trainedmodel.predict([[66774.995817,5.717143,7.795215,4.320000,36788.980327]])
print("kết quả =",prediction)


