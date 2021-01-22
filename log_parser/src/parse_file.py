import os, time 
from influxdb import InfluxDBClient
from src.parse_file import parse_line
from conf.constants import CONSTANTS
from conf.constants import INFLUX_INFO 

def check_error(line):
    return False 

def write_to_db(json, influx_client):
    if CONSTANTS["NO_DB"]:
        print(f"Writing to db: {json}")
        return None
    try:
        influx_client.ping()
    except:
        report_error("PYTHON ERROR: CONNECTION TO INFLUX LOST")
    if not influx_client.write_points(json):
        report_error("PYTHON ERROR: COULD NOT WRITE TO DATABASE")

def report_error(line):
    # TODO: handle errors separately
    print(f"ERROR: {line}")

def proces_file():
    filename = CONSTANTS["LOG_FILEPATH"]
    log_file = open(filename,'r')
    file_size = os.stat(filename)[6]
    log_file.seek(file_size)
    influx = InfluxDBClient(host=INFLUX_INFO['HOST'],
                            port=INFLUX_INFO['PORT'],
                            username=INFLUX_INFO['USERNAME'],
                            password=INFLUX_INFO['PASSWORD'])
    dbname = INFLUX_INFO['DBNAME'] 
    influx.create_database(dbname) #going to assume this gets ignored if it already exists for now
    influx.switch_database(dbname)
    while True:
        where = log_file.tell()
        line = log_file.readline()
        if not line:
            time.sleep(CONSTANTS["FILE_READ_RATE_IN_SEC"])
            log_file.seek(where)
        else:
            json_data = parse_line(line.strip())
            if json_data:
                write_to_db(json_data, influx)