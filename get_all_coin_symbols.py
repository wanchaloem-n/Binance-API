# -*- coding: utf-8 -*-

import requests
def get_all_pairs(base="USDT"):
    """
    get all pairs that can trade by the base coin
    param: base: base coin
    return: list of all pairs including  {'orderTypes',   'permissions',  'status',  'symbol'}
    """
    data=requests.get("https://www.binance.com/api/v1/exchangeInfo")
    pairs=[]
    for symbol in data.json()['symbols']:
        if symbol['symbol'][-len(base):]==base and "SPOT" in symbol['permissions'] and 'MARKET' in symbol['orderTypes'] and symbol['status']=="TRADING":
            pairs.append({'symbol':symbol['symbol'],'orderTypes':symbol['orderTypes'],'status':symbol['status'],'permissions':symbol['permissions']})
    return pairs
    
pairs=get_all_pairs()
print(pairs)
