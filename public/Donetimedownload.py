#!/usr/bin/env python3
import numpy as np
import pandas as pd
import nsepython
from nsepython import * 
from datetime import datetime, date, timedelta
from EwebDwnldmass import *
from Bwebdwnldpkg import *

"""
#Get Holiday list
#Holiday_list = pd.json_normalize(nse_holidays())
print(Holiday_list)
print(type(Holiday_list))
#nonTradedays= Holiday_list.tradingDate()
"""
nonTradeday18 = ["26-Jan-2018", "13-Feb-2018", "02-Mar-2018", "29-Mar-2018", "30-Mar-2018", 
                "15-Aug-2018", "01-May-2018", "25-Dec-2018", "22-Aug-2018", "15-Aug-2018",
                "13-Sep-2018","20-Sep-2018", "25-Dec-2018",
                "02-Oct-2018", "18-Oct-2018", "07-Nov-2018", "08-Nov-2018","23-Nov-2018"]


nonTradeday19 = ["21-Mar-2019", "04-Mar-2019", "05-Jun-2019", "17-Apr-2019", "19-Apr-2019", 
                "29-Apr-2019", "01-May-2019", "25-Dec-2019", "12-Aug-2019", "15-Aug-2019",
                "02-Sep-2019","10-Sep-2019",
                "02-Oct-2019", "08-Oct-2019", "21-Oct-2019", "28-Oct-2019","12-Nov-2019"]

nonTradeday20 = ["21-Feb-2020", "10-Mar-2020", "14-Apr-2020", "02-Apr-2020", "06-Apr-2020", 
                "10-Apr-2020", "01-May-2020", "25-Dec-2020", "25-May-2020", "02-Oct-2020",
                "16_nov-2020", "30-Nov-2020"]

nonTradeday21 = ["21-Mar-2021", "11-Mar-2021", "29-Mar-2021", "02-Apr-2021", "14-Apr-2021", 
                "21-Apr-2021", "13-May-2021", "21-Jul-2021", "19-Aug-2021", "10-Sep-2021",
                "15-Oct-2021","05-Nov-2021", "19-Nov-2021"]



#Set the date parameters
start_date = date(2021, 7, 16)
end_date = date(2021, 12, 9)
delta = timedelta(days=1)
 
while start_date <= end_date:
    d_day = start_date.strftime('%d-%b-%Y')
    day_num = start_date.strftime('%w')
    int_day_num = int(day_num)
    year = start_date.year
    if year == 2018:
        nonTradedays = nonTradeday18
    elif year == 2019:
        nonTradedays = nonTradeday19
    elif year == 2020:
        nonTradedays = nonTradeday20
    else:
        nonTradedays = nonTradeday21

    holiday_flag = d_day  in nonTradedays
    
    if (int_day_num > 5) or ( holiday_flag) or (int_day_num == 0):
        print("non trading day")
    else:
        bhav_dwnld_mass(start_date)
    start_date+=delta

"""
        bhav_dwnld_mass(start_date)            
        bulk_dwnld_mass(start_date)
        block_dwnld_mass(start_date)
        fo_dwnld_mass((start_date)
        bhav_dwnld_url(start_date)
"""

    














    
    





