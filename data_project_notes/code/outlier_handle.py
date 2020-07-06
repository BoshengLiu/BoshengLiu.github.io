import numpy as np
import pandas as pd


def outlier_analysis(df, col):
    Q_up = np.percentile(df[col], 25)   # 上四分位数
    Q_low = np.percentile(df[col], 75)# 下四分位数
    IQR = Q_up - Q_low
    outlier_step = 1.5 * IQR
    df = df[(df[col].values > Q_low - outlier_step) | (df[col] < Q_up + outlier_step)]
    return df


if __name__ == '__main__':
    pass
