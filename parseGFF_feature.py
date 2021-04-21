#! /usr/bin/env python3

import re
import csv
import argparse
from Bio import SeqIO

# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

# create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feature from the genome')

# add positional arguments
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help='name of the FASTA file')
parser.add_argument("gene_name", help='name of the gene to extract')
parser.add_argument("feature_type", help='type of feature to extract')

# parse the arguments
args = parser.parse_args()


# read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')

# open and read in GFF file
with open(args.gff, 'r') as gff_in:

	# create a csv reader object
	reader = csv.reader(gff_in, delimiter='\t')

	# loop over all the lines in our reader object (i.e., parsed file)
	for line in reader:
		# skip blank lines
		if(not line):
			continue

		# skip comment lines
		elif(re.search('^#', line[0])):
			continue

		# else it's a data line
		else:
			feature = line[2]
			start   = line[3]
			end     = line[4]
			strand  = line[6]
			attributes = line[8]

			if(feature == args.feature_type):
				pat = re.compile(args.gene_name)
				match = pat.search(attributes)
				if(match):
					fragment = genome.seq[int(start)-1:int(end)]
					print
					print(args.feature_type, start, end, strand, attributes)
				else:
					continue
					# print("no match for", args.gene_name)

			# extract the sequence
			

			#print('>' + genome.id + ' ' + line[8])
			#print(fragment)
























