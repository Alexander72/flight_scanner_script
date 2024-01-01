import webbrowser
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

url_template = "https://www.skyscanner.net/transport/flights/ams/cpt/{start_date}/{end_date}/?adultsv2=2&cabinclass=economy&childrenv2=&duration=1110&inboundaltsenabled=false&outboundaltsenabled=false&rtn=1&stops=!twoPlusStops"
start_date_X = '2024-02-08'
end_date_Y = '2024-02-14'
min_duration_N = 14
max_duration_M = 21

possible_trip_dates = generate_trip_dates(start_date_X, end_date_Y, min_duration_N, max_duration_M)

for start_date, end_date in possible_trip_dates:
    url = url_template.format(start_date=start_date, end_date=end_date)
    webbrowser.open(url, new=0, autoraise=True)
