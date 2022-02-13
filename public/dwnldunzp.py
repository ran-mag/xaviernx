#!/usr/bin/env python3
from datetime import datetime
import requests
import zipfile
from urldwnld import *

#Download file
t_day = datetime.today().strftime('%d%b%Y')
year = datetime.today().strftime('%Y/')
month = datetime.today().strftime('%b/')
fdate = t_day.upper()
fyear = year.upper()
fmonth = month.upper()
urlin = 'https://archives.nseindia.com/content/historical/DERIVATIVES/'+fyear+fmonth+'fo'+fdate+'bhav.csv.zip'

getFile(urlin)
loadDataFO()
