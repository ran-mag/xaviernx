#!/usr/bin/env python3
import pandas as pd
from nsepython import *  

from datetime import datetime, date





def bhav_dwnldmass(dwnld_day):
    get_bhavcopy_day = dwnld_day.strftime('%d-%m-%Y')
    fname = dwnld_day.strftime('%Y%m%d')

    print(dwnld_day)
    bhav = get_bhavcopy((get_bhavcopy_day))
    bhav_filtered = bhav.iloc[:, 0:14]
    bhav_cleaned = bhav_filtered.replace(to_replace =[" ", " -"],value ="")

    
#create filepath and name
    filename = "/home/ranmag/Desktop/pyPro/Finance/Stocks/Data/csv/1Download/"+fname+".csv"
    bhav_cleaned.to_csv(filename, index = False, header = False)

def fo_dwnldmass(dwnld_day):
    get_bhavcopy_day = dwnld_day.strftime('%d-%m-%Y')
    fname = dwnld_day.strftime('%Y%m%d')

    print(dwnld_day)
    bhav = get_bhavcopy((get_bhavcopy_day))
    bhav_filtered = bhav.iloc[:, 0:14]
    bhav_cleaned = bhav_filtered.replace(to_replace =[" ", " -"],value ="")

    
#create filepath and name
    filename = "/home/ranmag/Desktop/pyPro/Finance/Stocks/Data/csv/1Download/"+fname+".csv"
    bhav_cleaned.to_csv(filename, index = False, header = False)