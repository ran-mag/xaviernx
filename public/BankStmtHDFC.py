#!/usr/bin/env python3
import pandas as pd
from datetime import datetime
import glob
import os

from pandas.core.frame import DataFrame

def  update_csv():
#expand the file by adding columns   
    df['strng'] = ''
    df['narration1'] = ''
    df['narration2'] = ''
    for j in range(len(class_fil)):
        search_each_str(class_fil['string'].loc[j],class_fil['narration1'].loc[j],class_fil['narration2'].loc[j])

    return()

def search_each_str(srcstr,nar1,nar2):
    for i in range(len(df)):   
        if df['Narration'].loc[i].find(srcstr) == -1:
            continue
        else:
            df['strng'].loc[i] = srcstr
            df['narration1'].loc[i] = nar1
            df['narration2'].loc[i] = nar2
    



pathin = '/home/ranmag/Desktop/Finance/Tax/Bank statements/Test'

csv_files = glob.glob(os.path.join(pathin, "*.xls"))

# read classification file
class_fil = pd.read_excel('/home/ranmag/Desktop/Finance/Tax/Bank statements/HDFC Class.xls')



for f in csv_files:

# read the csv file
    df = pd.read_excel(f)
    pathout = f.replace('Test','output')
    print(f)

# update the csv file
    update_csv()
# write the csv file
    df.to_excel(pathout) 



