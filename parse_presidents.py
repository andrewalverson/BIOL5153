#! /usr/bin/env python3

# import some modules
import csv
from collections import defaultdict

# dictionary: key = president number, value = president name
presidents = defaultdict(dict)

# dictionary: key = party name, value = number of presidents in that party
party = defaultdict(dict)

# dictionary: key = president number, value = the entire data line in a list
all_of_it = defaultdict(dict)


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
			# make some variables for the columns, stripping as we go to remove whitespace
			pres_num   = line[0].strip()
			pres_name  = line[1].strip()
			party_name = line[5].strip()

			all_of_it[pres_num] = line

			# buid presidents dictionary
			presidents[pres_num] = pres_name

			# build party dictionary
			# test whether this key (party) exists in our dictionary
			# if it exists, increment the count (value) by 1
			if(party[party_name]):
				party[party_name] += 1
			# else this is the first time we've seen this party,
			# so set the value equal to 1
			else:
				party[party_name] = 1


print(all_of_it['16'][2])

# loop over the party dictionary
for i, j in all_of_it.items():
	print(i, j[0], j[1], j[2])

# loop over the party dictionary
#for i, j in party.items():
#	print(i, j)


# looping over the party dictionary
# for i in party.keys():
#	print('[' + i + ']' + ' ' + '[' + party[i] + ']')


# print('President #16 was', presidents.get('16'))
# print('President #16 was', presidents['16'])


# for beyonce, aretha in presidents.items():
# 	print('President number', beyonce, 'was', aretha)





















