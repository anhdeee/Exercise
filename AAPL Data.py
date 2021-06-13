import pandas as pd
import requests
import json


querystring = {"symbol":"AAPL","region":"US"}

headers = {
    'x-rapidapi-key': "0acb66bf99msh178030a1e9b9a86p106ba3jsn59034c6f8818",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

r = requests.get("https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data", headers=headers, params=querystring)

data = json.loads(r.text)

value = data['prices']

df = pd.json_normalize(value)
df = df.drop(df.columns[[6, 7, 8, 9, 10, 11, 12]], axis=1)

print(df.tail(10))






