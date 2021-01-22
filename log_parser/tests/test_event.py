from conf.events import EVENTS
from conf.constants import CONSTANTS
from src.process_line import parse_line

# testing for development
for event in EVENTS:
    if event['parser'](event['test_input']) == event['test_output']:
        print(f"Event: {event['name']}, Test Passed")
    else:
        print(f"Event: {event['name']}, Test Failed")
        print(f"Test input: '{event['test_input'].strip()}'")
        print(f"Expected_output: {str({key: value for key, value in zip(event['fields'], event['test_output'])})}")
        print(f"Event returned : {str({key: value for key, value in zip(event['fields'], event['parser'](event['test_input']))})}")

with open(CONSTANTS['LOG_FILEPATH']) as file:
    for line in file:
        line_output = parse_line(line)