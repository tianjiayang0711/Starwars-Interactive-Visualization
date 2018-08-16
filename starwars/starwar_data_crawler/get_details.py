#! /ussr/bin/env python
# coding:utf8

import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
import json
import http
import urllib.request
import urllib.parse


headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"


fr = open('C:/starwars/data/films.txt','r')
films = []
for line in fr:
	line = json.loads(line.strip('\n'))
	films.append(line)

fr.close()

targets = ['characters','planets','species','starships','vehicles']
for target in targets:
	fw = open('C:/starwars/data/' + target +'.csv','w')
	data = []
	for item in films:
		tmp = item[target]
		for tar in tmp:
			if tar in data:
				continue
			else:
				data.append(tar)

			while 1:
				print (tar)
				try:
					request = urllib.request.Request(url = tar ,headers = headers)
					response = urllib.request.urlopen(request,timeout = 10)
					result = response.read()
				except Exception as e:
					continue
				else:
					fw.write(result + '\n')
					break
				finally:
					pass



	print (str(len(data))+ ' '+target)
	fw.close()