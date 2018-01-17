#!/usr/bin/env python
import time

from classes.exchanges.BittrexExchange import BittrexExchange

##Strategies
from classes.strategies.DifToMinStrategy import DifToMinStrategy


strategies = [ DifToMinStrategy() ]

def getMarket(coin):
	if coin != 'BTC':
		return 'BTC-'+coin
	return 'USDT-'+coin


def checkCryptos():
	exchange = BittrexExchange()

	cryptos = exchange.getCryptosInMyWallet()

	for crypto in cryptos:
		
		market = getMarket(crypto['coin'])

		for strategy in strategies:
			if(	strategy.hasToSell(market)):
				print 'sell!!! '+market
while True:
	checkCryptos()

	print 'Time to sleep'
	time.sleep(3)