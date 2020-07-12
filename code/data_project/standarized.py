import pandas as pd
from sklearn.preprocessing import *


# 数学公式处理
def math_scale(X):
    X_mean = X.mean(axis=0)  # 求每列的均值
    X_std = X.std(axis=0)  # 求每列的标准差
    X_scale = (X - X_mean) / X_std
    print("数学公式处理后的数据为：")
    print(X_scale)


# scale处理
def stand_scale(X):
    X_scale = scale(X)
    print("Scale处理后的数据为：")
    print(X_scale)


# StandardScaler处理
def stand_std_scale(X):
    X_scale = StandardScaler().fit_transform(X)
    print("StandardScaler处理后的数据为：")
    print(X_scale)


# MinMaxScaler处理
def min_max_scale(X):
    X_scale = MinMaxScaler().fit_transform(X)
    print("MinMaxScaler处理后的数据为：")
    print(X_scale)


# MaxAbsScaler处理
def max_abs_scale(X):
    X_scale = MaxAbsScaler().fit_transform(X)
    print("MaxAbsScaler处理后的数据为：")
    print(X_scale)


# normalize处理
def normalize_process(X):
    X_normal = normalize(X, norm='l2')
    print("normalize处理后的数据为：")
    print(X_normal)


# Normalizer处理
def normalizer_process(X):
    normalizer = Normalizer().fit(X)
    X_normal = normalizer.transform(X)
    print("Normalizer处理后的数据为：")
    print(X_normal)


# Binarizer处理
def binary_trans(X):
    # binary = Binarizer(threshold=1.5).fit(X)  # 自定义阈值
    binary = Binarizer().fit(X)
    X_binary = binary.transform(X)
    print("Binarizer处理后的数据为：")
    print(X_binary)


if __name__ == '__main__':
    df = pd.read_csv("data/pm25_train.csv", low_memory=False)
    X = df.drop(columns=['pm2.5']).values

    math_scale(X)  # 数学公式处理
    stand_scale(X)  # scale标准化处理
    stand_std_scale(X)  # StandardScaler标准化处理
    min_max_scale(X)  # MinMaxScaler处理--[0,1]
    max_abs_scale(X)  # MaxAbsScaler处理--[-1,1]
    normalize_process(X)  # normalize处理
    normalizer_process(X)  # Normalizer处理
    binary_trans(X)  # Binarizer处理--0/1
