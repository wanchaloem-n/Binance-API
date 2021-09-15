# -*- coding: utf-8 -*-

# !pip install python-binance
from binance.client import Client
def info_account(client,stable_coin_symbol='USDT'):
    """
    return status: True, if you can trade, 
    stable_coin: amount your stable coin,

    parameters: api_key, 
    api_secret, 
    testnet=True if demo API, False if real API
    """
    try:
        info=client.get_account()
        if 'SPOT' not in info['permissions']:
            status=False
        else:
            status=True
    except:
        status=False
    if status:
        try:
            stable_coin=float(client.get_asset_balance(asset=stable_coin_symbol)['free'])
        except:
            stable_coin=0.
    else:
        stable_coin=0.
    return status,stable_coin
api_key= 'dNYZvurhuUInWuMO7JnqSn1BMjb2I'
api_secret= 'rnZRt2TXIfKPaeyBXmNYd8FILFNji'

client = Client(api_key, api_secret,testnet=True)
status,stable_coin=info_account(client,stable_coin_symbol='USDT')
print(status,stable_coin)
