
import pandas as pd
from datetime import datetime
from pandas.core.frame import DataFrame
import psycopg2
from psycopg2 import Error
import os


def read_database(query,cols):
    
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
        cursor.execute(query)
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=cols)
        
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            if len(cols) == 1:
                return rows
            else:
                return df