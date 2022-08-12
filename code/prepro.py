from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd
import numpy as np


class Prepro:

    def __init__(self, df:pd.DataFrame):
        self.df = df

    def create_series(self, xcol:str, datecol:str):
        # Create a dataframe with the features and the date time as the index
        features = self.df[[xcol]]
        features.index = self.df[datecol]
        features.index = features.index.astype('datetime64[ns]')
        return features
        
    def split_train_test(self, features:pd.DataFrame, split_size:int, look_back:int):

        # Split train data and test data
        train_size = int(len(features)*split_size)
        train_data = features.iloc[:train_size]
        test_data = features.iloc[train_size:]

        # Scale data
        # The input to scaler.fit -> array-like, sparse matrix, dataframe of shape (n_samples, n_features)
        scaler = MinMaxScaler().fit(train_data)

        train_scaled = scaler.transform(train_data)
        test_scaled = scaler.transform(test_data)

        # Th input rnn shape should be [samples, time steps, features]
        X_train = [train_scaled[i:i+look_back] for i in range(len(train_scaled)-look_back)]
        y_train = [train_scaled[i+look_back] for i in range(len(train_scaled)-look_back)]

        X_test = [test_scaled[i:i+look_back] for i in range(len(test_scaled)-look_back)]
        y_test = [test_scaled[i+look_back] for i in range(len(test_scaled)-look_back)]

        return np.array(X_train), np.array(y_train), np.array(X_test), np.array(y_test), scaler