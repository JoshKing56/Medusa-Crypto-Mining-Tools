from conf.events import EVENTS 

def parse_line(line):
    """
    :param line:
    :return:
    dict:
        "name": ,
        "fields": {
            "duration": 127
        }
        "time": "2018-03-28T8:01:00Z",
    """
    print("Line: '{}'".format(line.strip('\n')))
    line_output = {'time': line[:23].strip()}

    fields = line[25:].strip()
    print("\ttime: '{}', \n\tfields: '{}'".format(line_output['time'], fields))

    for event in EVENTS:
        if event['identifier'] in fields:
            line_output['event_name'] = event['event_name']
            line_output['fields'] = {key: value for key, value in zip(event['fields'], event['field_parser'](fields))}
        else:
            line_output = {}

    return line_output