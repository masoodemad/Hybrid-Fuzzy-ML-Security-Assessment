import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(df):

    # One-hot encoding
    df = pd.get_dummies(df)

    # Min-Max Normalization
    scaler = MinMaxScaler()
    df[df.columns] = scaler.fit_transform(df[df.columns])

    return df
