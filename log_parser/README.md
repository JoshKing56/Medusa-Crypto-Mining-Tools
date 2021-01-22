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