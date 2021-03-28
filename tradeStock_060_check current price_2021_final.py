# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:09:34 2021

@author: Noman

TIME: 11.00, 16.00
"""




from bs4 import BeautifulSoup
import urllib.request
# from os.path import join, exists
# from os import  remove, makedirs
# import numpy as np
# import pandas as pd
import requests
import os 
import time
import random



#[price][min][max]

stock_dict = {    'LALIN':[8.91, 11.20, 11.50]      , 
				  'HTC':[34.31, 31.20, 45.50]       ,
				  'CBG':[135.23, 116.00, 154.00]    ,
				  'PSH':[8.91, 11.00, 13.00]        ,
				  'QTC':[5.00, 4.50, 6.50]          ,
				  'UPF':[84.75, 66.22, 88.00]
			  
			  }


#stock_dict = {'QTC':[5.00, 4.50, 6.50] }



SENT_TO_LINE = True
symbols = stock_dict.keys()




head_list = []
head_head_list = []
stock_word = []
#each_symbol = 'LALIN'
 
for each_symbol in symbols:

	#time.sleep(random.randint(2, 5))

	url_string = "https://marketdata.set.or.th/mkt/stockquotation.do?symbol={0}&language=en&country=US".format(each_symbol)
	
	
	response = requests.get(url_string)
	#print(response.status_code, response.reason)
	#print(response.headers)
	
	
	page = urllib.request.urlopen(url_string).read()
	soup = BeautifulSoup(page, 'html.parser')
		
	
	try:
		table_green = soup.find('td', class_='set-color-green').getText()
	except:
		try:
			table_green = soup.find('td', class_='set-color-red').getText()
		except:
			table_green = soup.find('td', class_='set-color-black').getText()
		
		
	try:	
		latest_value = float(table_green)
	except:
		print ('could not qury value from web skip it na.')
		latest_value = 0
		pass
	
	print ('Symbol is: {0}\nLast is:{1}'.format(each_symbol,latest_value))

	
	
	
	
	
	
	
	
	if latest_value > stock_dict[each_symbol][1] and latest_value < stock_dict[each_symbol][2]:
		print ('The {0} is inbetween {1} and {2}'.format(latest_value, stock_dict[each_symbol][1], stock_dict[each_symbol][2])     )
		print ('\n')
		#print('{0}: {1} is inbetween it okay now'.format(each_symbol,latest_value))
		#word = '{0}: {1} is inbetween it okay now'.format(each_symbol,latest_value)
		#stock_word.append(word)
		
		
	elif latest_value < stock_dict[each_symbol][1]: # min val
		#print('{0}: {1} is inbetween it should buy. !!!'.format(each_symbol,latest_value))
		minus  = stock_dict[each_symbol][1] - latest_value
		word = '{0}: {1} is less than min ({2}, -{3}) it should Buy. ?'.format(each_symbol, latest_value, stock_dict[each_symbol][1], minus)
		stock_word.append('\n'+word+'\n')
		
	elif latest_value > stock_dict[each_symbol][2]: # max val
		minus  = latest_value - stock_dict[each_symbol][2]		
		#print('{0}: {1} is inbetween it should sell.!'.format(each_symbol,latest_value))
		word = '{0}: {1} is morn then max ({2}, +{3}) it should Sell. ?'.format(each_symbol, latest_value, stock_dict[each_symbol][2], minus)
		stock_word.append('\n'+word+'\n')
	elif latest_value == 0:
		print ('latest value equal zero try next time.')
		pass



	
print ('Analylze complete.')

if stock_word:
	for each in stock_word:
		print (each)
else:
	print ('Nothing update here.')


print ('Print complete.')


if SENT_TO_LINE:
	
	if stock_word:
	
		token = 'nLDAN5v096kqehdW01gXoZaMdm7Jwd6PTOpISB9IFun'
	
		url = 'https://notify-api.line.me/api/notify'
	
		headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
	
		r = requests.post(url, headers=headers, data = {'message':stock_word})
		print (r.text)
else:
	pass




