import requests
import datetime

def test_dol():

    req = requests.get('https://economia.awesomeapi.com.br/json/all')

    req_json = req.json()

    a = []
    for item in req_json.items():
        try:
            a.append('{}:{} -- Date:{}'.format(item[0], item[1]['varBid'], datetime.datetime.fromtimestamp(float(item[1]['timestamp']))))
        except:
            pass
    return a
print(test_dol())