import requests
API_KEY="L64F5MM967USPSC0" #get API key
api_url="https://www.alphavantage.co/" #api_url from source api
interval="5min" #
#symbol="AMZN"

def get_stock_market_data(symbol,is_timeseries):
    query=f"query?function=TIME_SERIES_DAILY&symbol={symbol}&{interval}={interval}&apikey={API_KEY}"
    response=requests.get(url=api_url+query)
    
    for key,value in response.json().items():
        if is_timeseries:
            print(key,value)
        else:
            if key == "Time Series (Daily)":
                continue
symbol=input("Enter the symbol you want for the stock market API eg. (AMZN, GOOGL, IBM)")
is_timeseries=True
get_stock_market_data(symbol,is_timeseries)




