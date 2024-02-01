import pandas as pd
import plotly.express as px
import calendar

#yearly exports data
us_exports_yearly = pd.read_csv('us_exports_yearly_avgs.csv')

#plotting data against year using plotly line
variables = ['avg_citrus_export_value', 'total_citrus_export_value',
       'avg_soybeans_export_value', 'total_soybeans_export_value']

for var in variables:
    fig = px.line(us_exports_yearly,
                x="year",
                y=var,
                title = f'{var} from 2002-2020',
                markers= True
                )
    fig.show()

#yearly citrus exports:
# It is evident that the average citrus export value has increased gradually from 2002 to 2020, with the exception of a dip in 2019.
#The total citrus exports value increased from 2002-2016 and decreased from 2017-2020.
#This is interesting since 2020 has a very high average citrus export value but low total value.
#This could indicate that citrus export patterns are more volatile in 2020, with a few very high months to skew the average up. 

#yearly soybean exports:
#The average soybean export value increased gradually from 2002 to 2012, with it decreasing gradually from 2012 onwards.
#A similar pattern was seen with total soybean export value.


#monthly exports data
us_exports_monthly = pd.read_csv('us_exports_monthly_avgs.csv')
us_exports_monthly.head()

#convert month from number value to abbreviated name:
months = [calendar.month_abbr[value] for value in us_exports_monthly['month']]
us_exports_monthly['month'] = months

#create line graphs
month_variables = ['citrus_export_value', 'soybeans_export_value',]

for var in month_variables:
    fig = px.line(us_exports_monthly,
                x='month',
                y=var,
                color='year',
                title = f'{var} from 2002-2020',
                markers= True
                )
    fig.show()

#It appears that citrus export values are higher in the winter, from december-march, with exports peaking in march.
#This is consistent from 2002-2020.
# By looking at the monthly citrus export value in 2020, it is evident that data was only collected up to August 2020 which explains the lower total citrus export value. 
#The much higher average citrus export value in 2020 also appears to be due to the lack of data collection from september to december 2020.
#Evidently citrus exports are not as high from october-december months compared to jan-march, so the absence of these months in the 2020 data is what skewed the average up.

#The export values for soybeans appears to peak in the fall and winter, from october-january with values peaking at october and november. 
#This is consistent from 2002-2019, with the data not in the dataset in 2020 for those months.

