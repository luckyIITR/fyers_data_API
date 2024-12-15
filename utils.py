from datetime import timedelta
import datetime
import os

def get_expires_2024():
    file_name = 'expiry_dates.txt'
    
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            dates_txt = file.read().splitlines()
        # print(f"File '{file_name}' exists, content read.")
        expiries = [datetime.datetime.strptime(date.strip(), "%Y-%m-%d").date() for date in dates_txt]
        return expiries
    
    holidays_strings = [
        "22-Jan-2024",
        "26-Jan-2024",
        "08-Mar-2024",
        "25-Mar-2024",
        "29-Mar-2024",
        "11-Apr-2024",
        "17-Apr-2024",
        "01-May-2024",
        "20-May-2024",
        "17-Jun-2024",
        "17-Jul-2024",
        "15-Aug-2024",
        "02-Oct-2024",
        "15-Nov-2024",
        "20-Nov-2024",
        "25-Dec-2024"
    ]

    # Convert to datetime objects
    holidays = [datetime.datetime.strptime(date, "%d-%b-%Y").date() for date in holidays_strings]

    def get_thursdays(year):
        # List to store all 
        thursdays = []

        # Start from the first day of the year
        current_date = datetime.date(year, 1, 1)

        # Adjust to the first 
        while current_date.weekday() != 3:  # 2 corresponds to Wednesday
            current_date += datetime.timedelta(days=1)

        # Collect  in the year
        while current_date.year == year:
            thursdays.append(current_date)
            current_date += datetime.timedelta(days=7)

        return thursdays
    expiries = get_thursdays(2024)

    # check for holidays and correct it
    for i in range(len(expiries)):
        if(expiries[i] in holidays):
            # print(expiries[i])
            expiries[i] -= timedelta(days=1)
            
    with open(file_name, 'w') as file:
            file.writelines('\n'.join(list(map(str,expiries))))
            
    return expiries

def create_symbol_true_data(expiry, instrument, ce_pe, strike_price):
    year = str(expiry)[2:4]
    month = str(expiry)[5:7]
    exp_date = str(expiry)[-2:]
    symbol = instrument + year + month + exp_date + str(strike_price) + ce_pe
    return symbol

# Create options symbols based on monthly / weekly
def create_symbol_fyers(exchange, expiry, instrument, ce_pe, strike_price):
    # Check monthly expiry or weekly expiry

    expiries = get_expires_2024()
    indexx = expiries.index(expiry)
    ismonthly = True
    if (indexx + 1 != len(expiries)):
        ismonthly = (expiries[indexx + 1].month != expiry.month)
        
    if(ismonthly):
        year = str(expiry)[2:4]
        month = expiry.strftime("%b").upper()
        symbol = exchange + ':' + instrument + year + month + str(strike_price) + ce_pe
        return symbol
    else:
        year = str(expiry)[2:4]
        month = str(expiry)[5:7]
        if(month == '10'):
            month = 'O'
        elif(month == '11'):
            month = 'N'
        elif (month == '12'):
            month = 'D'
        exp_date = str(expiry)[-2:]
        symbol = exchange + ':' + instrument + year + month + str(exp_date) + str(strike_price) + ce_pe
        return symbol
    
# expiry = get_expires_2024()[-1]
# print(create_symbol_true_data(expiry, 'NIFTY', 'CE', 24000))