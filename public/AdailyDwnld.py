#!/usr/bin/env python3
import pandas as pd
from nsepython import *  
from datetime import datetime
from Bwebdwnldpkg import *





Holiday_list = pd.json_normalize(nse_holidays()['FO'])
nonTradedays= str(Holiday_list.tradingDate)
#print (nonTradedays)

t_day = datetime.today().strftime('%d-%b-%Y')
day_num = datetime.today().strftime('%w')
int_day_num = int(day_num)

holiday_flag = t_day in nonTradedays


int_day_num = 4

if (int_day_num > 5) or ( holiday_flag) or (int_day_num == 0):
    print("non trading day")
else :
#    print("trading day")
    bhav_dwnld()
    bulk_dwnld()
    block_dwnld()
    fo_dwnld()

    
 
