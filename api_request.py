import requests
import datetime

req = requests.get('https://economia.awesomeapi.com.br/json/all')

req_json = req.json()

for item in req_json.items():
    print('{}:{} -- Date:{}'.format(item[0], item[1]['varBid'], datetime.datetime.fromtimestamp(float(item[1]['timestamp']))))