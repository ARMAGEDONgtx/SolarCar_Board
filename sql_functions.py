#File containg all functions handling sql database


import mysql.connector
import datetime
import random
import time
import json


######### CONNECT TO MYSQL DATABASE WITH DEFINED CREDENTIALS ##############
#user crediential must be provided
#database name and its location(IP adress, if on the same machine its 127.0.0.1)
def connect_to_sql():
    cnx = None
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
#function created for test purposes
#in futere date will come frome other devieces
def put_random_data_SQL(connection):
    try:
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO pomiary (czas, wartosc) VALUES (%s, %s)"
        val = (timestamp, random.randrange(0,100,1))
        print(val)
        cursor = connection.cursor()
        cursor.execute(query,val)
        connection.commit()
    except mysql.connector.Error as e:
        print(e)


###### GENERATE AND PUT RANDOM JSON TO DATABASE#############################
#function created for test purposes
#in futere date will come frome other devieces
def put_random_json_SQL(connection, object_id):
    if object_id is None:
        return None
    try:
        query = "INSERT INTO solar_dynamics.dane (jdoc, id_pomiaru) VALUES (%s, %s)"
        val = random.randrange(0,100,1)
        str_val = "{\"value\":"+ str(val) + "}"
        print(str_val)
        cursor = connection.cursor()
        cursor.execute(query,(str_val, object_id))
        connection.commit()
    except mysql.connector.Error as e:
        print(e)


####### RETURN ROWS THAT ARE BEETWEEN SELECTED DATES ############################
#function for historical plots, allows to check date beetween dates
def logs_btwn_dates(start, end, pom_id):
    if pom_id is None:
        return None
    data = None
    connection = None
    try:
        connection = connect_to_sql()
        query = """ SELECT czas, jdoc from solar_dynamics.dane
                    WHERE czas BETWEEN %s and %s
                    AND id_pomiaru = %s
                   """
        cursor = connection.cursor()
        cursor.execute(query, (start, end, pom_id))
        data = cursor.fetchall()
    except mysql.connector.Error as e:
        print(e)
    finally:
        if connection is not None:
            connection.close()
        return data


####### RETURN AVAIABLE MEASURMETNS IN SQL TABLE  ############################
def avaiable_measurments(connection, id_obiektu):
    if id_obiektu is None:
        return None
    data = None
    try:
        query = """ SELECT id_pomiaru, nazwa_pomiaru from solar_dynamics.pomiary
                      WHERE id_obiektu = %s
                     """
        cursor = connection.cursor()
        cursor.execute(query, (id_obiektu,))
        data = cursor.fetchall()
    except mysql.connector.Error as e:
        print(e)
    finally:
        return data


#transalte nazwa_pomiaru to id_pomiaru v2
def nazwa_pomiaru_to_id(connection, nazwa):
    if nazwa == "":
        return None
    data = None
    try:
        query1 = """ SELECT id_pomiaru from solar_dynamics.pomiary
                                  WHERE nazwa_pomiaru = %s
                                 """
        cursor = connection.cursor()
        cursor.execute(query1, (nazwa,))
        data = cursor.fetchall()
    except mysql.connector.Error as e:
        print(e)
    finally:
        return data[0][0]


def data_from_object(measurment):
    data = None
    try:
        connection = connect_to_sql()
        cursor = connection.cursor()
        tmp_id = nazwa_pomiaru_to_id(connection, measurment)
        query2 = """ SELECT * from solar_dynamics.dane
                      WHERE id_pomiaru = %s
                     """
        cursor.execute(query2,(tmp_id,))
        data = cursor.fetchall()
    except mysql.connector.Error as e:
        print(e)
    finally:
        connection.close()
        return data

###### CHECK LAST ROW's DATE - NEEDED FOR LIVE PLOTS ###########################
def check_last_row(pomiar):
    if pomiar is None:
        return (True, 0)
    connection = None
    try:
        connection = connect_to_sql()
        query = """ SELECT czas,jdoc from solar_dynamics.dane
                    WHERE id_pomiaru = %s
                    ORDER BY czas DESC
                    """
        cursor = connection.cursor(buffered=True)
        cursor.execute(query, (pomiar.measurment_id,))
        row = cursor.fetchone()
        row_ts = row[0].strftime('%Y-%m-%d %H:%M:%S')
        cursor.fetchall()
        if row_ts == pomiar.last_update :
            return (True , 0)
        else:
            pomiar.last_update = row_ts
            return (False, (json.loads(row[1]))['value'])
    except mysql.connector.Error as e:
        print(e)
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":

    str =  {"value" : 12}
    js = json.dumps(str)

    test = json.loads(js)
    print(test['value'])






