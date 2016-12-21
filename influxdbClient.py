#import datetime

from influxdb import InfluxDBClient

#set some constants as InfluxDB host and database name
influxdb_host = 'server's-ip-address'

influxdb_name = 'telegraf'

# Timestamp
timestamp = InfluxDBClient(influxdb_host,'8086','','',influxdb_name)

#Query against existing database
result = client.query('SELECT * FROM cpu')

points = list(result.get_points(measurement = 'cpu'))

for point in points:
    print('% CPU idle = ', point['usage_idle'])
