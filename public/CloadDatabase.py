
import pandas as pd
from nsepython import *  
from datetime import datetime
import psycopg2
from psycopg2 import Error
import os
import nsepython


def load_database(db_name):
    
    try:
#       Connect to an existing database
        connection = psycopg2.connect(user="finuser",
                                  password="finpswd",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="findb")

#       Create a cursor to perform database operations
        cursor = connection.cursor()
        # Executing a SQL query
        #cursor.execute(l_query)
        f = open(r'/home/ranmag/Desktop/Stocks/ztemp/temp.csv', 'r')
        cursor.copy_from(f, db_name, sep=',')
        connection.commit()
        
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            #Delete the files from the folder
            dir = '/home/ranmag/Desktop/Stocks/ztemp/'
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))