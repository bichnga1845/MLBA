import pandas as pd

df=pd.read_csv("../dataset/SalesTransactions.csv", sep=",",encoding='utf-8',dtype='unicode',low_memory=False)

print(df)