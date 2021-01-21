import os
import time
from constants import CONSTANTS

def get_new_lines():
    return [] 

def check_error(line):
    return True

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
    return line 

def write_to_db(line):
    return True

def report_error(line): # TODO: handle errors separately
    write_to_db(parse_data(line))

def main():
    while True:
        new_lines = get_new_lines()
        for line in new_lines:
            if check_error(line):
                report_error(line)
            elif check_relevant(line):
                write_to_db(parse_data(line))

# def test_stream_read():
