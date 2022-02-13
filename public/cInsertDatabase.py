
import pandas as pd
import psycopg2
from psycopg2 import Error
import os



def insert_database(data, columns):
    
    try:
#       Connect to an existing database
        connection = psycopg2.connect(user="finuser",
                                  password="finpswd",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="findb")

#       Create a cursor to perform database operations
        #sql="insert into stock_data values %s"
#        query = "INSERT INTO stock_data("+columns+") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        query = "INSERT INTO stock_data_all VALUES ("+data+")"
        cursor = connection.cursor()
        param = data
#       Executing a SQL query
        cursor.execute(query)
        connection.commit()
        
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed",data)
            