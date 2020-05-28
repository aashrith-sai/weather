from getll import weather

current,forecast=weather()
#print(current,forecast)
print('hello')
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='weather',
                                         user='some-mysql',
                                         password='my-secret-pw')

    mySql_Create_Table_Query = """CREATE TABLE Laptop (
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
                             slp_in DOUBLE) """
