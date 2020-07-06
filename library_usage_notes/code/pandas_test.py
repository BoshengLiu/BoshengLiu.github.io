import pandas
import numpy

file_info = pandas.read_csv["pandas.csv"]
file_info.head(3)
file_info.tail(3)
file_info.colsums()
file_info.shape()
file_info["foods"].max()

A = file_info.sort_values("Teach(mg)", inplace=True, ascending=False)
A.reset_index(drop=True)
file_info.isnull("age")

file_info.pivot_table(index="Place",values="Survived",aggfunc=numpy.mean)
file_info.dropna(axis=0,subset=["Age","Sex"])
file_info.loc[85,"Age"]

def X():
    print('=')
    return X
file_info.apply(X)

print(help(pandas.read_csv))