import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    df = pd.read_csv("data/pm25.csv", low_memory=False)

    # 获取特征和标签
    X = df.drop(columns=['pm2.5_log']).values

    # 对特征数据进行标准化处理，得到方差
    X_std = StandardScaler().fit_transform(X)

    # 求每个特征的标准化后的均值
    mean_vec = np.mean(X_std, axis=0)

    # 求协方差矩阵
    cov_mat = np.cov(X_std.T)

    # 对协方差矩阵做奇异值分解
    [U, S, V] = np.linalg.svd(cov_mat)

    # 求特征值矩阵之和
    sum_S = np.sum(S)

    # k值保存列表
    k_list = []

    # 遍历特征值矩阵
    for k in range(len(S)):
        # 求前k个值之和--> S[0]+S[1]+...S[K]
        sum_k = np.sum(S[:k])

        # 信息保留率
        info_rate = sum_k / sum_S
        print("k=%d 时，信息保存率为: %.4f." % (k + 1, info_rate))

        # 信息保留率大于0.95时的K值，这里保留率可以自己设定，一般为0.95~0.99
        if info_rate >= 0.95:
            k_list.append(k + 1)

    # k值列表，取最小的k
    print("k的取值可以为：%s." % k_list)
