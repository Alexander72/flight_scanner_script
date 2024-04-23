import webbrowser
import time
from datetime import datetime, timedelta

def generate_trip_dates(start_date_X, end_date_Y, min_duration_N, max_duration_M):
    trip_dates = []

    current_date = datetime.strptime(start_date_X, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_Y, '%Y-%m-%d')

    while current_date <= end_date:
        for duration in range(min_duration_N, max_duration_M + 1):
            end_diff = timedelta(days=duration - 1)
            trip_start = current_date.strftime('%y%m%d')
            trip_end = (current_date + end_diff).strftime('%y%m%d')
            trip_dates.append((trip_start, trip_end))
        current_date += timedelta(days=1)

    return trip_dates

url_template = "https://www.skyscanner.net/transport/flights/{origin}/{destination}/{start_date}/{end_date}/"
query_parameters = "?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=true&ref=home&rtn=1"
origins = ["dtm","dus","ams","mst","cgn","nrn"]
destinations = ["ayt"]
start_date_X = '2024-04-24'
end_date_Y = '2024-04-25'
min_duration_N = 5
max_duration_M = 6

possible_trip_dates = generate_trip_dates(start_date_X, end_date_Y, min_duration_N, max_duration_M)
url_template = url_template + query_parameters

for origin in origins:
    for destination in destinations:
        for start_date, end_date in possible_trip_dates:
            url = url_template.format(origin=origin, destination=destination, start_date=start_date, end_date=end_date)
            webbrowser.open(url, new=0, autoraise=True)
            time.sleep(1.5)
