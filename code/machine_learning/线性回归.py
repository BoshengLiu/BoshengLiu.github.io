import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression


# 时间拆分
def dateSplite(df):
    temp_df = df["date"].str.split('-', expand=True)
    temp_df.columns = ["year", "month", "day"]
    df = pd.concat([df, temp_df], axis=1)
    df = df.drop("date", axis=1)
    return df


# 基本的线性模型
def linearModel(X_train, y_train, X_test):
    # 归一化操作
    x_all = pd.concat([X_train, X_test], ignore_index=True)
    scale = MinMaxScaler(feature_range=(-1, 1))
    x_all = scale.fit_transform(x_all)
    x_train = scale.transform(X_train)
    x_test = scale.transform(X_test)

    # pca降维处理
    pca = PCA(n_components=4)
    pca.fit(x_all)
    x_tra_pca = pca.transform(x_train)
    x_test_pca = pca.transform(x_test)
    x_tra, x_val, y_tra, y_val = train_test_split(x_tra_pca, y_train, test_size=0.3, random_state=42)

    # 建立模型并验证mse
    reg = LinearRegression().fit(x_tra, y_tra)
    y_pre = reg.predict(x_val)
    print('Mean Squared Error: %.2f' % mean_squared_error(y_val, y_pre))

    # 预测
    test_pca = pca.transform(x_test_pca)
    y_test = reg.predict(test_pca)
    y_real = np.round(np.exp(y_test))

    df = pd.DataFrame(y_real, columns=['pm2.5'])
    return df


if __name__ == '__main__':
    train_file = "data/pm25_train.csv"
    test_file = "data/pm25_test.csv"

    df_train = pd.read_csv(train_file, low_memory=False)
    df_test = pd.read_csv(test_file, low_memory=False)

    train_new = dateSplite(df_train)
    test = dateSplite(df_test)

    train = train_new.drop(train_new[train_new['pm2.5'] == 0].index)
    train['pm2.5_log'] = np.log(train['pm2.5'])
    train.drop(columns=['pm2.5'], inplace=True)

    x_train = train.drop(columns=['pm2.5_log'])
    y_train = train['pm2.5_log']

    linearModel(x_train, y_train, test)
