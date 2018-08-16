#! /ussr/bin/env python
# coding:utf8

import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


import json
import http
import urllib.request
import urllib.parse

films = []

for x in range(1,8):
	films.append('http://swapi.co/api/films/' + str(x) + '/')

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

fw = open('films.txt','w')

for item in films:
	print(item)
	request = urllib.request.Request(url = item,headers=headers)
	response = urllib.request.urlopen(request,timeout = 20)
	result = response.read()
	print(result)
	fw.write(str(result) + '\n')

print('finished!')
fw.close()