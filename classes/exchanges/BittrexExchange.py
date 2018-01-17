import json
from bittrex.bittrex import *


class BittrexExchange():
	def __init__(self):	
		with open('config.json') as configFile:
		    config = json.load(configFile)
		    configFile.close()
		    self.bittrex = Bittrex(config['BITTREX_KEY'], config['BITTREX_SECRET'], api_version='v2.0')

	def getCryptosInMyWallet(self):
		balances = self.bittrex.get_balances()
		results = balances['result']
		cryptos = []

		for result in results:
			if result['Balance']['Currency']!='USDT' and result['Balance']['Available']>0:
				cryptos.append({'coin':result['Balance']['Currency'],'available':result['Balance']['Available']})
				
		return cryptos