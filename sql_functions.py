import mysql.connector
import datetime
import random
import time


##### MY SQL TABLE
##### time czas | real wartosc
#####

######### CONNECT TO MYSQL DATABASE WITH DEFINED CREDENTIALS ##############
def connect_to_sql():
    try:
        cnx = mysql.connector.connect(user='xmc_user', password='solarnewariaty2018', host='127.0.0.1', database='test')
        if cnx.is_connected():
            print("connected succesfully to MYSQL server")
        else:
            print("couldn't connect do MYSQL server")
    except mysql.connector.Error as e:
        print(e)
    finally:
        return cnx

###### GENERATE AND PUT RANDOM DATA TO DATABASE#############################
def put_random_data_SQL(connection):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    query = "INSERT INTO pomiary (czas, wartosc) VALUES (%s, %s)"
    val = (timestamp, random.randrange(0,100,1))
    print(val)
    cursor = connection.cursor()
    cursor.execute(query,val)
    connection.commit()

###### CHECK LAST ROW's DATE - NEEDED FOR LIVE PLOTS ###########################
def check_last_row(connection, timestamp_to_check):
    query = "SELECT * from pomiary ORDER BY czas DESC"
    cursor = connection.cursor(buffered=True)
    cursor.execute(query)
    row = cursor.fetchone()
    row_ts = row[0].strftime('%Y-%m-%d %H:%M:%S')
    cursor.fetchall()
    if row_ts == timestamp_to_check:
        return (True , 0, row_ts)
    else:
        return (False, row[1], row_ts)

####### RETURN ROWS THAT ARE BEETWEEN SELECTED DATES ############################
def logs_btwn_dates(connection, start, end):
    data = None
    try:
        query = """ SELECT * from pomiary
                    WHERE czas BETWEEN %s and %s
                   """
        cursor = connection.cursor()
        cursor.execute(query, (start, end))
        data = cursor.fetchall()
    except mysql.connector.Error as e:
        print(e)
    finally:
        return data








