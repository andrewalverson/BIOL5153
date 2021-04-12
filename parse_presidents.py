#! /usr/bin/env python3

# import some modules
import csv
from collections import defaultdict

# dictionary: key = president number, value = president name
presidents = defaultdict(dict)

# dictionary: key = party name, value = number of presidents in that party
party = defaultdict(dict)

# open and parse the data file
with open('presidents.csv', 'r') as infile:
	# create a csv reader object
	reader = csv.reader(infile, delimiter=',')

	# loop over each line in reader
	for line in reader:

		# skip the header line
		if(line[0] == 'Presidency '):
			continue

		# else it's a data line -- parse this
		else:
			presidents[line[0]] = line[1]
			party[line[5]] = line[1]


# looping over the party dictionary
for i in party.keys():
	print(i, party[i])


# print('President #16 was', presidents.get('16'))
# print('President #16 was', presidents['16'])


# for beyonce, aretha in presidents.items():
# 	print('President number', beyonce, 'was', aretha)





















