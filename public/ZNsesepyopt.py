#!/usr/bin/env python3
import numpy as np
import pandas as pd
from nsepython import *  
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from nsepy import *

# define and month year range to loop over
month_list = np.arange(1, 13, step = 1); print(month_list)

# break the year list into 2 parts - 2005 to 2012 and 2013 to 2020
yr_list = np.arange(2012, 2021, step = 1 ); print(yr_list)

# create empty dataframe to store results
nifty_data = pd.DataFrame() # to use in the loop
option_data = pd.DataFrame() # to store output
counter = 0


for yr in yr_list:
    # loop through all the months and years
    print('Year: ', yr)
    for mnth in month_list:
        current_dt = date(yr, mnth, 1)
        delta =  relativedelta(months = -2)
        start_dt = current_dt + delta
        end_dt = max(get_expiry_date(year = yr, month = mnth))
        
        # print('current: ', current_dt)
        # print('start: ', start_dt)
        # print('end: ', end_dt)
        
        # get nifty futures data
        nifty_fut = get_history(symbol = 'NIFTY',
                               start = start_dt, end = end_dt,
                               index = True,
                               expiry_date = end_dt)
        nifty_data = nifty_data.append(nifty_fut)
        
        # calculate high and low values for each month; round off to get strike prices
        high = nifty_fut['Close'].max()
        high = int(round(high/100)*100) + 1000# ; print('High:', high)
        
        low = nifty_fut['Close'].min()
        low = int(round(low/100)*100) + 1000# ; print('Low :', low)
        for strike in range(low, high, 100): # start, stop, step
            """
            get daily closing nifty index option prices for 3 months 
            over the entire range 
            """
            #time.sleep(random.randint(10,25)) # pause for random interval so as to not overwhelm the site
            nifty_opt = get_history(symbol = 'NIFTY',
                                   start = start_dt, end = end_dt,
                                   index = True, option_type = 'PE',
                                   strike_price = strike,
                                   expiry_date = end_dt)
            
            option_data = option_data.append(nifty_opt)
            
            #time.sleep(random.randint(20,50)) # pause for random interval so as to not overwhelm the site
            nifty_opt = get_history(symbol = 'NIFTY',
                                   start = start_dt, end = end_dt,
                                   index = True, option_type = 'CE',
                                   strike_price = strike,
                                   expiry_date = end_dt)
            
            option_data = option_data.append(nifty_opt)
            
        counter+=1
        print('Months: ', counter)
filename = "/home/ranmag/Desktop/Stocks/2download/nsepyopt2.csv"
option_data.to_csv(filename, index = False, header = True)
filename = "/home/ranmag/Desktop/Stocks/2download/nsepyfut2.csv"
option_data.to_csv(filename, index = False, header = True)