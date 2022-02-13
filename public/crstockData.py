#!/usr/bin/env python3
import pandas as pd
from datetime import datetime, date

from pandas.core.frame import DataFrame
from CreadDatabase import read_database
from cInsertDatabase import insert_database
import decimal

#select all IDs from stock_data
get_stock_list_query = "select distinct id from bhav_copy WHERE (series = 'EQ' or series = ' EQ') order by id"
column_names = ["id"]
stock_list = read_database(get_stock_list_query,column_names)
column_name = '"id","open_close_pos","open_close_neg","open_close_pos_perc","open_close_pos_mean","open_close_neg_mean","open_close_pos_stdd","open_close_pos_mean","open_close_neg_stdd","high_low_mean","high_low_stdd"'

def create_stock_data(df):
    
    df['open_close_gain']= df['close_price']-df['open_price']
    df['open_close']= (df['close_price']-df['open_price'])/(df['open_price'])
    df['high_low']= (df['high_price']-df['low_price'])/(df['high_price'])
    df_pos= df[df['open_close'] >=0]
    df_neg= df[df['open_close'] <0]
    

    stock_id= df['id'] 
    total_recs= len(df)
    open_close_pos= len(df_pos)
#    print(len(df_neg),len(df_pos))
    open_close_neg= len(df_neg)
    if total_recs > 0:
        open_close_pos_perc= open_close_pos*100/(total_recs)
        open_close_pos_perc_str="{:.2f}".format(open_close_pos_perc)
    else:
        open_close_pos_perc_str="0.00"
    open_close_pos_series= (pd.to_numeric(df_pos["open_close"]))*100
    open_close_neg_series= (pd.to_numeric(df_neg["open_close"]))*100
    open_close_gain_series=(pd.to_numeric(df["open_close"]))*100
    open_close_gain_sum= "{:+.2f}".format(open_close_gain_series.sum())
    open_close_pos_mean= "{:+.2f}".format(open_close_pos_series.mean())
    open_close_neg_mean= "{:+.2f}".format(open_close_neg_series.mean())
    open_close_pos_stdd= "{:+.2f}".format(open_close_pos_series.std())
    open_close_neg_stdd= "{:+.2f}".format(open_close_neg_series.std())
    open_close_pos_str = "{:+.2f}".format(open_close_pos)
    open_close_neg_str = "{:+.2f}".format(open_close_neg)
#    print(type(open_close_pos_stdd))
    high_low_series= (pd.to_numeric(df['high_low'])*100)
    high_low_mean= "{:+.2f}".format(high_low_series.mean())
    high_low_stdd= "{:+.2f}".format(high_low_series.std())


    if open_close_gain_sum=='+nan':
        open_close_gain_sum='0.00'

    if open_close_pos_mean=='+nan':
        open_close_pos_mean='0.00'

    if open_close_neg_mean=='+nan':
        open_close_neg_mean='0.00'

    if open_close_pos_stdd=='+nan':
        open_close_pos_stdd='0.00'

    if open_close_neg_stdd=='+nan':
        open_close_neg_stdd='0.00'

    if open_close_pos_str=='+nan':
        open_close_pos_str='0.00'

    if open_close_neg_str=='+nan':
        open_close_neg_str='0.00'

    if high_low_mean=='+nan':
        high_low_mean='0.00'

    if high_low_stdd=='+nan':
        high_low_stdd='0.00'

    stock_id_str= str
#    print(stock_id_str,open_close_gain_series, open_close_gain_sum)
    """
    print(type(stock_id))
    print(type(open_close_pos))
    print(type(open_close_neg))
    print(type(open_close_pos_perc))
    print(type(open_close_pos_mean))
    print(type(open_close_pos_stdd))
    """
    stock_data_string = "'"+stock_id_str+"'," +open_close_pos_str+"," +open_close_neg_str+"," +open_close_pos_perc_str+"," +open_close_pos_mean+"," +open_close_neg_mean+"," +open_close_pos_stdd+"," +open_close_neg_stdd+"," +high_low_mean+"," +high_low_stdd+","+open_close_gain_sum
    return stock_data_string


for x in stock_list:
    str = ''.join(x)
    get_stock_data_query = "select * from bhav_copy where id = '" + str+ "' and (series = 'EQ' or series = ' EQ') order by id"
    column_names = ["id","series","datex","prev_close","open_price","high_price","low_price","last_price","close_price","avg_price","ttl_trd_qnty","turnover_lacs","no_of_trades","deliv_qty"]
    stock_data = read_database(get_stock_data_query, column_names)
    
    stock_data_insert = create_stock_data(stock_data)
    insert_database(stock_data_insert, column_name)
























