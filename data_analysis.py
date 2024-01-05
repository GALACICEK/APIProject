import numpy as np
import pandas as pd

import pandas_init as pdinit


df_current,df_forecast,df_historical = pdinit.pandas_init()

def history_analysis_init():

    df_current.isna()

    if df_historical.duplicated().sum()>0:

        df_historical.drop_duplicates(inplace=True)


    return None



"""if __name__ == '__main__':
    data_analysis()
"""