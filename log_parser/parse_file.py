import os, time, 
from influxdb import InfluxDBClient
from constants import CONSTANTS
from constants import INFLUX_INFO 

def get_new_lines():
    return [] 

def check_error(line):
    return False 

def check_relevant(line):
    return True

def parse_data(line):
    # TODO @james pls implemnt
    # Sample lines
    #   2021.01.11:17:31:54.389: main Eth speed: 80.770 MH/s, shares: 606/0/0, time: 7:33
    #   2021.01.11:17:31:55.832: main Eth: Accepted shares 607 (0 stales), rejected shares 0 (0 stales)
    #   2021.01.11:17:31:55.832: main Eth: Incorrect shares 0 (0.00%), est. stales percentage 0.00% 
    #   2021.01.11:17:31:55.832: main Eth: Maximum difficulty of found share: 4008.0 GH (!)
    #   2021.01.11:17:31:55.832: main Eth: Average speed (5 min): 79.442 MH/s 
    #   GPUs power: 322.4 W
    #   2021.01.11:17:31:34.580: main GPU1: 70C 65% 322W
    return f"jsonified {line}"

def write_to_db(data, influx_client):
    if CONSTANTS["NO_DB"]:
        print(f"Writing to db: {line}")
        return None
    try:
        influx_client.ping()
    except:
        report_error("PYTHON ERROR: CONNECTION TO INFLUX LOST")
    if not influx_client.write_points(json):
        report_error("PYTHON ERROR: COULD NOT WRITE TO DATABASE")

def report_error(line):
    # TODO: handle errors separately
    write_to_db(parse_data(line))

def main():
    filename = CONSTANTS["LOG_FILEPATH"]
    log_file = open(filename,'r')
    file_size = os.stat(filename)[6]
    log_file.seek(file_size)
    influx = InfluxDBClient(host=INFLUX_INFO['HOST'],
                            port=INFLUX_INFO['PORT'],
                            username=INFLUX_INFO['USERNAME'],
                            password=INFLUX_INFO['PASSWORD'])
    dbname = INFLUX_INFO['DBNAME'] 
    client.create_database(dbname) #going to assume this gets ignored if it already exists for now
    client.switch_database(dbname)
    while True:
        where = log_file.tell()
        line = log_file.readline()
        if not line:
            time.sleep(CONSTANTS["FILE_READ_RATE_IN_SEC"])
            log_file.seek(where)
        else:
            line = line.strip()
            if check_error(line):
                report_error(line)
            elif check_relevant(line):
                write_to_db(parse_data(line), influx)

main()