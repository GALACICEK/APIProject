# Weather API Project

- An example project using the Weather API for data science.
There are Current, Forecast  and Historical air pollution data within the project data. 

- Our API gives historical data is accessible from 27th November 2020 and we worked data between 27th November 2020 - 31st December 2023 will be analyzed for Ankara/Turkey. 

 - Source : [Weather API](https://openweathermap.org/api)

 - [Look Detailed API Pricing](https://openweathermap.org/full-price#current)

 - Endpoint:
    - Please, use the endpoint [Air pollution data](https://openweathermap.org/api/air-pollution) for your API calls
    - Plaese, use for get geographical coordinates [by using name of the location](https://openweathermap.org/api/geocoding-api)


---

## __Requirements__ :

- Generate your Weather API with [sign_up](https://openweathermap.org/home/sign_up) on website
    For Api Key Check your email!

- Create config folder that contains config.py
    Add your Weather_API_KEY inside config.py

## __Notes__ :

- request_api.py inside files startdate,enddate variables convert in unix time, [UTC time zone](https://www.unixtimestamp.com/) 
    - in this project start date :  Fri Nov 27 2020 00:00:00 GMT+0000  | 1606435200
    - in this project end date :    Sun Dec 31 2023 23:59:00 GMT+0000  | 1704067140

- [API Error Codes](https://openweathermap.org/api/one-call-3#errors)

### Pollution Values
- Before we get to deep about the analysis We look about the pollutants.
    - Air quality index levels(For UK): 
    - Carbon monoxide(CO_μg/m3) : is a poisonous, flammable gas that is colorless, odorless, tasteless, and slightly less dense than air. [source](https://en.wikipedia.org/wiki/Carbon_monoxide)
    - Nitrogen monoxide(NO_μg/m3)
    - Nitrogen dioxide(NO2_μg/m3)
    - Ozone(O3_μg/m3)
    - Sulphur dioxide(SO2_μg/m3)
    - Fine particles matter(PM2_5_μg/m3)
    - Coarse particulate matter(PM10_μg/m3)
    - Ammonia(NH3_μg/m3)
- Look More Details [source](https://www.greenfacts.org/en/digests/air-pollution.htm)

- In this Project we use scale in UK for pollutants, because our api gives us this parameters.

| Qualitative name      | Index | SO2      | NO2 | PM2.5      | PM10 | O3      |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| Low 	      | 1       | 0-88 	     | 0-67 	      | 0-11 	   | 0-16 	      | 0-33            |
| Low 	      | 2       | 89-177     | 68-134 	      | 12-23 	   | 17-33 	      | 34-66           |
| Low 	      | 3       | 178-266    | 135-200        | 24-35 	   | 34-50 	      | 67-100          |
| Moderate    | 4       | 267-354    | 201-267        | 36-41 	   | 52-58 	      | 101-120         |
| Moderate    | 5       | 355-443    | 268-334        | 42-47 	   | 59-66 	      | 121-140         |
| Moderate    | 6       | 444-532    | 335-400        | 48-53 	   | 67-75 	      | 141-160         |
| High 	      | 7       | 533-710    | 401-467        | 54-58 	   | 76-83 	      | 161-187         |
| High 	      | 8       | 711-887    | 468-534        | 59-64 	   | 84-91 	      | 188-213         |
| High 	      | 9       | 888-1064   | 535-600        | 65-70 	   | 92-100 	  | 214-240         |
| Very High   | 10      | ⩾1065      | ⩾601 	     | P⩾71 	  | T⩾101 	     |  ⩾241          |

