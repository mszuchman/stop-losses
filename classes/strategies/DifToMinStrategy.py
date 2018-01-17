import json
from bittrex.bittrex import *


#TODO: Change bittrexclass to singleton
#TODO: Loose coupling with bittrex
#TODO: Compare with the purchased price (if I bought cheap I should wait)

class DifToMinStrategy():
	def __init__(self):	
		with open('config.json') as configFile:
		    config = json.load(configFile)
		    configFile.close()
		    self.bittrex = Bittrex(config['BITTREX_KEY'], config['BITTREX_SECRET'], api_version='v2.0')
		    self.threshold = config['DIF_TO_MIN_THRESHOLD']

	def hasToSell(self, market):
		marketDetail = self.bittrex.get_marketsummary(market)

		high = marketDetail['result']['High']
		last = marketDetail['result']['Last']
		low = marketDetail['result']['Low']
		
		percentage = (last-low)/(high-low)
		

		return percentage < self.threshold

