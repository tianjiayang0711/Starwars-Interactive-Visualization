#!/usr/bin/env python
# coding:utf8

import sys 
# reload(sys)
# sys.setdefaultencoding('utf8')

import json

data = {}

fr = open('C:/starwars/data/films.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	data[tmp['title']] = tmp
fr.close()
fr = open('C:/starwars/data/characters.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	data[tmp['name']] = tmp
fr.close()
fr = open('C:/starwars/data/planets.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	data[tmp['name']] = tmp
fr.close()
fr = open('C:/starwars/data/starships.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	data[tmp['name']] = tmp
fr.close()
fr = open('C:/starwars/data/vehicles.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	data[tmp['name']] = tmp
fr.close()
fr = open('C:/starwars/data/species.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	data[tmp['name']] = tmp
fr.close()




fw = open('/all.json','w')
fw.write(json.dumps(data))
fw.close()