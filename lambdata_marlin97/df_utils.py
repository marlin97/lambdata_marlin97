import numpy as np
import pandas as pd


ones = pd.Series(np.ones(20))
zeros = pd.Series(np.zeros(20))

def check_nulls(df):
    nans = sum(df.isna().sum())
    print("This DataFrame contains {} missing values".format(nans))


