# Medusa log parser
## What is this?
In order to monitor our miner, we want to use Grafana to be able to look at the miner. The problem is, Phoenix mine doesn't have an API, but outputs useful information in a massie log file. This project just parses that file and writes it to influxDB. Grafana will eventually be hooked up to this db.
## Usage
Install dependencies with:
```
python -m pip install -r requirements.txt
```
then, open conf/constants.py to edit settings. Finally, run the project with 
```
python log_parser.py
```

## Note
This isn't working right now, influx 2.0 has new access auth requirements that arent' fucking documented anywhere, and I'm pretty sure arent't implemented in the python api (or isn't documented)

[more info](https://community.influxdata.com/t/401-unauthorized-unable-to-parse-authentication-credentials/12714)

Solutions are:
- roll back to 1.8
- generate auth token using command `influx auth create`

I'm miffed as hell so gonna figure that all out later

actually so btfo'd