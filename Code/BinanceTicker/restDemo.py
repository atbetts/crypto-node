import requests
import json
apiurl='https://api.binance.com/'
def _url(path):
    return apiurl+path
def getCoinData(coinname,num):
    #ETCBTC, ADAUSD etc
    resp = requests.get(_url('api/v3/ticker/bookTicker'))
    if resp.status_code != 200:
    #Error
        raise ApiError('GET'.format(resp.status_code))
    coinlist = resp.json()
    valuelist = []

    for coin in coinlist:
        a=json.loads(json.dumps(coin))
        coin2coin = a['symbol']
        
        if(num==2):
            if((coinname[0:2] in coin2coin) and (coinname[3:5] in coin2coin)):
                valuelist.append(a['symbol']+'\t'+a['bidPrice'])
        elif(num==1): 
            if coinname in coin2coin:
                valuelist.append(a['symbol']+'\t'+a['bidPrice'])
        else:
            continue
    return valuelist
print(getCoinData('ETHBTC',1))
