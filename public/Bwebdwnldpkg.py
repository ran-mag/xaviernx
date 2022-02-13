#!/usr/bin/env python3
import pandas as pd
import nsepy
from datetime import datetime
import psycopg2
from psycopg2 import Error
import os
from CloadDatabase import *
from urldwnld import *

def bhav_dwnld():
    t_day = datetime.today().strftime('%d-%m-%Y')
#    fname = datetime.today().strftime('%Y%m%d')
    fname="temp" 
#    t_day = "02-07-2021"
    bhav = get_bhavcopy((t_day))

    bhav_filtered = bhav.iloc[:, 0:14]
    bhav_cleaned = bhav_filtered.replace(to_replace =[" ", " -"],value ="0")
    
#create filepath and name
    filename = "/home/ranmag/Desktop/Stocks/ztemp/"+fname+".csv"
    bhav_cleaned.to_csv(filename, index = False, header = False)
    load_database("bhav_copy")






def bulk_dwnld():
    t_day = datetime.today().strftime('%d-%m-%Y')
#    fname = datetime.today().strftime('%Y%m%d')
    fname="temp" 
#    t_day = "01-07-2021"
    bulk = get_bulkdeals()
    bulk_filtered = bulk.iloc[:, [0,1,3,4,5,6]]
    bulk_cleaner = bulk_filtered.replace(to_replace =["BUY"],value ="t")
    bulk_cleaned = bulk_cleaner.replace(to_replace =["SELL"],value ="f")
    
#create filepath and name
    filename = "/home/ranmag/Desktop/Stocks/ztemp/"+fname+".csv"
    bulk_cleaned.to_csv(filename, index = False, header = False)
    load_database("bulk_copy")






def block_dwnld():
    t_day = datetime.today().strftime('%d-%m-%Y')
#    fname = datetime.today().strftime('%Y%m%d')
    fname="temp" 
#    t_day = "01-07-2021"
    block = get_blockdeals()
    print(block)
    block_filtered = block.iloc[:, [0,1,3,4,5,6]]
    block_cleaner = block_filtered.replace(to_replace =["BUY"],value ="t")
    block_cleaned = block_cleaner.replace(to_replace =["SELL"],value ="f")
    
#create filepath and name
    filename = "/home/ranmag/Desktop/Stocks/ztemp/"+fname+".csv"
    block_cleaned.to_csv(filename, index = False, header = False)
    load_database("block_copy")

def fo_dwnld():
    
    t_day = datetime.today().strftime('%d%b%Y')
#    t_day = "02JUL2021"
    year = datetime.today().strftime('%Y/')
    month = datetime.today().strftime('%b/')
    fdate = t_day.upper()
    fyear = year.upper()
    fmonth = month.upper()
    urlin = 'https://archives.nseindia.com/content/historical/DERIVATIVES/'+fyear+fmonth+'fo'+fdate+'bhav.csv.zip'

    getFile(urlin)
    fo = pd.read_csv ('/home/ranmag/Desktop/Stocks/ztemp/tempde.csv', sep=',')
    fo_filter1 = fo.iloc[0:,0:15 ]
    fo_filtered = fo_filter1[fo_filter1['CONTRACTS'] > 0]
    print(fo_filtered)

#    print(fo_filtered)
    fo_grps = fo_filtered.groupby('INSTRUMENT', dropna=True)
    fo_id = fo_grps.get_group('FUTIDX')
    fo_stk = fo_grps.get_group('FUTSTK')
    fo_futures = pd.concat([fo_id,fo_stk], axis=0)
    fo_fut_final = fo_futures.iloc[0:,1:]
#    print(fo_fut_final)
    fo_id = fo_grps.get_group('OPTIDX')
    fo_stk = fo_grps.get_group('OPTSTK')
    fo_options = pd.concat([fo_id,fo_stk], axis=0)
    fo_opt_final = fo_options.iloc[0:,1:]
#    print(fo_options)

#create filepath and name
    filename = "/home/ranmag/Desktop/Stocks/ztemp/temp.csv"
    fo_fut_final.to_csv(filename, index = False, header = False)
    load_database("fo_fut")

    filename = "/home/ranmag/Desktop/Stocks/ztemp/temp.csv"
    fo_opt_final.to_csv(filename, index = False, header = False)
    load_database("fo_opt")


    load_database("fo_opt")

def bhav_dwnld_url(dwnld_date):
    
    t_day = dwnld_date.strftime('%d%b%Y')
#    t_day = "02JUL2021"
    year = dwnld_date.strftime('%Y/')
    month = dwnld_date.strftime('%b/')
    bdate = t_day.upper()
    bmonth = month.upper()
#    urlin = 'https://archives.nseindia.com/content/historical/DERIVATIVES/'+fyear+fmonth+'fo'+fdate+'bhav.csv.zip'
    urlin = 'https://archives.nseindia.com/content/historical/EQUITIES/'+year+'/'+bmonth+'/cm'+bdate+'bhav.csv.zip'
    getFile(urlin)
    prepare_load_bhav()
    load_database("bhav_copy")