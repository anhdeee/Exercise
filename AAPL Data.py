import pandas as pd
import requests
import json

# API
querystring = {"symbol":"AAPL","region":"US"}

headers = {
    'x-rapidapi-key': "0acb66bf99msh178030a1e9b9a86p106ba3jsn59034c6f8818",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

r = requests.get("https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data", headers=headers, params=querystring)

data = json.loads(r.text)
value = data['prices']
df = pd.json_normalize(value)

# Drop columns that contain null values
df = df.drop(df.columns[[7, 8, 9, 10, 11, 12]], axis=1)

# Format Currency columns to dollar value
def dollar_format(x):
    return "${:.2f}".format(x / 1)

df['open'] = df['open'].apply(dollar_format)
df['high'] = df['high'].apply(dollar_format)
df['low'] = df['low'].apply(dollar_format)
df['close'] = df['close'].apply(dollar_format)
df['adjclose'] = df['adjclose'].apply(dollar_format)

# Print the last 10 entries
print(df.tail(10))






