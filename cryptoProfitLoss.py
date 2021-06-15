from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import csv
import json


myAPIkey = "6cd46dc0-a1dc-4d03-8265-ad9fb78768d3"

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'GBP',
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': myAPIkey,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

print(data)