from getll import weather

c,forecast=weather()
#print(current,forecast)

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='weather',
                                         user='root',
                                         password='password')

    mySql_Create_Table_Query = """CREATE TABLE Current (
                             lat DOUBLE,
                             lon DOUBLE,
                             alt_m DOUBLE,
                             alt_f DOUBLE,
                             wx_desc VARCHAR(30),
                             wx_code INT,
                             wx_icon VARCHAR(300),
                             temp_c DOUBLE,
                             temp_f DOUBLE,
                             feelslike_c DOUBLE,
                             feelslike_f DOUBLE,
                             windspd_mph INT,
                             windspd_kmh INT,
                             windspd_kts INT,
                             windspd_ms DOUBLE,
                             winddir_deg INT,
                             winddir_compass VARCHAR(20),
                             cloudtotal_pct INT,
                             humid_pct INT,
                             dewpoint_c DOUBLE,
                             vis_km DOUBLE,
                             vis_mi DOUBLE,
                             slp_mb INT,
                             slp_in DOUBLE); """
    connection = mysql.connector.connect(host='localhost',
                                         database='weather',
                                         user='root',
                                         password='password')
    mySql_insert_query = """INSERT INTO Laptop (lat,
                             lon,
                             alt_m,
                             alt_f,
                             wx_desc,
                             wx_code,
                             wx_icon,
                             temp_c,
                             temp_f,
                             feelslike_c,
                             feelslike_f,
                             windspd_mph,
                             windspd_kmh,
                             windspd_kts,
                             windspd_ms,
                             winddir_deg,
                             winddir_compass,
                             cloudtotal_pct,
                             humid_pct,
                             dewpoint_c,
                             vis_km,
                             vis_mi,
                             slp_mb,
                             slp_in) 
                           VALUES (c['lat'],
                             c['lon'],
                             c['alt_m'],
                             c['alt_f'],
                             c['wx_desc'],
                             c['wx_code'],
                             c['wx_icon'],
                             c['temp_c'],
                             c['temp_f'],
                             c['feelslike_c'],
                             c['feelslike_f'],
                             c['windspd_mph'],
                             c['windspd_kmh'],
                             c['windspd_kts'],
                             c['windspd_ms'],
                             c['winddir_deg'],
                             c['winddir_compass'],
                             c['cloudtotal_pct'],
                             c['humid_pct'],
                             c['dewpoint_c'],
                             c['vis_km'],
                             c['vis_mi'],
                             c['slp_mb'],
                             c['slp_in']) """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
