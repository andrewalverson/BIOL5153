#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO

# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

# create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feature from the genome')

# add positional arguments
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help='name of the FASTA file')

# parse the arguments
args = parser.parse_args()

# GFF filename
gff_input = 'watermelon.gff'

# fasta filename
fasta_input = 'watermelon.fsa'

# open and read in GFF file
with open(gff_input, 'r') as gff_in:
	# create a csv reader object
	reader = csv.reader(gff_in, delimiter='\t')

	# loop over all the lines in our reader object (i.e., parsed file)
	for line in reader:
		# print(line)
		print(line[3], line[4])


# read in FASTA file

# parse the GFF file
