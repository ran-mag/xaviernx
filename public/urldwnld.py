#!/usr/bin/env python3
import pandas as pd
import os, sys
from datetime import datetime
import requests
from zipfile import ZipFile


def getFile(url):  
    path='/home/ranmag/Desktop/Stocks/ztemp/tempd'
    r = requests.get(url, allow_redirects=True)
    if r.status_code != 200:
        raise Exception(f"{url} is down!")
            
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)


#If zip file, unzip file
    if 'zip' in url:
        zf = ZipFile('/home/ranmag/Desktop/Stocks/ztemp/tempd', 'r')
        zf.extractall('/home/ranmag/Desktop/Stocks/ztemp')
        t_day = datetime.today().strftime('%d%b%Y')
#        t_day = "02JUL2021"
#        fdate = t_day.upper()
        fname = url[69:89]
        source='/home/ranmag/Desktop/Stocks/ztemp/'+fname
        dest  ='/home/ranmag/Desktop/Stocks/ztemp/tempde.csv'
        os.rename(source,dest)
        zf.close()

def prepare_load_bhav():
    bc = pd.read_csv ('/home/ranmag/Desktop/Stocks/ztemp/tempde.csv', sep=',')  
    bc_firststep = bc[['SYMBOL', 'SERIES', 'TIMESTAMP',  'PREVCLOSE', 'OPEN', 'HIGH', 'LOW', 'LAST', 'CLOSE', 'TOTTRDQTY', 'TOTTRDVAL', 'TOTALTRADES']]
    bc_firststep = bc_firststep.assign(AVERAGE = bc_firststep.loc[:,['HIGH','LOW']].mean(axis=1))
#    df = df.assign(avg=df.loc[:, ["Monday", "Tuesday", "Wednesday"]].mean(axis=1))
    bc_secondstep = bc_firststep[['SYMBOL', 'SERIES', 'TIMESTAMP',  'PREVCLOSE', 'OPEN', 'HIGH', 'LOW', 'LAST', 'CLOSE','AVERAGE', 'TOTTRDQTY', 'TOTTRDVAL', 'TOTALTRADES']]
    bc_secondstep['DELIV_QTY'] = 0
    bc_secondstep.to_csv('/home/ranmag/Desktop/Stocks/ztemp/temp.csv', sep=',', index = False, header=False)

        