import pandas as pd
from datetime import datetime

import request_api as reqdata

def convert_to_datetime(unix_timestamp):
    # Unix zaman damgasını tarih ve saat değerine çevir
    return datetime.utcfromtimestamp(unix_timestamp)


def create_dataframe_from_response(response_list):
    data = []
    for responce in response_list:
        record = {
            'datetimes': convert_to_datetime(responce['dt']),
            'air_quality_index': responce['main']['aqi'],
            'concentration_of_CO_μg/m3': responce['components']['co'],
            'concentration_of_NO_μg/m3': responce['components']['no'],
            'concentration_of_NO2_μg/m3': responce['components']['no2'],
            'concentration_of_O3_μg/m3': responce['components']['o3'],
            'concentration_of_SO2_μg/m3': responce['components']['so2'],
            'concentration_of_PM2_5_μg/m3': responce['components']['pm2_5'],
            'concentration_of_PM10_μg/m3': responce['components']['pm10'],
            'concentration_of_NH3_μg/m3': responce['components']['nh3']
        }
        data.append(record)
    
    return pd.DataFrame(data)

def pandas_init():

    current_response,forecast_response,historical_response =  reqdata.get_request()

    df_current = create_dataframe_from_response(current_response['list'])
    df_forecast = create_dataframe_from_response(forecast_response['list'])
    df_historical = create_dataframe_from_response(historical_response['list'])


if __name__ == '__main__':
    pandas_init()
