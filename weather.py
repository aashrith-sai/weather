from getll import weather

c,f=weather()
#print(f)

import mysql.connector
from mysql.connector import Error

try:
    
    connection = mysql.connector.connect(host='localhost',
                                         database='weather',
                                         user='root',
                                         password='password')

    query1=""" CREATE TABLE IF NOT EXISTS Current(lat DOUBLE,
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
                             winddir_compass VARCHAR(3),
                             cloudtotal_pct INT,
                             humid_pct INT,
                             dewpoint_c DOUBLE,
                             vis_km DOUBLE,
                             vis_mi DOUBLE,
                             slp_mb INT,
                             slp_in DOUBLE);"""
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

    query2=""" CREATE TABLE IF NOT EXISTS Forecast(date VARCHAR(10),
                            sunrise_time VARCHAR(10),
                            sunset_time VARCHAR(10),
                            moonrise_time VARCHAR(10),
                            moonset_time VARCHAR(10),
                            temp_max_c DOUBLE,
                            temp_max_f DOUBLE,
                            temp_min_c DOUBLE,
                            temp_min_f DOUBLE,
                            precip_total_mm DOUBLE,
                            precip_total_in DOUBLE,
                            rain_total_mm DOUBLE,
                            rain_total_in DOUBLE,
                            snow_total_mm DOUBLE,
                            snow_total_in DOUBLE,
                            prob_precip_pct INT,
                            humid_max_pct INT,
                            humid_min_pct INT,
                            windspd_max_mph INT,
                            windspd_max_kmh INT,
                            windspd_max_kts INT,
                            windspd_max_ms DOUBLE,
                            windgst_max_mph INT,
                            windgst_max_kmh INT,
                            windgst_max_kts INT,
                            windgst_max_ms DOUBLE,
                            slp_max_in DOUBLE,
                            slp_max_mb INT,
                            slp_min_in DOUBLE,
                            slp_min_mb INT);"""
    query3="""DELETE FROM Forecast;"""

    cursor = connection.cursor()
    cursor.execute(query1)
    connection.commit()
    cursor.execute(mySql_insert_query,val)
    connection.commit()
    cursor.execute(query2)
    connection.commit()
    cursor.execute(query3)
    connection.commit()
    for i in range(7):
        query4="""INSERT INTO Forecast (date,
            sunrise_time,
            sunset_time,
            moonrise_time,
            moonset_time,
            temp_max_c,
            temp_max_f,
            temp_min_c,
            temp_min_f,
            precip_total_mm,
            precip_total_in,
            rain_total_mm,
            rain_total_in,
            snow_total_mm,
            snow_total_in,
            prob_precip_pct,
            humid_max_pct,
            humid_min_pct,
            windspd_max_mph,
            windspd_max_kmh,
            windspd_max_kts,
            windspd_max_ms,
            windgst_max_mph,
            windgst_max_kmh,
            windgst_max_kts,
            windgst_max_ms,
            slp_max_in,
            slp_max_mb,
            slp_min_in,
            slp_min_mb ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        val=('abd',
            f['Days'][i]['sunrise_time'],
            f['Days'][i]['sunset_time'],
            f['Days'][i]['moonrise_time'],
            f['Days'][i]['moonset_time'],
            f['Days'][i]['temp_max_c'],
            f['Days'][i]['temp_max_f'],
            f['Days'][i]['temp_min_c'],
            f['Days'][i]['temp_min_f'],
            f['Days'][i]['precip_total_mm'],
            f['Days'][i]['precip_total_in'],
            f['Days'][i]['rain_total_mm'],
            f['Days'][i]['rain_total_in'],
            f['Days'][i]['snow_total_mm'],
            f['Days'][i]['snow_total_in'],
            f['Days'][i]['prob_precip_pct'],
            f['Days'][i]['humid_max_pct'],
            f['Days'][i]['humid_min_pct'],
            f['Days'][i]['windspd_max_mph'],
            f['Days'][i]['windspd_max_kmh'],
            f['Days'][i]['windspd_max_kts'],
            f['Days'][i]['windspd_max_ms'],
            f['Days'][i]['windgst_max_mph'],
            f['Days'][i]['windgst_max_kmh'],
            f['Days'][i]['windgst_max_kts'],
            f['Days'][i]['windgst_max_ms'],
            f['Days'][i]['slp_max_in'],
            f['Days'][i]['slp_max_mb'],
            f['Days'][i]['slp_min_in'],
            f['Days'][i]['slp_min_mb'] )
        cursor.execute(query4,val)
        connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
