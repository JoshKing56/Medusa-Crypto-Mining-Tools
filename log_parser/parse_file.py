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
    return data

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

