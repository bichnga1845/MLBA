import pandas as pd

df=pd.read_csv("../dataset/SalesTransactions.txt", encoding="utf-8", low_memory=False, sep="\t")
print(df)