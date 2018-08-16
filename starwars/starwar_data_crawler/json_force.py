#!/usr/bin/env python
# coding:utf8

import sys 
# reload(sys)
# sys.setdefaultencoding('utf8')


import json


films = {}
characters = {}
planets = {}
starships = {}
vehicles = {}
species = {}

fr = open('C:/starwars/data/films.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	films[tmp['url']] = tmp
fr.close()
fr = open('C:/starwars/data/characters.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	characters[tmp['url']] = tmp
fr.close()
fr = open('C:/starwars/data/planets.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	planets[tmp['url']] = tmp
fr.close()
fr = open('C:/starwars/data/starships.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	starships[tmp['url']] = tmp
fr.close()
fr = open('C:/starwars/data/vehicles.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	vehicles[tmp['url']] = tmp
fr.close()
fr = open('C:/starwars/data/species.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	species[tmp['url']] = tmp
fr.close()



nodes = []
links = []

for key, value in films.items():
	nodes.append({'id': value['title'], 'class': 'film', 'group': 0, 'size': 20})
	# characters
	for item in value['characters']:
		if characters.__contains__(item):
			links.append({'source': value['title'], 'target': characters[item]['name'], 'value': 3})
	# planets
	for item in value['planets']:
		if planets.__contains__(item):
			links.append({'source': value['title'], 'target': planets[item]['name'], 'value': 3})
	# species
	for item in value['species']:
		if species.__contains__(item):
			links.append({'source': value['title'], 'target': species[item]['name'], 'value': 3})
	# starships
	for item in value['starships']:
		if starships.__contains__(item):
			links.append({'source': value['title'], 'target': starships[item]['name'], 'value': 3})
	# vehicles
	for item in value['vehicles']:
		if vehicles.__contains__(item):
			links.append({'source': value['title'], 'target': vehicles[item]['name'], 'value': 3})



for key, value in characters.items():
	nodes.append({'id': value['name'], 'class': 'character', 'group': 1, 'size': 5})
	# films
	for item in value['films']:
		if films.__contains__(item):
			links.append({'source': value['name'], 'target': films[item]['title'], 'value': 3})
	# planets
	if planets.__contains__(value['homeworld']):
		links.append({'source': value['name'], 'target': planets[value['homeworld']]['name'], 'value': 3})
	# species
	for item in value['species']:
		if species.__contains__(item):
			links.append({'source': value['name'], 'target': species[item]['name'], 'value': 3})
	# starships
	for item in value['starships']:
		if starships.__contains__(item):
			links.append({'source': value['name'], 'target': starships[item]['name'], 'value': 3})
	# vehicles
	for item in value['vehicles']:
		if vehicles.__contains__(item):
			links.append({'source': value['name'], 'target': vehicles[item]['name'], 'value': 3})

for key, value in planets.items():
	nodes.append({'id': value['name'], 'class': 'planet', 'group': 2, 'size': 16})
	# films
	for item in value['films']:
		if films.__contains__(item):
			links.append({'source': value['name'], 'target': films[item]['title'], 'value': 3})
	# characters
	for item in value['residents']:
		if characters.__contains__(item):
			links.append({'source': value['name'], 'target': characters[item]['name'], 'value': 3})

for key, value in starships.items():
	nodes.append({'id': value['name'], 'class': 'starship', 'group': 3, 'size': 8})
	# films
	for item in value['films']:
		if films.__contains__(item):
			links.append({'source': value['name'], 'target': films[item]['title'], 'value': 3})
	# characters
	for item in value['pilots']:
		if characters.__contains__(item):
			links.append({'source': value['name'], 'target': characters[item]['name'], 'value': 3})

for key, value in vehicles.items():
	nodes.append({'id': value['name'], 'class': 'vehicle', 'group': 4, 'size': 8})
	# films
	for item in value['films']:
		if films.__contains__(item):
			links.append({'source': value['name'], 'target': films[item]['title'], 'value': 3})
	# characters
	for item in value['pilots']:
		if characters.__contains__(item):
			links.append({'source': value['name'], 'target': characters[item]['name'], 'value': 3})

for key, value in species.items():
	nodes.append({'id': value['name'], 'class': 'species', 'group': 5, 'size': 14})
	# planets
	if planets.__contains__(value['homeworld']):
		links.append({'source': value['name'], 'target': planets[value['homeworld']]['name'], 'value': 3})
	# films
	for item in value['films']:
		if films.__contains__(item):
			links.append({'source': value['name'], 'target': films[item]['title'], 'value': 3})
	# characters
	for item in value['people']:
		if characters.__contains__(item):
			links.append({'source': value['name'], 'target': characters[item]['name'], 'value': 3})

fw = open('C:/starwars/html/starwar.json', 'w')
fw.write(json.dumps({'nodes': nodes, 'links': links}))
fw.close()

