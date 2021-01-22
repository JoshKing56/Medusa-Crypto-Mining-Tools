#TODO implement other event types 
#     # Sample lines
#     #   2021.01.11:17:31:54.389: main Eth speed: 80.770 MH/s, shares: 606/0/0, time: 7:33
#     #   2021.01.11:17:31:55.832: main Eth: Accepted shares 607 (0 stales), rejected shares 0 (0 stales)
#     #   2021.01.11:17:31:55.832: main Eth: Incorrect shares 0 (0.00%), est. stales percentage 0.00%
#     #   2021.01.11:17:31:55.832: main Eth: Maximum difficulty of found share: 4008.0 GH (!)
#     #   2021.01.11:17:31:55.832: main Eth: Average speed (5 min): 79.442 MH/s
#     #   GPUs power: 322.4 W
#     #   2021.01.11:17:31:34.580: main GPU1: 70C 65% 322W

def line_split(s, leader, trailer):
    end_of_leader = s.index(leader) + len(leader)
    if trailer == "": return s[end_of_leader:]
    start_of_trailer = s.index(trailer, end_of_leader)
    return s[end_of_leader:start_of_trailer]

EVENTS = [

    {   # unique identifier for this string
        'identifier': 'main Eth speed:',
        # english description
        'name': 'MinerStatus',
        # field names
        'fields': ['speed', 'accepted_shares', 'stale_shares', 'rejected_shares', 'uptime'],
        # lambda function to parse the data corresponding to the field names
        'parser': lambda line: [line_split(line, 'Eth speed: ', ' MH/s'),

                                line_split(line, 'shares: ', ', time:').split('/')[0],
                                line_split(line, 'shares: ', ', time:').split('/')[1],
                                line_split(line, 'shares: ', ', time:').split('/')[2],
                                line_split(line, 'time: ', '').strip('\n')],
        # a typical input
        'test_input': "   2021.01.11:17:31:54.389: main Eth speed: 80.770 MH/s, shares: 606/0/0, time: 7:33\n",
        # the expected output
        'test_output': ['80.770', '606', '0', '0', '7:33']}
]