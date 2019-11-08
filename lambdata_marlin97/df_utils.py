import numpy as np
import pandas as pd


class LambData:
    """
    This class contains many useful functions for data science. It also contains some personal function that I find useful
    """

    def __init__(self, df=None):
        self.df = df

    def check_nulls(self):
        """
        Checks dataframe for Null values
        """
        nans = sum(self.df.isna().sum())
        print("This DataFrame contains {} missing values".format(nans))

    def list_to_col(self, arry, col_name):
        """
        Takes a list, then converts it to a Series object, and add it to the dataframe as a column
        :returns: Dataframe with new column
        """
        col_name = str(col_name) #ensure col name is a string
        series_obj = pd.Series(arry)
        self.df[col_name] = series_obj
        return self.df

    def set_nb_display(self):
        pass

