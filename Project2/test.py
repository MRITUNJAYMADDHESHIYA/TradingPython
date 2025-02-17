import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime

# Initialize MetaTrader 5
if not mt5.initialize():
    print("Initialization failed")
    mt5.shutdown()

def get_ohlc_history(symbol, timeframe, date_from, date_to, additional_columns=[]):
    # Get OHLC data within the date range
    ohlc = mt5.copy_rates_range(symbol, timeframe, date_from, date_to)
    
    if ohlc is None:
        raise ValueError(f"No data returned for the symbol '{symbol}' in the given timeframe.")
    if len(ohlc) == 0:
        raise ValueError(f"Empty data returned for the symbol '{symbol}' in the given timeframe.")
    
    # Convert to pandas DataFrame and format time column
    ohlc_df = pd.DataFrame(ohlc)
    ohlc_df['time'] = pd.to_datetime(ohlc_df['time'], unit='s')
    
    return ohlc_df[['time', 'open', 'high', 'low', 'close'] + additional_columns]

# Define date range
start_date = datetime(2024, 1, 1)
end_date = datetime.now()

# Get OHLC data
try:
    data = get_ohlc_history('USDJPYm', mt5.TIMEFRAME_D1, start_date, end_date)
    print(data)
except ValueError as e:
    print(e)

# Shutdown the MetaTrader 5 connection
mt5.shutdown()
