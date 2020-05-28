from getll import weather

c,forecast=weather()
print(c)

import mysql.connector
from mysql.connector import Error

try:
    
    connection = mysql.connector.connect(host='localhost',
                                         database='weather',
                                         user='root',
                                         password='password')
    mySql_insert_query = """INSERT INTO Current (lat,
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
                             slp_in) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); """
    val=(c['lat'],c['lon'],
                             c['alt_m'],
                             c['alt_ft'],
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
                             c['slp_in'])
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query,val)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
