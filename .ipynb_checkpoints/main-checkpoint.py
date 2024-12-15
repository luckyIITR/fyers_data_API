from fetch_data import Fetch_Fyers_data
import datetime
from datetime import timedelta
# import logging

# logging.basicConfig(level=logging.INFO, 
#                     format='%(asctime)s - %(levelname)s - %(message)s')
#                     # filename='app.log',  # Optional: Log to a file
#                     # filemode='a')        # 'w' overwrites log file on each run

fyers_obj = Fetch_Fyers_data()

todays_date = datetime.datetime.now().date()
# print(todays_date)
df = fyers_obj.get_data(symbol='NSE:NIFTY50-INDEX', resolution='1D', range_from=todays_date-timedelta(days=1), range_to=todays_date)

print(df.head())